from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, TimestampMixin

STATUS_VALUES = ("not_started", "in_progress", "completed", "skipped", "needs_revisit")


class UserSectionStatus(TimestampMixin, Base):
    __tablename__ = "user_section_status"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    section_id: Mapped[int] = mapped_column(ForeignKey("sections.id"), nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="not_started")
    knowledge_level: Mapped[int | None] = mapped_column(default=None)


class UserSubsectionStatus(TimestampMixin, Base):
    __tablename__ = "user_subsection_status"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    subsection_id: Mapped[int] = mapped_column(ForeignKey("subsections.id"), nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="not_started")
    knowledge_level: Mapped[int | None] = mapped_column(default=None)
