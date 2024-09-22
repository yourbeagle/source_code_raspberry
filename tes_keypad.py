import RPi.GPIO as GPIO
import time

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
correct_password = "1234"
input_password = ""

# The readLine function implements the procedure discussed in the article
# It sends out a single pulse to one of the rows of the keypad
# and then checks each column for changes
# If it detects a change, the user pressed the button that connects the given line
# to the detected column

prev_input = {C1: 0, C2: 0, C3: 0, C4: 0}

def readLine(line, characters):
    global input_password
    GPIO.output(line, GPIO.HIGH)
    for idx, col in enumerate([C1, C2, C3, C4]):
        current_input = GPIO.input(col)
        if current_input == 1 and prev_input[col] == 0:
            input_password += characters[idx]
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
            input_password = ""  # reset after successful entry
        elif len(input_password) >= len(correct_password):
            print("Access Denied")
            input_password = ""  # reset after incorrect entry

        time.sleep(0.3)

except KeyboardInterrupt:
    print("\nApplication stopped!")
    GPIO.cleanup()