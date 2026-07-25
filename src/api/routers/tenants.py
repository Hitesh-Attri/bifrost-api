from fastapi import APIRouter, status

from schemas.tenant import TenantCreate, TenantResponse, TenantUpdate
from services.tenant import tenant_service

router = APIRouter(prefix="/tenants", tags=["tenants"])


@router.get("", response_model=list[TenantResponse])
async def list_tenants(org_id: str):
    return await tenant_service.list(org_id)


@router.post("", response_model=TenantResponse, status_code=status.HTTP_201_CREATED)
async def create_tenant(org_id: str, payload: TenantCreate):
    return await tenant_service.create(org_id, payload)


@router.get("/{tenant_id}", response_model=TenantResponse)
async def get_tenant(org_id: str, tenant_id: str):
    return await tenant_service.get(org_id, tenant_id)


@router.put("/{tenant_id}", response_model=TenantResponse)
async def update_tenant(org_id: str, tenant_id: str, payload: TenantUpdate):
    return await tenant_service.update(org_id, tenant_id, payload)


@router.delete("/{tenant_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tenant(org_id: str, tenant_id: str):
    await tenant_service.delete(org_id, tenant_id)
