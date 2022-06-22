import logging
import pathlib

import fastapi
import uvicorn
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi.middleware.cors import CORSMiddleware
from omegaconf import OmegaConf
from paji_sdk.base.exceptions import NotFoundError

from paji.service.db_backup import DBBackupService


class Server:
    CONFIG_FOLDER = pathlib.Path('./conf.d')
    CONFIG_FILE_PATH = CONFIG_FOLDER / 'config.yml'

    def serve(self, host: str, port: int, is_dev: bool):
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

        # 設定 Scheduler
        scheduler = BackgroundScheduler()
        scheduler.start()

        app = fastapi.FastAPI()
        app.state.config = config
        app.state.logger = logging.getLogger()
        app.state.scheduler = scheduler

        # 設定第三方擴充
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[
            ],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # 設定並啟動服務
        if config.services.db_backup:
            serv = DBBackupService(app)
            serv.setup()

        uvicorn.run(app, host=host, port=port)
