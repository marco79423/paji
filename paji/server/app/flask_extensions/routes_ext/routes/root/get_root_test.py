import flask.views
import pytest

from paji import server


@pytest.fixture
def app():
    container = server.ServerContainer()
    paji_server = container.PAJIServer()

    app = paji_server.get_app()
    app.container = container

    return app


def test_get_root(client):
    res = client.get(flask.url_for('get_root'))

    assert res.status_code == 200
    assert res.data.decode() == '啪……啪唧！'
