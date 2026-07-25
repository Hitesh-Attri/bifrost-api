BASE = "/api/v1/health"


def test_health_check(client):
    response = client.get(BASE)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "environment" in data
    assert "version" in data


def test_ping(client):
    response = client.get(f"{BASE}/ping")
    assert response.status_code == 200
    assert response.json()["data"]["pong"] is True
