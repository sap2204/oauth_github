from threading import Timer
import random
from fastapi import APIRouter, Depends, Request

from app.dependencies import  get_token_from_cookies


router = APIRouter(
    prefix="/random",
    tags=["Генерация случайного числа"]
)


# Генерация случайного числа каждые 5 секунд
@router.get("/number",
            dependencies=[Depends(get_token_from_cookies)])
def get_random_number():
    number = random.randint(1, 1_000)
    return number
    
    

    
    

