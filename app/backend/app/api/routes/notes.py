from fastapi import APIRouter, status
from fastapi.responses import Response

from ...api.deps import CurrentUser, Db
from ...schemas.notes import NotesRead, NotesUpdate
from ...services import notes_service, syllabus_service

router = APIRouter(
    prefix="/api/tracks/{track_slug}/sections/{section_slug}/subsections/{subsection_slug}/notes",
    tags=["notes"],
)


@router.post("/generate", response_model=NotesRead, status_code=status.HTTP_201_CREATED)
async def generate_notes(
    track_slug: str, section_slug: str, subsection_slug: str, db: Db, user: CurrentUser
) -> NotesRead:
    subsection = syllabus_service.get_subsection(db, track_slug, section_slug, subsection_slug)
    row = await notes_service.generate_notes(db, user.id, subsection)
    return NotesRead.model_validate(row)


@router.get("", response_model=NotesRead)
def get_notes(
    track_slug: str, section_slug: str, subsection_slug: str, db: Db, user: CurrentUser
) -> NotesRead:
    subsection = syllabus_service.get_subsection(db, track_slug, section_slug, subsection_slug)
    row = notes_service.get_notes(db, user.id, subsection.id)
    return NotesRead.model_validate(row)


@router.put("", response_model=NotesRead)
def update_notes(
    track_slug: str,
    section_slug: str,
    subsection_slug: str,
    body: NotesUpdate,
    db: Db,
    user: CurrentUser,
) -> NotesRead:
    subsection = syllabus_service.get_subsection(db, track_slug, section_slug, subsection_slug)
    row = notes_service.update_notes(db, user.id, subsection.id, body.content_md)
    return NotesRead.model_validate(row)


@router.get("/download")
def download_notes(
    track_slug: str, section_slug: str, subsection_slug: str, db: Db, user: CurrentUser
) -> Response:
    subsection = syllabus_service.get_subsection(db, track_slug, section_slug, subsection_slug)
    row = notes_service.get_notes(db, user.id, subsection.id)
    filename = f"{subsection.slug}-notes.md"
    return Response(
        content=row.content_md,
        media_type="text/markdown",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )
