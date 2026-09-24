import os
from pathlib import Path

import pytest

TEST_DB_PATH = Path(__file__).resolve().parent / ".tmp" / "test.db"


@pytest.fixture()
def client():
    TEST_DB_PATH.parent.mkdir(exist_ok=True)
    TEST_DB_PATH.unlink(missing_ok=True)
    os.environ["DATABASE_PATH"] = str(TEST_DB_PATH)
    os.environ["SECRET_KEY"] = "test-secret-key-at-least-32-bytes-long"

    from app.core.config import get_settings

    get_settings.cache_clear()

    from app.db.session import get_engine
    from app.main import app

    get_engine.cache_clear()

    from fastapi.testclient import TestClient

    with TestClient(app) as test_client:
        yield test_client

    get_engine().dispose()
    TEST_DB_PATH.unlink(missing_ok=True)


@pytest.fixture()
def auth_headers(client):
    client.post(
        "/api/auth/register",
        json={
            "username": "test_user",
            "first_name": "Test",
            "last_name": "User",
            "email": "test@example.com",
            "password": "supersecret1",
        },
    )
    login = client.post("/api/auth/login", json={"identifier": "test_user", "password": "supersecret1"})
    token = login.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture()
def seeded_subsection(client):
    """Inserts one track/section/subsection/item directly via SQL, returning their slugs."""
    import sqlite3

    conn = sqlite3.connect(TEST_DB_PATH)
    conn.execute("INSERT INTO tracks (slug, title, source_dir) VALUES ('t1', 'Track One', 'T1')")
    conn.execute(
        "INSERT INTO sections (track_id, number, slug, title, source_path) "
        "VALUES (1, '01', 's1', 'Section One', 't1/01_s1/01_s1.md')"
    )
    conn.execute(
        "INSERT INTO subsections (section_id, kind, number, slug, title, body_md) "
        "VALUES (1, 'topic', '1.1', 'sub1', 'Subsection One', '- a point about the topic')"
    )
    conn.execute(
        "INSERT INTO subsection_items (subsection_id, kind, content) VALUES (1, 'point', 'An item')"
    )
    conn.commit()
    conn.close()
    return {"track_slug": "t1", "section_slug": "s1", "subsection_slug": "sub1"}
