from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication, QLineEdit

class Textlabel(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):

        line_edit = QLineEdit(self)
        line_edit.move(75, 75)

        text_label = QLabel(self)
        text_label.move(75, 125)
        text_label.setText('Default')

        button = QPushButton(self)
        button.move(75, 175)
        button.setText('Get config')
        button.clicked.connect(self.button_event)

        return line_edit, text_label, button

    def button_event(self):
        text = self.line_edit.text()  # line_edit text 값 가져오기
        self.text_label.setText(text)  # label에 text 설정하기


