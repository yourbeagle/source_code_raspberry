import time
import RPi.GPIO as GPIO

# Set the pin numbering mode to BCM (Broadcom)
GPIO.setmode(GPIO.BCM)

# Pin assignments
red_pin = 17
green_pin = 22
blue_pin = 27

# Setup GPIO pins as output
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

# RGB values (initial state)
rgb = [0, 1, 1]

# Function to rotate the RGB values
def rotate(x):
    z = x[0]
    for i in range(len(x)-1):
        x[i] = x[i+1]
    x[-1] = z

# Function to set the LED states
def set_leds():
    GPIO.output(red_pin, rgb[0])
    GPIO.output(green_pin, rgb[1])
    GPIO.output(blue_pin, rgb[2])
    print(rgb)

# Initial delay before starting
time.sleep(1)
print("Hello world!")

# Initial sleep time and ramp toggle
sleep_time = 1
ramp_toggle = True

# Main loop
try:
    while True:
        for _ in range(10):
            # Adjust sleep time based on ramp_toggle
            sleep_time *= 0.8 if ramp_toggle else 1.25
            print(f"Current sleep time: {sleep_time}")
            for _ in range(3):
                set_leds()
                rotate(rgb)
                time.sleep(sleep_time)
        ramp_toggle = not ramp_toggle

# Clean up GPIO pins on KeyboardInterrupt (Ctrl+C)
except KeyboardInterrupt:
    print("Program interrupted. Cleaning up GPIO...")
    GPIO.cleanup()