from unittest import mock

from paji.command.app.manager import Manager
from paji.command.domain import use_cases, helpers


def test_hello():
    console_helper = mock.MagicMock(spec=helpers.ConsoleHelperBase)
    run_paji_server_use_case = mock.MagicMock(spec=use_cases.RunPajiServerUseCaseBase)

    manager = Manager(
        console_helper=console_helper,
        run_paji_server_use_case=run_paji_server_use_case,
    )

    manager.hello('兩大類')

    console_helper.print.assert_called_with('哈囉 兩大類')


def test_run_server():
    console_helper = mock.MagicMock(spec=helpers.ConsoleHelperBase)
    run_paji_server_use_case = mock.Mock(spec=use_cases.RunPajiServerUseCaseBase)

    manager = Manager(
        console_helper=console_helper,
        run_paji_server_use_case=run_paji_server_use_case,
    )

    manager.run_server('1.1.1.1', 9527, True)
    run_paji_server_use_case.execute.assert_called_with(
        host='1.1.1.1',
        port=9527,
        is_dev=True,
    )
