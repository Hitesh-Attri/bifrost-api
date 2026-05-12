from datetime import datetime

from pydantic import BaseModel


class GroupCreate(BaseModel):
    name: str


class GroupUpdate(BaseModel):
    name: str | None = None


class GroupResponse(BaseModel):
    id: str
    org_id: str
    tenant_id: str
    name: str
    created_at: datetime
