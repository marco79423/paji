import flask
from dependency_injector import containers, providers
from dependency_injector.ext import flask as flask_ext

from paji.server.app import paji_server
from paji.server.infrastructure import helpers


class ServerContainer(containers.DeclarativeContainer):
    WSGIServerHelper = providers.Factory(
        helpers.WSGIServerHelper,
    )

    FlaskApp = flask_ext.Application(flask.Flask, __name__)

    PAJIServer = providers.Factory(
        paji_server.PAJIServer,
        flask_app=FlaskApp,
        wsgi_server_helper=WSGIServerHelper,
    )
