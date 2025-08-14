import os
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import PlainTextResponse

app = FastAPI()

# ----------------------------
# Welcome Page
# ----------------------------
@app.get("/welcome", response_class=PlainTextResponse)
async def welcome():
    return "Welcome! This is the Twilio GPT Relay service."
