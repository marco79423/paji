import abc

from paji_sdk.base import base_types


class WSGIServerHelperBase(base_types.Helper):

    @abc.abstractmethod
    def serve(self, app, host: str, port: int, is_dev: bool):
        pass
