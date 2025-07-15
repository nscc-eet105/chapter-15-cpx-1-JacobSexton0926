#Jacob Sexton 7/15/25

from adafruit_circuitplayground import cp
import time

class LightRegion:
    def __init__(self, color, leds, tone):
        self.__color = color
        self.__leds = leds
        self.__tone = tone
    def all_on(self):
        for i in self.__leds:
            cp.pixels[i] = self.__color
    def all_off(self):
        for i in self.__leds:
            cp.pixels[i] = (0, 0, 0)
    def play_tone(self, duration):
        cp.start_tone(self.__tone)
        time.sleep(duration)
        cp.stop_tone()
cp.pixels.brightness = 0.3
regions = {
    "red": LightRegion((255, 0, 0), (0, 1, 2), 440),
    "green": LightRegion((0, 255, 0), (3, 4), 550),
    "blue": LightRegion((0, 0, 255), (5, 6, 7), 660),
    "yellow": LightRegion((255, 255, 0), (8, 9), 770)
}

while True:
    for name, region in regions.items():
        region.all_on()
        region.play_tone(0.3)
        region.all_off()
        time.sleep(0.1)
