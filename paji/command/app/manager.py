import abc

from paji.command.domain import use_cases, helpers


class ManagerBase(abc.ABC):

    @abc.abstractmethod
    def hello(self, name: str):
        pass

    @abc.abstractmethod
    def run_server(self, host: str, port: int, is_dev: bool):
        pass


class Manager(ManagerBase):

    def __init__(self,
                 console_helper: helpers.ConsoleHelperBase,
                 run_paji_server_use_case: use_cases.RunPajiServerUseCaseBase
                 ):
        self._console_helper = console_helper
        self._run_paji_server_use_case = run_paji_server_use_case

    def hello(self, name: str):
        self._console_helper.print(f'哈囉 {name}')

    def run_server(self, host: str, port: int, is_dev: bool):
        self._run_paji_server_use_case.execute(
            host=host,
            port=port,
            is_dev=is_dev,
        )
