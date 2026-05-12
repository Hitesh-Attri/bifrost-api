from core.config import settings
from schemas.base import HealthResponse


class HealthService:
    def get_status(self) -> HealthResponse:
        return HealthResponse(
            status="ok",
            environment=settings.app_env,
        )


health_service = HealthService()
