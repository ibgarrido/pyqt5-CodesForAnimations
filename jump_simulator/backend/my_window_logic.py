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
        self.y = 200
        self.acceleration = 1
        self.speed = 5
        self.alive = False
        self.signal_position = None



    def run(self):
        "This part require to understand a bit of physics: uniformly accelerated motion"
        while self.alive:
            sleep(0.05)
            position = self.acceleration*(self.speed)**2  #The movement represent a parabola where speed is the x variable and position the f(x)
            # print(position) Debuging
            self.y -= position
            self.signal_position.emit((self.x, self.y))
            # print(self.x, self.y) Debuging
            self.speed -= 1
            if self.speed < 0:
                self.acceleration = -1
            if self.speed == -6:
                self.alive = False
                self.speed = 5
                self.acceleration = 1
