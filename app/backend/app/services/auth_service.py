import logging

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..core.config import get_settings
from ..core.exceptions import EmailAlreadyRegisteredError, InvalidCredentialsError, UsernameTakenError
from ..core.security import DUMMY_HASH, create_access_token, hash_password, verify_password
from ..models.user import User
from ..schemas.user import TokenResponse, UserLogin, UserRead, UserRegister

logger = logging.getLogger(__name__)


def register_user(db: Session, data: UserRegister) -> UserRead:
    # Checked up front (not just relying on the unique index) so a register with both an
    # already-used email AND username predictably reports the email conflict first.
    if db.scalar(select(User.id).where(User.email == data.email.lower())) is not None:
        raise EmailAlreadyRegisteredError
    if db.scalar(select(User.id).where(User.username == data.username.lower())) is not None:
        raise UsernameTakenError

    user = User(
        email=data.email.lower(),
        username=data.username.lower(),
        first_name=data.first_name,
        last_name=data.last_name,
        password_hash=hash_password(data.password),
    )
    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        logger.info("registration rejected: race on unique email/username")
        raise EmailAlreadyRegisteredError
    db.refresh(user)
    logger.info("user %s registered", user.id)
    return UserRead.model_validate(user)


def authenticate_user(db: Session, data: UserLogin) -> TokenResponse:
    identifier = data.identifier.strip().lower()
    user = db.scalar(
        select(User).where(
            (User.email == identifier) | (User.username == identifier),
            User.deleted_at.is_(None),
        )
    )
    password_ok = verify_password(data.password, user.password_hash if user else DUMMY_HASH)
    if user is None or not password_ok:
        logger.info("login failed for given identifier")
        raise InvalidCredentialsError

    logger.info("user %s logged in", user.id)
    return TokenResponse(
        access_token=create_access_token(user.id),
        expires_in=get_settings().access_token_minutes * 60,
        user=UserRead.model_validate(user),
    )
