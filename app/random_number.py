from threading import Timer
import random
from fastapi import APIRouter, Depends, Request

from app.dependencies import get_token_from_cookies


router = APIRouter(
    prefix="/random",
    tags=["Генерация случайного числа"]
)


# Генерация случайного числа каждые 5 секунд
@router.get("/number",
            dependencies=[Depends(get_token_from_cookies)])
def start_generate_random_number():
    number = random.randint(0, 1_000)
    print(number)
    Timer(5, start_generate_random_number).start()
    

