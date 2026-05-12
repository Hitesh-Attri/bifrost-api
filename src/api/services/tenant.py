from schemas.tenant import TenantCreate, TenantResponse, TenantUpdate


class TenantService:
    async def list(self, org_id: str) -> list[TenantResponse]:
        raise NotImplementedError

    async def get(self, org_id: str, tenant_id: str) -> TenantResponse:
        raise NotImplementedError

    async def create(self, org_id: str, payload: TenantCreate) -> TenantResponse:
        raise NotImplementedError

    async def update(self, org_id: str, tenant_id: str, payload: TenantUpdate) -> TenantResponse:
        raise NotImplementedError

    async def delete(self, org_id: str, tenant_id: str) -> None:
        raise NotImplementedError


tenant_service = TenantService()
