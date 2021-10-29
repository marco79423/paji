import abc


class ServiceBase(abc.ABC):

    @abc.abstractmethod
    def start(self):
        pass
