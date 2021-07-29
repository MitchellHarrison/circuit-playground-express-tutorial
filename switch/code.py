import time
import board
from digitalio import DigitalInOut, Direction, Pull
from neopixel import NeoPixel

# create switch with pin D7
switch_pin = board.D7
switch = DigitalInOut(switch_pin)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

# neopixel object
pixels = NeoPixel(board.NEOPIXEL, 10, brightness=0.15)

# default color is red
DEFAULT_COLOR = (255,0,0)

while True:
    # get switch value
    switch_on = switch.value

    if switch_on:
        pixels.fill((0,255,0))
    else:
        pixels.fill(DEFAULT_COLOR)

