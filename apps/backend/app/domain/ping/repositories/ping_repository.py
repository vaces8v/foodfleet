from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from app.domain.ping.entities.ping import Ping


class PingRepository(ABC):
    """Абстрактный интерфейс репозитория для сущности ping"""

    @abstractmethod
    async def get_ping(self, ping_id: UUID) -> Optional[Ping]:
        """Получение ping по id"""
        pass

    @abstractmethod
    async def create_ping(self, ping: Ping) -> Ping:
        """Создание нового ping"""
        pass

    @abstractmethod
    async def get_latest_ping(self) -> Optional[Ping]:
        """Получение последнего ping"""
        pass
