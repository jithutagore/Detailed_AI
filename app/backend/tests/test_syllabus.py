def test_list_tracks_requires_auth(client, seeded_subsection):
    assert client.get("/api/tracks").status_code == 401


def test_list_tracks(client, auth_headers, seeded_subsection):
    response = client.get("/api/tracks", headers=auth_headers)
    assert response.status_code == 200
    tracks = response.json()
    assert len(tracks) == 1
    assert tracks[0]["slug"] == "t1"
    assert tracks[0]["section_count"] == 1
    assert tracks[0]["completed_count"] == 0


def test_get_track_includes_sections(client, auth_headers, seeded_subsection):
    response = client.get("/api/tracks/t1", headers=auth_headers)
    assert response.status_code == 200
    body = response.json()
    assert body["title"] == "Track One"
    assert len(body["sections"]) == 1
    assert body["sections"][0]["status"] == "not_started"


def test_get_section_includes_subsections(client, auth_headers, seeded_subsection):
    response = client.get("/api/tracks/t1/sections/s1", headers=auth_headers)
    assert response.status_code == 200
    body = response.json()
    assert body["title"] == "Section One"
    assert len(body["subsections"]) == 1
    assert body["subsections"][0]["slug"] == "sub1"


def test_get_subsection_includes_items(client, auth_headers, seeded_subsection):
    response = client.get(
        "/api/tracks/t1/sections/s1/subsections/sub1", headers=auth_headers
    )
    assert response.status_code == 200
    body = response.json()
    assert body["title"] == "Subsection One"
    assert body["body_md"] == "- a point about the topic"
    assert len(body["items"]) == 1
    assert body["items"][0]["content"] == "An item"


def test_get_unknown_track_404s(client, auth_headers, seeded_subsection):
    response = client.get("/api/tracks/nope", headers=auth_headers)
    assert response.status_code == 404
