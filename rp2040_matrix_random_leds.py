# Originally from https://github.com/Guitarman9119/Raspberry-Pi-Pico-/blob/main/Neopixel/Example1.py
# Modified to randomly flash the RP2040-Matrix's LEDs

from neopixel import Neopixel
import utime
import random

"""
The class constructor accepts 5 arguments, out of which 3 are mandatory. Following 
are arguments and their meaning in same order as the class accepts them:

1 - numpix: number of leds on your led-strip
2 - state_machine: id of PIO state machine used
3 - pin: pin on which data line to led-strip is connected
4 - mode: [default: "RGB"] mode and order of bits representing the color value. This
    can be any order of RGB or RGBW (neopixels are usually "GRB")
5 - delay: [default: 0.0001] delay used for latching of leds when sending data
"""
numpix = 25
strip = Neopixel(numpix, 0, 16, "GRB") # Class Constructor

red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (200, 0, 100)
colors_rgb = [red, orange, yellow, green, blue, indigo, violet]

delay = 0.55         # Delay set to 0.55 seconds
strip.brightness(16) # Can be 0-255, I have it set quite low... was at 42
# blank = (0,0,0)    # Unsure what if anything this line does?

'''
set_pixel(pixel_num, rgb_w, how_bright=None)
1 - Parameter pixel_num: Index of pixel to be set or slice object representing multiple leds.
2 - Parameter rgb_w: Tuple of form (r, g, b) or (r, g, b, w) representing color to be used.
3 - Parameter how_bright: [default: None] Brightness of current interval. If how_bright is
    None, use global brightness value.
'''
while True:
    # Note: Code block sets 5 random pixels to random colors prior to the strip.show() command
    # From random module: random.randint(start, stop)
    strip.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    strip.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    strip.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    strip.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    strip.set_pixel(random.randint(0, numpix-1), colors_rgb[random.randint(0, len(colors_rgb)-1)])
    strip.show()
    utime.sleep(delay)  # Wait 0.55 seconds per "delay" 
    strip.fill((0,0,0)) # Clear Leds from previous pass, seems to provide a smooth transition
