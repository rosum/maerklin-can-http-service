import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://localhost:8888") as websocket:
        print("connected")
        async for message in websocket:
            print(message)

asyncio.run(hello())