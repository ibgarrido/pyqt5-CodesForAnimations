from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QThread
from time import sleep

class MyWindowLogic(QObject):
    signal_position = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        self.square = Square()

    def jump(self):
        self.square.alive = True
        self.square.signal_position = self.signal_position
        self.square.start()


class Square(QThread):

    def __init__(self):
        super().__init__()
        self.x = 200
        self._y = 200
        self.acceleration = 1
        self.speed = 5
        self.alive = False
        self.signal_position = None
        self.jump_limit = 145

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if value < self.jump_limit:
            self._y = self.jump_limit
            self.signal_position.emit((self.x, self.y))
        elif value >= 200:
            self._y = 200
            self.signal_position.emit((self.x, self.y))
        elif self.jump_limit < value < 200:
            self._y = value
            self.signal_position.emit((self.x, self.y))

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if -6 < value < 0:
            self._speed = value
            self.acceleration = -1
        elif value == -6:
            self.alive = False
            self._speed = 5
            self.acceleration = 1
        elif value >= 0:
            self._speed = value

    def run(self):
        "This part require to understand a bit of physics: uniformly accelerated motion"
        while self.alive:
            sleep(0.05)
            position = self.acceleration*(self.speed)**2  #The movement represent a parabola where speed is the x variable and position the f(x)
            print(position)
            self.y -= position
            self.signal_position.emit((self.x, self.y))
            #print(self.x, self.y)
            self.speed -= 1
