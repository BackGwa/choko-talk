import websockets
import asyncio
import json

clients = set()

async def main():
    with open("./config.json") as f:
        CONFIG = json.load(f)
        HOST = CONFIG["HOST"]
        PORT = CONFIG["PORT"]
    async with websockets.serve(recv_data, HOST, PORT):
        await asyncio.Future()


async def recv_data(websocket, path):
    print(f"{path} joined.")
    clients.add(websocket)
    
    while True:
        chat_data = json.loads(await websocket.recv())
        
        if chat_data.get("user") is None:
            continue
        if chat_data.get("content") is None:
            continue
        
        for client in clients:
            await asyncio.sleep(0)
            await client.send(
                json.dumps({
                    "user" : chat_data.get("user"),
                    "content" : chat_data.get("content")
                }))


if __name__ == "__main__":
    asyncio.run(main())