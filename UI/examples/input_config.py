import sys
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication, QLineEdit

class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle('LineEdit')
        self.resize(500, 500)

        self.line_edit = QLineEdit(self)
        self.line_edit.move(75, 75)

        self.text_label = QLabel(self)
        self.text_label.move(75, 125)
        self.text_label.setText('Default')



        self.button = QPushButton(self)
        self.button.move(75, 175)
        self.button.setText('Get config')
        self.button.clicked.connect(self.button_event)
        


        self.line_edit2 = QLineEdit(self)
        self.line_edit2.move(75, 220)
        


        self.text_label2 = QLabel(self)
        self.text_label2.move(75, 270)
        self.text_label2.setText('Default')

        self.button2 = QPushButton(self)
        self.button2.move(75, 320)
        self.button2.setText('Get config')
        self.button2.clicked.connect(self.button_event)

        self.show()

    def button_event(self):
        text = self.line_edit.text()  # line_edit text 값 가져오기
        self.text_label.setText(text)  # label에 text 설정하기


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()

    sys.exit(app.exec_())
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.move(60, 40)

        qle = QLineEdit(self)
        qle.move(60, 100)
        qle.textChanged[str].connect(self.onChanged)

        self.lbl2 = QLabel(self)
        self.lbl2.move(60, 120)

        qle2 = QLineEdit(self)
        qle2.move(60, 180)
        qle2.textChanged[str].connect(self.onChanged)



        self.setWindowTitle('QLineEdit')
        self.setGeometry(600, 600, 500, 500)
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""