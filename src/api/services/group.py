from schemas.group import GroupCreate, GroupResponse, GroupUpdate


class GroupService:
    async def list(self, org_id: str, tenant_id: str) -> list[GroupResponse]:
        raise NotImplementedError

    async def get(self, org_id: str, tenant_id: str, group_id: str) -> GroupResponse:
        raise NotImplementedError

    async def create(self, org_id: str, tenant_id: str, payload: GroupCreate) -> GroupResponse:
        raise NotImplementedError

    async def update(self, org_id: str, tenant_id: str, group_id: str, payload: GroupUpdate) -> GroupResponse:
        raise NotImplementedError

    async def delete(self, org_id: str, tenant_id: str, group_id: str) -> None:
        raise NotImplementedError


group_service = GroupService()
