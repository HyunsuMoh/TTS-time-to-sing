import sys

sys.path.append("../pyqt5Custom")
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QCheckBox, QVBoxLayout, QLabel, QApplication, QWidget
from PyQt5.QtGui import QColor, QFontDatabase
from pyqt5Custom import StyledButton
from Searchfile import Searchfile


class Select_path(QDialog):
    def __init__(self):
        super(Select_path, self).__init__()
        QFontDatabase.addApplicationFont("data/SFPro.ttf")
        self.setMinimumSize(150, 37)
        self.setGeometry(100, 100, 890, 610)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(255, 255, 255))
        self.setPalette(p)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.conlyt = QVBoxLayout()
        self.conlyt.setSpacing(0)
        self.conlyt.setContentsMargins(70, 0, 70, 0)
        h = QLabel(
            "<span style='font-size:50px; font-family:SF Pro Display; color:rgb(28,28,30);'>Config setting</span>")
        h.setContentsMargins(30, 0, 0, 50)
        self.conlyt.addWidget(h)
        self.layout.addLayout(self.conlyt)
        self.layout.setContentsMargins(0, 100, 0, 0)
        self.list = QHBoxLayout()
        self.list.setSpacing(10)
        self.conlyt.addLayout(self.list)
        self.findBtns = QVBoxLayout()
        self.texts = QVBoxLayout()
        self.labels = QVBoxLayout()
        self.findBtns.setSpacing(35)
        self.texts.setSpacing(33)
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
                "font-size": 21
            },
            'hover': {
                "background-color": (102, 71, 214),
                "border-color": (102, 71, 214),
            },
            'press': {
                "background-color": (102, 71, 214),
                "border-color": (102, 71, 214),
                "color": (255, 255, 255),
            }
        }

        self.label1 = QLabel('', self)
        self.text1 = QLabel(
            "<span style='font-size:21px; font-family:SF Pro Display; color:rgb(28,28,30);'>Dataset text path</span>")
        self.btn1 = StyledButton("Find")
        self.btn1.setFixedSize(100, 34)
        self.btn1.anim_press.speed = 7.3
        self.btn1.setStyleDict(button_style['normal'])
        self.btn1.setStyleDict(button_style['hover'], "hover")
        self.btn1.setStyleDict(button_style['press'], "press")
        self.btn1.clicked.connect(lambda: self.dirSearch(self.label1))
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
        self.btn2.clicked.connect(lambda: self.dirSearch(self.label2))
        self.btn2.setContentsMargins(0, 3, 0, 0)
        self.text2.setContentsMargins(20, 3, 0, 0)
        self.label2.setContentsMargins(20, 10, 0, 0)

        self.label3 = QLabel('', self)
        self.text3 = QLabel(
            "<span style='font-size:21px; font-family:SF Pro Display; color:rgb(28,28,30);'>Dataset wav path</span>")
        self.btn3 = StyledButton("Find")
        self.btn3.setFixedSize(100, 34)
        self.btn3.anim_press.speed = 7.3
        self.btn3.setStyleDict(button_style['normal'])
        self.btn3.setStyleDict(button_style['hover'], "hover")
        self.btn3.setStyleDict(button_style['press'], "press")
        self.btn3.clicked.connect(lambda: self.dirSearch(self.label3))
        self.text3.setContentsMargins(20, 3, 0, 0)
        self.label3.setContentsMargins(20, 10, 0, 0)

        self.label4 = QLabel('', self)
        self.text4 = QLabel(
            "<span style='font-size:21px; font-family:SF Pro Display; color:rgb(28,28,30);'>Feature path</span>")
        self.btn4 = StyledButton("Find")
        self.btn4.setFixedSize(100, 34)
        self.btn4.anim_press.speed = 7.3
        self.btn4.setStyleDict(button_style['normal'])
        self.btn4.setStyleDict(button_style['hover'], "hover")
        self.btn4.setStyleDict(button_style['press'], "press")
        self.btn4.clicked.connect(lambda: self.dirSearch(self.label4))
        self.text4.setContentsMargins(20, 3, 0, 0)
        self.label4.setContentsMargins(20, 10, 0, 0)

        self.label5 = QLabel('', self)
        self.text5 = QLabel(
            "<span style='font-size:21px; font-family:SF Pro Display; color:rgb(28,28,30);'>Checkpoint path action</span>")
        self.btn5 = StyledButton("Find")
        self.btn5.setFixedSize(100, 34)
        self.btn5.anim_press.speed = 7.3
        self.btn5.setStyleDict(button_style['normal'])
        self.btn5.setStyleDict(button_style['hover'], "hover")
        self.btn5.setStyleDict(button_style['press'], "press")
        self.btn5.clicked.connect(lambda: self.dirSearch(self.label5))
        self.text5.setContentsMargins(20, 3, 0, 0)
        self.label5.setContentsMargins(20, 10, 0, 0)

        self.label6 = QLabel('', self)
        self.text6 = QLabel(
            "<span style='font-size:21px; font-family:SF Pro Display; color:rgb(28,28,30);'>Load checkpoint</span>")
        self.checkbox6 = QCheckBox("")
        self.checkbox6.setStyleSheet(
            "QCheckBox::indicator"
            "{"
            "width :30px;"
            "height :30px;"
            "}"
        )
        self.checkbox6.setContentsMargins(0, 30, 0, 0)
        self.checkbox6.stateChanged.connect(self.changeCheckState)
        self.text6.setContentsMargins(20, 3, 0, 0)

        self.label7 = QLabel('', self)
        self.text7 = QLabel(
            "<span style='font-size:20px; font-family:SF Pro Display; color:rgb(28,28,30);'>Loaded checkpoint path G</span>")
        self.btn7 = StyledButton("Find")
        self.btn7.setFixedSize(100, 34)
        self.btn7.anim_press.speed = 7.3
        self.btn7.setStyleDict(button_style['normal'])
        self.btn7.setStyleDict(button_style['hover'], "hover")
        self.btn7.setStyleDict(button_style['press'], "press")
        self.btn7.clicked.connect(lambda: self.fileSearch(self.label7))
        self.text7.setContentsMargins(20, 3, 0, 0)
        self.label7.setContentsMargins(20, 10, 0, 0)

        self.label8 = QLabel('', self)
        self.text8 = QLabel(
            "<span style='font-size:20px; font-family:SF Pro Display; color:rgb(28,28,30);'>Loaded checkpoint path D</span>")
        self.btn8 = StyledButton("Find")
        self.btn8.setFixedSize(100, 34)
        self.btn8.anim_press.speed = 7.3
        self.btn8.setStyleDict(button_style['normal'])
        self.btn8.setStyleDict(button_style['hover'], "hover")
        self.btn8.setStyleDict(button_style['press'], "press")
        self.btn8.clicked.connect(lambda: self.fileSearch(self.label8))
        self.text8.setContentsMargins(20, 3, 0, 0)
        self.label8.setContentsMargins(20, 10, 0, 0)

        self.texts.addWidget(self.text1)
        self.texts.addWidget(self.text2)
        self.texts.addWidget(self.text3)
        self.texts.addWidget(self.text4)
        self.texts.addWidget(self.text5)
        self.texts.addWidget(self.text6)
        self.texts.addWidget(self.text7)
        self.texts.addWidget(self.text8)

        self.findBtns.addWidget(self.btn1)
        self.findBtns.addWidget(self.btn2)
        self.findBtns.addWidget(self.btn3)
        self.findBtns.addWidget(self.btn4)
        self.findBtns.addWidget(self.btn5)
        self.findBtns.addWidget(self.checkbox6)
        self.findBtns.addWidget(self.btn7)
        self.findBtns.addWidget(self.btn8)

        self.labels.addWidget(self.label1)
        self.labels.addWidget(self.label2)
        self.labels.addWidget(self.label3)
        self.labels.addWidget(self.label4)
        self.labels.addWidget(self.label5)
        self.labels.addWidget(self.label6)
        self.labels.addWidget(self.label7)
        self.labels.addWidget(self.label8)

    def changeCheckState(self, state):
        if state == Qt.Checked:
            self.label6.setText("Continue learning with the selected checkpoint")
        else:
            self.label6.setText("Create a new checkpoint to proceed with the learning")

    def fileSearch(self, labelName):
        filename = ""
        filename = Searchfile.add_open(self, filename)
        labelName.setText(filename)

    def dirSearch(self, labelName):
        filename = ""
        filename = Searchfile.find_folder(self, filename)
        labelName.setText(filename)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = Select_path()
    mw.show()

    mw.setFixedHeight(800)
    mw.setFixedWidth(1200)
    sys.exit(app.exec_())
