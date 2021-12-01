import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../pyqt5Custom"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../bridge"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../../ML/utils"))

import yaml
sys.path.append("../pyqt5Custom")
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QWidget, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QFrame, QGridLayout, \
     QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QHeaderView, QFileDialog
from PyQt5.QtGui import QColor, QFontDatabase, QFont

from pyqt5Custom import ToggleSwitch, StyledButton, ColorPicker, ColorPreview, DragDropFile, EmbedWindow, \
    TitleBar, CodeTextEdit, SegmentedButtonGroup, Spinner, Toast

from config_data_input import *
from config_parser import Config

class input_config(QDialog):
    def __init__(self, mode, config, close_action=None):
        def ok_action():
            self.table.setConfig(config)
            cancel_action()

        def cancel_action():
            if close_action is not None:
                close_action()

        super(input_config, self).__init__()
        self.table = input_config_table(mode, config)

        self.setWindowTitle("Configurations")
        self.setMinimumSize(600, 600)
        button_layout = QtWidgets.QVBoxLayout()
        button_style = {
            'normal': {
                "background-color": (255, 255, 255),
                "border-color": (0, 122, 255),
                "border-radius": 7,
                "color": (0, 122, 255),
                "font-family": "SF Pro Display",
                "font-size": 15
            },
            'hover' : {
                "color": (107, 178, 255),
            },
            'press' : {
                "background-color": (0, 122, 255),
                "color": (255, 255, 255),
            }
        }
        save_button = StyledButton('Save as File')
        load_button = StyledButton('Load from File')
        ok_button = StyledButton('OK')
        cancel_button = StyledButton('Cancel')
        save_button.anim_press.speed = 7.3
        load_button.anim_press.speed = 7.3
        ok_button.anim_press.speed = 7.3
        cancel_button.anim_press.speed = 7.3

        save_button.setStyleDict(button_style['normal'])
        save_button.setStyleDict(button_style['hover'], "hover")
        save_button.setStyleDict(button_style['press'], "press")
        load_button.setStyleDict(button_style['normal'])
        load_button.setStyleDict(button_style['hover'], "hover")
        load_button.setStyleDict(button_style['press'], "press")
        ok_button.setStyleDict({
            "background-color": (0, 122, 255),
            "border-color": (0, 122, 255),
            "border-radius": 7,
            "color": (255, 255, 255),
            "font-family": "SF Pro Display",
            "font-size": 15,
        })
        ok_button.setStyleDict(button_style['hover'], "hover")
        ok_button.setStyleDict(button_style['press'], "press")
        cancel_button.setStyleDict(button_style['normal'])
        cancel_button.setStyleDict(button_style['hover'], "hover")
        cancel_button.setStyleDict(button_style['press'], "press")

        save_button.clicked.connect(lambda: {self.table.saveConfigFile(config)})
        load_button.clicked.connect(lambda: {self.table.loadConfigFile(config)})
        ok_button.clicked.connect(ok_action)
        cancel_button.clicked.connect(cancel_action)

        button_layout.addStretch()
        button_layout.addWidget(save_button, alignment=Qt.AlignVCenter)
        button_layout.addWidget(load_button, alignment=Qt.AlignVCenter)
        button_layout.addWidget(ok_button, alignment=Qt.AlignVCenter)
        button_layout.addWidget(cancel_button, alignment=Qt.AlignVCenter)
        button_layout.addStretch()

        tablehbox = QtWidgets.QHBoxLayout()
        tablehbox.setContentsMargins(10, 10, 10, 10)
        tablehbox.addWidget(self.table)

        grid = QtWidgets.QGridLayout(self)
        grid.addLayout(button_layout, 0, 1)
        grid.addLayout(tablehbox, 0, 0)


class input_config_table(QTableWidget):
    def __init__(self, mode, config):
        super(input_config_table, self).__init__()
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

        data_type_file_path = os.path.join(os.path.dirname(__file__), "..", "bridge", "config", ("data_types_" + mode + ".yml"))
        yaml_file = open(data_type_file_path, 'r')
        data_type_info = yaml.safe_load(yaml_file)
        self.table_item = []
        for item in data_type_info:
            if data_type_info[item]['type'] == 'Int':
                self.table_item.append(IntInputForm(item, getattr(config, item)))
            elif data_type_info[item]['type'] == 'Float':
                self.table_item.append(FloatInputForm(item, getattr(config, item)))
            elif data_type_info[item]['type'] == 'IntList':
                self.table_item.append(IntListInputForm(item, getattr(config, item)))
            elif data_type_info[item]['type'] == 'FloatList':
                self.table_item.append(FloatListInputForm(item, getattr(config, item)))
            elif data_type_info[item]['type'] == 'MultiSelection':
                self.table_item.append(MultipleSelectionInputForm(item, getattr(config, item), data_type_info[item]['option']))
            elif data_type_info[item]['type'] == 'Bool':
                self.table_item.append(BoolSelectionInputForm(item, getattr(config, item)))
            else:
                self.table_item.append(TextInputForm(item, getattr(config, item)))
        self.setRowCount(len(self.table_item))
        self.setColumnCount(2)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        for i in range(len(self.table_item)):
            item = self.table_item[i]
            self.setItem(i, 0, QTableWidgetItem(item.label))
            self.setCellWidget(i, 1, item.widget)

    def loadConfigFile(self, config):
        filename = QFileDialog.getOpenFileName(self, 'Load from File', os.path.join(os.path.dirname(__file__), "../bridge/config"), filter='*.yml')
        if filename is not None and filename[0]:
            config = Config(filename[0:-1])
            self.loadConfig(config)

    def saveConfigFile(self, config):
        filename = QFileDialog.getSaveFileName(self, 'Save as File', '', filter='*.yml')[0]
        if filename:
            self.setConfig(config)
            config.save(filename)

    def loadConfig(self, config):
        for item in self.table_item:
            if hasattr(config, item.label):
                item.setValue(getattr(config, item.label))

    def setConfig(self, config):
        for item in self.table_item:
            setattr(config, item.label, item.getValue())


if __name__ == "__main__":

    app = QApplication(sys.argv)

    fontDB = QFontDatabase()
    fontDB.addApplicationFont('BMDOHYEON_ttf.ttf')
    app.setFont(QFont('BMDOHYEON_ttf'))
    #QFont font;
    #font.setFamily(QString("맑은 고딕"));
    #application.setFont(font);

    config = Config(["../bridge/config/default_train.yml"])
    mw = input_config('train', config, lambda: {print('close')})
    mw.show()

    sys.exit(app.exec_())