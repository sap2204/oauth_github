import asyncio
from contextlib import asynccontextmanager
from fastapi import APIRouter, FastAPI,  WebSocket, WebSocketDisconnect


from app.ws_help import number_generator, manager


#@asynccontextmanager
#async def lifespan(router: FastAPI):
    #number_generator.start_listening()
    #yield


router = APIRouter(
    prefix="/random",
    tags=["Генерация случайного числа"],
    #lifespan=lifespan,
)


# Генерация случайного числа каждые 5 секунд по веб-сокету
@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    print(f"{client_id=}")
    await manager.connect(websocket)
   
    q: asyncio.Queue = asyncio.Queue()
    await number_generator.subscribe(q=q)
    try:
        while True:
            data = await q.get()
            await websocket.send_text(data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)

        
    
    
    

    
    

