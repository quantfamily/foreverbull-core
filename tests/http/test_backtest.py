import requests_mock
import requests
from foreverbull_core.http import RequestError
from foreverbull_core.http.backtest import Backtest
import pytest


@pytest.fixture(scope="function")
def backtest_session():
    def setup():
        session = requests.Session()
        adapter = requests_mock.Adapter()
        session.mount("http://", adapter)
        backtest = Backtest("127.0.0.1:8080", session=session)
        return backtest, adapter

    return setup


def test_list_backtests(backtest_session):
    backtest, adapter = backtest_session()
    adapter.register_uri("GET", "http://127.0.0.1:8080/backtests", json=[])
    rsp = backtest.list_backtests()
    assert rsp == []


def test_list_backtests_negative(backtest_session):
    backtest, adapter = backtest_session()
    adapter.register_uri("GET", "http://127.0.0.1:8080/backtests", json=[], status_code=500)
    with pytest.raises(RequestError, match="get call /backtests gave bad return code: 500"):
        backtest.list_backtests()


def test_create_backtest(backtest_session):
    backtest, adapter = backtest_session()
    config = {
        "start_date": "2020-01-01",
        "end_date": "2022-12-31",
        "timezone": "utc",
        "benchmark": "AAPL",
        "assets": ["AAPLE", "TSLA"],
    }
    created_backtest = {"id": 1, "config": config}
    adapter.register_uri("POST", "http://127.0.0.1:8080/backtests", json=created_backtest)
    rsp = backtest.create_backtest(config)
    assert rsp["id"] == created_backtest["id"]


def test_create_backtest_negative(backtest_session):
    backtest, adapter = backtest_session()
    adapter.register_uri("POST", "http://127.0.0.1:8080/backtests", json={}, status_code=500)
    with pytest.raises(RequestError, match="post call /backtests gave bad return code: 500"):
        backtest.create_backtest({})


def test_get_backtest(backtest_session):
    backtest, adapter = backtest_session()
    adapter.register_uri("GET", "http://127.0.0.1:8080/backtests/1", json={})
    backtest.get_backtest(1)


def test_get_backtest_negative(backtest_session):
    backtest, adapter = backtest_session()
    backtest, adapter = backtest_session()
    adapter.register_uri("GET", "http://127.0.0.1:8080/backtests/1", status_code=500)
    with pytest.raises(RequestError, match="get call /backtests/1 gave bad return code: 500"):
        backtest.get_backtest(1)


def test_delete_backtest(backtest_session):
    backtest, adapter = backtest_session()
    adapter.register_uri("DELETE", "http://127.0.0.1:8080/backtests/1")
    backtest.delete_backtest(1)


def test_delete_backtest_negative(backtest_session):
    backtest, adapter = backtest_session()
    adapter.register_uri("DELETE", "http://127.0.0.1:8080/backtests/1", status_code=500)
    with pytest.raises(RequestError, match="delete call /backtests/1 gave bad return code: 500"):
        backtest.delete_backtest(1)


def test_list_backtest_services(backtest_session):
    backtest, adapter = backtest_session()
    adapter.register_uri("GET", "http://127.0.0.1:8080/backtests/1/services", json=[])
    rsp = backtest.list_backtest_services(1)
    assert rsp == []


def test_list_backtest_services_negative(backtest_session):
    backtest, adapter = backtest_session()
    adapter.register_uri("GET", "http://127.0.0.1:8080/backtests/1/services", status_code=500)
    with pytest.raises(RequestError, match="get call /backtests/1/services gave bad return code: 500"):
        backtest.list_backtest_services(1)


def test_add_backtest_services(backtest_session):
    backtest, adapter = backtest_session()
    adapter.register_uri("PUT", "http://127.0.0.1:8080/backtests/1/service")
    backtest.add_backtest_service(1, {})


def test_add_backtest_services_negative(backtest_session):
    backtest, adapter = backtest_session()
    adapter.register_uri("PUT", "http://127.0.0.1:8080/backtests/1/service", status_code=500)
    with pytest.raises(RequestError, match="post call /backtests/1/services gave bad return code: 500"):
        backtest.add_backtest_service(1, {})


def test_list_sessions(backtest_session):
    backtest, adapter = backtest_session()
    adapter.register_uri("GET", "http://127.0.0.1:8080/backtests/1/sessions", json=[])
    assert backtest.list_sessions(1) == []


def test_list_sessions_negative(backtest_session):
    backtest, adapter = backtest_session()
    adapter.register_uri("GET", "http://127.0.0.1:8080/backtests/1/sessions", status_code=500)
    with pytest.raises(RequestError, match="get call /backtests/1/sessions gave bad return code: 500"):
        backtest.list_sessions(1)


def test_create_session(backtest_session):
    backtest, adapter = backtest_session()
    adapter.register_uri("POST", "http://127.0.0.1:8080/backtests/1/sessions", json={})
    assert backtest.create_session(1) == {}


def test_create_session_negative(backtest_session):
    backtest, adapter = backtest_session()
    adapter.register_uri("POST", "http://127.0.0.1:8080/backtests/1/sessions", status_code=500)
    with pytest.raises(RequestError, match="post call /backtests/1/sessions gave bad return code: 500"):
        backtest.create_session(1)


def test_get_session(backtest_session):
    backtest, adapter = backtest_session()
    adapter.register_uri("GET", "http://127.0.0.1:8080/backtests/1/sessions/1", json={})
    assert backtest.get_session(1, 1) == {}


def test_get_session_negative(backtest_session):
    backtest, adapter = backtest_session()
    adapter.register_uri("GET", "http://127.0.0.1:8080/backtests/1/sessions/1", status_code=500)
    with pytest.raises(RequestError, match="get call /backtests/1/sessions/1 gave bad return code: 500"):
        backtest.get_session(1, 1)


def test_delete_session(backtest_session):
    backtest, adapter = backtest_session()
    adapter.register_uri("DELETE", "http://127.0.0.1:8080/backtests/1/sessions/1")
    assert backtest.delete_session(1, 1) is True


def test_delete_session_negative(backtest_session):
    backtest, adapter = backtest_session()
    adapter.register_uri("DELETE", "http://127.0.0.1:8080/backtests/1/sessions/1", status_code=500)
    with pytest.raises(RequestError, match="delete call /backtests/1/sessions/1 gave bad return code: 500"):
        backtest.delete_session(1, 1)


def test_run_session(backtest_session):
    backtest, adapter = backtest_session()
    adapter.register_uri("POST", "http://127.0.0.1:8080/backtests/1/sessions/1/run", json={})
    assert backtest.run_session(1, 1, {}) == {}


def test_run_session_negative(backtest_session):
    backtest, adapter = backtest_session()
    adapter.register_uri("POST", "http://127.0.0.1:8080/backtests/1/sessions/1/run", status_code=500)
    with pytest.raises(RequestError, match="post call /backtests/1/sessions/1/run gave bad return code: 500"):
        backtest.run_session(1, 1, {})
