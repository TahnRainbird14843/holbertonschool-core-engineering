#!/usr/bin/env python3

import asyncio
import websockets


async def connection_handler(websocket):
    async for message in websocket:
        await websocket.send(message)


async def main():
    server = await websockets.serve(connection_handler, "0.0.0.0", 8765)
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
