from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.ping.dto import CreatePingRequest, PingResponse
from app.application.ping.service import PingService
from app.domain.ping.repositories.ping_repository import PingRepository
from app.infrastructure.database.config import get_db_session
from app.infrastructure.repositories.ping_repository import SQLAlchemyPingRepository

router = APIRouter()


@router.get("/", response_model=PingResponse)
async def ping(
    session: AsyncSession = Depends(get_db_session),
) -> PingResponse:

    ping_repository: PingRepository = SQLAlchemyPingRepository(session)

    ping_service = PingService(ping_repository)

    return await ping_service.get_ping()


@router.post("/", response_model=PingResponse)
async def create_ping(
    ping_request: CreatePingRequest,
    session: AsyncSession = Depends(get_db_session),
) -> PingResponse:

    ping_repository: PingRepository = SQLAlchemyPingRepository(session)

    ping_service = PingService(ping_repository)

    ping = await ping_service.create_ping(ping_request)

    return PingResponse(
        id=ping.id,
        message=ping.message,
        timestamp=ping.timestamp,
    )
