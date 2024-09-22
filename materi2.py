from gpiozero import LED
from time import sleep

# Mendefinisikan pin output yang tidak busy
led_pins = [2, 3, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26]

# Membuat objek LED untuk setiap pin
leds = [LED(pin) for pin in led_pins]

try:
    while True:
        # Menyalakan semua LED
        for led in leds:
            led.on()
        sleep(1)  # Tunda 1 detik

        # Mematikan semua LED
        for led in leds:
            led.off()
        sleep(1)  # Tunda 1 detik

except KeyboardInterrupt:
    # Mematikan semua LED saat program dihentikan
    for led in leds:
        led.off()
    print("Program dihentikan")