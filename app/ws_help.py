import random
from fastapi import WebSocket
import asyncio


class ConnectionManager:
    '''
    Класс для хранения активных веб-сокет соединений
    для и действий с ними
    '''
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    # Подключение нового пользователя
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)


    # Отключение пользователя
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    
    # Отправка сообщения всем клиентам
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()



class NumberGenerator:
    '''
    Генерация случайного числа, создание очередей из соединений
    '''
    def __init__(self):
        # Создание очереди из входящих соединений (клиентов)
        self.subscribers: list[asyncio.Queue] = []

        # Асинхронная задача, которая получает задачу и транслирует всем клиентам
        self.listener_task: asyncio.Task

    # Каждое входящее соединение должно добавиться в очередь
    async def subscribe(self, q: asyncio.Queue):
        self.subscribers.append(q)


    # Генерация случайного числа и 
    # передача числа для каждого клиента в очереди
    async def generate_number(self) -> None:
        while True:
            random_number = random.randint(1, 1000)
            msg = str(random_number)
            for q in self.subscribers:
                await q.put(msg)
            await asyncio.sleep(5)
    

    def subscribe_new_user(self, user_id: int):
        self.subscribers.append(user_id)


    def start_listening(self):
        self.listener_task = asyncio.create_task(self.generate_number())

    
    async def stop_listening(self):
        if self.listener_task.done():
            self.listener_task.result()
        else:
            self.listener_task.cancel()
            

number_generator = NumberGenerator()