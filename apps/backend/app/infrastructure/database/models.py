from time import timezone
import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app.infrastructure.database.config import Base


class PingModel(Base):
    """SQLAlchemy модель для сущности ping"""
    __tablename__ = "pings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    message = Column(String, nullable=False, default="pong")
    timestamp = Column(DateTime, nullable=False, default=datetime.now())

    def __repr__(self) -> str:
        return f"<Ping(id={self.id}, message={self.message})>"
