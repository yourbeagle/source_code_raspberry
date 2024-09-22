import RPi.GPIO as GPIO
import time

# Pin Definitions
segmentPins = [2, 3, 4, 17, 27, 22, 10, 9]  # Segments a, b, c, d, e, f, g, DP
digitPins = [11, 5, 6]  # Digits 1, 2, 3

# 7-segment display digit mapping (common cathode)
segments = {
    '0': (1, 1, 1, 1, 1, 1, 0, 0),
    '1': (0, 1, 1, 0, 0, 0, 0, 0),
    '2': (1, 1, 0, 1, 1, 0, 1, 0),
    '3': (1, 1, 1, 1, 0, 0, 1, 0),
    '4': (0, 1, 1, 0, 0, 1, 1, 0),
    '5': (1, 0, 1, 1, 0, 1, 1, 0),
    '6': (1, 0, 1, 1, 1, 1, 1, 0),
    '7': (1, 1, 1, 0, 0, 0, 0, 0),
    '8': (1, 1, 1, 1, 1, 1, 1, 0),
    '9': (1, 1, 1, 1, 0, 1, 1, 0)
}

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for pin in segmentPins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
    for pin in digitPins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)  # Turn off all digits initially

def displayDigit(value, digit):
    # Activate the corresponding digit
    for i in range(3):
        GPIO.output(digitPins[i], GPIO.HIGH)
    GPIO.output(digitPins[digit], GPIO.LOW)

    # Set the segments
    segmentValues = segments.get(value, (0, 0, 0, 0, 0, 0, 0, 0))
    for i in range(8):
        GPIO.output(segmentPins[i], segmentValues[i])

def displayNumber(number):
    s = str(number).zfill(3)  # Zero fill to 3 digits
    for digit in range(3):
        displayDigit(s[digit], digit)
        time.sleep(0.005)  # Short delay for multiplexing

try:
    setup()
    while True:
        displayNumber(123)  # Display the number 123
except KeyboardInterrupt:
    GPIO.cleanup()