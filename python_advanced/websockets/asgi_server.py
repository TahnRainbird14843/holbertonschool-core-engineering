#!/usr/bin/env python3

from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute


async def homepage(request):
    response = HTMLResponse("<h1>WebSocket Echo</h1>")
    await response()


async def websocket_endpoint(websocket):
    await websocket.accept()
    async for message in websocket:
        await websocket.send(message)


app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint)
])