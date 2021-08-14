from unittest import mock

from foreverbull_core.broker import Broker
from foreverbull_core.http.http import HTTPClient
from foreverbull_core.http.service import Service
from foreverbull_core.socket.client import SocketClient


def test_broker():
    host = "my_host.com"
    service_id = "my_service_id"
    instance_id = "my_instance_id"
    local_host = "127.0.0.1"
    broker = Broker(host, service_id, instance_id, local_host)
    assert broker._host == host
    assert broker._service_id == service_id
    assert broker._instance_id == instance_id
    assert broker._local_host == local_host
    assert type(broker.http) == HTTPClient
    assert type(broker.socket) == SocketClient


def test_mark_as_online():
    host = "my_host.com"
    service_id = "my_service_id"
    instance_id = "my_instance_id"
    local_host = "127.0.0.1"
    with mock.patch.object(Service, "update_instance", return_value=None) as update_service:
        broker = Broker(host, service_id, instance_id, local_host)
        broker.mark_as_online()

    update_service.assert_called_once_with(service_id, instance_id, local_host, mock.ANY, True)


def test_mark_as_offline():
    host = "my_host.com"
    service_id = "my_service_id"
    instance_id = "my_instance_id"
    local_host = "127.0.0.1"
    with mock.patch.object(Service, "update_instance", return_value=None) as update_service:
        broker = Broker(host, service_id, instance_id, local_host)
        broker.mark_as_offline()

    update_service.assert_called_once_with(service_id, instance_id, local_host, mock.ANY, False)
