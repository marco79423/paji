import pathlib

import flask
from omegaconf import OmegaConf

from paji.config_ext.db_backup_config import DBBackupConfig


class ConfigExt:
    CONFIG_FOLDER = pathlib.Path('./conf.d')

    def __init__(self, app: flask.Flask):
        self._config = None

        self.init_app(app)

    def init_app(self, app: flask.Flask):
        self._config = OmegaConf.load(self.CONFIG_FOLDER / 'config.yml')

        app.config.update({
            'config': self,
        })

    @property
    def db_backup(self):
        return DBBackupConfig(self, self._config.db_backup)
