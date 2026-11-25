from starlette.applications import Starlette
from starlette.endpoints import WebSocketEndpoint, HTTPEndpoint
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute


class Homepage(HTTPEndpoint):
    async def get(self, request):
        with open('index.html', 'r') as f:
            return HTMLResponse(f.read())

class Echo(WebSocketEndpoint):
    encoding = "text"

    async def on_receive(self, websocket, data):
        await websocket.send_text(f"Message text was: {data}")

routes = [
    Route("/", Homepage),
    WebSocketRoute("/ws", Echo)
]

app = Starlette(routes=routes)