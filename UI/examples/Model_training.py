#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #
#                                                     #
#    This script is one of the pyqt5Custom examples   #

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../ML/utils"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../bridge"))
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QFileDialog, QVBoxLayout, QLabel, QCheckBox
from PyQt5.QtGui import QColor, QFontDatabase
from pyqt5Custom import StyledButton, Spinner
from input_config import input_config
from config_parser import Config
from training_ui import train_test
from preprocess_ui import start_preprocess


class Model_training(QDialog):
    def __init__(self, switchWidget):
        super(Model_training, self).__init__()
        QFontDatabase.addApplicationFont("data/SFPro.ttf")
        self.setMinimumSize(150, 37)
        self.setGeometry(100, 100, 890, 610)
        self.config = Config([os.path.join(os.path.dirname(__file__), "../bridge/config/default_train.yml")])
        self.configWidget = input_config('train', self.config)

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
        self.start.clicked.connect(train_test)
        self.preprocess.clicked.connect(lambda: start_preprocess(self.config))
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
        self.findBtns.setSpacing(33)
        self.texts.setSpacing(27)
        self.texts.setContentsMargins(40, 0, 10, 0)
        self.labels.setSpacing(35)
        self.findBtns.setAlignment(Qt.AlignVCenter)
        self.list.addLayout(self.texts)
        self.list.addLayout(self.findBtns)
        self.list.addLayout(self.labels)

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
        self.text1.setContentsMargins(20, 3, 0, 0)
        self.label1.setContentsMargins(20, 5, 0, 0)

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
        self.btn2.setContentsMargins(0, 3, 0, 0)
        self.text2.setContentsMargins(20, 3, 0, 0)
        self.label2.setContentsMargins(20, 5, 0, 0)

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
        self.text5.setContentsMargins(20, 3, 0, 0)
        self.label5.setContentsMargins(20, 5, 0, 0)

        self.label6 = QLabel('', self)
        self.text6 = QLabel(
            "<span style='font-size:21px; font-family:SF Pro Display; color:rgb(28,28,30);'>Load checkpoint</span>")
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
