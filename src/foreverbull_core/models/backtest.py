from foreverbull_core.models.socket import SocketConfig
from typing import List, Optional
from foreverbull_core.models.base import Base


class Info(Base):
    main: SocketConfig
    feed: SocketConfig
    broker: SocketConfig
    running: bool


class BacktestConfig(Base):
    start_date: str
    end_date: str
    timezone: str = "utc"
    benchmark: str
    assets: List[str]
