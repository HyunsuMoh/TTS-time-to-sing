from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QFileDialog, QLabel

class Searchfile(QFileDialog):

    def __init__(self):
        super().__init__()

        self.num = 0

        self.setWindowTitle("file_search")

        self.resize(800, 800)

        self.qclist = []

        self.position = 0

        self.Lgrid = QGridLayout()

        self.setLayout(self.Lgrid)

        self.label1 = QLabel('', self)

        self.label2 = QLabel('', self)

        self.label3 = QLabel('', self)

        addbutton1 = QPushButton('Open File', self)

        self.Lgrid.addWidget(self.label1, 1, 1)

        self.Lgrid.addWidget(addbutton1, 2, 1)

        addbutton1.clicked.connect(self.add_open)


        addbutton2 = QPushButton('Save File', self)

        self.Lgrid.addWidget(self.label2, 3, 1)

        self.Lgrid.addWidget(addbutton2, 4, 1)

        addbutton2.clicked.connect(self.add_save)


        addbutton3 = QPushButton('Find Folder', self)

        self.Lgrid.addWidget(self.label3, 5, 1)

        self.Lgrid.addWidget(addbutton3, 6, 1)

        addbutton3.clicked.connect(self.find_folder)

        self.show()

    def add_open(self, filename):
        FileOpen = QFileDialog.getOpenFileName(self, 'Open file', './')
        filename = filename + FileOpen[0]
        return filename

    def add_save(self):
        FileSave = QFileDialog.getSaveFileName(self, 'Save file', './')

        self.label2.setText(FileSave[0])

    def find_folder(self, filename):
        FileFolder = QFileDialog.getExistingDirectory(self, 'Find Folder')
        filename = filename + FileFolder
        return filename
