import abc

from paji.domain import base_types


class WSGIServerHelperBase(base_types.Helper):

    @abc.abstractmethod
    def serve(self, host: str, port: int, is_dev: bool):
        pass
