import secrets
from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# app/backend/app/core/config.py -> repo root is four parents up.
REPO_ROOT = Path(__file__).resolve().parents[4]
BACKEND_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BACKEND_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "Detailed AI API"
    environment: str = "development"
    debug: bool = True

    database_path: Path = REPO_ROOT / "db" / "syllabus.db"

    # Left unset in production, a random key is generated per process, silently
    # invalidating every previously issued token on each restart — set APP_SECRET_KEY.
    secret_key: str = Field(default_factory=lambda: secrets.token_urlsafe(32))
    access_token_minutes: int = 60

    cors_origins: list[str] = ["http://localhost:5173"]

    log_level: str = "INFO"
    log_json: bool = False

    # Notes-generation provider. No default key — set OPENROUTER_API_KEY in your local
    # .env (gitignored); generation endpoints error clearly if it's missing.
    openrouter_api_key: str | None = None
    openrouter_model: str = "google/gemma-4-31b-it:free"

    @property
    def database_url(self) -> str:
        return f"sqlite:///{self.database_path}"


@lru_cache
def get_settings() -> Settings:
    return Settings()
