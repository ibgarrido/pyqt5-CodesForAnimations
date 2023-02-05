# Source : https://www.geeksforgeeks.org/making-label-jump-using-pyqt5-in-python/
# importing required libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
  
# Window class
class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
  
        # setting title
        self.setWindowTitle("Python ")
  
        # width of window
        self.w_width = 500
  
        # height of window
        self.w_height = 500
  
        # setting geometry
        self.setGeometry(100, 100, 
                         self.w_width, self.w_height)
  
        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()
  
        # speed variable
        self.speed = 5
  
        self.mass = 1
  
        # jump flag
        self.jump = False
  
    # method for components
    def UiComponents(self):
  
        # creating a label
        self.label = QLabel(self)
  
        # label width
        self.l_width = 40
  
        # label height
        self.l_height = 40
  
        # setting geometry to the label
        self.label.setGeometry(200, 200, 
                               self.l_width,
                               self.l_height)
  
        # setting stylesheet to the label
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px solid darkgreen;"
                                 "background : lightgreen;"
                                 "}")
  
  
        # creating a timer object
        timer = QTimer(self)
  
        # setting timer start time
        timer.start(50)
  
        # adding action to the timer
        timer.timeout.connect(self.show_time)
  
  
    # method called by the timer
    def show_time(self):
  
        # checking jump flag
        if self.jump:
  
            y = self.label.y()
  
            # calculate force (F). 
            # F = 1 / 2 * mass * velocity ^ 2.
            # here we are not using  ( 1/2 )
            Force = self.mass * (self.speed ** 2)
  
            # change in the y co-ordinate
            y -= Force
  
            self.label.move(200, y)
  
            # decreasing velocity while going up 
            # and become negative while coming down
            self.speed = self.speed - 1
  
            # object reached its maximum height
            if self.speed < 0:
                # negative sign is added to 
                # counter negative velocity
                self.mass = -1
  
            # objected reaches its original state
            if self.speed == -6:
                # making jump equal to false
                self.jump = False
  
                # setting original values to 
                # speed  and mass
                self.speed = 5
                self.mass = 1
  
    # override the key press event
    def keyPressEvent(self, event):
        
       # if space bar is pressed
       if event.key() == Qt.Key_Space:
          
           # make the jump flag true
           self.jump = True
  
  
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())