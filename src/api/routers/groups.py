from fastapi import APIRouter, status

from schemas.group import GroupCreate, GroupResponse, GroupUpdate
from services.group import group_service

router = APIRouter(prefix="/groups", tags=["groups"])


@router.get("", response_model=list[GroupResponse])
async def list_groups(org_id: str, tenant_id: str):
    return await group_service.list(org_id, tenant_id)


@router.post("", response_model=GroupResponse, status_code=status.HTTP_201_CREATED)
async def create_group(org_id: str, tenant_id: str, payload: GroupCreate):
    return await group_service.create(org_id, tenant_id, payload)


@router.get("/{group_id}", response_model=GroupResponse)
async def get_group(org_id: str, tenant_id: str, group_id: str):
    return await group_service.get(org_id, tenant_id, group_id)


@router.put("/{group_id}", response_model=GroupResponse)
async def update_group(org_id: str, tenant_id: str, group_id: str, payload: GroupUpdate):
    return await group_service.update(org_id, tenant_id, group_id, payload)


@router.delete("/{group_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_group(org_id: str, tenant_id: str, group_id: str):
    await group_service.delete(org_id, tenant_id, group_id)
