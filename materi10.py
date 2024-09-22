from RPLCD.i2c import CharLCD
from gpiozero import MotionSensor, LED
from time import sleep

# Inisialisasi LCD
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)

# Inisialisasi PIR sensor dan LED
pir = MotionSensor(21)
led = LED(17)

try:
    while True:
        if pir.motion_detected:
            lcd.clear()
            lcd.write_string('Ada Gerakan')
            print('Ada Gerakan')
            led.on()
        else:
            lcd.clear()
            lcd.write_string('Standby')
            led.off()
        sleep(0.1)
except KeyboardInterrupt:
    lcd.clear()
    lcd.write_string('Program berhenti')
    led.off()
    print("Program dihentikan oleh pengguna")
