from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from ..core.exceptions import NotFoundError
from ..models.syllabus import Section, Subsection, Track


def list_tracks(db: Session) -> list[Track]:
    stmt = (
        select(Track)
        .where(Track.deleted_at.is_(None))
        .options(joinedload(Track.sections))
        .order_by(Track.sort_order)
    )
    return list(db.scalars(stmt).unique())


def get_track(db: Session, track_slug: str) -> Track:
    stmt = (
        select(Track)
        .where(Track.slug == track_slug, Track.deleted_at.is_(None))
        .options(joinedload(Track.sections))
    )
    track = db.scalar(stmt)
    if track is None:
        raise NotFoundError("Track not found")
    return track


def get_section(db: Session, track_slug: str, section_slug: str) -> Section:
    stmt = (
        select(Section)
        .join(Track)
        .where(
            Track.slug == track_slug,
            Section.slug == section_slug,
            Track.deleted_at.is_(None),
            Section.deleted_at.is_(None),
        )
        .options(joinedload(Section.subsections))
    )
    section = db.scalar(stmt)
    if section is None:
        raise NotFoundError("Section not found")
    return section


def get_subsection(db: Session, track_slug: str, section_slug: str, subsection_slug: str) -> Subsection:
    stmt = (
        select(Subsection)
        .join(Section)
        .join(Track)
        .where(
            Track.slug == track_slug,
            Section.slug == section_slug,
            Subsection.slug == subsection_slug,
            Track.deleted_at.is_(None),
            Section.deleted_at.is_(None),
            Subsection.deleted_at.is_(None),
        )
        .options(joinedload(Subsection.items))
    )
    subsection = db.scalar(stmt)
    if subsection is None:
        raise NotFoundError("Subsection not found")
    return subsection
