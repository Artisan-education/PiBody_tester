from tester.tester import Tester
from machine import Pin, I2C
from utime import sleep
from libs.MPU6050 import MPU6050
from root_tools import *

class GyroTester(Tester):
    name = "Gyroscope Accelerometer"

    def __init__(self, pin):
            super().__init__(self.name, pin)
            init_loading_bar()
    
    def start(self):    
        super().start()

        if self.pin[0] == 0:
            bus = 0
        else:
            bus = 1
        i2c = I2C(bus, sda=Pin(self.pin[0]), scl=Pin(self.pin[1]))

        for i in range(5): 
            try:
                self.mpu = MPU6050(i2c=i2c)
                self.mpu.wake()
                display.fill_rectangle(0, 90, display.width, 100, color565(0,0,0))
                return True
            except Exception as e:
                display.display_text(f"Sensor not found. Attempt {i + 1} in {5}. {e}", 20, 100)
                sleep(2)
        
        return False
        
    def test(self):
        try:
            gyro = self.mpu.read_gyro_data()
            accel = self.mpu.read_accel_data()
        except:
            gyro = (0, 0, 0)
            accel = (0, 0, 0)
            
        # Print sensor readings
        display.display_text(f"Gyroscope: x: {gyro[0] :.3f} y: {gyro[1] :.3f} z: {gyro[2] :.3f}", 40, 100)
        display.display_text(f"Accelermoter: x: {accel[0] :.3f} y: {accel[1] :.3f} z: {accel[2] :.3f}", 40, 130)

        print()

        sleep_ms(10)


    def finish(self):
        super().finish()