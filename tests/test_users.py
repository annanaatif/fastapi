from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"email": "user@email.com", "password": "pass"})
    assert response.status_code == 201
    assert response.json() == {"email": "user@email.com", "password": "pass"}