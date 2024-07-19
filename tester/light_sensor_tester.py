from tester.tester import Tester
from machine import Pin, ADC
from utime import sleep

from root_tools import ctrl_button, display, color565

class LightSensorTester(Tester):
    name = "Light Sensor"
    def draw_loading_bar(self, value):
        display.fill_rectangle(40, display.height - 80, int(value * 240), 20, color565(255, 0, 0))
        display.fill_rectangle(40 + int(value * 240), display.height - 80, 240 - int(value * 240), 20, color565(64, 64, 64))

    def init_loading_bar(self):
        display.fill_rectangle(40, display.height - 80, 240, 20, color565(64, 64, 64))

    def __init__(self, pin):
        super().__init__(self.name, pin)
        self.pin = pin
        self.init_loading_bar()
        
 
    def start(self):    
        super().start()
        self.pot = ADC(Pin(self.pin))
       
    def test(self):
        value = self.pot.read_u16()
        self.draw_loading_bar(value / 65535)

    def finish(self):
        super().finish()
        


