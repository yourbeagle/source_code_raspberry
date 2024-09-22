import RPi.GPIO as GPIO
import time
from RPLCD.i2c import CharLCD


#Initialize LCD
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
lcd.clear()

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
TRIG = 23
ECHO = 24

# Set up GPIO pins
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

try:
    while True:
        # Ensure trigger is low
        GPIO.output(TRIG, False)
        print("Waiting For Sensor To Settle")
        time.sleep(2)

        # Send trigger pulse
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        # Initialize pulse_start and pulse_end
        pulse_start = time.time()
        pulse_end = time.time()

        # Measure the pulse start time
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        # Measure the pulse end time
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        # Calculate pulse duration
        pulse_duration = pulse_end - pulse_start

        # Calculate distance
        distance = pulse_duration * 17150
        distance = round(distance, 2)

        #Display to LCD
        lcd.cursor_pos = (0,0)
        lcd.write_string("Jarak: {:.1f} CM".format(distance))

        # Print the distance
        print("Distance:", distance, "cm")

        # Sleep for a short duration before the next measurement
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    lcd.clear()

finally:
    GPIO.cleanup()