import secrets
from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash

from .config import get_settings

ALGORITHM = "HS256"

_password_hash = PasswordHash.recommended()
# Verified against on a "user not found" login so response time doesn't reveal which emails exist.
DUMMY_HASH = _password_hash.hash(secrets.token_urlsafe(16))


def hash_password(password: str) -> str:
    return _password_hash.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    return _password_hash.verify(password, password_hash)


def create_access_token(user_id: int) -> str:
    settings = get_settings()
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_minutes)
    return jwt.encode({"sub": str(user_id), "exp": expires_at}, settings.secret_key, algorithm=ALGORITHM)


def decode_access_token(token: str) -> int:
    """Returns the user id encoded in the token. Raises jwt.PyJWTError (or ValueError for a
    malformed subject) on anything invalid/expired — callers translate that to 401."""
    settings = get_settings()
    payload = jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
    return int(payload["sub"])
