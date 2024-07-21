from tester.tester import Tester
from machine import Pin, ADC
from utime import sleep

from root_tools import *

class SoundTester(Tester):
    name = "Microphone"

    def __init__(self, pin):
            super().__init__(self.name, pin)
            init_loading_bar()
    
    def start(self):    
        super().start()

        self.analog = ADC(self.pin[0])
        self.digital = Pin(self.pin[1], Pin.IN)

        return True
        
    def test(self):
        sound_analog = self.analog.read_u16()
        sound_digital = self.digital.value()

        draw_loading_bar(sound_analog / 65535)
        show_circile(sound_digital)
        sleep_ms(1)


    def finish(self):
        super().finish()