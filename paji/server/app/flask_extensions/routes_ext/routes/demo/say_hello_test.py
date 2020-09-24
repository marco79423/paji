import flask.views
import pytest

from paji import server


@pytest.fixture
def app():
    container = server.ServerContainer()
    paji_server = container.PAJIServer()
    return paji_server.get_app()


def test_hello_without_name(client, app):
    res = client.get(flask.url_for('demo.hello'))
    assert res.status_code == 200
    assert res.data.decode('utf-8') == '哈囉 陌生人'
