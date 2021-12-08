import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../ML/utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../ML/model'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../ML/g2p'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../ML'))

import torch
import torch.nn as nn
from torch.optim.lr_scheduler import StepLR
from tqdm import tqdm

from config_parser import Config
from file_utils import create_path
from torch_utils import set_device, save_checkpoint, load_checkpoint

import preprocess_ui
import dataprocess
from models import Generator, Discriminator
from logger import Logger
from train import AverageMeter, criterionAdv

def start_train(config, queue):
    queue.put_nowait({'index': 1, 'action': 'reset', 'value': config.stop_epoch})
    config_basename = os.path.basename(config.config[0])
    print("Configuration file: \'%s\'" % (config_basename))

    checkpoint_path = create_path(config.checkpoint_path, action='overwrite')
    config.save(os.path.join(checkpoint_path, config_basename))
    logger = Logger(os.path.join(checkpoint_path, 'log'))
    dataloader = dataprocess.load_train(config)
    step_size = config.step_epoch * len(dataloader.train)

    G = Generator(config)
    D = Discriminator(config)
    G, D = set_device((G, D), config.device, config.use_cpu)


    criterionL1 = nn.L1Loss()
    optimizerG = torch.optim.Adam(G.parameters(), lr=config.learn_rate, betas=config.betas,
                                  weight_decay=config.weight_decay)
    optimizerD = torch.optim.Adam(D.parameters(), lr=config.learn_rate, betas=config.betas,
                                  weight_decay=config.weight_decay)
    schedulerG = StepLR(optimizerG, step_size=step_size, gamma=config.decay_factor)
    schedulerD = StepLR(optimizerD, step_size=step_size, gamma=config.decay_factor)

    # For loading checkpoint
    mode = config.load_checkpoint
    cnt = 1
    if mode == True:
        objG = load_checkpoint(config.loaded_checkpoint_path_G, G, optimizerG, config.learn_rate, cnt)
        objD = load_checkpoint(config.loaded_checkpoint_path_D, D, optimizerD, config.learn_rate, cnt)
        G = objG[0]  # loaded Generator
        D = objD[0]  # loaded Discriminator
        cnt = objG[4]  # loaded epoch

    k = 0.0
    M = AverageMeter()
    lossG_train = AverageMeter()
    lossG_valid = AverageMeter()
    lossD_train = AverageMeter()

    print('Training start')
    for epoch in range(cnt + 1, config.stop_epoch + 1):
        # Training Loop
        # print("epoch in for loop : " + str(epoch))
        queue.put_nowait({'index': 1, 'action': 'set', 'value': epoch})
        G.train()
        D.train()
        queue.put_nowait({'index': 2, 'action': 'reset', 'value': len(dataloader.train)})
        for batch in tqdm(dataloader.train, leave=False, ascii=True):
            queue.put_nowait({'index': 2, 'action': 'increment'})
            x, y_prev, y = set_device(batch, config.device, config.use_cpu)
            y = y.unsqueeze(1)

            optimizerG.zero_grad()
            y_gen = G(x, y_prev)
            lossL1 = criterionL1(y_gen, y)
            loss_advG = criterionAdv(D, y_gen)
            lossG = lossL1 + loss_advG
            lossG.backward()
            optimizerG.step()
            schedulerG.step()

            optimizerD.zero_grad()
            loss_real = criterionAdv(D, y)
            loss_fake = criterionAdv(D, y_gen.detach())
            loss_advD = loss_real - k * loss_fake
            loss_advD.backward()
            optimizerD.step()
            schedulerD.step()

            diff = torch.mean(config.gamma * loss_real - loss_fake)
            k = k + config.lambda_k * diff.item()
            k = min(max(k, 0), 1)

            measure = (loss_real + torch.abs(diff)).data
            M.step(measure, y.size(0))

            logger.log_train(lossL1, loss_advG, lossG, loss_real, loss_fake, loss_advD, M.avg, k, lossG_train.steps)
            lossG_train.step(lossG.item(), y.size(0))
            lossD_train.step(loss_advD.item(), y.size(0))

        # Validation Loop
        G.eval()
        D.eval()
        for batch in tqdm(dataloader.valid, leave=False, ascii=True):
            x, y_prev, y = set_device(batch, config.device, config.use_cpu)
            y = y.unsqueeze(1)

            y_gen = G(x, y_prev)
            lossL1 = criterionL1(y_gen, y)
            loss_advG = criterionAdv(D, y_gen)
            lossG = lossL1 + loss_advG

            logger.log_valid(lossL1, loss_advG, lossG, lossG_valid.steps)
            lossG_valid.step(lossG.item(), y.size(0))

        for param_group in optimizerG.param_groups:
            learn_rate = param_group['lr']

        print("[Epoch %d/%d] [loss G train: %.5f] [loss G valid: %.5f] [loss D train: %.5f] [lr: %.6f]" %
              (epoch, config.stop_epoch, lossG_train.avg, lossG_valid.avg, lossD_train.avg, learn_rate))

        lossG_train.reset()
        lossG_valid.reset()
        lossD_train.reset()

        savename = os.path.join(checkpoint_path, 'latest_')
        save_checkpoint(savename + 'G.pt', G, optimizerG, learn_rate, lossG_train.steps, False, epoch + 1)
        save_checkpoint(savename + 'D.pt', D, optimizerD, learn_rate, lossD_train.steps, False, epoch + 1)
        if epoch % config.save_epoch == 0:
            savename = os.path.join(checkpoint_path, 'epoch' + str(epoch) + '_')
            save_checkpoint(savename + 'G.pt', G, optimizerG, learn_rate, lossG_train.steps, False, epoch + 1)
            save_checkpoint(savename + 'D.pt', D, optimizerD, learn_rate, lossD_train.steps, False, epoch + 1)

    print('Training finished')
    queue.put_nowait({'index':1, 'action': 'quit'})

def train_test():
    print('train started')
    config = Config(['..\\..\\ML\\config\\default_train_windows.yml', '..\\..\\ML\\config\\default_infer_windows.yml'])
    config.dataset_wav_path = '..\\..\\ML\\sample_dataset\\wav'
    config.dataset_text_path = '..\\..\\ML\\sample_dataset\\txt'
    config.dataset_midi_path = '..\\..\\ML\\sample_dataset\\mid'
    config.dataset_train_list = '..\\..\\ML\\sample_dataset\\train_list.txt'
    config.dataset_valid_list = '..\\..\\ML\\sample_dataset\\valid_list.txt'
    preprocess_ui.start_preprocess(config)
    start_train(config)

