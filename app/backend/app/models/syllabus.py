from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, TimestampMixin


class Track(TimestampMixin, Base):
    __tablename__ = "tracks"

    id: Mapped[int] = mapped_column(primary_key=True)
    slug: Mapped[str] = mapped_column(String(100), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    source_dir: Mapped[str] = mapped_column(String(255), nullable=False)
    sort_order: Mapped[int] = mapped_column(default=0)

    sections: Mapped[list["Section"]] = relationship(back_populates="track", order_by="Section.sort_order")


class Section(TimestampMixin, Base):
    __tablename__ = "sections"

    id: Mapped[int] = mapped_column(primary_key=True)
    track_id: Mapped[int] = mapped_column(ForeignKey("tracks.id"), nullable=False)
    number: Mapped[str] = mapped_column(String(20), nullable=False)
    slug: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    goal: Mapped[str | None] = mapped_column(Text)
    level: Mapped[str | None] = mapped_column(String(50))
    est_time: Mapped[str | None] = mapped_column(String(50))
    intro_md: Mapped[str | None] = mapped_column(Text)
    source_path: Mapped[str] = mapped_column(String(500), nullable=False)
    sort_order: Mapped[int] = mapped_column(default=0)

    track: Mapped["Track"] = relationship(back_populates="sections")
    subsections: Mapped[list["Subsection"]] = relationship(back_populates="section", order_by="Subsection.sort_order")


class Subsection(TimestampMixin, Base):
    __tablename__ = "subsections"

    id: Mapped[int] = mapped_column(primary_key=True)
    section_id: Mapped[int] = mapped_column(ForeignKey("sections.id"), nullable=False)
    kind: Mapped[str] = mapped_column(String(30), nullable=False)
    number: Mapped[str | None] = mapped_column(String(20))
    slug: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    body_md: Mapped[str] = mapped_column(Text, default="")
    sort_order: Mapped[int] = mapped_column(default=0)

    section: Mapped["Section"] = relationship(back_populates="subsections")
    items: Mapped[list["SubsectionItem"]] = relationship(back_populates="subsection", order_by="SubsectionItem.sort_order")


class SubsectionItem(TimestampMixin, Base):
    __tablename__ = "subsection_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    subsection_id: Mapped[int] = mapped_column(ForeignKey("subsections.id"), nullable=False)
    kind: Mapped[str] = mapped_column(String(30), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    is_checkbox: Mapped[int] = mapped_column(default=0)
    sort_order: Mapped[int] = mapped_column(default=0)

    subsection: Mapped["Subsection"] = relationship(back_populates="items")
