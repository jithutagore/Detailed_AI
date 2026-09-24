from fastapi import APIRouter

from ...api.deps import CurrentUser, Db
from ...schemas.profile import ProfileRead, ProfileUpdate

router = APIRouter(prefix="/api/profile", tags=["profile"])


@router.get("", response_model=ProfileRead)
def get_profile(user: CurrentUser) -> ProfileRead:
    return ProfileRead.model_validate(user)


@router.put("", response_model=ProfileRead)
def update_profile(body: ProfileUpdate, db: Db, user: CurrentUser) -> ProfileRead:
    user.first_name = body.first_name
    user.last_name = body.last_name
    db.commit()
    db.refresh(user)
    return ProfileRead.model_validate(user)
