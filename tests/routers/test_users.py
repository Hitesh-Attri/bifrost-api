from datetime import datetime, timezone
from unittest.mock import AsyncMock, patch

from services.user import user_service

BASE = "/api/v1/organizations/org-1/tenants/t-1/users"
NOW = datetime(2024, 1, 1, tzinfo=timezone.utc)
USER = {
    "id": "u-1",
    "org_id": "org-1",
    "tenant_id": "t-1",
    "email": "alice@example.com",
    "name": "Alice",
    "created_at": NOW,
}


def test_list_users(client):
    with patch.object(user_service, "list", new_callable=AsyncMock, return_value=[USER]):
        response = client.get(BASE)
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_user(client):
    with patch.object(user_service, "get", new_callable=AsyncMock, return_value=USER):
        response = client.get(f"{BASE}/u-1")
    assert response.status_code == 200
    assert response.json()["email"] == "alice@example.com"


def test_create_user(client):
    with patch.object(user_service, "create", new_callable=AsyncMock, return_value=USER):
        response = client.post(BASE, json={"email": "alice@example.com", "name": "Alice"})
    assert response.status_code == 201
    assert response.json()["tenant_id"] == "t-1"


def test_update_user(client):
    updated = {**USER, "name": "Alice Smith"}
    with patch.object(user_service, "update", new_callable=AsyncMock, return_value=updated):
        response = client.put(f"{BASE}/u-1", json={"email": "alice@example.com", "name": "Alice Smith"})
    assert response.status_code == 200
    assert response.json()["name"] == "Alice Smith"


def test_delete_user(client):
    with patch.object(user_service, "delete", new_callable=AsyncMock, return_value=None):
        response = client.delete(f"{BASE}/u-1")
    assert response.status_code == 204
