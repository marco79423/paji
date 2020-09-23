import abc
from typing import Type

import flask

from paji.server.app.flask_extensions.routes_ext.routes import demo


class RoutesExtBase(abc.ABC):

    @abc.abstractmethod
    def init_app(self, app: flask.Flask):
        pass


class RoutesExt(RoutesExtBase):
    """設定 paji 的路由"""

    def __init__(self,
                 say_hello_view_class: Type[demo.SayHelloView],
                 ):
        self._say_hello_view_class = say_hello_view_class

    def init_app(self, app: flask.Flask):
        # DEMO 相關路由
        with app.app_context():
            blueprint = flask.Blueprint('demo', __name__, url_prefix='/demo')
            blueprint.add_url_rule('/hello', view_func=self._say_hello_view_class.as_view('hello'), methods=['GET'])
            app.register_blueprint(blueprint)
