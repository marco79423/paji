from dependency_injector import containers, providers

from paji import server
from paji.command.app.cli import create_cli
from paji.command.app.manager import Manager
from paji.command.domain import use_cases
from paji.command.infrastructure import helpers


class CommandContainer(containers.DeclarativeContainer):
    ServerContainer = providers.Container(
        server.ServerContainer
    )

    ConsoleHelper = providers.Factory(
        helpers.ConsoleHelper,
    )

    PAJIServerHelper = providers.Factory(
        helpers.PAJIServerHelper,
        paji_server=ServerContainer.PAJIServer,
    )

    RunPajiServerUseCase = providers.Factory(
        use_cases.RunPajiServerUseCase,
        paji_server_helper=PAJIServerHelper,
    )

    Manager = providers.Factory(
        Manager,
        console_helper=ConsoleHelper,
        run_paji_server_use_case=RunPajiServerUseCase,
    )

    create_cli = providers.Callable(
        create_cli,
        Manager,
    )
