from tester.tester import Tester
from machine import Pin, PWM
from utime import sleep

from root_tools import ctrl_button, display, color565

class TouchTester(Tester):
    name = "Touch Sensor"
    def __init__(self, pin):
        super().__init__(self.name, pin)
        self.pin = pin
        

    def start(self):    
        super().start()
        self.touch = Pin(self.pin, Pin.IN)
        return True
    def test(self):
        if self.touch.value():
            display.fill_circle(display.width // 2, display.height  - 80, 10,  color565(0, 255, 0))
        else:
            display.fill_circle(display.width // 2, display.height  - 80, 10,  color565(0, 0, 0))

    def finish(self):
        super().finish()
        
