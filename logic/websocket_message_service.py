import websockets
import asyncio
import json
import sys
import os

from dotenv import load_dotenv
load_dotenv()

user_id = os.environ.get('user_id')
print(user_id)

translated_text = sys.stdin.read()

async def send_message(url):
  async with websockets.connect(url) as websocket:
    await websocket.send(json.dumps({"message": translated_text, "user_id": user_id}))
    print('published message')


websocket_url = "ws://127.0.0.1:8000"

asyncio.get_event_loop().run_until_complete(send_message(websocket_url))