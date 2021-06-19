import abc

import flask

from paji.server.app import flask_extensions
from paji.server.domain import helpers


class PAJIServerBase(abc.ABC):

    @abc.abstractmethod
    def get_app(self):
        pass

    @abc.abstractmethod
    def serve(self, host: str, port: int, is_dev: bool):
        pass


class PAJIServer(PAJIServerBase):

    def __init__(self,
                 flask_app: flask.Flask,
                 routes_ext: flask_extensions.RoutesExtBase,
                 wsgi_server_helper: helpers.WSGIServerHelperBase,
                 ):
        self._flask_app = flask_app
        self._routes_ext = routes_ext
        self._wsgi_server_helper = wsgi_server_helper

        self._setup_extensions()

    def get_app(self):
        return self._flask_app

    def serve(self, host: str, port: int, is_dev: bool):
        self._wsgi_server_helper.serve(
            app=self._flask_app,
            host=host,
            port=port,
            is_dev=is_dev,
        )

    def _setup_extensions(self):
        # 設定路由
        self._routes_ext.init_app(self._flask_app)
