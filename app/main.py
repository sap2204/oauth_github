from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.github_outh import router as router_github_auth
from app.random_number import router as router_random_number
from app.pages.router import router as router_pages
from app.ws_help import number_generator


@asynccontextmanager
async def lifespan(router: FastAPI):
    number_generator.start_listening()
    yield

    
app = FastAPI(lifespan=lifespan,)


app.include_router(router_github_auth)
app.include_router(router_random_number)
app.include_router(router_pages)


app.mount("/static", StaticFiles(directory="app/static"), "static")


