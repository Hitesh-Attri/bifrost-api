from fastapi import APIRouter, status

from schemas.org import OrgCreate, OrgResponse, OrgUpdate
from services.org import org_service

router = APIRouter(prefix="/organizations", tags=["organizations"])


@router.get("", response_model=list[OrgResponse])
async def list_orgs():
    return await org_service.list()


@router.post("", response_model=OrgResponse, status_code=status.HTTP_201_CREATED)
async def create_org(payload: OrgCreate):
    return await org_service.create(payload)


@router.get("/{org_id}", response_model=OrgResponse)
async def get_org(org_id: str):
    return await org_service.get(org_id)


@router.put("/{org_id}", response_model=OrgResponse)
async def update_org(org_id: str, payload: OrgUpdate):
    return await org_service.update(org_id, payload)


@router.delete("/{org_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_org(org_id: str):
    await org_service.delete(org_id)
