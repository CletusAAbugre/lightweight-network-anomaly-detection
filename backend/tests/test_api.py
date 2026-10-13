
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_network_samples_endpoint():
    response = client.get("/network-samples/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_alerts_endpoint():
    response = client.get("/alerts/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_evaluation_summary_endpoint():
    response = client.get("/evaluation/summary")

    assert response.status_code == 200

    data = response.json()
    assert "total_network_samples" in data
    assert "total_detection_results" in data
    assert "total_recorded_events" in data


def test_evaluation_methods_endpoint():
    response = client.get("/evaluation/methods")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
