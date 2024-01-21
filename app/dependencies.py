import random
from fastapi import  Request, HTTPException, Response, status
import httpx

from app.config import settings


# Получение токена из кукиз
def get_token_from_cookies(request:Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return token



# Удаление токена из кукиз
def delete_token_from_cookies(response: Response):
    response.delete_cookie("access_token")




