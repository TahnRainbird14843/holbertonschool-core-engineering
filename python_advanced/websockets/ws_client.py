#!/usr/bin/env python3

import asyncio
from websockets.sync.client import connect


async def connect_and_send(uri: str, text: str) -> str:
    with connect(uri) as websocket:
        websocket.send(text)
        message = websocket.recv()
        print(message, end="")


async def main():
    await connect_and_send("ws://0.0.0.0:8765", "Hello WebSocket")


asyncio.run(main())
