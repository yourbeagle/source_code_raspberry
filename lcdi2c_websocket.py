import asyncio
import websockets
import smbus2
import time

# Konfigurasi I2C LCD
I2C_ADDR = 0x27  # Ganti dengan alamat I2C dari LCD Anda
LCD_WIDTH = 16   # Lebar dari LCD (16 karakter)

# Perintah LCD
LCD_CHR = 1  # Kirim data
LCD_CMD = 0  # Kirim perintah

LCD_LINE_1 = 0x80  # Alamat untuk baris pertama
LCD_LINE_2 = 0xC0  # Alamat untuk baris kedua

LCD_BACKLIGHT = 0x08  # Backlight on
ENABLE = 0b00000100  # Enable bit

# Waktu delay
E_PULSE = 0.0005
E_DELAY = 0.0005

# Inisialisasi I2C
bus = smbus2.SMBus(1)

def lcd_init():
    lcd_byte(0x33, LCD_CMD)  # 110011 Initialize
    lcd_byte(0x32, LCD_CMD)  # 110010 Initialize
    lcd_byte(0x06, LCD_CMD)  # Cursor move direction
    lcd_byte(0x0C, LCD_CMD)  # Display On,Cursor Off, Blink Off
    lcd_byte(0x28, LCD_CMD)  # Data length, number of lines, font size
    lcd_byte(0x01, LCD_CMD)  # Clear display
    time.sleep(E_DELAY)

def lcd_byte(bits, mode):
    bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
    bits_low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT

    bus.write_byte(I2C_ADDR, bits_high)
    lcd_toggle_enable(bits_high)

    bus.write_byte(I2C_ADDR, bits_low)
    lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
    time.sleep(E_DELAY)
    bus.write_byte(I2C_ADDR, (bits | ENABLE))
    time.sleep(E_PULSE)
    bus.write_byte(I2C_ADDR, (bits & ~ENABLE))
    time.sleep(E_DELAY)

def lcd_string(message, line):
    message = message.ljust(LCD_WIDTH, " ")
    lcd_byte(line, LCD_CMD)
    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)

async def handle_message(websocket, path):
    lcd_init()  # Inisialisasi LCD
    async for message in websocket:
        print(f"Menerima pesan: {message}")
        if len(message) > LCD_WIDTH:
            lcd_string(message[:LCD_WIDTH], LCD_LINE_1)
            lcd_string(message[LCD_WIDTH:LCD_WIDTH*2], LCD_LINE_2)
        else:
            lcd_string(message, LCD_LINE_1)
            lcd_string("", LCD_LINE_2)

# Memulai server WebSocket
async def main():
    async with websockets.serve(handle_message, "192.168.1.5", 6789):
        print("Server WebSocket dimulai pada port 6789")
        await asyncio.Future()  # Berjalan selamanya

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server dihentikan. Membersihkan layar LCD...")
        lcd_clear()