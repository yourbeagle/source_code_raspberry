import time
import adafruit_dht
import board
from RPLCD.i2c import CharLCD

# Inisialisasi sensor DHT11
dht_device = adafruit_dht.DHT11(board.D18)

# Inisialisasi LCD
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
lcd.clear()

while True:
    try:
        # Baca nilai suhu dan kelembaban dari sensor DHT11
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity

        # Tampilkan nilai suhu di baris 0 dan nilai kelembaban di baris 1
        lcd.cursor_pos = (0, 0)
        lcd.write_string("Temp: {:.1f} C".format(temperature_c))
        lcd.cursor_pos = (1, 0)
        lcd.write_string("Humidity: {}%".format(humidity))

    except RuntimeError as err:
        print(err.args[0])

    time.sleep(2.0)