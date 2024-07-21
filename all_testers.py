
from tester.led_tester import LedTester
from tester.led_tower_tester import LedTowerTester
from tester.servo_tester import ServoTester
from tester.motion_tester import MotionTester
from tester.touch_tester import TouchTester
from tester.potentiometer_tester import PotentiometerTester
from tester.light_sensor_tester import LightSensorTester
from tester.ultrasonic_tester import UltrasonicTester
from tester.encoder_tester import EncoderTester
from tester.joystick_tester import JoystickTester
from tester.sound_tester import SoundTester
from tester.climate_tester import ClimateTester
from tester.gyro_tester import GyroTester
from tester.gesture_tester import GestureTester
from tester.color_tester import ColorTester


led_tester = LedTester(7)
led_tower_tester = LedTowerTester(8)
servo_tester = ServoTester(9)
motion_tester = MotionTester(28)
touch_tester = TouchTester(28)
potentiometer_tester = PotentiometerTester(28)
light_sensor_tester = LightSensorTester(28)
ultrasonic_tester = UltrasonicTester([2, 3])
encoder_tester = EncoderTester([0, 1])
joystick_tester = JoystickTester([26, 27])
sound_tester = SoundTester([26, 27])
climate_tester = ClimateTester([0, 1])
gyro_tester = GyroTester([2, 3])
gesture_tester = GestureTester([0, 1])
color_tester = ColorTester([0, 1])


test_list = [led_tester, led_tower_tester, servo_tester, motion_tester, touch_tester, potentiometer_tester, light_sensor_tester, ultrasonic_tester, encoder_tester, joystick_tester, sound_tester, climate_tester, gyro_tester, gesture_tester, color_tester ]


