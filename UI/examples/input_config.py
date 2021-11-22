import sys
sys.path.append("../pyqt5Custom")

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QWidget, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QFrame, QGridLayout, \
     QPushButton, QLineEdit
from PyQt5.QtGui import QColor, QFontDatabase, QFont

from pyqt5Custom import ToggleSwitch, StyledButton, ColorPicker, ColorPreview, DragDropFile, EmbedWindow, \
    TitleBar, CodeTextEdit, SegmentedButtonGroup, Spinner, Toast

import example_ios, Model_training

class input_config(QDialog):
    def __init__(self):
        super(input_config, self).__init__()
        #QFontDatabase.addApplicationFont("data/BMDOHYEON_ttf.ttf")
        # app.setFont(QFont('data/BMDOHYEON_ttf.tff'))

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

        """
        self.textlabel = Textlabel()
        self.textlabel.setupUi()
        self.textlabel.button_event()
        """

        self.line_edit = QLineEdit(self)
        self.line_edit.move(25, 0)

        self.text_label = QLabel(self)
        self.text_label.move(150, 0)
        self.text_label.setText('Default')

        self.input1 = QVBoxLayout()
        self.layout.addLayout(self.input1)
        #self.input2.addWidget(self.text_label, alignment=Qt.AlignTop | Qt.AlignHCenter)

        self.button = StyledButton("Input")
        self.button.setFixedSize(120, 30)
        self.button.anim_press.speed = 7.3
        self.button.setStyleDict({
            "background-color": (0, 122, 255),
            "border-color": (0, 122, 255),
            "border-radius": 7,
            "color": (255, 255, 255),
            "font-family": "SF Pro Display",
            "font-size": 21,
        })
        self.button.setStyleDict({
            "background-color": (36, 141, 255),
            "border-color": (36, 141, 255)
        }, "hover")
        self.button.setStyleDict({
            "background-color": (130, 190, 255),
            "border-color": (130, 190, 255),
            "color": (255, 255, 255),
        }, "press")

        self.button.setText('Get config')
        self.button.clicked.connect(self.button_event)

        self.input1.addWidget(self.button, alignment=Qt.AlignTop | Qt.AlignHCenter)

        #self.button = QPushButton(self)
        #self.button.move(75, 175)
        #self.button.setText('Get config')
        #self.button.clicked.connect(self.button_event)


        self.line_edit2 = QLineEdit(self)
        self.line_edit2.move(75, 225)

        self.text_label2 = QLabel(self)
        self.text_label2.move(75, 275)
        self.text_label2.setText('Default')

        self.button2 = QPushButton(self)
        self.button2.move(75, 325)
        self.button2.setText('Get config')
        self.button2.clicked.connect(self.button_event2)

    def button_event(self):
        text = self.line_edit.text()  # line_edit text 값 가져오기
        self.text_label.setText(text)  # label에 text 설정하기

    def button_event2(self):
        text = self.line_edit2.text()  # line_edit text 값 가져오기
        self.text_label2.setText(text)  # label에 text 설정하기


if __name__ == "__main__":

    app = QApplication(sys.argv)

    fontDB = QFontDatabase()
    fontDB.addApplicationFont('BMDOHYEON_ttf.ttf')
    app.setFont(QFont('BMDOHYEON_ttf'))
    #QFont font;
    #font.setFamily(QString("맑은 고딕"));
    #application.setFont(font);

    mw = input_config()
    mw.show()

    sys.exit(app.exec_())


