from foreverbull_core.models.socket import Request, Response, SocketConfig
from foreverbull_core.socket.nanomsg import NanomsgContextSocket, NanomsgSocket


class SocketClient:
    def __init__(self, config: SocketConfig) -> None:
        self.config = config
        self._socket = NanomsgSocket(config)

    def url(self):
        return self._socket.url()

    def send(self, message: Response) -> None:
        self._socket.send(message.dump())

    def recv(self):
        data = self._socket.recv()
        return Request.load(data)

    def close(self):
        self._socket.close()

    def new_context(self) -> NanomsgContextSocket:
        return NanomsgContextSocket(self._socket.new_context())
