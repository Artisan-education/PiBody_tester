from tester.tester import Tester
from machine import Pin, PWM
from utime import sleep

from root_tools import ctrl_button, display
class ServoTester(Tester):
    name = "Servo"
    def __init__(self, pin):
        super().__init__(self.name, pin)
        self.pin = pin
        
    def start(self):
        super().start()
        self.servo = PWM(Pin(self.pin))
        self.servo.freq(50)
        return True
    
    def set_angle(self, angle):
        # Convert angle to duty cycle (16-bit integer)
        duty = int((angle / 180 * 2 + 0.5) * 65535 / 20)
        self.servo.duty_u16(duty)

    def test(self):
        self.set_angle(ctrl_button.value() * 180)
    def finish(self):
        super().finish()
        # self.servo.deinit()
        


  