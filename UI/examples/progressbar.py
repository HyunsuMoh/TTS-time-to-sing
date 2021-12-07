import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../pyqt5Custom"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../bridge"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../../ML/utils"))
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QWidget, QProgressBar, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QFrame, QGridLayout,QFileDialog, QLabel
from PyQt5.QtGui import QColor, QFontDatabase, QFont
from pyqt5Custom import ToggleSwitch, StyledButton, ColorPicker, ColorPreview, DragDropFile, EmbedWindow, \
    TitleBar, CodeTextEdit, SegmentedButtonGroup, Spinner
from inference_ui import infer_test
from input_config import input_config
from config_parser import Config

DEFAULT_STYLE = """
QProgressBar{
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center;
}
QProgressBar::chunk 
{
background-color: #9a54ed;
border-radius :5px;
}  
"""
DEFAULT_STYLE2 = """
QProgressBar{
    border: 2px solid grey;
    border-radius: 5px;
    color: #ffffff;
    text-align: center;
}
QProgressBar::chunk 
{
    background-color: #6647d6;
    color: #ffffff;
border-radius :5px;
}  
"""

class Progressbar(QDialog):
    def __init__(self, switchWidget):
        super(Progressbar, self).__init__()
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
        self.conlyt.setContentsMargins(70, 15, 70, 60)
        self.conlyt.setSpacing(40)
        self.layout.addLayout(self.conlyt)

        self.list = QHBoxLayout()
        h = QLabel(
            "<span style='font-size:48px; font-family:SF Pro Display; color:rgb(28,28,30);'>\U000023F3 Progress</span>")
        self.gohome = StyledButton("Go home")
        self.gohome.setFixedSize(130, 40)

        self.gohome.setStyleDict({
            "background-color": (255, 255, 255),
            "border-color": (154, 84, 237),
            "border-radius": 7,
            "color": (154, 84, 237),
            "font-family": "SF Pro Display",
            "font-size": 21,
        }, "default")
        self.gohome.setStyleDict({
            "background-color": (154, 84, 237),
            "border-color": (154, 84, 237),
            "color": (255, 255, 255),
            "font-size": 21,
        }, "hover")
        self.gohome.setStyleDict({
            "background-color": (154, 84, 237),
            "border-color": (154, 84, 237),
            "color": (255, 255, 255),
            "font-size": 21,
        }, "press")

        self.gohome.clicked.connect(lambda: switchWidget(0))
        self.list.addWidget(h)
        self.list.addWidget(self.gohome)
        self.list.setContentsMargins(0, 50, 0, 100)
        self.conlyt.addLayout(self.list)

        self.label1 = QLabel("<span style='font-size:25px; font-family:SF Pro Display;'> Iteration</span>")
        self.topPb = QProgressBar()
        self.topPb.setStyleSheet(DEFAULT_STYLE)
        self.topPb.setValue(37)
        self.topPb.setContentsMargins(0, 50, 0, 130)

        self.label2 = QLabel("<span style='font-size:25px; font-family:SF Pro Display;'> Individual task</span>")
        self.underPb = QProgressBar()
        self.underPb.setStyleSheet(DEFAULT_STYLE2)
        self.underPb.setValue(55)
        self.conlyt.addWidget(self.label1)
        self.conlyt.addWidget(self.topPb)
        self.conlyt.addWidget(self.label2)
        self.conlyt.addWidget(self.underPb)


