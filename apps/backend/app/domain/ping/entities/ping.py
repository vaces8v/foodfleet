from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass
class Ping:
    """Сущность ping"""
    id: UUID = field(default_factory=uuid4)
    message: str = "pong"
    timestamp: datetime = field(default_factory=datetime.utcnow)
