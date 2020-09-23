import abc


class ManagerBase(abc.ABC):

    @abc.abstractmethod
    def hello(self, name: str):
        pass

    @abc.abstractmethod
    def run_server(self, host: str, port: int, is_dev: bool):
        pass


class Manager(ManagerBase):

    def hello(self, name):
        print(f'哈囉 {name}')

    def run_server(self, host, port, is_dev):
        print(f'啟動 paji 伺服器 (http://{host}:{port}) 開發者模式：{is_dev}')
