from datetime import datetime, timezone
from unittest.mock import AsyncMock, patch

from services.tenant import tenant_service

BASE = "/api/v1/organizations/org-1/tenants"
NOW = datetime(2024, 1, 1, tzinfo=timezone.utc)
TENANT = {"id": "t-1", "org_id": "org-1", "name": "Tenant A", "slug": "tenant-a", "created_at": NOW}


def test_list_tenants(client):
    with patch.object(tenant_service, "list", new_callable=AsyncMock, return_value=[TENANT]):
        response = client.get(BASE)
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_tenant(client):
    with patch.object(tenant_service, "get", new_callable=AsyncMock, return_value=TENANT):
        response = client.get(f"{BASE}/t-1")
    assert response.status_code == 200
    assert response.json()["id"] == "t-1"


def test_create_tenant(client):
    with patch.object(tenant_service, "create", new_callable=AsyncMock, return_value=TENANT):
        response = client.post(BASE, json={"name": "Tenant A", "slug": "tenant-a"})
    assert response.status_code == 201
    assert response.json()["org_id"] == "org-1"


def test_update_tenant(client):
    updated = {**TENANT, "name": "Tenant B"}
    with patch.object(tenant_service, "update", new_callable=AsyncMock, return_value=updated):
        response = client.put(f"{BASE}/t-1", json={"name": "Tenant B", "slug": "tenant-a"})
    assert response.status_code == 200
    assert response.json()["name"] == "Tenant B"


def test_delete_tenant(client):
    with patch.object(tenant_service, "delete", new_callable=AsyncMock, return_value=None):
        response = client.delete(f"{BASE}/t-1")
    assert response.status_code == 204
