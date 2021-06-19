from paji.command.domain import helpers
from paji.server.app.paji_server import PAJIServerBase


class PAJIServerHelper(helpers.PAJIServerHelperBase):

    def __init__(self, paji_server: PAJIServerBase):
        self._paji_server = paji_server

    def serve(self, host: str, port: int, is_dev: bool):
        return self._paji_server.serve(
            host=host,
            port=port,
            is_dev=is_dev,
        )
