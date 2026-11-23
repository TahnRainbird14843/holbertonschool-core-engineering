#!/usr/bin/env python3

from starlette.applications import Starlette
from starlette.responses import HTMLResponse, PlainTextResponse
from starlette.routing import Route, WebSocketRoute


async def homepage(request):
    with open('index.html', 'r') as f:
        return HTMLResponse(f.read())


async def websocket_endpoint(websocket):
    await websocket.accept()
    async for message in websocket:
        await websocket.send(message)


async def js_file(request):
    with open('chat.js', 'r') as f:
        return PlainTextResponse(f.read())


app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
    Route("/chat.js", js_file)
])