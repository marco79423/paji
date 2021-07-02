import logging

import flask
import waitress

from paji.demo_ext import DemoExt
from paji.internal_ext import InternalExt


class Server:

    def __init__(self):
        self._flask_app = flask.Flask(__name__)

        self._setup_extensions()

    def get_app(self):
        return self._flask_app

    def serve(self, host: str, port: int, is_dev: bool):
        if is_dev:
            self._flask_app.logger.setLevel(logging.DEBUG)
            self._flask_app.run(host=host, port=port, debug=True)
        else:
            waitress.serve(self._flask_app, host=host, port=port)

    def _setup_extensions(self):
        DemoExt(self._flask_app)
        InternalExt(self._flask_app)
