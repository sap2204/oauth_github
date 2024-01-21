from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix="/pages",
    tags=['Фронтенд']
)


templates = Jinja2Templates(directory="app/templates")


# Страница авторизации
@router.get("/auth")
async def get_auth_page(
    request: Request
):
    return templates.TemplateResponse(name="auth.html", context={"request":request})


# Страница с отображением случайного числа
@router.get("/number")
async def get_random_number(
    request: Request
):
    return templates.TemplateResponse(name="random_number.html", context={"request":request})