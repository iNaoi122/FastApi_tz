from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

with open("base.html") as f:
    html = f.read()

app = FastAPI(title="Тествоое задание")


@app.get('/')
async def get():
    return HTMLResponse(html)


@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    i = 0
    while True:
        data = await websocket.receive_json()
        i += 1
        await websocket.send_text(f"{i}: {data['message']}")
