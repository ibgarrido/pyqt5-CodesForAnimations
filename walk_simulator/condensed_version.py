### You may notice this version doesn't require a Qtimer to update the windows.
### Is very simple and is not useful if you want to develop a game with colisions.
### This versions has not limits in the window borders.

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class CondensedWindow(QWidget):


    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt5 walk simulator ")
        self.windows_width = 500
        self.windows_height = 500
        self.setGeometry(100, 100, self.windows_width, self.windows_height)
        self.speed = 10
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

    def recieve_position(self, key):
        """update the position using math"""
        x = self.label.x()
        y = self.label.y()
        if key == 'a':
            x -= self.speed

        elif key == 'd':
            x += self.speed

        elif key == 's':
            y += self.speed

        elif key == 'w':
            y -= self.speed

        self.label.move(x, y)

    def keyPressEvent(self, event):
        """Basic keyboard detection"""
        key = event.text().lower()
        # print(f"key pressed {key}")
        if key in ['a', 's', 'w', 'd']:
            self.recieve_position(key)


App = QApplication(sys.argv)

# create the instance of our Window
window = CondensedWindow()

# start the app
sys.exit(App.exec())
