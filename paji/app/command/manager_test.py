from .manager import Manager


def test_hello(capsys):
    manager = Manager()

    manager.hello('兩大類')

    captured = capsys.readouterr()
    assert captured.out == '哈囉 兩大類\n'
