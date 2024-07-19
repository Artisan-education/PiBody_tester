from machine import Pin, SPI
from utime import sleep_ms  

from libs.ILI9341 import Display, color565


def initialize_display():
    spi = SPI(1, baudrate=40000000, sck=Pin(14), mosi=Pin(15))
    display = Display(spi, dc=Pin(12), cs=Pin(11), rst=Pin(13), width=320, height=240)
    display.clear()
    return display

    

ctrl_button = Pin(6, Pin.IN)
display = initialize_display()
    
