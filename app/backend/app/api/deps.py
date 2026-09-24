from typing import Annotated

import jwt
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..core.exceptions import NotAuthenticatedError
from ..core.security import decode_access_token
from ..db.session import get_db
from ..models.user import User

_bearer = HTTPBearer(auto_error=False)

Db = Annotated[Session, Depends(get_db)]
Credentials = Annotated[HTTPAuthorizationCredentials | None, Depends(_bearer)]


def get_current_user(credentials: Credentials, db: Db) -> User:
    if credentials is None:
        raise NotAuthenticatedError

    try:
        user_id = decode_access_token(credentials.credentials)
    except (jwt.PyJWTError, ValueError, KeyError):
        raise NotAuthenticatedError

    user = db.scalar(select(User).where(User.id == user_id, User.deleted_at.is_(None)))
    if user is None:
        raise NotAuthenticatedError
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]
