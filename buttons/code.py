import time
import board
from digitalio import DigitalInOut, Direction, Pull
from neopixel import NeoPixel

# use left button at pin D4
left_button_pin = board.D4
left_button = DigitalInOut(left_button_pin)
left_button.direction = Direction.INPUT
left_button.pull = Pull.DOWN

# use right button at pin D5
right_button_pin = board.D5
right_button = DigitalInOut(right_button_pin)
right_button.direction = Direction.INPUT
right_button.pull = Pull.DOWN

# create neopixels object
pixels = NeoPixel(board.NEOPIXEL, 10, brightness = 0.15)

while True:
    # check for button presses
    left_pressed = left_button.value
    right_pressed = right_button.value

    # change color based on button press combnations
    if left_pressed and right_pressed:
        pixels.fill((0,255,255))

    elif left_pressed:
        pixels.fill((0,255,0))

    elif right_pressed:
        pixels.fill((255,0,0))

    else:
        pixels.fill((0,0,0))

