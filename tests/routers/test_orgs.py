from datetime import datetime, timezone
from unittest.mock import AsyncMock, patch

from services.org import org_service

BASE = "/api/v1/organizations"
NOW = datetime(2024, 1, 1, tzinfo=timezone.utc)
ORG = {"id": "org-1", "name": "Acme", "slug": "acme", "created_at": NOW}


def test_list_orgs(client):
    with patch.object(org_service, "list", new_callable=AsyncMock, return_value=[ORG]):
        response = client.get(BASE)
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_org(client):
    with patch.object(org_service, "get", new_callable=AsyncMock, return_value=ORG):
        response = client.get(f"{BASE}/org-1")
    assert response.status_code == 200
    assert response.json()["id"] == "org-1"


def test_create_org(client):
    with patch.object(org_service, "create", new_callable=AsyncMock, return_value=ORG):
        response = client.post(BASE, json={"name": "Acme", "slug": "acme"})
    assert response.status_code == 201
    assert response.json()["slug"] == "acme"


def test_update_org(client):
    updated = {**ORG, "name": "Acme Updated"}
    with patch.object(org_service, "update", new_callable=AsyncMock, return_value=updated):
        response = client.put(f"{BASE}/org-1", json={"name": "Acme Updated", "slug": "acme"})
    assert response.status_code == 200
    assert response.json()["name"] == "Acme Updated"


def test_delete_org(client):
    with patch.object(org_service, "delete", new_callable=AsyncMock, return_value=None):
        response = client.delete(f"{BASE}/org-1")
    assert response.status_code == 204
