from foreverbull_core.models.backtest import BacktestConfig, Info
from foreverbull_core.models.socket import SocketConfig


def test_info():
    main = SocketConfig(socket_type="requester")
    feed = SocketConfig(socket_type="publisher")
    broker = SocketConfig(socket_type="requester")
    info = Info(main=main, feed=feed, broker=broker, running=True)

    dumped = info.dump()
    loaded = Info.load(dumped)
    assert info == loaded


def test_config():
    config = BacktestConfig(
        start_date="2017-01-01", end_date="2018-01-01", timezone="utc", benchmark="AAPL", assets=["TSLA", "AAPL"]
    )

    dumped = config.dump()
    loaded = BacktestConfig.load(dumped)
    assert config == loaded
