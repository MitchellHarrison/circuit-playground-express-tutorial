import time
import board
from adafruit_thermistor import Thermistor
from analogio import AnalogIn

# thermistor pin (board.A9 also works)
temp_pin = board.TEMPERATURE

# thermistor parameters
SERIES_RESISTOR = 10000
NOMINAL_RESISTANCE = 10000
NOMINAL_TEMP = 25
B_COEFFICIENT = 3950

# define thermistor
thermistor = Thermistor(
    temp_pin, 
    SERIES_RESISTOR, 
    NOMINAL_RESISTANCE, 
    NOMINAL_TEMP, 
    B_COEFFICIENT
)

# main loop
while True:
    # thermistor returns temp in Celcius
    c = thermistor.temperature

    # convert to freedom temperature
    f = (c*(9/5)) + 32

    # display temp and sleep for one second
    print(f)
    time.sleep(1)

