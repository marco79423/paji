from dependency_injector import containers, providers

from .cli import create_cli
from .manager import Manager


class Container(containers.DeclarativeContainer):
    Manager = providers.Factory(Manager)

    create_cli = providers.Callable(
        create_cli,
        Manager,
    )
