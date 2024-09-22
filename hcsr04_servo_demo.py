import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24
SERVO_PIN = 25

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.setup(SERVO_PIN, GPIO.OUT)
servo = GPIO.PWM(SERVO_PIN, 50)
servo.start(0)

def get_distance():

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        start_time = time.time()
    while GPIO.input(ECHO) == 1:
        end_time = time.time()

    duration = end_time - start_time
    distance = (duration * 34300) / 2

    return distance

def move_servo(angle):
    duty_cycle = 2 + (angle / 18)
    servo.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)

try:
    while True:
        distance = get_distance()
        print(f"Distance: {distance:.2f} cm")
        if distance < 20:
            move_servo(90)
        else:
            move_servo(0)
        time.sleep(1)

except KeyboardInterrupt:
    print("Program stopped")

finally:
    servo.stop()
    GPIO.cleanup()