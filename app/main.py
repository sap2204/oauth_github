from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import httpx

from app.config import settings
from app.github_outh import router as router_github_auth
from app.random_number import router as router_random_number

app = FastAPI()


app.include_router(router_github_auth)
app.include_router(router_random_number)


