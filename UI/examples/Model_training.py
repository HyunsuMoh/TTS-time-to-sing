#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #
#                                                     #
#    This script is one of the pyqt5Custom examples   #

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../ML/utils"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../bridge"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../pyqt5Custom"))
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QDialog, QPushButton, QHBoxLayout, QFileDialog, QVBoxLayout, QLabel, QCheckBox
from PyQt5.QtGui import QColor, QFontDatabase, QIcon, QPixmap
from pyqt5Custom import StyledButton, Spinner
from input_config import input_config
from config_parser import Config
from training_ui import start_train
from preprocess_ui import start_preprocess
from embedwindow import EmbedWindow
from progressbar import Progressbar
from multiprocessing import Process, Queue
from threading import Thread


class Model_training(QDialog):
    def __init__(self, switchWidget, progressBar):
        def preprocess():
            pbtemp = Progressbar((lambda x: x))
            queue = Queue()
            p_pp = Process(target=start_preprocess, args=(self.config, queue,))
            t_pp = Thread(target=pbtemp.update, args=(queue,))
            p_pp.start()
            t_pp.start()
            pbtemp.show()

        def train():
            queue = Queue()
            p_train = Process(target=start_train, args=(self.config, queue,))
            t_train = Thread(target=progressBar.update, args=(queue,))
            p_train.start()
            t_train.start()
            switchWidget(3)

        super(Model_training, self).__init__()
        QFontDatabase.addApplicationFont("data/SFPro.ttf")
        self.setMinimumSize(150, 37)
        self.setGeometry(100, 100, 890, 610)
        self.config = Config([os.path.join(os.path.dirname(__file__), "../bridge/config/default_train.yml")])
        self.configWidget = input_config(self, 'train', self.config)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(255, 255, 255))
        self.setPalette(p)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignVCenter)

        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.conlyt = QVBoxLayout()
        self.conlyt.setSpacing(0)
        # self.conlyt.setContentsMargins(0, 0, 0, 0)
        self.conlyt.setContentsMargins(70, 15, 70, 60)
        self.switchButton = QHBoxLayout()
        self.switchButton.setContentsMargins(100, 0, 0, 30)
        self.switchButton.setSpacing(200)
        self.layout.addLayout(self.conlyt)
        self.layout.addLayout(self.switchButton)
        h = QLabel(
            "<span style='font-size:40px; font-family:SF Pro Display; color:rgb(28,28,30);'>\U0001F5A5 Model Training</span>")
        ah = QLabel(
            "<span style='font-size:26px; font-family:SF Pro Display; color:rgb(89,89,92);'>\U0001F5C2 File & Directory selection</span>")
        h.setContentsMargins(100, 15, 0, 0)
        ah.setContentsMargins(110, 10, 0, 0)

        self.conlyt.addWidget(h)
        self.conlyt.addWidget(ah)
        self.conlyt.addSpacing(25)
        self.next = StyledButton("Config setting")
        self.back = StyledButton("Back")
        self.start = StyledButton("Training Start", icon=Spinner(1.5, QColor(0, 255, 255)))
        self.preprocess = StyledButton("Preprocess")
        self.back.clicked.connect(lambda: switchWidget(0))
        self.next.clicked.connect(self.configWidget.load)
        self.start.clicked.connect(train)
        self.preprocess.clicked.connect(preprocess)
        # self.start.clicked.connect()

        self.switchButton.addWidget(self.back)
        self.switchButton.addWidget(self.next)
        self.switchButton.addWidget(self.start)
        self.switchButton.addWidget(self.preprocess)
        self.list = QHBoxLayout()
        self.list.setSpacing(15)
        self.conlyt.addLayout(self.list)

        self.findBtns = QVBoxLayout()
        self.texts = QVBoxLayout()
        self.labels = QVBoxLayout()
        self.lights = QVBoxLayout()
        self.findBtns.setSpacing(33)
        self.texts.setSpacing(27)
        self.lights.setSpacing(27)
        self.texts.setContentsMargins(20, 0, 0, 0)
        self.labels.setSpacing(35)
        self.lights.setAlignment(Qt.AlignLeft)
        self.findBtns.setAlignment(Qt.AlignLeft)
        self.list.addLayout(self.texts)
        self.list.addLayout(self.lights)
        self.list.addLayout(self.findBtns)
        self.list.addLayout(self.labels)
        self.ewlist = list()

        button_style = {
            'normal': {
                "background-color": (154, 84, 237),
                "border-color": (154, 84, 237),
                "border-radius": 7,
                "color": (255, 255, 255),
                "font-family": "SF Pro Display",
                "font-size": 21,
            },
            'hover': {
                "background-color": (102, 71, 214),
                "border-color": (102, 71, 214),
            },
            'press': {
                "background-color": (102, 71, 214),
                "border-color": (102, 71, 214),
            }
        }

        button_style2 = {
            'normal': {
                "background-color": (255, 255, 255),
                "border-color": (154, 84, 237),
                "border-radius": 7,
                "color": (154, 84, 237),
                "font-family": "SF Pro Display",
                "font-size": 16,
            },
            'hover': {
                "background-color": (154, 84, 237),
                "border-color": (154, 84, 237),
                "color": (255, 255, 255),
                "font-size": 16,
            },
            'press': {
                "background-color": (154, 84, 237),
                "border-color": (154, 84, 237),
                "color": (255, 255, 255),
                "font-size": 16,
            }
        }

        self.back.setFixedSize(100, 54)
        self.back.anim_press.speed = 7.3
        self.back.setStyleDict(button_style2['normal'], "default")
        self.back.setStyleDict(button_style2['hover'], "hover")
        self.back.setStyleDict(button_style2['press'], "press")

        self.next.setFixedSize(120, 54)
        self.next.anim_press.speed = 7.3
        self.next.setStyleDict(button_style2['normal'], "default")
        self.next.setStyleDict(button_style2['hover'], "hover")
        self.next.setStyleDict(button_style2['press'], "press")

        self.start.setFixedSize(120, 54)
        self.start.setStyleDict(button_style2['normal'], "default")
        self.start.setStyleDict(button_style2['hover'], "hover")
        self.start.setStyleDict(button_style2['press'], "press")

        self.preprocess.setFixedSize(120, 54)
        self.preprocess.setStyleDict(button_style2['normal'], "default")
        self.preprocess.setStyleDict(button_style2['hover'], "hover")
        self.preprocess.setStyleDict(button_style2['press'], "press")

        self.label1 = QLabel('', self)
        self.text1 = QLabel(
            "<span style='font-size:21px; font-family:SF Pro Display; color:rgb(28,28,30);'>Dataset text path</span>")
        self.btn1 = StyledButton("Find")
        self.btn1.setFixedSize(100, 34)
        self.btn1.anim_press.speed = 7.3
        self.btn1.setStyleDict(button_style['normal'])
        self.btn1.setStyleDict(button_style['hover'], "hover")
        self.btn1.setStyleDict(button_style['press'], "press")
        self.btn1.clicked.connect(lambda: self.dirSearch(self.label1, "dataset_text_path"))
        self.btn1.setContentsMargins(0, 3, 0, 0)
        self.light1 = QPushButton('')
        self.light1.setStyleSheet("background-color:#ffffff")
        self.light1.setStyleSheet("border: None")
        self.light1.setIcon(QIcon('bulb.png'))
        self.light1.setIconSize(QSize(35,35))
        self.light1.clicked.connect(lambda : self.infoWindow("Dataset text path", "Path for raw dataset containing .txt files"))
        self.text1.setContentsMargins(20, 3, 0, 0)
        self.label1.setContentsMargins(20, 5, 0, 0)
        self.light1.setContentsMargins(0, 3, 0, 0)

        self.label2 = QLabel('', self)
        self.text2 = QLabel(
            "<span style='font-size:21px; font-family:SF Pro Display; color:rgb(28,28,30);'>Dataset midi path</span>")
        self.btn2 = StyledButton("Find")
        self.btn2.setFixedSize(100, 34)
        self.btn2.anim_press.speed = 7.3
        self.btn2.setStyleDict(button_style['normal'])
        self.btn2.setStyleDict(button_style['hover'], "hover")
        self.btn2.setStyleDict(button_style['press'], "press")
        self.btn2.clicked.connect(lambda: self.dirSearch(self.label2, "dataset_midi_path"))
        self.light2 = QPushButton('')
        self.light2.setStyleSheet("background-color:#ffffff")
        self.light2.setStyleSheet("border: None")
        self.light2.setIcon(QIcon('bulb.png'))
        self.light2.setIconSize(QSize(35, 35))
        self.light2.clicked.connect(
            lambda: self.infoWindow("Dataset midi path", "Path for raw dataset containing .mid files"))
        self.btn2.setContentsMargins(0, 3, 0, 0)
        self.text2.setContentsMargins(20, 3, 0, 0)
        self.label2.setContentsMargins(0, 5, 0, 0)

        self.label3 = QLabel('', self)
        self.text3 = QLabel(
            "<span style='font-size:21px; font-family:SF Pro Display; color:rgb(28,28,30);'>Dataset wav path</span>")
        self.btn3 = StyledButton("Find")
        self.btn3.setFixedSize(100, 34)
        self.btn3.anim_press.speed = 7.3
        self.btn3.setStyleDict(button_style['normal'])
        self.btn3.setStyleDict(button_style['hover'], "hover")
        self.btn3.setStyleDict(button_style['press'], "press")
        self.btn3.clicked.connect(lambda: self.dirSearch(self.label3, "dataset_wav_path"))
        self.light3 = QPushButton('')
        self.light3.setStyleSheet("background-color:#ffffff")
        self.light3.setStyleSheet("border: None")
        self.light3.setIcon(QIcon('bulb.png'))
        self.light3.setIconSize(QSize(35, 35))
        self.light3.clicked.connect(
            lambda: self.infoWindow("Dataset wav path", "Path for raw dataset containing .wav files"))
        self.text3.setContentsMargins(20, 3, 0, 0)
        self.label3.setContentsMargins(20, 5, 0, 0)

        self.label4 = QLabel('', self)
        self.text4 = QLabel(
            "<span style='font-size:21px; font-family:SF Pro Display; color:rgb(28,28,30);'>Feature path</span>")
        self.btn4 = StyledButton("Find")
        self.btn4.setFixedSize(100, 34)
        self.btn4.anim_press.speed = 7.3
        self.btn4.setStyleDict(button_style['normal'])
        self.btn4.setStyleDict(button_style['hover'], "hover")
        self.btn4.setStyleDict(button_style['press'], "press")
        self.btn4.clicked.connect(lambda: self.dirSearch(self.label4, "feature_path"))
        self.light4 = QPushButton('')
        self.light4.setStyleSheet("background-color:#ffffff")
        self.light4.setStyleSheet("border: None")
        self.light4.setIcon(QIcon('bulb.png'))
        self.light4.setIconSize(QSize(35, 35))
        self.light4.clicked.connect(
            lambda: self.infoWindow("Feature path", "Path for feature created using preprocess.py"))
        self.text4.setContentsMargins(20, 3, 0, 0)
        self.label4.setContentsMargins(20, 5, 0, 0)

        self.label5 = QLabel('', self)
        self.text5 = QLabel(
            "<span style='font-size:21px; font-family:SF Pro Display; color:rgb(28,28,30);'>Checkpoint path</span>")
        self.btn5 = StyledButton("Find")
        self.btn5.setFixedSize(100, 34)
        self.btn5.anim_press.speed = 7.3
        self.btn5.setStyleDict(button_style['normal'])
        self.btn5.setStyleDict(button_style['hover'], "hover")
        self.btn5.setStyleDict(button_style['press'], "press")
        self.btn5.clicked.connect(lambda: self.dirSearch(self.label5, "checkpoint_path"))
        self.light5 = QPushButton('')
        self.light5.setStyleSheet("background-color:#ffffff")
        self.light5.setStyleSheet("border: None")
        self.light5.setIcon(QIcon('bulb.png'))
        self.light5.setIconSize(QSize(35, 35))
        self.light5.clicked.connect(
            lambda: self.infoWindow("Checkpoint path", "Path for checkpoint and tensorboard log created when training"))
        self.text5.setContentsMargins(20, 3, 0, 0)
        self.label5.setContentsMargins(20, 5, 0, 0)

        self.label6 = QLabel('', self)
        self.text6 = QLabel(
            "<span style='font-size:21px; font-family:SF Pro Display; color:rgb(28,28,30);'>Load checkpoint</span>")
        self.light6 = QPushButton('')
        self.light6.setStyleSheet("background-color:#ffffff")
        self.light6.setStyleSheet("border: None")
        self.light6.setIcon(QIcon('bulb.png'))
        self.light6.setIconSize(QSize(35, 35))
        self.light6.clicked.connect(
            lambda: self.infoWindow("Load checkpoint", "Option to choose whether to resume learning or proceed with new learning using saved checkpoints.T"))
        self.checkbox6 = QCheckBox("")
        self.checkbox6.setStyleSheet(
            "QCheckBox::indicator"
            "{"
            "width :20px;"
            "height :20px;"
            "}"
        )
        self.checkbox6.setContentsMargins(0, 0, 0, 0)
        self.checkbox6.stateChanged.connect(self.changeCheckState)
        self.text6.setContentsMargins(20, 3, 0, 0)
        self.label6.setContentsMargins(23, 5, 0, 0)

        self.label7 = QLabel('', self)
        self.text7 = QLabel(
            "<span style='font-size:20px; font-family:SF Pro Display; color:rgb(28,28,30);'>Loaded checkpoint path G</span>")
        self.btn7 = StyledButton("Find")
        self.btn7.setFixedSize(100, 34)
        self.btn7.anim_press.speed = 7.3
        self.btn7.setStyleDict(button_style['normal'])
        self.btn7.setStyleDict(button_style['hover'], "hover")
        self.btn7.setStyleDict(button_style['press'], "press")
        self.btn7.clicked.connect(lambda: self.fileSearch(self.label7, "loaded_checkpoint_path_G", '*.pt'))
        self.light7 = QPushButton('')
        self.light7.setStyleSheet("background-color:#ffffff")
        self.light7.setStyleSheet("border: None")
        self.light7.setIcon(QIcon('bulb.png'))
        self.light7.setIconSize(QSize(35, 35))
        self.light7.clicked.connect(
            lambda: self.infoWindow("Loaded checkpoint path G", "Path for checkpoint(Generator)"))
        self.text7.setContentsMargins(20, 3, 0, 0)
        self.label7.setContentsMargins(20, 5, 0, 0)

        self.label8 = QLabel('', self)
        self.text8 = QLabel(
            "<span style='font-size:20px; font-family:SF Pro Display; color:rgb(28,28,30);'>Loaded checkpoint path D</span>")
        self.btn8 = StyledButton("Find")
        self.btn8.setFixedSize(100, 34)
        self.btn8.anim_press.speed = 7.3
        self.btn8.setStyleDict(button_style['normal'])
        self.btn8.setStyleDict(button_style['hover'], "hover")
        self.btn8.setStyleDict(button_style['press'], "press")
        self.btn8.clicked.connect(lambda: self.fileSearch(self.label8, "loaded_checkpoint_path_D", '*.pt'))
        self.light8 = QPushButton('')
        self.light8.setStyleSheet("background-color:#ffffff")
        self.light8.setStyleSheet("border: None")
        self.light8.setIcon(QIcon('bulb.png'))
        self.light8.setIconSize(QSize(35, 35))
        self.light8.clicked.connect(
            lambda: self.infoWindow("Loaded checkpoint path D", "Path for checkpoint(Discriminator)"))
        self.text8.setContentsMargins(20, 3, 0, 0)
        self.label8.setContentsMargins(20, 5, 0, 0)

        self.label9 = QLabel('', self)
        self.text9 = QLabel(
            "<span style='font-size:20px; font-family:SF Pro Display; color:rgb(28,28,30);'>Dataset train list</span>")
        self.btn9 = StyledButton("Find")
        self.btn9.setFixedSize(100, 34)
        self.btn9.anim_press.speed = 7.3
        self.btn9.setStyleDict(button_style['normal'])
        self.btn9.setStyleDict(button_style['hover'], "hover")
        self.btn9.setStyleDict(button_style['press'], "press")
        self.btn9.clicked.connect(lambda: self.fileSearch(self.label9, "dataset_train_list", '*.txt'))
        self.light9 = QPushButton('')
        self.light9.setStyleSheet("background-color:#ffffff")
        self.light9.setStyleSheet("border: None")
        self.light9.setIcon(QIcon('bulb.png'))
        self.light9.setIconSize(QSize(35, 35))
        self.light9.clicked.connect(
            lambda: self.infoWindow("Dataset train list", "List for training dataset"))
        self.text9.setContentsMargins(20, 3, 0, 0)
        self.label9.setContentsMargins(20, 5, 0, 0)

        self.label10 = QLabel('', self)
        self.text10 = QLabel(
            "<span style='font-size:20px; font-family:SF Pro Display; color:rgb(28,28,30);'>Dataset valid list</span>")
        self.btn10 = StyledButton("Find")
        self.btn10.setFixedSize(100, 34)
        self.btn10.anim_press.speed = 7.3
        self.btn10.setStyleDict(button_style['normal'])
        self.btn10.setStyleDict(button_style['hover'], "hover")
        self.btn10.setStyleDict(button_style['press'], "press")
        self.btn10.clicked.connect(lambda: self.fileSearch(self.label10, "dataset_valid_list", '*.txt'))
        self.light10 = QPushButton('')
        self.light10.setStyleSheet("background-color:#ffffff")
        self.light10.setStyleSheet("border: None")
        self.light10.setIcon(QIcon('bulb.png'))
        self.light10.setIconSize(QSize(35, 35))
        self.light10.clicked.connect(
            lambda: self.infoWindow("Dataset valid list", "List for validating dataset"))
        self.text10.setContentsMargins(20, 3, 0, 0)
        self.label10.setContentsMargins(20, 5, 0, 0)

        self.texts.addWidget(self.text1)
        self.texts.addWidget(self.text2)
        self.texts.addWidget(self.text3)
        self.texts.addWidget(self.text4)
        self.texts.addWidget(self.text5)
        self.texts.addWidget(self.text6)
        self.texts.addWidget(self.text7)
        self.texts.addWidget(self.text8)
        self.texts.addWidget(self.text9)
        self.texts.addWidget(self.text10)

        self.findBtns.addWidget(self.btn1)
        self.findBtns.addWidget(self.btn2)
        self.findBtns.addWidget(self.btn3)
        self.findBtns.addWidget(self.btn4)
        self.findBtns.addWidget(self.btn5)
        self.findBtns.addWidget(self.checkbox6)
        self.findBtns.addWidget(self.btn7)
        self.findBtns.addWidget(self.btn8)
        self.findBtns.addWidget(self.btn9)
        self.findBtns.addWidget(self.btn10)

        self.labels.addWidget(self.label1)
        self.labels.addWidget(self.label2)
        self.labels.addWidget(self.label3)
        self.labels.addWidget(self.label4)
        self.labels.addWidget(self.label5)
        self.labels.addWidget(self.label6)
        self.labels.addWidget(self.label7)
        self.labels.addWidget(self.label8)
        self.labels.addWidget(self.label9)
        self.labels.addWidget(self.label10)

        self.lights.addWidget(self.light1)
        self.lights.addWidget(self.light2)
        self.lights.addWidget(self.light3)
        self.lights.addWidget(self.light4)
        self.lights.addWidget(self.light5)
        self.lights.addWidget(self.light6)
        self.lights.addWidget(self.light7)
        self.lights.addWidget(self.light8)
        self.lights.addWidget(self.light9)
        self.lights.addWidget(self.light10)



    def changeCheckState(self, state):
        if state == Qt.Checked:
            self.label6.setText("Continue learning with the selected checkpoint")
            setattr(self.config, "load_checkpoint", True)
        else:
            self.label6.setText("Create a new checkpoint to proceed with the learning")
            setattr(self.config, "load_checkpoint", False)

    def fileSearch(self, labelName, configLabel, extension):
        fileOpen = QFileDialog.getOpenFileName(self, 'Open file', filter=extension)
        filename = fileOpen[0]
        labelName.setText(filename)
        setattr(self.config, configLabel, filename)

    def dirSearch(self, labelName, configLabel):
        filename = QFileDialog.getExistingDirectory(self, 'Find folder')
        labelName.setText(filename)
        setattr(self.config, configLabel, filename)

    def infoWindow(self, _title, _content):
        content = QLabel()
        content.setText(_content)
        ew = EmbedWindow(self, title=_title)
        ew.headerColor = QColor(154, 84, 237)
        ew.content.setAlignment(Qt.AlignVCenter)
        ew.content.addWidget(content)
        ew.closed.connect(lambda : self.ewlist.remove(ew))
        self.ewlist.append(ew)
        ew.show()
        ew.raise_()

    def update(self):
        self.label1.setText(self.config.dataset_text_path)
        self.label2.setText(self.config.dataset_midi_path)
        self.label3.setText(self.config.dataset_wav_path)
        self.label4.setText(self.config.feature_path)
        self.label5.setText(self.config.checkpoint_path)
        self.label7.setText(self.config.loaded_checkpoint_path_G)
        self.label8.setText(self.config.loaded_checkpoint_path_D)
        self.label9.setText(self.config.dataset_train_list)
        self.label10.setText(self.config.dataset_valid_list)
        self.checkbox6.setChecked(self.config.load_checkpoint)