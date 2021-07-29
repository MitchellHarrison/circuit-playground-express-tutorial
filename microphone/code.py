import math
import simpleio
import board
import array 
from neopixel import NeoPixel
from audiobusio import PDMIn

NUM_SAMPS = 160
NUM_PX = 10
CURVE = 2
SCALE_EXPONENT = math.pow(10, CURVE * -0.1)

def constrain(value, floor, ceiling):
    return max(floor, min(value, ceiling))


# Scale input_value between output_min and output_max, exponentially.
def log_scale(input_value, input_min, input_max, output_min, output_max):
    normalized_input_value = (input_value - input_min) / \
                             (input_max - input_min)
    return output_min + \
        math.pow(normalized_input_value, SCALE_EXPONENT) \
        * (output_max - output_min)


# Remove DC bias before computing RMS.
def normalized_rms(values):
    minbuf = int(mean(values))
    samples_sum = sum(
        float(sample - minbuf) * (sample - minbuf)
        for sample in values
    )
    return math.sqrt(samples_sum / len(values))


def mean(values):
    return sum(values) / len(values)


def volume_color(volume):
    return 200, volume * (255 // NUM_PIXELS), 0


pixels = NeoPixel(board.NEOPIXEL, NUM_PX, brightness = 0.15)
mic = PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA, sample_rate=16000, bit_depth=16)
samples = array.array("H", [0] * NUM_SAMPS)

# starting off in a quiet room
mic.record(samples, len(samples))
print("SAMPLES:")
print(samples)
input_floor = normalized_rms(samples) + 69
print("FLOOR:")
print(input_floor)
input_ceiling = input_floor + 500

while True:
    pixels.fill((255,0,0))
    mic.record(samples, len(samples))
    magnitude = normalized_rms(samples)
    c = log_scale(constrain(magnitude, input_floor, input_ceiling),
            input_floor, input_ceiling, 0, NUM_PX)

    bright = simpleio.map_range(c, 0, 10, 0, 0.5)
    pixels.brightness = bright
    print(bright)

