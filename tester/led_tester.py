from tester.tester import Tester
from machine import Pin

from root_tools import ctrl_button, display
class LedTester(Tester):
    name = "LED"
    def __init__(self, led_pin):
        super().__init__(self.name, led_pin)
        self.led_pin = led_pin

    def start(self):
        super().start()
        self.led = Pin(self.led_pin, Pin.OUT)

    def test(self):
        self.led.value(ctrl_button.value())

    def finish(self):
        super().finish()
        led = Pin(self.pin, Pin.OUT)
        led.value(0)
        