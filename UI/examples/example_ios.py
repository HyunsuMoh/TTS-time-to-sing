#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #
#                                                     #
#    This script is one of the pyqt5Custom examples   #
import sys
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QWidget, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QFrame, QGridLayout
from PyQt5.QtGui import QColor, QFontDatabase, QIcon
from pyqt5Custom import ToggleSwitch, StyledButton, ImageBox, ColorPicker, ColorPreview, DragDropFile, EmbedWindow, \
    TitleBar, CodeTextEdit, SegmentedButtonGroup, Spinner, Toast


#import infer_test
#import torch

import Make_new_song, Model_training

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
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
        h = QLabel("<span style='font-size:60px; font-family:SF Pro Display; color:rgb(28,28,30);'>TTS</span>")
        ah = QLabel(
            "<span style='font-size:30px; font-family:SF Pro Display; color:rgb(89,89,92);'>Time to Sing</span>")
        h.setContentsMargins(100, 0, 0, 0)
        ah.setContentsMargins(103, 0, 0, 0)
        self.conlyt.addWidget(h)
        self.conlyt.addWidget(ah)
        self.conlyt.addSpacing(90)

        self.ibtnlyt = ImageBox(source="data/tts.png")
        self.layout.addWidget(self.ibtnlyt, alignment=Qt.AlignTop | Qt.AlignTop)

        self.btnslyt = QHBoxLayout()
        self.conlyt.addLayout(self.btnslyt)

        self.btnlyt = QVBoxLayout()
        self.btnlyt.setSpacing(110)

        self.btnslyt.addLayout(self.btnlyt)

        self.btnlyt2 = QVBoxLayout()
        self.btnslyt.addLayout(self.btnlyt2)

        self.btn2 = StyledButton("모델 학습")
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
        self.btn2.clicked.connect(self.gotoML)
        self.btnlyt.addWidget(self.btn2, alignment=Qt.AlignBottom | Qt.AlignHCenter)

        self.btn1 = StyledButton("새로운 노래 생성")
        self.btn1.setFixedSize(170, 54)
        self.btn1.anim_press.speed = 5
        self.btn1.setStyleDict({
            "background-color": (255, 255, 255),
            "border-color": (0, 122, 255),
            "border-radius": 7,
            "color": (0, 122, 255),
            "font-family": "SF Pro Display",
            "font-size": 21
        })
        self.btn1.setStyleDict({
            "color": (107, 178, 255),
        }, "hover")
        self.btn1.setStyleDict({
            "background-color": (0, 122, 255),
            "color": (255, 255, 255),
        }, "press")
        self.btn1.clicked.connect(self.gotoNewSong)
        self.btnlyt.addWidget(self.btn1, alignment=Qt.AlignBaseline | Qt.AlignHCenter)

        """
        self.btn3 = StyledButton("3")
        self.btn3.setFixedSize(170, 54)
        self.btn3.anim_press.speed = 5
        self.btn3.setStyleDict({
            "background-color": (255, 255, 255),
            "border-color": (0, 122, 255),
            "border-radius": 7,
            "color": (0, 122, 255),
            "font-family": "SF Pro Display",
            "font-size": 21
        })
        self.btn3.setStyleDict({
            "color": (107, 178, 255),
        }, "hover")
        self.btn3.setStyleDict({
            "background-color": (0, 122, 255),
            "color": (255, 255, 255),
        }, "press")
        self.btn3.clicked.connect(self.gotoNewSong)
        self.btnlyt.addWidget(self.btn3, alignment=Qt.AlignBaseline | Qt.AlignHCenter)

        self.btn4 = StyledButton("4")
        self.btn4.setFixedSize(170, 54)
        self.btn4.anim_press.speed = 5
        self.btn4.setStyleDict({
            "background-color": (255, 255, 255),
            "border-color": (0, 122, 255),
            "border-radius": 7,
            "color": (0, 122, 255),
            "font-family": "SF Pro Display",
            "font-size": 21
        })
        self.btn4.setStyleDict({
            "color": (107, 178, 255),
        }, "hover")
        self.btn4.setStyleDict({
            "background-color": (0, 122, 255),
            "color": (255, 255, 255),
        }, "press")
        self.btn4.clicked.connect(self.gotoNewSong)
        self.btnlyt.addWidget(self.btn4, alignment=Qt.AlignBaseline | Qt.AlignHCenter)

        self.btn5 = StyledButton("5")
        self.btn5.setFixedSize(170, 54)
        self.btn5.anim_press.speed = 5
        self.btn5.setStyleDict({
            "background-color": (255, 255, 255),
            "border-color": (0, 122, 255),
            "border-radius": 7,
            "color": (0, 122, 255),
            "font-family": "SF Pro Display",
            "font-size": 21
        })
        self.btn5.setStyleDict({
            "color": (107, 178, 255),
        }, "hover")
        self.btn5.setStyleDict({
            "background-color": (0, 122, 255),
            "color": (255, 255, 255),
        }, "press")
        self.btn5.clicked.connect(self.gotoNewSong)
        self.btnlyt.addWidget(self.btn5, alignment=Qt.AlignBaseline | Qt.AlignHCenter)

        self.btn6 = StyledButton("6")
        self.btn6.setFixedSize(170, 54)
        self.btn6.anim_press.speed = 5
        self.btn6.setStyleDict({
            "background-color": (255, 255, 255),
            "border-color": (0, 122, 255),
            "border-radius": 7,
            "color": (0, 122, 255),
            "font-family": "SF Pro Display",
            "font-size": 21
        })
        self.btn6.setStyleDict({
            "color": (107, 178, 255),
        }, "hover")
        self.btn6.setStyleDict({
            "background-color": (0, 122, 255),
            "color": (255, 255, 255),
        }, "press")
        self.btn6.clicked.connect(self.gotoNewSong)
        self.btnlyt.addWidget(self.btn6, alignment=Qt.AlignBaseline | Qt.AlignHCenter)

        self.btn7 = StyledButton("7")
        self.btn7.setFixedSize(170, 54)
        self.btn7.anim_press.speed = 5
        self.btn7.setStyleDict({
            "background-color": (255, 255, 255),
            "border-color": (0, 122, 255),
            "border-radius": 7,
            "color": (0, 122, 255),
            "font-family": "SF Pro Display",
            "font-size": 21
        })
        self.btn7.setStyleDict({
            "color": (107, 178, 255),
        }, "hover")
        self.btn7.setStyleDict({
            "background-color": (0, 122, 255),
            "color": (255, 255, 255),
        }, "press")
        self.btn7.clicked.connect(self.gotoNewSong)
        self.btnlyt.addWidget(self.btn7, alignment=Qt.AlignBaseline | Qt.AlignHCenter)

        self.btn8 = StyledButton("4")
        self.btn8.setFixedSize(170, 54)
        self.btn8.anim_press.speed = 5
        self.btn8.setStyleDict({
            "background-color": (255, 255, 255),
            "border-color": (0, 122, 255),
            "border-radius": 7,
            "color": (0, 122, 255),
            "font-family": "SF Pro Display",
            "font-size": 21
        })
        self.btn8.setStyleDict({
            "color": (107, 178, 255),
        }, "hover")
        self.btn8.setStyleDict({
            "background-color": (0, 122, 255),
            "color": (255, 255, 255),
        }, "press")
        self.btn8.clicked.connect(self.gotoNewSong)
        self.btnlyt.addWidget(self.btn8, alignment=Qt.AlignBaseline | Qt.AlignHCenter)

        self.btn9 = StyledButton("4")
        self.btn9.setFixedSize(170, 54)
        self.btn9.anim_press.speed = 5
        self.btn9.setStyleDict({
            "background-color": (255, 255, 255),
            "border-color": (0, 122, 255),
            "border-radius": 7,
            "color": (0, 122, 255),
            "font-family": "SF Pro Display",
            "font-size": 21
        })
        self.btn9.setStyleDict({
            "color": (107, 178, 255),
        }, "hover")
        self.btn9.setStyleDict({
            "background-color": (0, 122, 255),
            "color": (255, 255, 255),
        }, "press")
        self.btn9.clicked.connect(self.gotoNewSong)
        self.btnlyt.addWidget(self.btn9, alignment=Qt.AlignBaseline | Qt.AlignHCenter)

        self.btn10 = StyledButton("4")
        self.btn10.setFixedSize(170, 54)
        self.btn10.anim_press.speed = 5
        self.btn10.setStyleDict({
            "background-color": (255, 255, 255),
            "border-color": (0, 122, 255),
            "border-radius": 7,
            "color": (0, 122, 255),
            "font-family": "SF Pro Display",
            "font-size": 21
        })
        self.btn10.setStyleDict({
            "color": (107, 178, 255),
        }, "hover")
        self.btn10.setStyleDict({
            "background-color": (0, 122, 255),
            "color": (255, 255, 255),
        }, "press")
        self.btn10.clicked.connect(self.gotoNewSong)
        self.btnlyt.addWidget(self.btn10, alignment=Qt.AlignBaseline | Qt.AlignHCenter)

        self.btn11 = StyledButton("4")
        self.btn11.setFixedSize(170, 54)
        self.btn11.anim_press.speed = 5
        self.btn11.setStyleDict({
            "background-color": (255, 255, 255),
            "border-color": (0, 122, 255),
            "border-radius": 7,
            "color": (0, 122, 255),
            "font-family": "SF Pro Display",
            "font-size": 21
        })
        self.btn11.setStyleDict({
            "color": (107, 178, 255),
        }, "hover")
        self.btn11.setStyleDict({
            "background-color": (0, 122, 255),
            "color": (255, 255, 255),
        }, "press")
        self.btn11.clicked.connect(self.gotoNewSong)
        self.btnlyt.addWidget(self.btn11, alignment=Qt.AlignBaseline | Qt.AlignHCenter)
        """

    def gotoML(self):
        print("gotoML start")
        ml = Model_training.Model_training()
        widget.addWidget(ml)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        print("gotoML end")

    def gotoNewSong(self):
        print("gotoNewSong start")
        ns = Make_new_song.Make_new_song()
        widget.addWidget(ns)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        print("gotoNewSong end")


if __name__ == "__main__":
    sys.path.append('../pyqt5Custom')
    app = QApplication(sys.argv)
    mw = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.setWindowTitle("Sogang and SmileGate")
    widget.setWindowIcon(QIcon('TTS.png'))

    widget.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)
    widget.addWidget(mw)
    widget.setFixedHeight(800)
    widget.setFixedWidth(1200)
    widget.show()

    sys.exit(app.exec_())
