from tester.tester import Tester
from machine import Pin, ADC
from utime import sleep

from root_tools import ctrl_button, display, color565

class PotentiometerTester(Tester):
    name = "Potentiometer"
    def draw_loading_bar(self, value):
        display.fill_rectangle(40, display.height - 80, int(value * 240), 20, color565(255, 10, 128))
        display.fill_rectangle(40 + int(value * 240), display.height - 80, 240 - int(value * 240), 20, color565(64, 64, 64))

    def init_loading_bar(self):
        display.fill_rectangle(40, display.height - 80, 240, 20, color565(64, 64, 64))

    def __init__(self, pin):
        super().__init__(self.name, pin)
        self.pin = pin
        
 
    def start(self):    
        super().start()
        self.init_loading_bar()
        self.pot = ADC(Pin(self.pin))
        return True
       
    def test(self):
        value = self.pot.read_u16()
        self.draw_loading_bar(value / 65535)

    def finish(self):
        super().finish()
        


