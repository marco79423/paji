import logging
import pathlib

import flask
import flask_cors
import redis
import waitress
from apscheduler.schedulers.background import BackgroundScheduler
from omegaconf import OmegaConf
from paji_sdk.base.exceptions import NotFoundError

from paji.service.db_backup import DBBackupService
from paji.service.jessiclient import JessiclientService


class Server:
    CONFIG_FOLDER = pathlib.Path('./conf.d')
    CONFIG_FILE_PATH = CONFIG_FOLDER / 'config.yml'

    def serve(self, host: str, port: int, is_dev: bool):
        flask_app = flask.Flask(__name__)

        # 設定設定檔
        try:
            config = OmegaConf.load(self.CONFIG_FILE_PATH)
            config.merge_with({
                'app': {
                    'config_folder': str(self.CONFIG_FOLDER)
                }
            })
        except FileNotFoundError:
            raise NotFoundError(f'設定檔 {self.CONFIG_FILE_PATH} 不存在 ')

        # 設定環境
        logging.basicConfig(
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S',
            format='[%(asctime)s][%(levelname)s] %(message)s',
        )

        # 設定第三方擴充
        flask_cors.CORS(flask_app, origins=[
            r'http://localhost:\d+',
            r'https://[^.]*.?marco79423.net',
        ])

        # 設定 Scheduler
        scheduler = BackgroundScheduler()
        scheduler.start()

        # 設定 cache client
        redis_client = redis.Redis(
            host=config.cache.redis.host,
            port=config.cache.redis.port,
        )

        # 設定並啟動服務
        if config.services.jessiclient:
            serv = JessiclientService(flask_app, config, redis_client)
            serv.start()

        if config.services.db_backup:
            serv = DBBackupService(flask_app, config, scheduler)
            serv.start()

        if is_dev:
            flask_app.logger.setLevel(logging.DEBUG)
            flask_app.run(host=host, port=port, debug=True)
        else:
            waitress.serve(flask_app, host=host, port=port)
