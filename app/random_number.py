from threading import Timer
import random
from fastapi import APIRouter, Depends, Request

from app.dependencies import get_token


router = APIRouter(
    prefix="/random_number",
    tags=["Генерация случайного числа"]
)


# Генерация случайного числа каждые 5 секунд
@router.get("/random_number",
            dependencies=[Depends(get_token)])
def start_generate_random_number():
    number = random.randint(0, 1_000)
    print(number)
    Timer(5, start_generate_random_number).start()
    

