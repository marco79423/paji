from unittest import mock

from paji.server.domain import helpers, entities
from paji.server.domain.use_cases import GetAllRoutesUseCase


def test_get_all_routes():
    routes = [
        entities.Route(
            methods={'GET'},
            endpoint='endpoint',
            path='/resource',
        ),
    ]

    flask_helper = mock.MagicMock(spec=helpers.FlaskHelperBase)
    flask_helper.get_all_routes.return_value = routes

    uc = GetAllRoutesUseCase(
        flask_helper=flask_helper,
    )

    assert uc.execute() == routes
