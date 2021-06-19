import abc

from paji.shared import base_types


class PAJIServerHelperBase(base_types.Helper):

    @abc.abstractmethod
    def serve(self, host: str, port: int, is_dev: bool):
        pass
