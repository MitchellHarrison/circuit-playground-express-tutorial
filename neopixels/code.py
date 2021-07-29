import time
import board
from neopixel import NeoPixel

# number of pixels to work with
num_pixels = 10

# brightness value (0-1)
brightness = 0.15

# pixels acts like a list of tuples
pixels = NeoPixel(board.NEOPIXEL, num_pixels, brightness=brightness)

while True:
    # fill all pixels in one line
    pixels.fill((0,255,0))

    time.sleep(1)

    # fill with for loop
    red = 255
    green = 0
    blue = 0
    for i in range(num_pixels):
        inc = i*25
        color = (red-inc, green, blue+inc)
        pixels[i] = color

    time.sleep(3)

