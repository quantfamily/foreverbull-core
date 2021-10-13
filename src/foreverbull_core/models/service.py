import enum
from typing import Optional

import pydantic

from foreverbull_core.models.base import Base


class ServiceType(enum.Enum):
    WORKER = "worker"
    BACKTEST = "backtest"


class Service(Base):
    id: Optional[str]
    name: str
    image: str
    type: ServiceType

    @pydantic.validator("type")
    def validate_type(cls, v):
        if type(v) is str:
            return getattr(ServiceType, v.upper())
        return v

    def dict(self, *args, **kwargs):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "type": self.type if type(self.type) is str else self.type.value,
        }


class Instance(Base):
    id: str
    service_id: str
    session_id: str
    host: str
    port: int
    listen: bool
    online: bool
