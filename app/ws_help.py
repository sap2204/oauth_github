from fastapi import WebSocket


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