from unittest import mock

import flask

from paji.server.app.paji_server import PAJIServer
from paji.server.domain import helpers


def test_serve():
    flask_app = mock.MagicMock(spec=flask.Flask)
    wsgi_server_helper = mock.MagicMock(spec=helpers.WSGIServerHelperBase)

    paji_server = PAJIServer(
        flask_app=flask_app,
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
