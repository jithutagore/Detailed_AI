import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .api.router import api_router
from .core.config import get_settings
from .core.exceptions import AppError
from .core.logging import configure_logging
from .core.middleware import RequestContextMiddleware
from .db.init_db import init_db
from .services.llm_providers.base import LLMProviderError

settings = get_settings()
configure_logging(level=settings.log_level, json_output=settings.log_json)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    logger.info("%s starting (environment=%s)", settings.app_name, settings.environment)
    yield
    logger.info("%s shutting down", settings.app_name)


app = FastAPI(title=settings.app_name, debug=settings.debug, lifespan=lifespan)

app.add_middleware(RequestContextMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(AppError)
async def app_error_handler(_: Request, exc: AppError) -> JSONResponse:
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


@app.exception_handler(LLMProviderError)
async def llm_provider_error_handler(_: Request, exc: LLMProviderError) -> JSONResponse:
    logger.warning("LLM provider error: %s", exc)
    return JSONResponse(status_code=502, content={"detail": "Notes generation failed — the AI provider didn't respond correctly. Try again."})


app.include_router(api_router)
