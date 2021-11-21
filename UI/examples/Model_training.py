#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #
#                                                     #
#    This script is one of the pyqt5Custom examples   #


import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QWidget, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QFrame, QGridLayout
from PyQt5.QtGui import QColor, QFontDatabase
from PyQt5 import QtWidgets
from pyqt5Custom import ToggleSwitch, StyledButton, ImageBox, ColorPicker, ColorPreview, DragDropFile, EmbedWindow, \
    TitleBar, CodeTextEdit, SegmentedButtonGroup, Spinner, Toast
import example_ios, Make_new_song


class Model_training(QDialog):
    def __init__(self):
        super(Model_training, self).__init__()
        QFontDatabase.addApplicationFont("data/SFPro.ttf")

        self.setMinimumSize(150, 37)
        self.setGeometry(100, 100, 890, 610)

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
        self.conlyt.setContentsMargins(70, 15, 70, 0)
        self.layout.addLayout(self.conlyt)
        h = QLabel(
            "<span style='font-size:58px; font-family:SF Pro Display; color:rgb(28,28,30);'>Model Training</span>")
        ah = QLabel("<span style='font-size:26px; font-family:SF Pro Display; color:rgb(89,89,92);'>신규 모델 학습</span>")
        h.setContentsMargins(100, 0, 0, 0)
        ah.setContentsMargins(103, 0, 0, 0)
        self.conlyt.addWidget(h)
        self.conlyt.addWidget(ah)

        self.conlyt.addSpacing(90)

        self.btnslyt = QHBoxLayout()
        self.conlyt.addLayout(self.btnslyt)
        self.btnlyt = QVBoxLayout()
        self.btnlyt.setSpacing(50)
        self.btnslyt.addLayout(self.btnlyt)

        self.btnlyt2 = QVBoxLayout()
        self.btnslyt.addLayout(self.btnlyt2)

        self.btn2 = StyledButton("Find")
        self.btn2.setFixedSize(170, 54)
        self.btn2.anim_press.speed = 7.3
        self.btn2.setStyleDict({
            "background-color": (0, 122, 255),
            "border-color": (0, 122, 255),
            "border-radius": 7,
            "color": (255, 255, 255),
            "font-family": "SF Pro Display",
            "font-size": 21,
        })
        self.btn2.setStyleDict({
            "background-color": (36, 141, 255),
            "border-color": (36, 141, 255)
        }, "hover")
        self.btn2.setStyleDict({
            "background-color": (130, 190, 255),
            "border-color": (130, 190, 255),
            "color": (255, 255, 255),
        }, "press")

        self.btnlyt.addWidget(self.btn2, alignment=Qt.AlignTop | Qt.AlignHCenter)

        self.btnlyt2.setAlignment(Qt.AlignTop)
        self.btnlyt2.addWidget(QLabel(
            "<span style='font-size:27px; font-family:SF Pro Display; color:rgb(99,99,102);'>Song</span>"))
        self.btnlyt2.addSpacing(10)

        self.btn3 = StyledButton("Find")
        self.btn3.setFixedSize(170, 54)
        self.btn3.anim_press.speed = 5
        self.btn3.setStyleDict({
            "background-color": (0, 122, 255),
            "border-color": (0, 122, 255),
            "border-radius": 7,
            "color": (255, 255, 255),
            "font-family": "SF Pro Display",
            "font-size": 21
        })
        self.btn3.setStyleDict({
            "background-color": (36, 141, 255),
            "border-color": (36, 141, 255)
        }, "hover")
        self.btn3.setStyleDict({
            "background-color": (130, 190, 255),
            "border-color": (130, 190, 255),
            "color": (255, 255, 255),
        }, "press")

        self.btnlyt.addWidget(self.btn3, alignment=Qt.AlignTop | Qt.AlignHCenter)

        self.btn1 = StyledButton("Find")
        self.btn1.setFixedSize(170, 54)
        self.btn1.anim_press.speed = 5
        self.btn1.setStyleDict({
            "background-color": (0, 122, 255),
            "border-color": (0, 122, 255),
            "border-radius": 7,
            "color": (255, 255, 255),
            "font-family": "SF Pro Display",
            "font-size": 21
        })
        self.btn1.setStyleDict({
            "background-color": (36, 141, 255),
            "border-color": (36, 141, 255)
        }, "hover")
        self.btn1.setStyleDict({
            "background-color": (130, 190, 255),
            "border-color": (130, 190, 255),
            "color": (255, 255, 255),
        }, "press")

        self.btnlyt.addWidget(self.btn1, alignment=Qt.AlignTop | Qt.AlignHCenter)

