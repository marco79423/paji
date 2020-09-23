from unittest import mock

from paji.domain.command import helpers
from paji.domain.command.use_cases.run_paji_server_use_case import RunPajiServerUseCase


def test_run_paji_server():
    wsgi_server_helper = mock.MagicMock(spec=helpers.WSGIServerHelperBase)

    uc = RunPajiServerUseCase(
        wsgi_server_helper=wsgi_server_helper,
    )

    uc.execute(
        host='0.0.0.0',
        port=9527,
        is_dev=True,
    )

    wsgi_server_helper.serve.assert_called_with(
        host='0.0.0.0',
        port=9527,
        is_dev=True,
    )
