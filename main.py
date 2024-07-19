from machine import Pin, SPI
from utime import sleep_ms, ticks_ms
from root_tools import display, ctrl_button 
from libs.ILI9341 import Display, color565
from tester.led_tester import LedTester
from tester.led_tower_tester import LedTowerTester
from tester.servo_tester import ServoTester
from tester.motion_tester import MotionTester
from tester.touch_tester import TouchTester
from tester.potentiometer_tester import PotentiometerTester
from tester.light_sensor_tester import LightSensorTester

test_ind = 0
hold_duration = 1500


led_tester = LedTester(7)
led_tower_tester = LedTowerTester(8)
servo_tester = ServoTester(9)
motion_tester = MotionTester(28)
touch_tester = TouchTester(28)
potentiometer_tester = PotentiometerTester(28)
light_sensor_tester = LightSensorTester(28)

test_list = [light_sensor_tester ,potentiometer_tester, touch_tester, motion_tester, led_tester, led_tower_tester, servo_tester]

def start_test(ind):
    
    test_list[test_ind - 1].finish()
    display.clear()
    current_test = test_list[ind]

    current_test.start()



def draw_loading_bar(value):
    display.fill_rectangle(40, 100, int(value * 240), 40, color565(128, 255, 0))

def init_loading_bar():
    display.fill_rectangle(40, 100, 240, 40, color565(64, 64, 64))


def main():
    global test_ind
    start_test(test_ind)
    hold_time_elapsed = ticks_ms()



    init_loading_bar()
    while True:
        if ctrl_button.value():
            if ticks_ms() - hold_time_elapsed > hold_duration:
                test_ind = (test_ind + 1) % len(test_list)

                start_test(test_ind)
                hold_time_elapsed = ticks_ms()
                print("Ticked")
            else:
                draw_loading_bar((ticks_ms() - hold_time_elapsed) / hold_duration)
        else:
            hold_time_elapsed = ticks_ms()
            init_loading_bar()
            test_list[test_ind].test()



main()