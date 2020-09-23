from paji.command.infrastructure.helpers import WSGIServerHelper


def test_run_server(capsys):
    wsgi_server_helper = WSGIServerHelper()
    wsgi_server_helper.serve('1.1.1.1', 9527, True)

    captured = capsys.readouterr()
    assert captured.out == f'啟動 paji 伺服器 (http://1.1.1.1:9527) 開發者模式：True\n'
