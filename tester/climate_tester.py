from tester.tester import Tester
from machine import Pin, I2C
from utime import sleep
from libs.BME280 import BME280
from root_tools import *

class ClimateTester(Tester):
    name = "Climate Sensor"

    def __init__(self, pin):
            super().__init__(self.name, pin)
    
    def start(self):    
        super().start()

        if self.pin[0] == 0:
            bus = 0
        else:
            bus = 1
        i2c = I2C(bus, sda=Pin(self.pin[0]), scl=Pin(self.pin[1]))

        for i in range(5): 
            try:
                self.bme280 = BME280(i2c=i2c)
                self.bme280.temperature
                display.fill_rectangle(0, 90, display.width, 100, color565(0,0,0))
                return True
            except Exception as e:
                display.display_text(f"Sensor not found. Attempt {i + 1} in {5}. {e}", 20, 100)
                sleep(2)
        
        
        return False
        
    def test(self):
        try :
            temp = self.bme280.temperature
            hum = self.bme280.humidity
            pres = self.bme280.pressure
        except:
            temp = 0
            hum = 0
            pres = 0
        # Print sensor readings
        display.display_text(f"Temperature: {temp}", 40, 100)
        display.display_text(f"Humidity: {hum}", 40, 130)
        display.display_text(f"Pressure: {pres}", 40, 160)

        print()

        sleep_ms(10)


    def finish(self):
        super().finish()