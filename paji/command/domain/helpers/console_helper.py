import abc

from paji_sdk.base import base_types


class ConsoleHelperBase(base_types.Helper):

    @abc.abstractmethod
    def print(self, message: str):
        pass
