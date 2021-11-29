from abc import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QDialog, QWidget, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QFrame, QGridLayout, \
    QPushButton, QLineEdit, QTableWidget, QComboBox, QCheckBox
from PyQt5.QtGui import QColor, QFontDatabase, QFont

from pyqt5Custom import ToggleSwitch, StyledButton, ColorPicker, ColorPreview, DragDropFile, EmbedWindow, \
    TitleBar, CodeTextEdit, SegmentedButtonGroup, Spinner, Toast


class InputForm(metaclass=ABCMeta):
    def __init__(self, label, value):
        self.label = label
        self.value = value

    def getValue(self):
        pass

    def setValue(self, value):
        pass


class TextInputForm(InputForm):
    def __init__(self, label, value):
        super().__init__(label, value)
        self.widget = QLineEdit()
        self.widget.setText(str(value))

    def getValue(self):
        self.value = self.widget.text()
        return self.value

    def setValue(self, value):
        self.widget.setText(str(value))


class IntInputForm(TextInputForm):
    def getValue(self):
        self.value = int(self.widget.text())
        return self.value


class FloatInputForm(TextInputForm):
    def getValue(self):
        self.value = float(self.widget.text())
        return self.value


class IntListInputForm(TextInputForm):
    def getValue(self):
        datastr = self.widget.text()
        strlist = datastr.strip('[]').split(',')
        self.value = [int(str.strip()) for str in strlist]


class FloatListInputForm(TextInputForm):
    def getValue(self):
        datastr = self.widget.text()
        strlist = datastr.strip('[]').split(',')
        self.value = [float(str.strip()) for str in strlist]


class MultipleSelectionInputForm(InputForm):
    def __init__(self, label, value, options):
        super().__init__(label, value)
        self.widget = QComboBox()
        self.widget.addItems(options)
        self.widget.setCurrentIndex(options.index(str(value)))

    def getValue(self):
        self.value = self.widget.currentText()
        return self.value

    def setValue(self, value):
        index = self.widget.findData(value)
        if index >= 0:
            self.widget.setCurrentIndex(index)


class BoolSelectionInputForm(InputForm):
    def __init__(self, label, value):
        super().__init__(label, value)
        self.widget = QCheckBox()
        self.widget.setChecked(value)

    def getValue(self):
        self.value = self.widget.isChecked()
        return self.value

    def setValue(self, value):
        self.widget.setChecked(value)