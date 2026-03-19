from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_get_speed():
    response = client.get("/speed")
    assert response.status_code == 200
    assert "average" in response.json()

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "running"
