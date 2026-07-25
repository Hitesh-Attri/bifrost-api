from datetime import datetime, timezone
from unittest.mock import AsyncMock, patch

from services.group import group_service

BASE = "/api/v1/organizations/org-1/tenants/t-1/groups"
NOW = datetime(2024, 1, 1, tzinfo=timezone.utc)
GROUP = {
    "id": "g-1",
    "org_id": "org-1",
    "tenant_id": "t-1",
    "name": "Admins",
    "created_at": NOW,
}


def test_list_groups(client):
    with patch.object(group_service, "list", new_callable=AsyncMock, return_value=[GROUP]):
        response = client.get(BASE)
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_group(client):
    with patch.object(group_service, "get", new_callable=AsyncMock, return_value=GROUP):
        response = client.get(f"{BASE}/g-1")
    assert response.status_code == 200
    assert response.json()["name"] == "Admins"


def test_create_group(client):
    with patch.object(group_service, "create", new_callable=AsyncMock, return_value=GROUP):
        response = client.post(BASE, json={"name": "Admins"})
    assert response.status_code == 201
    assert response.json()["org_id"] == "org-1"


def test_update_group(client):
    updated = {**GROUP, "name": "Super Admins"}
    with patch.object(group_service, "update", new_callable=AsyncMock, return_value=updated):
        response = client.put(f"{BASE}/g-1", json={"name": "Super Admins"})
    assert response.status_code == 200
    assert response.json()["name"] == "Super Admins"


def test_delete_group(client):
    with patch.object(group_service, "delete", new_callable=AsyncMock, return_value=None):
        response = client.delete(f"{BASE}/g-1")
    assert response.status_code == 204
