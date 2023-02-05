from sys import exit
from PyQt5.QtWidgets import QApplication
from frontend.walk_window import WalkWindow
from backend.walk_window_logic import WalkWindowLogic, Square


if __name__ == '__main__':
    app = QApplication([])
    window = WalkWindow()
    square = Square()
    window_logic = WalkWindowLogic(square)

    window.signal_send_key.connect(window_logic.move_square)
    window_logic.signal_move_square.connect(window.recieve_position)
    #conections

    exit(app.exec())
