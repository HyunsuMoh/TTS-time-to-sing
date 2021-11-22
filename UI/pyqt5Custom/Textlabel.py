from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication, QLineEdit

class Textlabel(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        #self.setWindowTitle('LineEdit')
        #self.resize(500, 500)

        self.line_edit = QLineEdit(self)
        self.line_edit.move(75, 75)

        self.text_label = QLabel(self)
        self.text_label.move(75, 125)
        self.text_label.setText('Default')

        self.button = QPushButton(self)
        self.button.move(75, 175)
        self.button.setText('Get config')
        self.button.clicked.connect(self.button_event)

        self.show()

    def button_event(self):
        text = self.line_edit.text()  # line_edit text 값 가져오기
        self.text_label.setText(text)  # label에 text 설정하기


