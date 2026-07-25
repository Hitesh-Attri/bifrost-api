from datetime import datetime

from pydantic import BaseModel


class OrgCreate(BaseModel):
    name: str
    slug: str


class OrgUpdate(BaseModel):
    name: str | None = None
    slug: str | None = None


class OrgResponse(BaseModel):
    id: str
    name: str
    slug: str
    created_at: datetime
