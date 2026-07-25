from fastapi import APIRouter

from schemas.base import HealthResponse
from services.health import health_service
from utils.response import success

router = APIRouter(prefix="/health", tags=["health"])


@router.get("", response_model=HealthResponse)
async def health_check():
    return health_service.get_status()


@router.get("/ping")
async def ping():
    return success(data={"pong": True})
