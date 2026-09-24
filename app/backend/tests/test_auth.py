def test_register_then_login_by_email(client):
    register = client.post(
        "/api/auth/register",
        json={
            "username": "ada_lovelace",
            "first_name": "  Ada  ",
            "last_name": "Lovelace",
            "email": "Ada@Example.com",
            "password": "supersecret1",
        },
    )
    assert register.status_code == 201
    body = register.json()
    assert body["email"] == "ada@example.com"
    assert body["username"] == "ada_lovelace"
    assert body["first_name"] == "Ada"
    assert body["last_name"] == "Lovelace"

    login = client.post("/api/auth/login", json={"identifier": "ADA@example.com", "password": "supersecret1"})
    assert login.status_code == 200
    body = login.json()
    assert body["token_type"] == "bearer"
    assert body["user"]["email"] == "ada@example.com"
    assert len(body["access_token"].split(".")) == 3


def test_login_by_username(client):
    client.post(
        "/api/auth/register",
        json={
            "username": "grace_h",
            "first_name": "Grace",
            "last_name": "Hopper",
            "email": "grace@example.com",
            "password": "supersecret1",
        },
    )
    login = client.post("/api/auth/login", json={"identifier": "GRACE_H", "password": "supersecret1"})
    assert login.status_code == 200
    assert login.json()["user"]["username"] == "grace_h"


def test_register_duplicate_email_rejected(client):
    payload = {"username": "user_a", "first_name": "A", "last_name": "A", "email": "dup@example.com", "password": "supersecret1"}
    assert client.post("/api/auth/register", json=payload).status_code == 201
    duplicate = client.post("/api/auth/register", json={**payload, "username": "user_b"})
    assert duplicate.status_code == 409
    assert "email" in duplicate.json()["detail"].lower()


def test_register_duplicate_username_rejected(client):
    payload = {"username": "dupe_name", "first_name": "A", "last_name": "A", "email": "a@example.com", "password": "supersecret1"}
    assert client.post("/api/auth/register", json=payload).status_code == 201
    duplicate = client.post("/api/auth/register", json={**payload, "email": "b@example.com"})
    assert duplicate.status_code == 409
    assert "username" in duplicate.json()["detail"].lower()


def test_register_username_case_insensitive_conflict(client):
    payload = {"username": "CaseTest", "first_name": "A", "last_name": "A", "email": "a@example.com", "password": "supersecret1"}
    assert client.post("/api/auth/register", json=payload).status_code == 201
    duplicate = client.post(
        "/api/auth/register", json={**payload, "username": "casetest", "email": "b@example.com"}
    )
    assert duplicate.status_code == 409


def test_register_invalid_username_characters_rejected(client):
    response = client.post(
        "/api/auth/register",
        json={"username": "not valid!", "first_name": "A", "last_name": "A", "email": "x@example.com", "password": "supersecret1"},
    )
    assert response.status_code == 422


def test_register_short_password_rejected(client):
    response = client.post(
        "/api/auth/register",
        json={"username": "shortpw", "first_name": "A", "last_name": "A", "email": "short@example.com", "password": "short"},
    )
    assert response.status_code == 422


def test_login_wrong_password_rejected(client):
    client.post(
        "/api/auth/register",
        json={"username": "wrongpw", "first_name": "A", "last_name": "A", "email": "wrong@example.com", "password": "correcthorse"},
    )
    response = client.post("/api/auth/login", json={"identifier": "wrong@example.com", "password": "incorrecthorse"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid email/username or password"


def test_login_unknown_identifier_rejected(client):
    response = client.post("/api/auth/login", json={"identifier": "nobody@example.com", "password": "supersecret1"})
    assert response.status_code == 401


def test_health(client):
    assert client.get("/api/health").json() == {"status": "ok"}


def test_request_id_header_present(client):
    assert "x-request-id" in client.get("/api/health").headers
