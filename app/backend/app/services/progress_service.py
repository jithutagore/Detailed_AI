from sqlalchemy import select
from sqlalchemy.orm import Session

from ..models.progress import UserSectionStatus, UserSubsectionStatus
from ..schemas.progress import StatusUpdate


def upsert_section_status(db: Session, user_id: int, section_id: int, data: StatusUpdate) -> UserSectionStatus:
    row = db.scalar(
        select(UserSectionStatus).where(
            UserSectionStatus.user_id == user_id,
            UserSectionStatus.section_id == section_id,
        )
    )
    if row is None:
        row = UserSectionStatus(user_id=user_id, section_id=section_id)
        db.add(row)

    row.status = data.status
    row.knowledge_level = data.knowledge_level
    row.deleted_at = None
    db.commit()
    db.refresh(row)
    return row


def upsert_subsection_status(
    db: Session, user_id: int, subsection_id: int, data: StatusUpdate
) -> UserSubsectionStatus:
    row = db.scalar(
        select(UserSubsectionStatus).where(
            UserSubsectionStatus.user_id == user_id,
            UserSubsectionStatus.subsection_id == subsection_id,
        )
    )
    if row is None:
        row = UserSubsectionStatus(user_id=user_id, subsection_id=subsection_id)
        db.add(row)

    row.status = data.status
    row.knowledge_level = data.knowledge_level
    row.deleted_at = None
    db.commit()
    db.refresh(row)
    return row


def get_section_statuses(db: Session, user_id: int, section_ids: list[int]) -> dict[int, UserSectionStatus]:
    if not section_ids:
        return {}
    rows = db.scalars(
        select(UserSectionStatus).where(
            UserSectionStatus.user_id == user_id,
            UserSectionStatus.section_id.in_(section_ids),
            UserSectionStatus.deleted_at.is_(None),
        )
    )
    return {row.section_id: row for row in rows}


def get_subsection_statuses(db: Session, user_id: int, subsection_ids: list[int]) -> dict[int, UserSubsectionStatus]:
    if not subsection_ids:
        return {}
    rows = db.scalars(
        select(UserSubsectionStatus).where(
            UserSubsectionStatus.user_id == user_id,
            UserSubsectionStatus.subsection_id.in_(subsection_ids),
            UserSubsectionStatus.deleted_at.is_(None),
        )
    )
    return {row.subsection_id: row for row in rows}
