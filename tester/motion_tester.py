from tester.tester import Tester
from machine import Pin, PWM
from utime import sleep

from root_tools import ctrl_button, display, color565

class MotionTester(Tester):
    name = "Motion Detector"
    def __init__(self, pin):
        super().__init__(self.name, pin)
        self.pin = pin
        

    def start(self):    
        super().start()
        self.detector = Pin(self.pin, Pin.IN)
        return True
    def test(self):
        if self.detector.value():
            display.display_text("Motion is detected", 50, display.height - 50)
            display.fill_circle(display.width // 2, display.height  - 80, 10,  color565(0, 255, 0))
        else:
            display.display_text("No motion detected", 50, display.height - 50)
            display.fill_circle(display.width // 2, display.height  - 80, 10,  color565(0, 0, 0))

    def finish(self):
        super().finish()
        
