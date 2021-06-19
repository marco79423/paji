from unittest import mock

import flask

from paji.server.app import flask_extensions
from paji.server.app.paji_server import PAJIServer
from paji.server.domain import helpers


def test_setup():
    flask_app = mock.MagicMock(spec=flask.Flask)
    routes_ext = mock.MagicMock(spec=flask_extensions.RoutesExtBase)
    wsgi_server_helper = mock.MagicMock(spec=helpers.WSGIServerHelperBase)

    PAJIServer(
        flask_app=flask_app,
        routes_ext=routes_ext,
        wsgi_server_helper=wsgi_server_helper,
    )

    routes_ext.init_app.assert_called_with(flask_app)


def test_get_app():
    flask_app = mock.MagicMock(spec=flask.Flask)
    routes_ext = mock.MagicMock(spec=flask_extensions.RoutesExtBase)
    wsgi_server_helper = mock.MagicMock(spec=helpers.WSGIServerHelperBase)

    paji_server = PAJIServer(
        flask_app=flask_app,
        routes_ext=routes_ext,
        wsgi_server_helper=wsgi_server_helper,
    )

    assert paji_server.get_app() == flask_app


def test_serve():
    flask_app = mock.MagicMock(spec=flask.Flask)
    routes_ext = mock.MagicMock(spec=flask_extensions.RoutesExtBase)
    wsgi_server_helper = mock.MagicMock(spec=helpers.WSGIServerHelperBase)

    paji_server = PAJIServer(
        flask_app=flask_app,
        routes_ext=routes_ext,
        wsgi_server_helper=wsgi_server_helper,
    )

    paji_server.serve(
        host='1.1.1.1',
        port=9527,
        is_dev=True,
    )

    wsgi_server_helper.serve.assert_called_with(
        app=flask_app,
        host='1.1.1.1',
        port=9527,
        is_dev=True,
    )
