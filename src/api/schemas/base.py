from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    environment: str
    version: str = "1.0.0"
