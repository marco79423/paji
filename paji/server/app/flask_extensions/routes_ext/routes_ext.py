import abc
from typing import Type

import flask

from paji.server.app.flask_extensions.routes_ext.routes import demo, internal, root


class RoutesExtBase(abc.ABC):

    @abc.abstractmethod
    def init_app(self, app: flask.Flask):
        pass


class RoutesExt(RoutesExtBase):
    """設定 paji 的路由"""

    def __init__(self,
                 # 根
                 get_root_view_class: Type[root.GetRootView],
                 # 內部相關
                 get_all_routes_class: Type[internal.GetAllRoutesView],
                 # DEMO 相關
                 say_hello_view_class: Type[demo.SayHelloView],
                 ):
        self._get_root_view_class = get_root_view_class
        self._get_all_routes_class = get_all_routes_class
        self._say_hello_view_class = say_hello_view_class

    def init_app(self, app: flask.Flask):
        with app.app_context():
            self._set_root_route(app)
            self._set_internal_routes(app)
            self._set_demo_routes(app)

    def _set_root_route(self, app: flask.Flask):
        """設定根路由"""
        app.add_url_rule('/', view_func=self._get_root_view_class.as_view('get_root'), methods=['GET'])

    def _set_internal_routes(self, app: flask.Flask):
        """設定內部相關路由"""
        blueprint = flask.Blueprint('internal', __name__, url_prefix='/internal')
        blueprint.add_url_rule('/routes',
                               view_func=self._get_all_routes_class.as_view('get_all_routes'),
                               methods=['GET'])
        app.register_blueprint(blueprint)

    def _set_demo_routes(self, app: flask.Flask):
        """設定 DEMO 相關路由"""
        blueprint = flask.Blueprint('demo', __name__, url_prefix='/demo')
        blueprint.add_url_rule('/hello', view_func=self._say_hello_view_class.as_view('hello'), methods=['GET'])
        app.register_blueprint(blueprint)
