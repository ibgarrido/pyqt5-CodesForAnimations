from sys import exit
from PyQt5.QtWidgets import QApplication
from frontend.animation_window import AnimationWindow
from backend.animation_window_logic import AnimationWindowLogic


if __name__ == '__main__':
    app = QApplication([])
    window = AnimationWindow()
    window_logic = AnimationWindowLogic()
    #conections
    window.signal_start.connect(window_logic.animation)
    window_logic.signal_frame.connect(window.set_frame)

    window.signal_stop.connect(window_logic.no_animation)

    window.show()
    exit(app.exec())
