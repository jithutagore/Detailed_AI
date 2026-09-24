from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ...db.session import get_db
from ...schemas.user import TokenResponse, UserLogin, UserRead, UserRegister
from ...services import auth_service

router = APIRouter(prefix="/api/auth", tags=["auth"])

Db = Annotated[Session, Depends(get_db)]


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserRead)
def register(body: UserRegister, db: Db) -> UserRead:
    return auth_service.register_user(db, body)


@router.post("/login", response_model=TokenResponse)
def login(body: UserLogin, db: Db) -> TokenResponse:
    return auth_service.authenticate_user(db, body)
