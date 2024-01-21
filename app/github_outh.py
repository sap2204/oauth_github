from fastapi import APIRouter, Depends, Response
from fastapi.responses import RedirectResponse
import httpx

from app.config import settings
from app.dependencies import delete_token_from_cookies


router = APIRouter(
    prefix="/github",
    tags=["Авторизация GitHub"]
)


# Перенаправление на страницу авторизации GitHub
@router.get("/login")
async def github_login():
    return RedirectResponse(
        f'https://github.com/login/oauth/authorize?client_id={settings.github_client_id}'
        )


# Получение кода с GitHub, обмен этого кода на токен GitHub 
# и установка токена в куки
@router.get('/token')
async def get_github_token(response: Response, code: str):
    params = {
        'client_id': settings.github_client_id,
        'client_secret': settings.github_client_secret,
        'code': code
    }

    headers = {'Accept': 'application/json'}
    async with httpx.AsyncClient() as client:
        response_github = await client.post(
                    url='https://github.com/login/oauth/access_token', 
                    params=params,
                    headers= headers
                    )
    response_json = response_github.json()
    github_token = response_json.get('access_token') # токен, полученный от GitHub
    
    response.set_cookie("access_token", github_token, httponly=True)
    


# Выход пользователя
@router.get("/logout")
async def logout_user(response: Response):
    response.delete_cookie("access_token")
    