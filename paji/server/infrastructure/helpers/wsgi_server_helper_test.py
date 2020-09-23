import logging
from unittest import mock

import flask
import pytest

from paji.server.infrastructure.helpers import WSGIServerHelper


def test_run_dev_server_with_flask_app():
    flask_app = mock.MagicMock(spec=flask.Flask)

    wsgi_server_helper = WSGIServerHelper()
    wsgi_server_helper.serve(flask_app, '1.1.1.1', 9527, True)

    flask_app.logger.setLevel.assert_called_with(logging.DEBUG)
    flask_app.run(host='1.1.1.1', port=9527, debug=True)


def test_run_dev_server_without_flask_app():
    app = mock.MagicMock()

    wsgi_server_helper = WSGIServerHelper()

    with pytest.raises(NotImplementedError):
        wsgi_server_helper.serve(app, '1.1.1.1', 9527, True)


def test_run_prod_server():
    app = mock.MagicMock()

    wsgi_server_helper = WSGIServerHelper()

    with pytest.raises(NotImplementedError):
        wsgi_server_helper.serve(app, '1.1.1.1', 9527, False)
