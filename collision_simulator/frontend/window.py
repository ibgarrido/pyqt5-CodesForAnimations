from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 1000, 350)
        self.setWindowTitle('Collision Simulator')

        self.label_1 = QLabel(self)
        self.label_1.setGeometry(0, 310, 40, 40)
        self.label_1.setStyleSheet('background-color: black')
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(960, 310, 40, 40)
        self.label_2.setStyleSheet('background-color: red')



