import time
from RPLCD.i2c import CharLCD

# Alamat I2C dan konfigurasi LCD
I2C_ADDR = 0x27  # Ganti dengan alamat I2C Anda
lcd = CharLCD('PCF8574', I2C_ADDR)

# Pesan yang ingin ditampilkan pada baris kedua sebagai running text
message = "Praktikum IOT Stiki Malang "

# Fungsi untuk membuat teks berjalan
def scroll_text(lcd, text, row, delay=0.3):
    length = len(text)
    if length <= 16:
        lcd.cursor_pos = (row, 0)
        lcd.write_string(text)
        return

    for i in range(length - 15):
        lcd.cursor_pos = (row, 0)
        lcd.write_string(text[i:i+16])
        time.sleep(delay)

try:
    while True:
        # Baris pertama menampilkan STIKI Malang secara statis
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string("STIKI Malang")

        # Baris kedua menampilkan teks berjalan
        scroll_text(lcd, message, row=1, delay=0.2)

except KeyboardInterrupt:
    # Bersihkan layar jika program dihentikan
    lcd.clear()