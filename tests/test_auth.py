def test_register_success(client):
    resp = client.post("/auth/register", json={"username": "alice", "email": "alice@test.com", "password": "pass123"})
    assert resp.status_code == 201
    assert resp.get_json()["user"]["username"] == "alice"

def test_register_duplicate(client):
    client.post("/auth/register", json={"username": "bob", "email": "bob@test.com", "password": "pass123"})
    resp = client.post("/auth/register", json={"username": "bob", "email": "bob@test.com", "password": "pass123"})
    assert resp.status_code == 409

def test_register_missing_fields(client):
    resp = client.post("/auth/register", json={"username": "carol"})
    assert resp.status_code == 400

def test_login_success(client):
    client.post("/auth/register", json={"username": "dave", "email": "dave@test.com", "password": "pass123"})
    resp = client.post("/auth/login", json={"username": "dave", "password": "pass123"})
    assert resp.status_code == 200
    assert "access_token" in resp.get_json()

def test_login_wrong_password(client):
    client.post("/auth/register", json={"username": "eve", "email": "eve@test.com", "password": "pass123"})
    resp = client.post("/auth/login", json={"username": "eve", "password": "wrong"})
    assert resp.status_code == 401