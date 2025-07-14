from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class PingResponse(BaseModel):
    """Ответ на пинг DTO"""
    id: UUID
    message: str = "pong"
    timestamp: datetime

    class Config:
        """Конфигурация Pydantic модели"""
        from_attributes = True
        arbitrary_types_allowed = True


class CreatePingRequest(BaseModel):
    """Создание запроса на пинг DTO"""
    message: str = Field(default="pong", description="Ping message")
