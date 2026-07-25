from schemas.org import OrgCreate, OrgResponse, OrgUpdate


class OrgService:
    async def list(self) -> list[OrgResponse]:
        raise NotImplementedError

    async def get(self, org_id: str) -> OrgResponse:
        raise NotImplementedError

    async def create(self, payload: OrgCreate) -> OrgResponse:
        raise NotImplementedError

    async def update(self, org_id: str, payload: OrgUpdate) -> OrgResponse:
        raise NotImplementedError

    async def delete(self, org_id: str) -> None:
        raise NotImplementedError


org_service = OrgService()
