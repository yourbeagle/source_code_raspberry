from gpiozero import LED, Servo
from time import sleep

# Inisialisasi LED untuk lampu lalu lintas
red = LED(17)    # LED merah
yellow = LED(27) # LED kuning
green = LED(22)  # LED hijau

# Inisialisasi Servo
servo = Servo(25)

try:
    while True:
        # Lampu hijau menyala dan gerbang terbuka
        green.on()
        yellow.off()
        red.off()
        servo.min()  # Gerbang terbuka
        sleep(5)  # Hijau menyala selama 5 detik

        # Lampu kuning menyala dan gerbang setengah terbuka
        green.off()
        yellow.on()
        red.off()
        servo.mid()  # Gerbang setengah terbuka
        sleep(2)  # Kuning menyala selama 2 detik

        # Lampu merah menyala dan gerbang tertutup
        green.off()
        yellow.off()
        red.on()
        servo.max()  # Gerbang tertutup
        sleep(5)  # Merah menyala selama 5 detik

except KeyboardInterrupt:
    print("Program stopped")
    red.off()
    yellow.off()
    green.off()
    servo.value = None  # Matikan servo