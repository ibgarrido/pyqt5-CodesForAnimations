from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QThread
from PyQt5

class MyWindowLogic(QObject):
    signal_position = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        self.square = Square(self.signal_position)
        self.timer_jump = QTimer()
        self.set_timer()

    def set_timer(self):
        pass



class Square(QThread):


    def __init__(self, signal_position):
        super().__init__()
        self.x = 200
        self._y = 200
        self.acceleration = 1
        self.speed = 5
        self.run = None
        self.signal_position = signal_position

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        pass

    def jump(self):
        "This part require to understand a bit of physics: uniformly accelerated motion"
        position = self.acceleration*(self.speed)**2
        self.y -= position
        self.signal_position.emit((self.x, self.y))
        print(self.x, self.y)
        self.speed -= 1
        if self.speed < 0:
            self.acceleration *= -1
        if self.speed == -6:
            self.run = False
            self.speed = 5
            self.mass = 1
