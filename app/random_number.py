import asyncio
import random
from fastapi import APIRouter,  WebSocket, WebSocketDisconnect


from app.ws_help import manager


router = APIRouter(
    prefix="/random",
    tags=["Генерация случайного числа"]
)


# Генерация случайного числа каждые 5 секунд по веб-сокету
@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    print("CONNECTTED", client_id)
    try:
        while True:
            random_number = random.randint(1, 1_000)
            await manager.broadcast(str(random_number))
            await asyncio.sleep(5)
    except WebSocketDisconnect as ex:
        manager.disconnect(websocket)
        print("ОШИБКА", ex)
    
    
    

    
    

