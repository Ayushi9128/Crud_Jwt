def test_get_users_requires_auth(client):
    resp = client.get("/users")
    assert resp.status_code == 401

def test_get_users(client, auth_header):
    resp = client.get("/users", headers=auth_header)
    assert resp.status_code == 200
    assert "users" in resp.get_json()

def test_get_single_user(client, auth_header):
    resp = client.get("/users/1", headers=auth_header)
    assert resp.status_code == 200
    assert resp.get_json()["user"]["username"] == "testuser"

def test_update_own_profile(client, auth_header):
    resp = client.put("/users/1", json={"email": "new@test.com"}, headers=auth_header)
    assert resp.status_code == 200
    assert resp.get_json()["user"]["email"] == "new@test.com"

def test_update_other_profile_forbidden(client, auth_header):
    # Register a second user
    client.post("/auth/register", json={"username": "other", "email": "other@test.com", "password": "pass123"})
    resp = client.put("/users/2", json={"email": "hacked@test.com"}, headers=auth_header)
    assert resp.status_code == 403

def test_delete_own_account(client, auth_header):
    resp = client.delete("/users/1", headers=auth_header)
    assert resp.status_code == 200

def test_user_not_found(client, auth_header):
    resp = client.get("/users/999", headers=auth_header)
    assert resp.status_code == 404