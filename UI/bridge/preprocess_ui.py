import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../ML/utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../ML'))

import torch
import torchaudio
from multiprocessing import Pool
from functools import partial

import dsp
from config_parser import Config
from file_utils import create_path
from midi_utils import load_midi
from preprocess import load_text, get_phoneme_duration, align_label, files4train, zero_pad, read_file_list, make_indices


def preprocess(config, txt_file, mid_file, wav_file='', set_type='infer'):
    infer = set_type == 'infer'

    text = load_text(txt_file)
    note = load_midi(mid_file)
    text, note = align_label(text, note, config)

    # Zero pad to make 1 more iteration
    data_stride = config.spec_length
    if text.size(0) % data_stride != 0:
        pad_length = (text.size(0) // data_stride + 1) * data_stride - text.size(0)
        text = zero_pad(text, pad_length)
        note = zero_pad(note, pad_length)

    num_stride = text.size(0) // data_stride

    if not infer:
        wave = dsp.load(wav_file, config.sample_rate)[0]
        spec = dsp.spectrogram(wave, config).cpu().transpose(0, 1)  # D x T -> T x D
        spec = torch.cat((torch.zeros(config.prev_length, config.fft_size // 2 + 1), spec))

        min_length = min(text.size(0), spec.size(0))
        data_stride = config.data_stride
        num_stride = (min_length - (config.spec_length + config.prev_length)) // data_stride

    data_list = []
    for i in range(num_stride):
        text_start = i * data_stride
        t = text[text_start:text_start + config.spec_length]
        n = note[text_start:text_start + config.spec_length]

        data = dict(text=t, note=n)

        if not infer:
            spec_start = i * data_stride + config.prev_length
            s = spec[spec_start:spec_start + config.spec_length]
            s_prev = spec[spec_start - config.prev_length:spec_start]

            data = dict(text=t, note=n, spec_prev=s_prev, spec=s)

        data_list.append(data)

    if not infer:
        tmp = os.path.basename(txt_file)
        basename = os.path.splitext(tmp)[0]
        savename = os.path.join(config.feature_path, set_type, basename + '.pt')
        torch.save(data_list, savename)
        print(basename)

    return data_list


def start_preprocess(config, queue):
    set_list = ['train', 'valid']
    file_list = {}

    # Creating Path for Features
    create_path(config.feature_path, action='overwrite', verbose=False)
    for set_type in set_list:
        path = os.path.join(config.feature_path, set_type)
        create_path(path, action='overwrite')

        list_file = config.dataset_train_list if set_type == 'train' else config.dataset_valid_list
        file_list[set_type] = read_file_list(list_file)

    # Extracting Features
    if config.num_proc > 1:
        if config.use_cpu is False:
            raise AssertionError("You can not use GPU with multiprocessing.")

        p = Pool(config.num_proc)
        for set_type in set_list:
            p.map(partial(preprocess, set_type=set_type, config=config), file_list[set_type])
    else:
        queue.put_nowait({'index': 1, 'action': 'reset', 'value': len(set_list)})
        for set_type in set_list:
            queue.put_nowait({'index': 1, 'action': 'increment'})
            queue.put_nowait({'index': 2, 'action': 'reset', 'value': len(file_list[set_type])})
            for f in file_list[set_type]:
                queue.put_nowait({'index': 2, 'action': 'increment'})
                f_txt = os.path.join(config.dataset_text_path, (f + '.txt'))
                f_mid = os.path.join(config.dataset_midi_path, (f + '.mid'))
                f_wav = os.path.join(config.dataset_wav_path, (f + '.wav'))
                preprocess(config=config, txt_file=f_txt, mid_file=f_mid, wav_file=f_wav, set_type=set_type)

    # Creating Files Indices
    for set_type in set_list:
        path = os.path.join(config.feature_path, set_type)
        file_indices = make_indices(path)
        torch.save(file_indices, os.path.join(config.feature_path, set_type + '_indices.pt'))

    print("Feature saved to \'%s\'." % (config.feature_path))
    queue.put_nowait({'index':1, 'action': 'quit'})


if __name__ == "__main__":
    main()
