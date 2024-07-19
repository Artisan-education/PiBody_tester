from libs.ST7789 import *
from machine import Pin, SPI
import gc


SSD = ST7789


pdc = Pin(14, Pin.OUT, value=0)
pcs = Pin(15, Pin.OUT, value=1)
prst = Pin(13, Pin.OUT, value=1)

spi = SPI(1, 60_000_000, sck=Pin(10), mosi=Pin(11))
gc.collect()  

ssd = SSD(spi, height=240, width=300, disp_mode=4, dc=pdc, cs=pcs, rst=prst)
ssd.text('Hello, World!', 0, 0, 0xffff)