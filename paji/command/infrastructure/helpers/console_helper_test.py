from paji.command.infrastructure.helpers import ConsoleHelper


def test_run_server(capsys):
    console_helper = ConsoleHelper()
    console_helper.print('今天天氣不錯')

    captured = capsys.readouterr()
    assert captured.out == '今天天氣不錯\n'
