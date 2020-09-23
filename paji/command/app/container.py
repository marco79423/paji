from dependency_injector import containers, providers

from paji.command.app.cli import create_cli
from paji.command.app.manager import Manager
from paji.command.domain import use_cases
from paji.command.infrastructure import helpers


class Container(containers.DeclarativeContainer):
    ConsoleHelper = providers.Factory(
        helpers.ConsoleHelper,
    )

    WSGIServerHelper = providers.Factory(
        helpers.WSGIServerHelper,
        console_helper=ConsoleHelper,
    )

    RunPajiServerUseCase = providers.Factory(
        use_cases.RunPajiServerUseCase,
        wsgi_server_helper=WSGIServerHelper,
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
