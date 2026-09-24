from unittest.mock import AsyncMock, patch

NOTES_URL = "/api/tracks/t1/sections/s1/subsections/sub1/notes"


def test_generate_without_api_key_configured_503s(client, auth_headers, seeded_subsection):
    response = client.post(f"{NOTES_URL}/generate", headers=auth_headers)
    assert response.status_code == 503


def test_get_notes_before_generation_404s(client, auth_headers, seeded_subsection):
    response = client.get(NOTES_URL, headers=auth_headers)
    assert response.status_code == 404


def test_generate_saves_and_returns_notes(client, auth_headers, seeded_subsection, monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-key-not-real")
    from app.core.config import get_settings

    get_settings.cache_clear()

    with patch(
        "app.services.llm_providers.openrouter.OpenRouterProvider.complete",
        new=AsyncMock(return_value="## Heading\n\nSome generated notes with $E=mc^2$."),
    ):
        response = client.post(f"{NOTES_URL}/generate", headers=auth_headers)

    assert response.status_code == 201
    body = response.json()
    assert "Some generated notes" in body["content_md"]
    assert body["model_used"]
    assert body["edited_at"] is None

    fetched = client.get(NOTES_URL, headers=auth_headers)
    assert fetched.status_code == 200
    assert fetched.json()["content_md"] == body["content_md"]


def test_generate_strips_script_tags(client, auth_headers, seeded_subsection, monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-key-not-real")
    from app.core.config import get_settings

    get_settings.cache_clear()

    malicious = "Notes text.\n<script>alert('x')</script>\nMore notes."
    with patch(
        "app.services.llm_providers.openrouter.OpenRouterProvider.complete",
        new=AsyncMock(return_value=malicious),
    ):
        response = client.post(f"{NOTES_URL}/generate", headers=auth_headers)

    assert response.status_code == 201
    assert "<script>" not in response.json()["content_md"]
    assert "Notes text." in response.json()["content_md"]


def test_update_notes_sets_edited_at(client, auth_headers, seeded_subsection, monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-key-not-real")
    from app.core.config import get_settings

    get_settings.cache_clear()

    with patch(
        "app.services.llm_providers.openrouter.OpenRouterProvider.complete",
        new=AsyncMock(return_value="Original notes."),
    ):
        client.post(f"{NOTES_URL}/generate", headers=auth_headers)

    updated = client.put(NOTES_URL, json={"content_md": "Hand-edited notes."}, headers=auth_headers)
    assert updated.status_code == 200
    assert updated.json()["content_md"] == "Hand-edited notes."
    assert updated.json()["edited_at"] is not None


def test_download_returns_markdown_attachment(client, auth_headers, seeded_subsection, monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-key-not-real")
    from app.core.config import get_settings

    get_settings.cache_clear()

    with patch(
        "app.services.llm_providers.openrouter.OpenRouterProvider.complete",
        new=AsyncMock(return_value="Downloadable content."),
    ):
        client.post(f"{NOTES_URL}/generate", headers=auth_headers)

    response = client.get(f"{NOTES_URL}/download", headers=auth_headers)
    assert response.status_code == 200
    assert "attachment" in response.headers["content-disposition"]
    assert response.text == "Downloadable content."


def test_notes_require_auth(client, seeded_subsection):
    assert client.get(NOTES_URL).status_code == 401
    assert client.post(f"{NOTES_URL}/generate").status_code == 401
