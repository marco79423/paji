import logging

import flask
import flask_cors
import waitress

from paji.jessigod_ext import JessigodExt
from paji.config_ext import ConfigExt
from paji.db_backup_ext import DBBackupExt
from paji.demo_ext import DemoExt
from paji.internal_ext import InternalExt
from paji.jessiclient_ext import JessiclientExt


class Server:

    def __init__(self):
        self._flask_app = flask.Flask(__name__)

        self._setup_extensions()

    def get_app(self):
        return self._flask_app

    def serve(self, host: str, port: int, is_dev: bool):
        # 設定環境
        logging.basicConfig(
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S',
            format='[%(asctime)s][%(levelname)s] %(message)s',
        )

        if is_dev:
            self._flask_app.logger.setLevel(logging.DEBUG)
            self._flask_app.run(host=host, port=port, debug=True)
        else:
            waitress.serve(self._flask_app, host=host, port=port)

    def _setup_extensions(self):
        flask_cors.CORS(self._flask_app, origins=[
            r'http://localhost:\d+',
            r'https://[^.]*.?marco79423.net',
        ])

        ConfigExt(self._flask_app)
        InternalExt(self._flask_app)
        DemoExt(self._flask_app)
        DBBackupExt(self._flask_app)
        JessiclientExt(self._flask_app)
        JessigodExt(self._flask_app)
