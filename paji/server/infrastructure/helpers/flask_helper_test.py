from unittest import mock

import werkzeug.routing

from paji.server.domain import entities
from paji.server.infrastructure.helpers import FlaskHelper


def test_get_all_routes():
    flask_app = mock.MagicMock()
    flask_app.url_map.iter_rules.return_value = [
        werkzeug.routing.Rule('/resource', endpoint='endpoint', methods=['GET']),
    ]

    flask_helper = FlaskHelper(
        flask_app=flask_app,
    )

    assert flask_helper.get_all_routes() == [
        entities.Route(
            methods={'HEAD', 'GET'},
            endpoint='endpoint',
            path='/resource'
        )
    ]
