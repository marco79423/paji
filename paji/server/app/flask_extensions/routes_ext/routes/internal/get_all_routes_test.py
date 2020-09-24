from unittest import mock

import flask.views
import pytest

from paji import server
from paji.server.domain import helpers, entities, use_cases


@pytest.fixture
def app():
    container = server.ServerContainer()
    paji_server = container.PAJIServer()

    app = paji_server.get_app()
    app.container = container

    return app


def test_get_all_routes(client, app):
    get_all_routes_use_case = mock.MagicMock(spec=use_cases.GetAllRoutesUseCase)
    get_all_routes_use_case.execute.return_value = [
        entities.Route(
            methods={'GET'},
            endpoint='endpoint',
            path='/resource',
        ),
    ]

    with app.container.GetAllRoutesUseCase.override(get_all_routes_use_case):
        res = client.get(flask.url_for('internal.get_all_routes'))

    assert res.status_code == 200
    assert res.json == [
        {
            'methods': ['GET'],
            'endpoint': 'endpoint',
            'path': '/resource'
        }
    ]
