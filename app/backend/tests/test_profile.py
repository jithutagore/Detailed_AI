def test_get_profile_requires_auth(client):
    assert client.get("/api/profile").status_code == 401


def test_get_profile(client, auth_headers):
    response = client.get("/api/profile", headers=auth_headers)
    assert response.status_code == 200
    body = response.json()
    assert body["username"] == "test_user"
    assert body["first_name"] == "Test"


def test_update_profile(client, auth_headers):
    response = client.put(
        "/api/profile", json={"first_name": "Updated", "last_name": "Name"}, headers=auth_headers
    )
    assert response.status_code == 200
    body = response.json()
    assert body["first_name"] == "Updated"
    assert body["last_name"] == "Name"
    assert body["username"] == "test_user"

    refetched = client.get("/api/profile", headers=auth_headers)
    assert refetched.json()["first_name"] == "Updated"
