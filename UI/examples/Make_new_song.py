#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #
#                                                     #
#    This script is one of the pyqt5Custom examples   #

import sys
sys.path.append("../pyqt5Custom")

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QWidget, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QFrame, QGridLayout
from PyQt5.QtGui import QColor, QFontDatabase, QFont

from pyqt5Custom import ToggleSwitch, StyledButton, ColorPicker, ColorPreview, DragDropFile, EmbedWindow, \
    TitleBar, CodeTextEdit, SegmentedButtonGroup, Spinner, Toast

import example_ios, Model_training
from Searchfile import Searchfile

class Make_new_song(QDialog):
    def __init__(self):
        super(Make_new_song, self).__init__()
        QFontDatabase.addApplicationFont("data/BMDOHYEON_ttf.ttf")

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
            "<span style='font-size:48px; font-family:SF Pro Display; color:rgb(28,28,30);'>Making new songs</span>")
        ah = QLabel(
            "<span style='font-size:24px; font-family:SF Pro Display; color:rgb(89,89,92);'>기존 모델들을 바탕으로 새로운 노래 생성</span>")

        self.conlyt.addSpacing(90)

        self.btnslyt = QHBoxLayout()
        self.conlyt.addLayout(self.btnslyt)
        self.btnlyt2 = QVBoxLayout()
        self.btnlyt2.setSpacing(16)
        self.btnslyt.addLayout(self.btnlyt2)

        self.btnlyt2.setAlignment(Qt.AlignTop)
        self.btnlyt2.addWidget(QLabel(
            "<span style='font-size:17px; font-family:SF Pro Display; color:rgb(99,99,102);'>Choosing Model</span>"))
        self.btnlyt2.addSpacing(10)

        self.segbg = SegmentedButtonGroup(radio=True)
        self.segbg.setFixedSize(349, 36)
        self.segbg.setStyleDict({
            "background-color": (255, 255, 255),
            "border-color": (0, 122, 255),
            "border-radius": 7,
            "color": (0, 122, 255),
            "font-family": "SF Pro Display",
            "font-size": 15,
            "font-subpixel-aa": True
        })
        self.segbg.setStyleDict({
            "color": (107, 178, 255),
        }, "hover")
        self.segbg.setStyleDict({
            "background-color": (0, 122, 255),
            "color": (255, 255, 255),
        }, "press")
        self.segbg.setStyleDict({
            "background-color": (61, 154, 255),
            "color": (255, 255, 255),
        }, "check-hover")

        self.segbg.addButton("Default")
        self.segbg.addButton("Another option")
        #    self.segbg.addButton("Third")

        self.btnlyt2.addWidget(self.segbg)

        self.btnlyt2.addSpacing(10)
        self.btnlyt2.addWidget(QLabel(
            "<span style='font-size:17px; font-family:SF Pro Display; color:rgb(99,99,102);'>Lyrics</span>"))
        self.btnlyt2.addSpacing(10)
        self.btnlyt2.addWidget(QLabel(
            "<span style='font-size:17px; font-family:SF Pro Display; color:rgb(99,99,102);'>SheetMusic</span>"))
        self.btnlyt2.addSpacing(10)

        self.ibtnlyt = QHBoxLayout()
        self.btnlyt2.addLayout(self.ibtnlyt)

        self.ibtn = StyledButton("Find", icon="data/TTS.png")
        self.ibtn.setFixedSize(140, 45)
        self.ibtn.anim_press.speed = 7.3
        self.ibtn.setStyleDict({
            "background-color": (0, 122, 255),
            "border-color": (0, 122, 255),
            "border-radius": 7,
            "color": (255, 255, 255),
            "font-family": "SF Pro Display",
            "font-size": 18,
        })
        self.ibtn.setStyleDict({
            "background-color": (36, 141, 255),
            "border-color": (36, 141, 255)
        }, "hover")
        self.ibtn.setStyleDict({
            "background-color": (130, 190, 255),
            "border-color": (130, 190, 255),
            "color": (255, 255, 255),
        }, "press")

        self.ibtnlyt.addWidget(self.ibtn)

        self.ibtnl = StyledButton("Making New Songs", icon=Spinner(1.5, QColor(255, 255, 255)))
        self.ibtnl.setMinimumSize(118, 38)
        self.ibtnl.anim_press.speed = 7.3
        self.ibtnl.setStyleDict({
            "background-color": (52, 199, 89),
            "border-color": (2, 199, 89),
            "border-radius": 39,
            "color": (255, 255, 255),
            "font-family": "SF Pro Display",
            "font-size": 18,
        })
        self.ibtnl.setStyleDict({
            "background-color": (47, 212, 119),
            "border-color": (47, 212, 119)
        }, "hover")
        self.ibtnl.setStyleDict({
            "background-color": (89, 227, 149),
            "border-color": (89, 227, 149),
            "color": (255, 255, 255),
        }, "press")

        self.btnlyt2.addSpacing(15)
        self.btnlyt2.addWidget(self.ibtnl, alignment=Qt.AlignHCenter)

        self.toast = Toast(self, text="Making new Songs", icon=Spinner(1.3, QColor(255, 255, 255)))
        self.toast.setFixedWidth(287)
        self.toast.setStyleDict({
            "font-family": "SF Pro Display",
            "font-size": 17
        })

        self.ibtnl.clicked.connect(lambda: self.toast.rise(3))
