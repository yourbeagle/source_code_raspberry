from RPLCD.i2c import CharLCD
from gpiozero import LED
import RPi.GPIO as GPIO
import time

# Initialize the LCD
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
lcd.clear()
lcd.write_string('Enter Password:')

# Initialize LED
red = LED(17)
green = LED (22)

# these GPIO pins are connected to the keypad
# change these according to your connections!
L1 = 5
L2 = 6
L3 = 13
L4 = 19

C1 = 12
C2 = 16
C3 = 20
C4 = 21

# Initialize the GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

# Make sure to configure the input pins to use the internal pull-down resistors
GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Define the correct password
correct_password = "110801"
input_password = ""

prev_input = {C1: 0, C2: 0, C3: 0, C4: 0}

def readLine(line, characters):
    global input_password
    GPIO.output(line, GPIO.HIGH)
    for idx, col in enumerate([C1, C2, C3, C4]):
        current_input = GPIO.input(col)
        if current_input == 1 and prev_input[col] == 0:
            input_password += characters[idx]
            lcd.clear()
            lcd.write_string('Enter Password:')
            lcd.crlf()
            lcd.write_string(input_password)
            print(characters[idx])
        prev_input[col] = current_input
    GPIO.output(line, GPIO.LOW)

try:
    while True:
        # call the readLine function for each row of the keypad
        readLine(L1, ["1", "2", "3", "A"])
        readLine(L2, ["4", "5", "6", "B"])
        readLine(L3, ["7", "8", "9", "C"])
        readLine(L4, ["*", "0", "#", "D"])

        # Check if input password matches the correct password
        if input_password == correct_password:
            print("Access Granted")
            lcd.clear()
            lcd.write_string('Access Granted')
            green.on()
            time.sleep(5)  # display message for 3 seconds
            green.off()
            lcd.clear()
            lcd.write_string('Enter Password:')
            input_password = ""  # reset after successful entry
        elif len(input_password) >= len(correct_password):
            print("Access Denied")
            lcd.clear()
            lcd.write_string('Access Denied')
            red.on()
            time.sleep(5)  # display message for 3 seconds
            red.off()
            lcd.clear()
            lcd.write_string('Enter Password:')
            input_password = ""  # reset after incorrect entry

        time.sleep(0.3)

except KeyboardInterrupt:
    print("\nApplication stopped!")
    GPIO.cleanup()