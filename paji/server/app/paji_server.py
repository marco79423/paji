import abc

import flask

from paji.server.domain import helpers


class PAJIServerBase(abc.ABC):

    @abc.abstractmethod
    def serve(self, host: str, port: int, is_dev: bool):
        pass


class PAJIServer(PAJIServerBase):

    def __init__(self,
                 flask_app: flask.Flask,
                 wsgi_server_helper: helpers.WSGIServerHelperBase,
                 ):
        self._flask_app = flask_app
        self._wsgi_server_helper = wsgi_server_helper

    def serve(self, host: str, port: int, is_dev: bool):
        self._wsgi_server_helper.serve(
            app=self._flask_app,
            host=host,
            port=port,
            is_dev=is_dev,
        )
