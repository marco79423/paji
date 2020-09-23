from paji.app.command.manager import Manager


def test_hello(capsys):
    manager = Manager()

    manager.hello('兩大類')

    captured = capsys.readouterr()
    assert captured.out == '哈囉 兩大類\n'


def test_run_server(capsys):
    manager = Manager()

    manager.run_server('1.1.1.1', 9527, True)

    captured = capsys.readouterr()
    assert captured.out == f'啟動 paji 伺服器 (http://1.1.1.1:9527) 開發者模式：True\n'
