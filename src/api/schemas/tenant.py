from datetime import datetime

from pydantic import BaseModel


class TenantCreate(BaseModel):
    name: str
    slug: str


class TenantUpdate(BaseModel):
    name: str | None = None
    slug: str | None = None


class TenantResponse(BaseModel):
    id: str
    org_id: str
    name: str
    slug: str
    created_at: datetime
