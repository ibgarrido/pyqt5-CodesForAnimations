from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QThread
from time import sleep

class AnimationWindowLogic(QObject):

    signal_frame = pyqtSignal(int)
    signal_finished = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.dinosaur = Dinosaur()

    def animation(self):
        self.dinosaur.animation = True
        self.dinosaur.start()
        self.dinosaur.signal_frame = self.signal_frame

    def no_animation(self):
        self.dinosaur.animation = False
        self.signal_finished.emit(0)


class Dinosaur(QThread):

    def __init__(self):
        super().__init__()
        self._frame = 1
        self.signal_frame = None
        self.animation = True

    @property
    def frame(self):
        return self._frame

    @frame.setter
    def frame(self, value):
        if value >= 3:
            self._frame = 1
        elif value <= 0:
            self._frame = 1
        elif 0 < value < 3:
            self._frame = value

    def run(self):
        while self.animation:
            sleep(0.1)
            self.frame += 1
            self.signal_frame.emit(self.frame)
        else:
            self.signal_frame.emit(0)
