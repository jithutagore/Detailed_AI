from fastapi import APIRouter

from ...api.deps import CurrentUser, Db
from ...schemas.syllabus import (
    SectionRead,
    SectionSummary,
    SubsectionItemRead,
    SubsectionRead,
    SubsectionSummary,
    TrackRead,
    TrackSummary,
)
from ...services import progress_service, syllabus_service

router = APIRouter(prefix="/api/tracks", tags=["syllabus"])


@router.get("", response_model=list[TrackSummary])
def list_tracks(db: Db, user: CurrentUser) -> list[TrackSummary]:
    tracks = syllabus_service.list_tracks(db)
    all_section_ids = [s.id for t in tracks for s in t.sections]
    statuses = progress_service.get_section_statuses(db, user.id, all_section_ids)

    return [
        TrackSummary(
            id=t.id,
            slug=t.slug,
            title=t.title,
            description=t.description,
            section_count=len(t.sections),
            completed_count=sum(1 for s in t.sections if statuses.get(s.id, None) and statuses[s.id].status == "completed"),
        )
        for t in tracks
    ]


@router.get("/{track_slug}", response_model=TrackRead)
def get_track(track_slug: str, db: Db, user: CurrentUser) -> TrackRead:
    track = syllabus_service.get_track(db, track_slug)
    statuses = progress_service.get_section_statuses(db, user.id, [s.id for s in track.sections])

    return TrackRead(
        id=track.id,
        slug=track.slug,
        title=track.title,
        description=track.description,
        sections=[
            SectionSummary(
                id=s.id,
                number=s.number,
                slug=s.slug,
                title=s.title,
                level=s.level,
                est_time=s.est_time,
                status=statuses[s.id].status if s.id in statuses else "not_started",
                knowledge_level=statuses[s.id].knowledge_level if s.id in statuses else None,
            )
            for s in track.sections
        ],
    )


@router.get("/{track_slug}/sections/{section_slug}", response_model=SectionRead)
def get_section(track_slug: str, section_slug: str, db: Db, user: CurrentUser) -> SectionRead:
    section = syllabus_service.get_section(db, track_slug, section_slug)
    section_status = progress_service.get_section_statuses(db, user.id, [section.id]).get(section.id)
    sub_statuses = progress_service.get_subsection_statuses(db, user.id, [sub.id for sub in section.subsections])

    return SectionRead(
        id=section.id,
        number=section.number,
        slug=section.slug,
        title=section.title,
        goal=section.goal,
        level=section.level,
        est_time=section.est_time,
        intro_md=section.intro_md,
        status=section_status.status if section_status else "not_started",
        knowledge_level=section_status.knowledge_level if section_status else None,
        subsections=[
            SubsectionSummary(
                id=sub.id,
                kind=sub.kind,
                number=sub.number,
                slug=sub.slug,
                title=sub.title,
                status=sub_statuses[sub.id].status if sub.id in sub_statuses else "not_started",
                knowledge_level=sub_statuses[sub.id].knowledge_level if sub.id in sub_statuses else None,
            )
            for sub in section.subsections
        ],
    )


@router.get(
    "/{track_slug}/sections/{section_slug}/subsections/{subsection_slug}",
    response_model=SubsectionRead,
)
def get_subsection(
    track_slug: str, section_slug: str, subsection_slug: str, db: Db, user: CurrentUser
) -> SubsectionRead:
    subsection = syllabus_service.get_subsection(db, track_slug, section_slug, subsection_slug)
    sub_status = progress_service.get_subsection_statuses(db, user.id, [subsection.id]).get(subsection.id)

    return SubsectionRead(
        id=subsection.id,
        kind=subsection.kind,
        number=subsection.number,
        slug=subsection.slug,
        title=subsection.title,
        body_md=subsection.body_md,
        status=sub_status.status if sub_status else "not_started",
        knowledge_level=sub_status.knowledge_level if sub_status else None,
        items=[SubsectionItemRead.model_validate(item) for item in subsection.items],
    )
