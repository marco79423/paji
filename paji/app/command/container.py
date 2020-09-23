from dependency_injector import containers, providers

from paji.app.command.cli import create_cli
from paji.app.command.manager import Manager
from paji.domain.command import use_cases
from paji.infrastructure.command import helpers


class Container(containers.DeclarativeContainer):
    WSGIServerHelper = providers.Factory(
        helpers.WSGIServerHelper,
    )

    RunPajiServerUseCase = providers.Factory(
        use_cases.RunPajiServerUseCase,
        wsgi_server_helper=WSGIServerHelper,
    )

    Manager = providers.Factory(
        Manager,
        run_paji_server_use_case=RunPajiServerUseCase
    )

    create_cli = providers.Callable(
        create_cli,
        Manager,
    )
