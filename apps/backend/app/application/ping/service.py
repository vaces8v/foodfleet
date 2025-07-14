from typing import Optional

from app.application.ping.dto import CreatePingRequest, PingResponse
from app.domain.ping.entities.ping import Ping
from app.domain.ping.repositories.ping_repository import PingRepository


class PingService:
    """Сервис для обработки операций пинга"""

    def __init__(self, ping_repository: PingRepository):
        self.ping_repository = ping_repository

    async def get_ping(self) -> PingResponse:
        ping = await self.ping_repository.get_latest_ping()

        if ping is None:
            ping = await self.create_ping(CreatePingRequest())

        # Можно безопасно использовать ping здесь, так как он никогда не будет None в этой точке
        # Либо он был получен из репозитория, либо был создан новый
        return PingResponse(
            id=ping.id,
            message=ping.message,
            timestamp=ping.timestamp,
        )

    async def create_ping(self, ping_request: CreatePingRequest) -> Ping:
        ping = Ping(message=ping_request.message)

        return await self.ping_repository.create_ping(ping)
