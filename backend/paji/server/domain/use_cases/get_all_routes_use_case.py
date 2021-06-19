from typing import List

from paji.server.domain import helpers, entities
from paji_sdk.base import base_types


class GetAllRoutesUseCase(base_types.UseCase):

    def __init__(self, flask_helper: helpers.FlaskHelperBase):
        self._flask_helper = flask_helper

    def execute(self) -> List[entities.Route]:
        return self._flask_helper.get_all_routes()
