import asyncio
import random
from fastapi import APIRouter,  WebSocket, WebSocketDisconnect


from app.ws_help import manager


router = APIRouter(
    prefix="/random",
    tags=["Генерация случайного числа"]
)


# Генерация случайного числа каждые 5 секунд по веб-сокету
@router.websocket("/ws")
async def get_random_number(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    while True:
        random_number = random.randint(1, 1_000)
        await manager.broadcast(random_number)
        asyncio.sleep(5)
    
    
    

    
    

