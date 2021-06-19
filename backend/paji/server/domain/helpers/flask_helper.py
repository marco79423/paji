import abc
from typing import List

from paji.server.domain import entities
from paji_sdk.base import base_types


class FlaskHelperBase(base_types.Helper):

    @abc.abstractmethod
    def get_all_routes(self) -> List[entities.Route]:
        pass
