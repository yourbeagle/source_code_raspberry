import asyncio
import websockets
import RPi.GPIO as GPIO

# Setup GPIO
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

async def control_led(websocket, path):
    async for message in websocket:
        if message == "on":
            GPIO.output(LED_PIN, GPIO.HIGH)
            await websocket.send("LED is ON")
        elif message == "off":
            GPIO.output(LED_PIN, GPIO.LOW)
            await websocket.send("LED is OFF")

start_server = websockets.serve(control_led, "192.168.1.5", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
