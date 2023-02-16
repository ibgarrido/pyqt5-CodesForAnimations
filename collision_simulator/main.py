from frontend.window import Window
from sys import exit
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication([])
    window = Window()

    #conections

    window.show()
    exit(app.exec())