import time
from Buzzer import *
from Button import *
from Displays import *

class CounterGadget:
    """
    this is the class for the counter gadget that can count up and reset and display 
    a count on an LCD
    """

    def __init__(self):
        self._number = 0
        self._display = LCDDisplay(sda = 0, scl = 1, i2cid = 0)
        self._buzzer = PassiveBuzzer(15)
        self._buttonup = Button(17,"up", buttonhandler =self)
        self._buttonreset = Button(16, "reset", buttonhandler =self)
        self.display()
        
    def increment(self):
        """ Add one to the number attribute """

        self._number = self._number + 1

    def reset(self):
        """ Reset the attributes number """

        self._number = 0

    def display(self):
        """ Show the number on the display"""

        self._display.showNumber(self._number)

    def run(self):
        """ Keep this app runing """

        while True:
            time.sleep(0.5)
    def buttonPressed(self,name):
        """ Handle the button presses """
        if name == "up":
            self.increment()
        elif name == "reset":
            self.reset()
        self.display()
    

    def buttonReleased(self,name):
        """ Handle Button releases"""
        pass