from foreverbull_core.models.socket import Request, Response, SocketConfig


def test_socket_config():
    config = SocketConfig(socket_type="requester")

    data = config.dump()
    loaded = SocketConfig.load(data)
    assert config == loaded
    assert loaded.socket_type == "requester"
    assert loaded.port == 0
    assert loaded.listen
    assert loaded.recv_timeout == 5000
    assert loaded.send_timeout == 5000


def test_request():
    config = SocketConfig(socket_type="requester")
    request = Request(task="demo", data=config)

    data = request.dump()
    loaded = Request.load(data)
    assert request == loaded


def test_response():
    config = SocketConfig(socket_type="requester")
    response = Response(task="demo", data=config, error=None)

    data = response.dump()
    loaded = Response.load(data)
    assert response == loaded
