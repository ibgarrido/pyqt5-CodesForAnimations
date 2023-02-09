from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from os.path import join

class AnimationWindow(QWidget):

    signal_start = pyqtSignal()
    signal_stop = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Windows settings
        self.setWindowTitle("pyqt5 Jump simulator ")
        self.windows_width = 500
        self.windows_height = 500
        self.setGeometry(100, 100, self.windows_width, self.windows_height)
        self.route_1 = join('frontend', 'sprites', 'img_1.png')
        self.route_2 = join('frontend', 'sprites', 'img_2.png')
        self.route_3 = join('frontend', 'sprites', 'img_3.png')
        self.start_button = QPushButton('Start', self)
        self.start_button.move(150, 350)
        self.start_button.clicked.connect(self.start)

        self.stop_button = QPushButton('Stop', self)
        self.stop_button.move(300, 350)
        self.stop_button.clicked.connect(self.stop)
        
        self.movable_label()
        self.show()

    def movable_label(self):
        # Labels settings

        self.dinosaur = QLabel(self)
        self.label_width = 40
        self.label_height = 40
        self.dinosaur.setGeometry(200, 200, self.label_width, self.label_height)
        self.dinosaur.setPixmap(QPixmap(self.route_1).scaled(40, 40))

    def set_frame(self, value):
        if value == 1:
            self.dinosaur.setPixmap(QPixmap(self.route_2).scaled(40, 40))
        elif value == 2:
            self.dinosaur.setPixmap(QPixmap(self.route_3).scaled(40, 40))
        elif value == 0:
            self.dinosaur.setPixmap(QPixmap(self.route_1).scaled(40, 40))

    def start(self):
        self.signal_start.emit()

    def stop(self):
        self.signal_stop.emit()

