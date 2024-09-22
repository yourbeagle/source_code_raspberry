import RPi.GPIO as GPIO
import time

# Use Broadcom (BCM) GPIO numbering
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins for the RGB LED
red_pin = 17
green_pin = 22
blue_pin = 27

# Setup all the pins as outputs
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

# Function to turn off all LEDs
def turn_off_all():
    GPIO.output(red_pin, GPIO.LOW)
    GPIO.output(green_pin, GPIO.LOW)
    GPIO.output(blue_pin, GPIO.LOW)

# Function to light up the RGB LED with specific color
def light_up_color(red, green, blue, delay=2):
    GPIO.output(red_pin, red)
    GPIO.output(green_pin, green)
    GPIO.output(blue_pin, blue)
    time.sleep(delay)
    turn_off_all()

try:
    while True:
        # Red for 2 seconds
        light_up_color(GPIO.HIGH, GPIO.LOW, GPIO.LOW)

        # Green for 2 seconds
        light_up_color(GPIO.LOW, GPIO.HIGH, GPIO.LOW)

        # Blue for 2 seconds
        light_up_color(GPIO.LOW, GPIO.LOW, GPIO.HIGH)

# Cleanup GPIO on program exit
except KeyboardInterrupt:
    print("Program interrupted. Cleaning up GPIO...")
    GPIO.cleanup()

finally:
    GPIO.cleanup()