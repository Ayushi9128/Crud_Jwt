import pytest
from app import create_app
from models import db as _db

class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    JWT_SECRET_KEY = "test-secret-key-that-is-longer-than-32-bytes"
    SECRET_KEY = "test-secret"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

@pytest.fixture
def app():
    app = create_app(TestConfig)
    with app.app_context():
        _db.create_all()
        yield app
        _db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_header(client):
    client.post("/auth/register", json={"username": "testuser", "email": "test@test.com", "password": "test123"})
    resp = client.post("/auth/login", json={"username": "testuser", "password": "test123"})
    token = resp.get_json()["access_token"]
    return {"Authorization": f"Bearer {token}"}