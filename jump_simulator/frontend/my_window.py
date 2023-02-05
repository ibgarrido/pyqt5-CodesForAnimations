from PyQt5.QtCore import pyqtSignal, QThread, Qt
from PyQt5.QtWidgets import QWidget, QLabel


class MyWindow(QWidget):

    signal_jump = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Windows settings
        self.setWindowTitle("pyqt5 Jump simulator ")
        self.windows_width = 500
        self.windows_height = 500
        self.setGeometry(100, 100, self.windows_width, self.windows_height)

        self.movable_label()
        self.show()

    def movable_label(self):
        # Labels settings

        self.square = QLabel(self)
        self.label_width = 40
        self.label_height = 40

        self.square.setGeometry(200, 200, self.label_width, self.label_height)
        self.square.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px solid darkred;"
                                 "background : red;"
                                 "}")

    def recieve_position(self, position: tuple):
        self.square.move(position[0], position[1])

    def keyPressEvent(self, event):
        # Very standard code for Keyboard interaction
        if event.key() == Qt.Key_Space:
            print('space pressed')
            self.signal_jump.emit()

