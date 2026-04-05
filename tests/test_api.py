from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_get_speed():
    response = client.get("/speed")
    assert response.status_code == 200
    data = response.json()
    assert "average" in data
    assert "max" in data

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "running"

def test_invalid_input():
    response = client.get("/speed?data=fast")
    assert response.status_code in [400, 422]
