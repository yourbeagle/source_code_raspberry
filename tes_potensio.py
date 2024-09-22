from gpiozero import LightSensor
from time import sleep

potensio = LightSensor(18)
while True:
    print(potensio.value)
    sleep(0.1)