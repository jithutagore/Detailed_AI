"""Applies db/schema.sql (the syllabus importer's schema, source of truth for table
shape) then makes sure SQLAlchemy's own models agree with what's on disk.
"""
import logging

from sqlalchemy import inspect

from ..core.config import REPO_ROOT, get_settings
from ..models.base import Base
from ..models.notes import GeneratedNotes  # noqa: F401  (import registers the mapper)
from ..models.progress import UserSectionStatus, UserSubsectionStatus  # noqa: F401
from ..models.syllabus import Section, Subsection, SubsectionItem, Track  # noqa: F401
from ..models.user import User  # noqa: F401  (import registers the mapper)
from .session import get_engine

logger = logging.getLogger(__name__)


def init_db() -> None:
    settings = get_settings()
    # Always the repo's canonical schema, even when DATABASE_PATH points somewhere else (e.g. tests).
    schema_path = REPO_ROOT / "db" / "schema.sql"

    settings.database_path.parent.mkdir(parents=True, exist_ok=True)
    engine = get_engine()
    with engine.begin() as conn:
        # schema.sql has multiple statements (tables, indexes, triggers) — the DBAPI cursor's
        # execute() only accepts one, so this needs sqlite3's own executescript().
        conn.connection.driver_connection.executescript(schema_path.read_text(encoding="utf-8"))

    inspector = inspect(engine)
    missing = set(Base.metadata.tables) - set(inspector.get_table_names())
    if missing:
        raise RuntimeError(
            f"Tables declared in ORM models but missing from {schema_path.name}: {sorted(missing)}"
        )
    logger.info("database ready at %s", settings.database_path)
