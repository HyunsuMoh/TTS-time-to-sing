#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #
#                                                     #
#    This script is one of the pyqt5Custom examples   #


import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QFileDialog, QWidget, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QFrame, QGridLayout
from PyQt5.QtGui import QColor, QFontDatabase
from PyQt5 import QtWidgets
from pyqt5Custom import ToggleSwitch, StyledButton, ImageBox, ColorPicker, ColorPreview, DragDropFile, EmbedWindow, \
    TitleBar, CodeTextEdit, SegmentedButtonGroup, Spinner, Toast
import example_ios, Make_new_song
from Searchfile import Searchfile
import example_ios



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
        self.back = StyledButton("Back")
        self.back.clicked.connect(self.gotoPrev)
        h = QLabel(
            "<span style='font-size:58px; font-family:SF Pro Display; color:rgb(28,28,30);'>Model Training</span>")
        ah = QLabel("<span style='font-size:26px; font-family:SF Pro Display; color:rgb(89,89,92);'>신규 모델 학습</span>")
        h.setContentsMargins(100, 50, 0, 0)
        ah.setContentsMargins(100, 50, 0, 0)
        print("here3")
        self.conlyt.addWidget(self.back)
        self.conlyt.addWidget(h)
        self.conlyt.addWidget(ah)

        self.conlyt.addSpacing(90)
        self.back.setFixedSize(100, 54)
        self.back.anim_press.speed = 7.3
        self.back.setStyleDict({
            "background-color": (0, 0, 0),
            "border-color": (0, 0, 0),
            "border-radius": 7,
            "color": (255, 255, 255),
            "font-family": "SF Pro Display",
            "font-size": 21,
        })

        self.label1 = QLabel('label1', self)
        self.label2 = QLabel('label2', self)
        self.label3 = QLabel('label3', self)
        self.btnslyt = QHBoxLayout()
        self.conlyt.addLayout(self.btnslyt)
        self.btnlyt = QVBoxLayout()
        self.labellyt = QVBoxLayout()
        self.btnlyt = QVBoxLayout()
        self.btnlyt.setSpacing(50)
        self.btnslyt.addLayout(self.btnlyt)

        self.btnlyt2 = QVBoxLayout()
        self.btnlyt.setSpacing(30)
        self.labellyt.setSpacing(30)
        self.btnlyt2.setSpacing(55)
        self.btnlyt2.setContentsMargins(100, 30, 0, 30) #L,T,R,B
        self.btnlyt.setContentsMargins(100, 30, 50, 30)
        self.labellyt.setContentsMargins(100, 30, 0, 30)
        self.btnslyt.addLayout(self.btnlyt2)
        self.btnslyt.addLayout(self.btnlyt)
        self.btnslyt.addLayout(self.labellyt)

        self.labellyt.addWidget(self.label1, alignment=Qt.AlignTop | Qt.AlignLeft)
        self.btn2 = StyledButton("Find")
        self.btn2.setFixedSize(170, 54)
        self.btn2.anim_press.speed = 7.3
        self.btn2.setStyleDict({
            "background-color": (154, 84, 237),
            "border-color": (154, 84, 237),
            "border-radius": 7,
            "color": (255, 255, 255),
            "font-family": "SF Pro Display",
            "font-size": 21,
        })
        self.btn2.setStyleDict({
            "background-color": (102, 71, 214),
            "border-color": (102, 71, 214)
        }, "hover")
        self.btn2.setStyleDict({
            "background-color": (102, 71, 214),
            "border-color": (102, 71, 214),
            "color": (255, 255, 255),
        }, "press")
        self.btn2.clicked.connect(self.fileSearch)
        self.btnlyt.addWidget(self.btn2, alignment=Qt.AlignTop | Qt.AlignHCenter | Qt.AlignLeft)
        self.btnlyt2.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.btnlyt2.addWidget(QLabel(
            "<span style='font-size:27px; font-family:SF Pro Display; color:rgb(99,99,102);'>Song</span>"))
        self.btnlyt2.addWidget(QLabel(
            "<span style='font-size:27px; font-family:SF Pro Display; color:rgb(99,99,102);'>Lyrics</span>"))
        self.btnlyt2.addWidget(QLabel(
            "<span style='font-size:27px; font-family:SF Pro Display; color:rgb(99,99,102);'>Sheet music</span>"))

        self.labellyt.addWidget(self.label2, alignment=Qt.AlignTop | Qt.AlignHCenter | Qt.AlignLeft)
        self.btn3 = StyledButton("Find")
        self.btn3.setFixedSize(170, 54)
        self.btn3.anim_press.speed = 5
        self.btn3.setStyleDict({
            "background-color": (154, 84, 237),
            "border-color": (154, 84, 237),
            "border-radius": 7,
            "color": (255, 255, 255),
            "font-family": "SF Pro Display",
            "font-size": 21
        })
        self.btn3.setStyleDict({
            "background-color": (102, 71, 214),
            "border-color": (102, 71, 214)
        }, "hover")
        self.btn3.setStyleDict({
            "background-color": (102, 71, 214),
            "border-color": (102, 71, 214),
            "color": (255, 255, 255),
        }, "press")
        self.btn3.clicked.connect(self.fileSearch)
        self.btnlyt.addWidget(self.btn3, alignment=Qt.AlignTop | Qt.AlignHCenter | Qt.AlignLeft)
        self.labellyt.addWidget(self.label3, alignment=Qt.AlignTop | Qt.AlignHCenter | Qt.AlignLeft)
        self.btn1 = StyledButton("Find")
        self.btn1.setFixedSize(170, 54)
        self.btn1.anim_press.speed = 5
        self.btn1.setStyleDict({
            "background-color": (154, 84, 237),
            "border-color": (154, 84, 237),
            "border-radius": 7,
            "color": (255, 255, 255),
            "font-family": "SF Pro Display",
            "font-size": 21
        })
        self.btn1.setStyleDict({
            "background-color": (102, 71, 214),
            "border-color": (102, 71, 214)
        }, "hover")
        self.btn1.setStyleDict({
            "background-color": (102, 71, 214),
            "border-color": (102, 71, 214),
            "color": (255, 255, 255),
        }, "press")
        self.btn1.clicked.connect(self.fileSearch)
        self.btnlyt.addWidget(self.btn1, alignment=Qt.AlignTop | Qt.AlignHCenter | Qt.AlignLeft)


    def fileSearch(self):
        filename = ""
        filename = Searchfile.add_open(self, filename)
        self.label1.setText(filename)

    def gotoPrev(self):
        example_ios.gotoPrev()




