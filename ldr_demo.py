import RPi.GPIO as GPIO
from time import sleep

# Set the Raspberry Pi GPIO pin number connected to the DO pin of the ldr light sensor module
DO_PIN = 7

# Set the GPIO mode and configure the ldr light sensor module pin as INPUT
GPIO.setmode(GPIO.BCM)
GPIO.setup(DO_PIN, GPIO.IN)

# Initialize the previous state variable with the current state
prev_light_state = GPIO.input(DO_PIN)

try:
    while True:
        # Read the current state of the ldr light sensor module
        light_state = GPIO.input(DO_PIN)

        # Check for a state change (LOW to HIGH or HIGH to LOW)
        if light_state != prev_light_state:
            if light_state == GPIO.LOW:
                print("Cahaya Terdeteksi")
            else:
                print("Cahaya Hilang")

        # Update the previous state variable
        prev_light_state = light_state

        # Add a small delay to prevent continuous readings
        sleep(0.1)

except KeyboardInterrupt:
    # Clean up GPIO settings when Ctrl+C is pressed
    GPIO.cleanup()
    print("\n Exiting the program.")