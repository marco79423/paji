import abc

from paji.domain import base_types
from paji.domain.command import helpers


class RunPajiServerUseCaseBase(base_types.UseCase):

    @abc.abstractmethod
    def execute(self, host: str, port: int, is_dev: bool):
        pass


class RunPajiServerUseCase(RunPajiServerUseCaseBase):

    def __init__(self, wsgi_server_helper: helpers.WSGIServerHelperBase):
        self._wsgi_server_helper = wsgi_server_helper

    def execute(self, host: str, port: int, is_dev: bool):
        self._wsgi_server_helper.serve(
            host=host,
            port=port,
            is_dev=is_dev,
        )
