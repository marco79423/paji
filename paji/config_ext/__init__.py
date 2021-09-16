import pathlib

import flask
from omegaconf import OmegaConf
from paji_sdk.base.exceptions import NotFoundError

from paji.config_ext.db_backup_config import DBBackupConfig
from paji.config_ext.jessiclient_config import JessiclientConfig


class ConfigExt:
    CONFIG_FOLDER = pathlib.Path('./conf.d')
    CONFIG_FILE_PATH = CONFIG_FOLDER / 'config.yml'

    def __init__(self, app: flask.Flask):
        self._config = None

        self.init_app(app)

    def init_app(self, app: flask.Flask):
        try:
            self._config = OmegaConf.load(self.CONFIG_FILE_PATH)
        except FileNotFoundError:
            raise NotFoundError(f'設定檔 {self.CONFIG_FILE_PATH} 不存在 ')

        app.config.update({
            'config': self,
        })

    @property
    def db_backup(self):
        if not self._config.db_backup:
            return None
        return DBBackupConfig(self, self._config.db_backup)

    @property
    def jessiclient(self):
        if not self._config.jessiclient:
            return None
        return JessiclientConfig(self, self._config.jessiclient)
