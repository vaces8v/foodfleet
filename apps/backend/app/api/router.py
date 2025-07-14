from fastapi import APIRouter

from app.api.endpoints import ping
from app.core.config import settings

api_router = APIRouter()

api_router.include_router(
    ping.router,
    prefix="/ping",
    tags=["ping"],
)


router = APIRouter(prefix=settings.API_V1_PREFIX)
