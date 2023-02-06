from sys import exit
from PyQt5.QtWidgets import QApplication
from frontend.my_window import MyWindow
from backend.my_window_logic import MyWindowLogic


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window_logic = MyWindowLogic()
    #conections
    window.signal_jump.connect(window_logic.jump)
    window_logic.signal_position.connect(window.update_position)
    exit(app.exec())
