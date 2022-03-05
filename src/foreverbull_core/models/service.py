import enum
from typing import Optional

import pydantic

from foreverbull_core.models.base import Base


class ServiceType(enum.Enum):
    WORKER = "worker"
    BACKTEST = "backtest"


class Service(Base):
    """_summary_

    Args:
        id (str, optional): Optional[str]
        name (str): str
        image (str): str
        type (ServiceType): ServiceType

    Returns:
        Service: _description_
    """

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
    """_summary_

    Args:
        id (str): str
        service_id (str): str
        session_id (str, optional): Optional[str]
        host (str, optional): Optional[str]
        port (int, optional): Optional[int]
        listen (bool, optional): Optional[bool]
        online (bool, optional): Optional[bool]

    Returns:
        Instance: instance
    """

    id: str
    service_id: str
    session_id: Optional[str]
    host: Optional[str]
    port: Optional[int]
    listen: Optional[bool]
    online: Optional[bool]


class RawConnection(Base):
    """_summary_

    Args:
        host (str): str
        port (int): int

    Returns:
        RawConnection: raw
    """

    host: str
    port: int
