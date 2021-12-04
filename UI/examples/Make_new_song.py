#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #
#                                                     #
#    This script is one of the pyqt5Custom examples   #

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../pyqt5Custom"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../bridge"))

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../ML/utils"))
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QWidget, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QFrame, QGridLayout,QFileDialog, QLabel
from PyQt5.QtGui import QColor, QFontDatabase, QFont
from pyqt5Custom import ToggleSwitch, StyledButton, ColorPicker, ColorPreview, DragDropFile, EmbedWindow, \
    TitleBar, CodeTextEdit, SegmentedButtonGroup, Spinner, Toast
from inference_ui import infer_test
from input_config import input_config
from config_parser import Config

from input_config import input_config
from config_parser import Config
# from training_ui import train_test

class Make_new_song(QDialog):
    def __init__(self, switchWidget):
        super(Make_new_song, self).__init__()
        QFontDatabase.addApplicationFont("data/BMDOHYEON_ttf.ttf")
        self.setMinimumSize(150, 37)
        self.setGeometry(100, 100, 890, 610)
        self.config = Config([os.path.join(os.path.dirname(__file__), "../bridge/config/default_infer.yml"),
                              os.path.join(os.path.dirname(__file__), "../bridge/config/default_train.yml")])
        self.config.checkpoint_file = os.path.join(__file__[0:__file__.find('UI')], 'default_checkpoint.pt')
        self.configWidget = input_config('infer', self.config)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(255, 255, 255))
        self.setPalette(p)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)

        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.conlyt = QVBoxLayout()
        self.conlyt.setSpacing(0)
        self.conlyt.setContentsMargins(70,15,70,60)
        self.switchButton = QHBoxLayout()
        self.switchButton.setSpacing(50)
        self.layout.addLayout(self.conlyt)
        self.layout.addLayout(self.switchButton)
        h = QLabel(
            "<span style='font-size:48px; font-family:SF Pro Display; color:rgb(28,28,30);'>\U0001F399 Making new songs</span>")
        ah = QLabel(
            "<span style='font-size:24px; font-family:SF Pro Display; color:rgb(89,89,92);'>기존 모델들을 바탕으로 새로운 노래 생성</span>")

        self.conlyt.addWidget(h)
        self.conlyt.addWidget(ah)
        self.conlyt.addSpacing(90)

        self.next = StyledButton("Config setting")
        self.back = StyledButton("Back")
        self.back.clicked.connect(lambda: switchWidget(0))
        self.next.clicked.connect(self.configWidget.load)


        self.switchButton.addWidget(self.back)
        self.switchButton.addWidget(self.next)

        self.list = QHBoxLayout()
        self.list.setSpacing(15)
        self.conlyt.addLayout(self.list)

        self.findBtns = QVBoxLayout()
        self.texts = QVBoxLayout()
        self.labels = QVBoxLayout()
        self.findBtns.setSpacing(35)
        self.texts.setSpacing(33)
        self.texts.setContentsMargins(50, 0, 30, 0)
        self.labels.setSpacing(40)
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
                "font-size": 18,
            },
            'hover': {
                "background-color": (154, 84, 237),
                "border-color": (154, 84, 237),
                "color": (255, 255, 255),
                "font-size": 18,
            },
            'press': {
                "background-color": (154, 84, 237),
                "border-color": (154, 84, 237),
                "color": (255, 255, 255),
                "font-size": 18,
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

        self.label1 = QLabel('', self)
        self.text1 = QLabel(
            "<span style='font-size:24px; font-family:SF Pro Display; color:rgb(28,28,30);'>Default voice</span>")
        self.btn1 = StyledButton("Choose")
        self.btn1.setFixedSize(100, 34)
        self.btn1.anim_press.speed = 7.3
        self.btn1.setStyleDict(button_style['normal'])
        self.btn1.setStyleDict(button_style['hover'], "hover")
        self.btn1.setStyleDict(button_style['press'], "press")
        self.btn1.clicked.connect(lambda: self.fileSearch(self.label1, "checkpoint_file", '*.pt'))
        self.btn1.setContentsMargins(0, 3, 0, 0)
        self.text1.setContentsMargins(20, 3, 0, 0)
        self.label1.setContentsMargins(20, 5, 0, 0)

        self.label2 = QLabel('', self)
        self.text2 = QLabel(
            "<span style='font-size:24px; font-family:SF Pro Display; color:rgb(28,28,30);'>Another voice</span>")
        self.btn2 = StyledButton("Choose")
        self.btn2.setFixedSize(100, 34)
        self.btn2.anim_press.speed = 7.3
        self.btn2.setStyleDict(button_style['normal'])
        self.btn2.setStyleDict(button_style['hover'], "hover")
        self.btn2.setStyleDict(button_style['press'], "press")
        self.btn2.clicked.connect(lambda: self.fileSearch(self.label2, "checkpoint_file", '*.pt'))
        self.btn2.setContentsMargins(0, 3, 0, 0)
        self.text2.setContentsMargins(20, 3, 0, 0)
        self.label2.setContentsMargins(20, 5, 0, 0)

        self.label3 = QLabel('', self)
        self.text3 = QLabel(
            "<span style='font-size:24px; font-family:SF Pro Display; color:rgb(28,28,30);'>Lyrics</span>")
        self.btn3 = StyledButton("Find")
        self.btn3.setFixedSize(100, 34)
        self.btn3.anim_press.speed = 7.3
        self.btn3.setStyleDict(button_style['normal'])
        self.btn3.setStyleDict(button_style['hover'], "hover")
        self.btn3.setStyleDict(button_style['press'], "press")
        self.btn3.clicked.connect(lambda: self.fileSearch(self.label3, "text_file", '*.txt'))
        self.btn3.setContentsMargins(0, 3, 0, 0)
        self.text3.setContentsMargins(20, 3, 0, 0)
        self.label3.setContentsMargins(20, 5, 0, 0)

        self.label4 = QLabel('', self)
        self.text4 = QLabel(
            "<span style='font-size:24px; font-family:SF Pro Display; color:rgb(28,28,30);'>Sheet Music</span>")
        self.btn4 = StyledButton("Find")
        self.btn4.setFixedSize(100, 34)
        self.btn4.anim_press.speed = 7.3
        self.btn4.setStyleDict(button_style['normal'])
        self.btn4.setStyleDict(button_style['hover'], "hover")
        self.btn4.setStyleDict(button_style['press'], "press")
        self.btn4.clicked.connect(lambda: self.fileSearch(self.label4, "midi_file", '*.mid'))
        self.text4.setContentsMargins(20, 3, 0, 0)
        self.label4.setContentsMargins(20, 5, 0, 0)

        self.label5 = QLabel('', self)
        self.text5 = QLabel(
            "<span style='font-size:24px; font-family:SF Pro Display; color:rgb(28,28,30);'>Target path</span>")
        self.btn5 = StyledButton("Choose")
        self.btn5.setFixedSize(100, 34)
        self.btn5.anim_press.speed = 7.3
        self.btn5.setStyleDict(button_style['normal'])
        self.btn5.setStyleDict(button_style['hover'], "hover")
        self.btn5.setStyleDict(button_style['press'], "press")
        self.btn5.clicked.connect(lambda: self.fileSave(self.label5, '*.wav'))
        self.text5.setContentsMargins(20, 3, 0, 0)
        self.label5.setContentsMargins(20, 5, 0, 0)

        self.texts.addWidget(self.text1)
        self.texts.addWidget(self.text2)
        self.texts.addWidget(self.text5)
        self.texts.addWidget(self.text3)
        self.texts.addWidget(self.text4)

        self.findBtns.addWidget(self.btn1)
        self.findBtns.addWidget(self.btn2)
        self.findBtns.addWidget(self.btn5)
        self.findBtns.addWidget(self.btn3)
        self.findBtns.addWidget(self.btn4)

        self.labels.addWidget(self.label1)
        self.labels.addWidget(self.label2)
        self.labels.addWidget(self.label5)
        self.labels.addWidget(self.label3)
        self.labels.addWidget(self.label4)

        self.btnslyt = QVBoxLayout()
        self.conlyt.addLayout(self.btnslyt)
        self.btnlyt2 = QVBoxLayout()
        self.btnlyt2.setSpacing(16)
        self.btnslyt.addLayout(self.btnlyt2)


        self.ibtnl = StyledButton("Making New Songs", icon=Spinner(1.5, QColor(0, 255, 255)))
        self.ibtnl.setFixedSize(200, 47)
        self.ibtnl.anim_press.speed = 7.3

        self.ibtnl.setStyleDict(button_style2['normal'], "default")
        self.ibtnl.setStyleDict(button_style2['hover'], "hover")
        self.ibtnl.setStyleDict(button_style2['press'], "press")

        self.ibtnl.clicked.connect(infer_test)

        self.btnlyt2.addSpacing(15)
        self.btnlyt2.addWidget(self.ibtnl, alignment=Qt.AlignHCenter)

        self.toast = Toast(self, text="Making new Songs", icon=Spinner(1.3, QColor(255, 255, 255)))
        self.toast.setFixedWidth(287)
        self.toast.setStyleDict({
            "font-family": "SF Pro Display",
            "font-size": 17
        })

        self.ibtnl.clicked.connect(lambda: self.toast.rise(3))

    def fileSearch(self, labelName, configLabel, extension):
        fileOpen = QFileDialog.getOpenFileName(self, 'open file', './', filter=extension)
        filename = fileOpen[0]
        labelName.setText(filename)
        setattr(self.config, configLabel, filename)

    def fileSave(self, labelName, extension):
        filename = QFileDialog.getSaveFileName(self, 'Target path', './', filter=extension)[0]
        labelName.setText(filename)
        if filename:
            setattr(self.config, 'target_path', './')

    def default_checkpoint(self, labelName):
        config.checkpoint_file = '..\\..\\..\\pretrained_sample.pt'
        labelName.setText(config.checkpoint_file)

    def CheckPointSearch(self, labelName):
        filename = ""
        #filename = Searchfile.add_open(self, filename)
        filename = QFileDialog.getOpenFileName(self,'Load Checkpoint', '..\\..\\..\\', filter = '*.pt')
        labelName.setText(filename)
