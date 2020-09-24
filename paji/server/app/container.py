import flask
import waitress
from dependency_injector import containers, providers
from dependency_injector.ext import flask as flask_ext

from paji.server.app import paji_server, flask_extensions
from paji.server.app.flask_extensions.routes_ext.routes import demo, internal
from paji.server.domain import use_cases
from paji.server.infrastructure import helpers


class ServerContainer(containers.DeclarativeContainer):
    # flask application
    FlaskApp = providers.Singleton(flask.Flask, __name__)

    # helpers
    WSGIServerHelper = providers.Factory(
        helpers.WSGIServerHelper,
        wsgi_application_prod_serve_func=waitress.serve,
    )

    FlaskHelper = providers.Factory(
        helpers.FlaskHelper,
        flask_app=FlaskApp,
    )

    # use_cases
    GetAllRoutesUseCase = providers.Factory(
        use_cases.GetAllRoutesUseCase,
        flask_helper=FlaskHelper,
    )

    # views
    GetAllRoutesView = flask_ext.ClassBasedView(
        internal.GetAllRoutesView,
        get_all_routes_use_case=GetAllRoutesUseCase,
    )
    SayHelloView = flask_ext.ClassBasedView(
        demo.SayHelloView,
    )

    # flask extensions
    RoutesExt = flask_ext.Extension(
        flask_extensions.RoutesExt,
        get_all_routes_class=GetAllRoutesView.provider,
        say_hello_view_class=SayHelloView.provider,
    )

    # paji server
    PAJIServer = providers.Factory(
        paji_server.PAJIServer,
        flask_app=FlaskApp,
        routes_ext=RoutesExt,
        wsgi_server_helper=WSGIServerHelper,
    )
