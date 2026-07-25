from fastapi import APIRouter, status

from schemas.user import UserCreate, UserResponse, UserUpdate
from services.user import user_service

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=list[UserResponse])
async def list_users(org_id: str, tenant_id: str):
    return await user_service.list(org_id, tenant_id)


@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(org_id: str, tenant_id: str, payload: UserCreate):
    return await user_service.create(org_id, tenant_id, payload)


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(org_id: str, tenant_id: str, user_id: str):
    return await user_service.get(org_id, tenant_id, user_id)


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(org_id: str, tenant_id: str, user_id: str, payload: UserUpdate):
    return await user_service.update(org_id, tenant_id, user_id, payload)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(org_id: str, tenant_id: str, user_id: str):
    await user_service.delete(org_id, tenant_id, user_id)
