from fastapi import APIRouter

from ...api.deps import CurrentUser, Db
from ...schemas.progress import SectionStatusRead, StatusUpdate, SubsectionStatusRead
from ...services import progress_service, syllabus_service

router = APIRouter(prefix="/api/tracks", tags=["progress"])


@router.put("/{track_slug}/sections/{section_slug}/status", response_model=SectionStatusRead)
def set_section_status(
    track_slug: str, section_slug: str, body: StatusUpdate, db: Db, user: CurrentUser
) -> SectionStatusRead:
    section = syllabus_service.get_section(db, track_slug, section_slug)
    row = progress_service.upsert_section_status(db, user.id, section.id, body)
    return SectionStatusRead.model_validate(row)


@router.put(
    "/{track_slug}/sections/{section_slug}/subsections/{subsection_slug}/status",
    response_model=SubsectionStatusRead,
)
def set_subsection_status(
    track_slug: str,
    section_slug: str,
    subsection_slug: str,
    body: StatusUpdate,
    db: Db,
    user: CurrentUser,
) -> SubsectionStatusRead:
    subsection = syllabus_service.get_subsection(db, track_slug, section_slug, subsection_slug)
    row = progress_service.upsert_subsection_status(db, user.id, subsection.id, body)
    return SubsectionStatusRead.model_validate(row)
