import datetime
from typing import Optional, cast
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import desc

from app.domain.ping.entities.ping import Ping
from app.domain.ping.repositories.ping_repository import PingRepository
from app.infrastructure.database.models import PingModel


class SQLAlchemyPingRepository(PingRepository):
    """SQLAlchemy implementation of PingRepository"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_ping(self, ping_id: UUID) -> Optional[Ping]:
        """Get ping by id"""
        query = select(PingModel).where(PingModel.id == ping_id)
        result = await self.session.execute(query)
        ping_model = result.scalar_one_or_none()

        if ping_model is None:
            return None

        # Преобразование SQLAlchemy модели в сущность домена
        return self._to_domain_entity(ping_model)

    async def create_ping(self, ping: Ping) -> Ping:
        """Create new ping"""
        ping_model = PingModel(
            id=ping.id,
            message=ping.message,
            timestamp=ping.timestamp,
        )

        self.session.add(ping_model)
        await self.session.flush()

        return ping

    async def get_latest_ping(self) -> Optional[Ping]:
        """Get latest ping"""
        query = select(PingModel).order_by(desc(PingModel.timestamp)).limit(1)
        result = await self.session.execute(query)
        ping_model = result.scalar_one_or_none()

        if ping_model is None:
            return None

        # Преобразование SQLAlchemy модели в сущность домена
        return self._to_domain_entity(ping_model)

    def _to_domain_entity(self, ping_model: PingModel) -> Ping:
        """Convert SQLAlchemy model to domain entity"""
        return Ping(
            id=cast(UUID, ping_model.id),
            message=cast(str, ping_model.message),
            timestamp=cast(datetime.datetime, ping_model.timestamp),
        )
