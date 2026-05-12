from schemas.user import UserCreate, UserResponse, UserUpdate


class UserService:
    async def list(self, org_id: str, tenant_id: str) -> list[UserResponse]:
        raise NotImplementedError

    async def get(self, org_id: str, tenant_id: str, user_id: str) -> UserResponse:
        raise NotImplementedError

    async def create(self, org_id: str, tenant_id: str, payload: UserCreate) -> UserResponse:
        raise NotImplementedError

    async def update(self, org_id: str, tenant_id: str, user_id: str, payload: UserUpdate) -> UserResponse:
        raise NotImplementedError

    async def delete(self, org_id: str, tenant_id: str, user_id: str) -> None:
        raise NotImplementedError


user_service = UserService()
