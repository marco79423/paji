import flask
from dependency_injector import containers, providers
from dependency_injector.ext import flask as flask_ext

from paji.server.app import paji_server, flask_extensions
from paji.server.app.flask_extensions.routes_ext.routes import demo
from paji.server.infrastructure import helpers


class ServerContainer(containers.DeclarativeContainer):
    # helpers
    WSGIServerHelper = providers.Factory(
        helpers.WSGIServerHelper,
    )

    # views
    SayHelloView = flask_ext.ClassBasedView(
        demo.SayHelloView,
    )

    # flask application
    FlaskApp = flask_ext.Application(flask.Flask, __name__)

    # flask extensions
    RoutesExt = flask_ext.Extension(
        flask_extensions.RoutesExt,
        say_hello_view_class=SayHelloView.provider,
    )

    # paji server
    PAJIServer = providers.Factory(
        paji_server.PAJIServer,
        flask_app=FlaskApp,
        routes_ext=RoutesExt,
        wsgi_server_helper=WSGIServerHelper,
    )
