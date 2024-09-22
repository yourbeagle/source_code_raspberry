import time
import asyncio
import websockets
import adafruit_dht
import board
import json
from gpiozero import Servo

# Setup DHT11 sensor and servo motor
dht_device = adafruit_dht.DHT11(board.D18)
servo = Servo(25)

async def handle_client(websocket, path):
    while True:
        try:
            # Read temperature and humidity from DHT11
            temperature_c = dht_device.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = dht_device.humidity

            # Prepare the data to send
            data = {
                "temperature_c": temperature_c,
                "temperature_f": temperature_f,
                "humidity": humidity
            }
            data_json = json.dumps(data)
            print(f"Sending data: {data_json}")  # Log the data being sent
            await websocket.send(data_json)

            # Receive commands from the client
            command = await websocket.recv()
            if command == "servo_min":
                servo.min()
            elif command == "servo_mid":
                servo.mid()
            elif command == "servo_max":
                servo.max()

            time.sleep(2)
        except RuntimeError as err:
            print(f"RuntimeError: {err.args[0]}")
            time.sleep(2)
        except websockets.ConnectionClosed:
            print("Client disconnected")
            break

start_server = websockets.serve(handle_client, "192.168.1.5", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
