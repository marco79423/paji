from unittest import mock

from paji.command.domain import helpers
from paji.command.infrastructure.helpers import WSGIServerHelper


def test_run_server():
    console_helper = mock.MagicMock(spec=helpers.ConsoleHelperBase)

    wsgi_server_helper = WSGIServerHelper(
        console_helper=console_helper,
    )
    wsgi_server_helper.serve('1.1.1.1', 9527, True)
    console_helper.print.assert_called_with(f'啟動 paji 伺服器 (http://1.1.1.1:9527) 開發者模式：True')
