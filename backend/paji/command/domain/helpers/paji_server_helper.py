import abc

from paji_sdk.base import base_types


class PAJIServerHelperBase(base_types.Helper):

    @abc.abstractmethod
    def serve(self, host: str, port: int, is_dev: bool):
        pass
