def test_set_section_status_requires_auth(client, seeded_subsection):
    response = client.put("/api/tracks/t1/sections/s1/status", json={"status": "completed"})
    assert response.status_code == 401


def test_set_and_read_section_status(client, auth_headers, seeded_subsection):
    put = client.put(
        "/api/tracks/t1/sections/s1/status",
        json={"status": "in_progress", "knowledge_level": 3},
        headers=auth_headers,
    )
    assert put.status_code == 200
    assert put.json()["status"] == "in_progress"
    assert put.json()["knowledge_level"] == 3

    track = client.get("/api/tracks/t1", headers=auth_headers).json()
    assert track["sections"][0]["status"] == "in_progress"
    assert track["sections"][0]["knowledge_level"] == 3


def test_set_subsection_status(client, auth_headers, seeded_subsection):
    put = client.put(
        "/api/tracks/t1/sections/s1/subsections/sub1/status",
        json={"status": "completed", "knowledge_level": 5},
        headers=auth_headers,
    )
    assert put.status_code == 200
    assert put.json()["status"] == "completed"


def test_status_upsert_overwrites_previous_value(client, auth_headers, seeded_subsection):
    url = "/api/tracks/t1/sections/s1/status"
    client.put(url, json={"status": "in_progress", "knowledge_level": 2}, headers=auth_headers)
    second = client.put(url, json={"status": "completed", "knowledge_level": 4}, headers=auth_headers)
    assert second.json()["status"] == "completed"
    assert second.json()["knowledge_level"] == 4

    tracks = client.get("/api/tracks", headers=auth_headers).json()
    assert tracks[0]["completed_count"] == 1


def test_knowledge_level_out_of_range_rejected(client, auth_headers, seeded_subsection):
    response = client.put(
        "/api/tracks/t1/sections/s1/status",
        json={"status": "completed", "knowledge_level": 0},
        headers=auth_headers,
    )
    assert response.status_code == 422


def test_invalid_status_value_rejected(client, auth_headers, seeded_subsection):
    response = client.put(
        "/api/tracks/t1/sections/s1/status", json={"status": "bogus"}, headers=auth_headers
    )
    assert response.status_code == 422
