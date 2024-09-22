import RPi.GPIO as GPIO
import tm1637
import time

# Initialize the TM1637 7-segment display
CLK = 25  # Ganti dengan pin GPIO yang Anda gunakan untuk CLK
DIO = 18  # Ganti dengan pin GPIO yang Anda gunakan untuk DIO
display = tm1637.TM1637(clk=CLK, dio=DIO)

# Initialize the LCD (optional, can be removed if you don't need it)

# GPIO pins connected to the keypad
L1 = 5
L2 = 6
L3 = 13
L4 = 19

C1 = 12
C2 = 16
C3 = 20
C4 = 21

# Initialize GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Define the correct password

input_angka = ""

prev_input = {C1: 0, C2: 0, C3: 0, C4: 0}

def read_line(line, characters):
    """Read a line of keypad and update the input_password."""
    global input_angka
    GPIO.output(line, GPIO.HIGH)
    for idx, col in enumerate([C1, C2, C3, C4]):
        current_input = GPIO.input(col)
        if current_input == 1 and prev_input[col] == 0:
            input_angka += characters[idx]
            display.number(int(characters[idx]))  # Display the pressed key on TM1637
            print(characters[idx])
        prev_input[col] = current_input
    GPIO.output(line, GPIO.LOW)

try:
    while True:
        # Call the read_line function for each row of the keypad
        read_line(L1, ["1", "2", "3", "A"])
        read_line(L2, ["4", "5", "6", "B"])
        read_line(L3, ["7", "8", "9", "C"])
        read_line(L4, ["*", "0", "#", "D"])

        time.sleep(0.3)

except KeyboardInterrupt:
    print("\nApplication stopped!")
finally:
    GPIO.cleanup()