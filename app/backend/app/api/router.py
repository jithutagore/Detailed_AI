from fastapi import APIRouter

from .routes.auth import router as auth_router
from .routes.health import router as health_router
from .routes.notes import router as notes_router
from .routes.profile import router as profile_router
from .routes.progress import router as progress_router
from .routes.syllabus import router as syllabus_router

api_router = APIRouter()
api_router.include_router(health_router)
api_router.include_router(auth_router)
api_router.include_router(profile_router)
api_router.include_router(syllabus_router)
api_router.include_router(progress_router)
api_router.include_router(notes_router)
