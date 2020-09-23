from unittest import mock

from paji.app.command.manager import Manager
from paji.domain.command import use_cases


def test_hello(capsys):
    run_paji_server_use_case = mock.MagicMock(spec=use_cases.RunPajiServerUseCaseBase)

    manager = Manager(
        run_paji_server_use_case
    )

    manager.hello('兩大類')

    captured = capsys.readouterr()
    assert captured.out == '哈囉 兩大類\n'


def test_run_server():
    run_paji_server_use_case = mock.Mock(spec=use_cases.RunPajiServerUseCaseBase)

    manager = Manager(
        run_paji_server_use_case
    )

    manager.run_server('1.1.1.1', 9527, True)
    run_paji_server_use_case.execute.assert_called_with(
        host='1.1.1.1',
        port=9527,
        is_dev=True,
    )
