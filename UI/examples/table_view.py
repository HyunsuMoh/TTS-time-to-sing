import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

config_view = {
    'feature': ['47', '51', '29', '3', '0'],
    'infer': ['1', '1', 'true', '[0]', 'false'],
    'model': ['48', '256', '32', '1.0', '0.001']
}
column_idx_lookup = {'feature': 0, 'infer': 1, 'model': 2}

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 500, 500, 300)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(290, 290)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.setTableWidgetData()

    def setTableWidgetData(self):
        column_headers = ['feature', 'infer', 'model']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)

        for k, v in config_view.items():
            col = column_idx_lookup[k]
            for row, val in enumerate(v):
                item = QTableWidgetItem(val)
                if col == 2:
                    item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)

                self.tableWidget.setItem(row, col, item)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()