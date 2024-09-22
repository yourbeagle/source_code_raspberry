import tm1637
import time
from datetime import datetime
import RPi.GPIO as GPIO

# Define GPIO pins for CLK and DIO
CLK = 24  # GPIO 18 (BCM mode)
DIO = 23  # GPIO 17 (BCM mode)

# Initialize the display
display = tm1637.TM1637(clk=CLK, dio=DIO)

# Configure the display brightness (range 0-7)
display.brightness(1)

def show_time():
    while True:
        now = datetime.now()
        hour = now.hour
        minute = now.minute

        # Display the time as HH:MM
        display.numbers(hour, minute)

        time.sleep(1)

if __name__ == "__main__":
    try:
        show_time()
    except KeyboardInterrupt:
        # Clear the display when the program is interrupted
        display.write([0, 0, 0, 0])
        GPIO.cleanup()
        print("Program interrupted and display cleared.")