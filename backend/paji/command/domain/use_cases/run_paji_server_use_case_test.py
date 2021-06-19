from unittest import mock

from paji.command.domain import helpers
from paji.command.domain.use_cases import RunPajiServerUseCase


def test_run_paji_server():
    paji_server_helper = mock.MagicMock(spec=helpers.PAJIServerHelperBase)

    uc = RunPajiServerUseCase(
        paji_server_helper=paji_server_helper,
    )

    uc.execute(
        host='0.0.0.0',
        port=9527,
        is_dev=True,
    )

    paji_server_helper.serve.assert_called_with(
        host='0.0.0.0',
        port=9527,
        is_dev=True,
    )
