#Jacob Sexton 7/15/25

from adafruit_circuitplayground import cp
import time

class LightRegion:
    def __init__(self, color, leds):
        self.__color = color
        self.__leds = leds

    def all_on(self):
        for i in self.__leds:
            cp.pixels[i] = self.__color

    def all_off(self):
        for i in self.__leds:
            cp.pixels[i] = (0, 0, 0)

cp.pixels.brightness = 0.3

red_region = LightRegion((255, 0, 0), (0, 1, 2, 3, 4))
blue_region = LightRegion((0, 0, 255), (5, 6, 7, 8, 9))

while True:
    red_region.all_on()
    blue_region.all_off()
    time.sleep(0.5)

    red_region.all_off()
    blue_region.all_on()
    time.sleep(0.5)
