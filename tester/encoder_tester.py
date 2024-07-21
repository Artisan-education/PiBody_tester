from tester.tester import Tester
from machine import Pin, PWM, time_pulse_us
from utime import sleep, sleep_us

from root_tools import *

from libs.rotary_irq_rp2 import RotaryIRQ

class EncoderTester(Tester):
    name = "Encoder"
    def __init__(self, pin):
            super().__init__(self.name, pin)
    
    def start(self):    
        super().start()
        init_loading_bar()
        self.encoder = RotaryIRQ(self.pin[0], self.pin[1], min_val=-15, max_val=15, incr=1, reverse=False, range_mode=RotaryIRQ.RANGE_WRAP)
        return True

    def test(self):
        counter = self.encoder.value()
        value = max(min((counter + 15) / 30, 1), 0)
        draw_loading_bar(value)
        display_info(f"Counter: {counter}")
        # Optional debounce delay

# Set up the encoder pins

# Initialize counter and previous state variable
