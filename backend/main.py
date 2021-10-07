from fastapi import FastAPI, WebSocket
import random
import uvicorn

app = FastAPI(title="Websocket Example")

@app.websocket("/ping")
async def websocket_endpoint(websocket: WebSocket):
    print("Accepting Client Connection......")
    await websocket.accept()
    while True:
        try:
            text = await websocket.receive_text()
            print(text)
            resp = {'request': text, 'value': random.uniform(0,1)}
            await websocket.send_json(resp)
        except Exception as e:
            print('error', e)
            break
    print("No Longer Accepting Connection.....")

uvicorn.run(app, host="0.0.0.0", port=8000)