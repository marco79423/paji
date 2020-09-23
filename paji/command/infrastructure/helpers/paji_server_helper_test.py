from unittest import mock

from paji.command.infrastructure.helpers import PAJIServerHelper
from paji.server.app.paji_server import PAJIServerBase


def test_serve():
    paji_server = mock.MagicMock(spec=PAJIServerBase)

    paji_server_helper = PAJIServerHelper(
        paji_server=paji_server
    )

    paji_server_helper.serve(
        host='0.0.0.0',
        port=9527,
        is_dev=True,
    )

    paji_server.serve.assert_called_with(
        host='0.0.0.0',
        port=9527,
        is_dev=True,
    )
