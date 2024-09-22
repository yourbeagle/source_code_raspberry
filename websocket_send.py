import asyncio
import websockets

async def send_message():
    uri = "ws://192.168.1.5:6789"
    async with websockets.connect(uri) as websocket:
        message = "Pesan ini Dikirim dari Websocket"
        await websocket.send(message)
        print(f"Sent: {message}")

asyncio.get_event_loop().run_until_complete(send_message())