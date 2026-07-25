from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    name: str


class UserUpdate(BaseModel):
    email: EmailStr | None = None
    name: str | None = None


class UserResponse(BaseModel):
    id: str
    org_id: str
    tenant_id: str
    email: str
    name: str
    created_at: datetime
