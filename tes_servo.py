from gpiozero import Servo
from time import sleep

servo = Servo(25)

try:
    while True:
        servo.min()
        sleep(1.5)
        servo.mid()
        sleep(1.5)
        servo.max()
        sleep(1.5)
except KeyboardInterrupt:
    print("Program stopped")