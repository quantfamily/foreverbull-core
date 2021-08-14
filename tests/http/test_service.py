import requests_mock
import requests
from foreverbull_core.http import RequestError
from foreverbull_core.http.service import Service
import pytest

@pytest.fixture(scope="function")
def service_session():
    def setup():
        session = requests.Session()
        adapter = requests_mock.Adapter()
        session.mount("http://", adapter)
        service = Service("127.0.0.1:8080", session=session)
        return service, adapter

    return setup

def test_list_services(service_session):
    service, adapter = service_session()
    adapter.register_uri("GET", "http://127.0.0.1:8080/services", json=[])
    assert service.list_services() == []


def test_list_services_negative(service_session):
    service, adapter = service_session()
    adapter.register_uri("GET", "http://127.0.0.1:8080/services", status_code=500)

    with pytest.raises(RequestError, match="get call /services gave bad return code: 500"):
        service.list_services()


def test_create_service(service_session):
    service, adapter = service_session()
    adapter.register_uri("POST", "http://127.0.0.1:8080/services", json={"id": 1})
    assert service.create_service({}) == {"id": 1}


def test_create_service_negative(service_session):
    service, adapter = service_session()
    adapter.register_uri("POST", "http://127.0.0.1:8080/services", status_code=500)

    with pytest.raises(RequestError, match="post call /services gave bad return code: 500"):
        service.create_service({})


def test_get_service(service_session):
    service, adapter = service_session()
    adapter.register_uri("GET", "http://127.0.0.1:8080/services/1", json={"id": 1})
    assert service.get_service(1) == {"id": 1}


def test_get_service_negative(service_session):
    service, adapter = service_session()
    adapter.register_uri("GET", "http://127.0.0.1:8080/services/1", status_code=500)

    with pytest.raises(RequestError, match="get call /services/1 gave bad return code: 500"):
        service.get_service(1)


def test_delete_service(service_session):
    service, adapter = service_session()
    adapter.register_uri("DELETE", "http://127.0.0.1:8080/services/1")
    assert service.delete_service(1) is True


def test_delete_service_negative(service_session):
    service, adapter = service_session()
    adapter.register_uri("DELETE", "http://127.0.0.1:8080/services/1", status_code=500)

    with pytest.raises(RequestError, match="delete call /services/1 gave bad return code: 500"):
        service.delete_service(1)


def test_list_instances(service_session):
    service, adapter = service_session()
    adapter.register_uri("GET", "http://127.0.0.1:8080/services/1/instances", json=[])
    assert service.list_instances(1) == []


def test_list_instances_negative(service_session):
    service, adapter = service_session()
    adapter.register_uri("GET", "http://127.0.0.1:8080/services/1/instances", status_code=500)

    with pytest.raises(RequestError, match="get call /services/1/instances gave bad return code: 500"):
        service.list_instances(1)


def test_create_instance(service_session):
    service, adapter = service_session()
    adapter.register_uri("POST", "http://127.0.0.1:8080/services/1/instances", json={"id": 14})
    assert service.create_instance(1, {}) == {"id": 14}


def test_create_instance_negative(service_session):
    service, adapter = service_session()
    adapter.register_uri("POST", "http://127.0.0.1:8080/services/1/instances", status_code=500)

    with pytest.raises(RequestError, match="post call /services/1/instances gave bad return code: 500"):
        service.create_instance(1, {})


def test_get_instance(service_session):
    service, adapter = service_session()
    adapter.register_uri("GET", "http://127.0.0.1:8080/services/1/instances/1", json={"id": 14})
    assert service.get_instance(1, 1) == {"id": 14}


def test_get_instance_negative(service_session):
    service, adapter = service_session()
    adapter.register_uri("GET", "http://127.0.0.1:8080/services/1/instances/1", status_code=500)

    with pytest.raises(RequestError, match="get call /services/1/instances/1 gave bad return code: 500"):
        service.get_instance(1, 1)


def test_delete_instance(service_session):
    service, adapter = service_session()
    adapter.register_uri("DELETE", "http://127.0.0.1:8080/services/1/instances/1")
    assert service.delete_instance(1, 1) is True


def test_delete_instance_negative(service_session):
    service, adapter = service_session()
    adapter.register_uri("DELETE", "http://127.0.0.1:8080/services/1/instances/1", status_code=500)

    with pytest.raises(RequestError, match="delete call /services/1/instances/1 gave bad return code: 500"):
        service.delete_instance(1, 1)


def test_list_containers(service_session):
    service, adapter = service_session()
    adapter.register_uri("GET", "http://127.0.0.1:8080/services/containers", json=[])
    assert service.list_containers() == []


def test_list_containers_negative(service_session):
    service, adapter = service_session()
    adapter.register_uri("GET", "http://127.0.0.1:8080/services/containers", status_code=500)

    with pytest.raises(RequestError, match="get call /services/containers gave bad return code: 500"):
        service.list_containers()


def test_create_container(service_session):
    service, adapter = service_session()
    adapter.register_uri("POST", "http://127.0.0.1:8080/services/containers", json={})
    assert service.create_container({}) == {}


def test_create_container_negative(service_session):
    service, adapter = service_session()
    adapter.register_uri("POST", "http://127.0.0.1:8080/services/containers", status_code=500)

    with pytest.raises(RequestError, match="post call /services/containers gave bad return code: 500"):
        service.create_container({})


def test_get_container(service_session):
    service, adapter = service_session()
    adapter.register_uri("GET", "http://127.0.0.1:8080/services/containers/1", json={})
    assert service.get_container(1) == {}


def test_get_container_negative(service_session):
    service, adapter = service_session()
    adapter.register_uri("GET", "http://127.0.0.1:8080/services/containers/1", status_code=500)

    with pytest.raises(RequestError, match="get call /services/containers/1 gave bad return code: 500"):
        service.get_container(1)


def test_delete_container(service_session):
    service, adapter = service_session()
    adapter.register_uri("DELETE", "http://127.0.0.1:8080/services/containers/1", json={})
    assert service.delete_container(1) is True


def test_delete_container_negative(service_session):
    service, adapter = service_session()
    adapter.register_uri("DELETE", "http://127.0.0.1:8080/services/containers/1", status_code=500)

    with pytest.raises(RequestError, match="delete call /services/containers/1 gave bad return code: 500"):
        service.delete_container(1)


def test_HTTPClient():
    pass
