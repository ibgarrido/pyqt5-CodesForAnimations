from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel


class WalkWindow(QWidget):

    signal_send_key = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt5 walk simulator ")
        self.windows_width = 500
        self.windows_height = 500
        self.setGeometry(100, 100, self.windows_width, self.windows_height)
        self.label_square()
        self.show()

    def label_square(self):
        self.label = QLabel(self)
        self.label_width = 40
        self.label_height = 40

        self.label.setGeometry(200, 200, self.label_width, self.label_height)
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px solid darkred;"
                                 "background : black;"
                                 "}")

    def recieve_position(self, position: tuple):
        """recieve the position from logic windows (Square)"""
        self.label.move(position[0], position[1])

    def keyPressEvent(self, event):
        """Basic keyboard detection"""
        key = event.text().lower()
        self.signal_send_key.emit(key)
