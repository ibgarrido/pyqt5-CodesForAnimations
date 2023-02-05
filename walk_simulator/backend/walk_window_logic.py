from PyQt5.QtCore import QObject, pyqtSignal, QTimer
import parameters as p


class WalkWindowLogic(QObject):

    signal_move_square = pyqtSignal(tuple)

    def __init__(self, square):
        super().__init__()
        self.square = square
        self.timer_window = QTimer(self)
        self.update_window()

    def move_square(self, key):
        if key == p.KEY_DOWN or p.KEY_UP or p.KEY_RIGHT or p.KEY_LEFT:
            position = self.square.move(key)
        self.signal_move_square.emit(position)

    def update_window(self):
        self.timer_window.setInterval(50)
        self.timer_window.start()


class Square(QObject):

    def __init__(self):
        super().__init__()
        self._x = p.INITIAL_POS_SQUARE_X
        self._y = p.INITIAL_POS_SQUARE_Y
        self.height = p.HEIGHT_SQUARE
        self.widht = p.WIDHT_SQUARE
        self.speed = p.SPEED_SQUARE

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value >= p.LIMIT_RIGHT - self.widht:
            self._x = p.LIMIT_RIGHT - self.widht

        elif value <= p.LIMIT_LEFT:
            self._x = p.LIMIT_LEFT
        else:
            self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if value >= p.LIMIT_DOWN - self.height:
            self._y = p.LIMIT_DOWN - self.height
        elif value < p.LIMIT_UP:
            self._y = p.LIMIT_UP
        else:
            self._y = value

    def move(self, key: str):
        """This method recieve the keys and execute the movements.
        It returns a tuple with the final position."""
        if key == p.KEY_LEFT:
            self.x -= self.speed

        elif key == p.KEY_RIGHT:
            self.x += self.speed

        elif key == p.KEY_DOWN:
            self.y += self.speed

        elif key == p.KEY_UP:
            self.y -= self.speed

        # print(self.x, self.y)

        return self.x, self.y
