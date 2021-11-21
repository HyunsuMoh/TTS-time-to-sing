#                 PyQt5 Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #
#                                                     #
#    This script is one of the pyqt5Custom examples   #
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QFrame, QGridLayout
from PyQt5.QtGui import QColor, QFontDatabase

from pyqt5Custom import ToggleSwitch, StyledButton, ImageBox, ColorPicker, ColorPreview, DragDropFile, EmbedWindow, TitleBar, CodeTextEdit, SegmentedButtonGroup, Spinner, Toast

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        QFontDatabase.addApplicationFont("data/SFPro.ttf")

        self.setMinimumSize(150, 37)
        self.setGeometry(100, 100, 890, 610)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(255, 255, 255))
        self.setPalette(p)

        self.layout = QVBoxLayout()
        #self.layout.setAlignment(Qt.AlignLeft)
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.titlebar = TitleBar(self, title="Sogang and SmileGate")
        self.titlebar.setStyleDict({
                "background-color" : (255, 255, 255),
                "font-size" : 17,
                "border-radius": 6,
                "font-family" : "SF Pro Display"
            })

        self.layout.addWidget(self.titlebar, alignment=Qt.AlignTop)
        self.conlyt = QVBoxLayout()
        self.conlyt.setSpacing(0)
        self.conlyt.setContentsMargins(20, 0, 100, 0)
        self.layout.addLayout(self.conlyt)
        h = QLabel("<span style='font-size:60px; font-family:SF Pro Display; color:rgb(28,28,30);'>TTS</span>")
        ah = QLabel("<span style='font-size:30px; font-family:SF Pro Display; color:rgb(89,89,92);'>Time to Sing</span>")
        h.setContentsMargins(0, 0, 0, 0)
        ah.setContentsMargins(3, 30, 20, 0)


        self.conlyt.addWidget(h)
        self.conlyt.addWidget(ah)

        self.conlyt.addSpacing(0)

        self.ibtnlyt = ImageBox(source="data/tts.png")
        self.layout.addWidget(self.ibtnlyt, alignment=Qt.AlignTop|Qt.AlignTop)

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
                "background-color" : (0, 122, 255),
                "border-color" : (0, 122, 255),
                "border-radius" : 7,
                "color" : (255, 255, 255),
                "font-family" : "SF Pro Display",
                "font-size" : 21,
            })

        self.btn2.setStyleDict({
                "background-color" : (36, 141, 255),
                "border-color" : (36, 141, 255)
            }, "hover")
        self.btn2.setStyleDict({
                "background-color" : (130, 190, 255),
                "border-color" : (130, 190, 255),
                "color" : (255, 255, 255),
            }, "press")

        self.btnlyt.addWidget(self.btn2, alignment=Qt.AlignBottom|Qt.AlignHCenter)
        #self.btnlyt.addWidget(self.btn2)

        self.btn1 = StyledButton("새로운 노래 생성")
        self.btn1.setFixedSize(170, 54)
        self.btn1.anim_press.speed = 5
        self.btn1.setStyleDict({
                "background-color" : (255, 255, 255),
                "border-color" : (0, 122, 255),
                "border-radius" : 7,
                "color" : (0, 122, 255),
                "font-family" : "SF Pro Display",
                "font-size" : 21
            })
        self.btn1.setStyleDict({
                "color" : (107, 178, 255),
            }, "hover")
        self.btn1.setStyleDict({
                "background-color" : (0, 122, 255),
                "color" : (255, 255, 255),
            }, "press")

        self.btnlyt.addWidget(self.btn1, alignment=Qt.AlignBaseline|Qt.AlignHCenter)

        #self.btnlyt2.setAlignment(Qt.AlignLeft)
        #self.btnlyt2.addWidget(QLabel("<span style='font-size:17px; font-family:SF Pro Display; color:rgb(99,99,102);'>Segmented Button Group (Horizontal)</span>"))
        #self.btnlyt2.addSpacing(10)

        #self.ibtnlyt = ImageBox(source="data/tts.png")
        #self.layout.addWidget(self.ibtnlyt, alignment=Qt.AlignCenter)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mw = MainWindow()
    mw.show()

    sys.exit(app.exec_())
