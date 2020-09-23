import abc

from paji.command.domain import use_cases


class ManagerBase(abc.ABC):

    @abc.abstractmethod
    def hello(self, name: str):
        pass

    @abc.abstractmethod
    def run_server(self, host: str, port: int, is_dev: bool):
        pass


class Manager(ManagerBase):

    def __init__(self,
                 run_paji_server_use_case=use_cases.RunPajiServerUseCaseBase
                 ):
        self._run_paji_server_use_case = run_paji_server_use_case

    def hello(self, name: str):
        print(f'哈囉 {name}')

    def run_server(self, host: str, port: int, is_dev: bool):
        self._run_paji_server_use_case.execute(
            host=host,
            port=port,
            is_dev=is_dev,
        )
