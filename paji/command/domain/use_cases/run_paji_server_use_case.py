import abc

from paji.command.domain import helpers
from paji.shared import base_types


class RunPajiServerUseCaseBase(base_types.UseCase):

    @abc.abstractmethod
    def execute(self, host: str, port: int, is_dev: bool):
        pass


class RunPajiServerUseCase(RunPajiServerUseCaseBase):

    def __init__(self,
                 paji_server_helper: helpers.PAJIServerHelperBase,
                 ):
        self._paji_server_helper = paji_server_helper

    def execute(self, host: str, port: int, is_dev: bool):
        self._paji_server_helper.serve(
            host=host,
            port=port,
            is_dev=is_dev,
        )
