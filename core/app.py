from contextlib import asynccontextmanager
from db.db import close_database
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from collections.abc import AsyncGenerator
from core.config import app_config
from api.routes.employee import router as employee_router
from models import *

@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    yield
    await close_database()

def start_app() -> FastAPI:
    app = FastAPI(
        title=app_config.app_name,
        version=app_config.app_version,
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=app_config.cors_origins,
        allow_credentials=False,
        allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
        allow_headers=["Authorization", "Content-Type"]
    )
    app.include_router(employee_router)
    return app

app = start_app()