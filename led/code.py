import time
import board
from digitalio import DigitalInOut, Direction

# define LED (board.D13 also works)
led_pin = board.LED
led = DigitalInOut(led_pin)
led.direction = Direction.OUTPUT

# toggle light every second
while True:
    led.value = 1
    time.sleep(1)
    led.value = 0
    time.sleep(1)
