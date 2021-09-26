import flask
import pytz
import telegram
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from paji.jessigod_ext import models
from paji.jessigod_ext.routes.get_origins import GetOriginView


class JessigodExt:

    def __init__(self, app: flask.Flask):
        self.app = None

        self.init_app(app)

    def init_app(self, app: flask.Flask):
        self.app = app

        config = app.config['config'].jessigod
        if not config:
            app.logger.info('放棄啟動 Jessigod： 不存在必要的設定檔')
            return

        # 設定資料庫
        engine = create_engine(
            config.database_url,
            pool_recycle=100,  # 多少時間自動重連 (MySQL 預設會 8 小時踢人)
        )
        models.Base.metadata.create_all(bind=engine)

        SessionLocal = sessionmaker(bind=engine)
        db = SessionLocal()

        # # 設定機器人
        # if config.bots.telegram_bot:
        #     bot = telegram.Bot(config.bots.telegram_bot.token)
        #     bot.set_webhook(config.bots.telegram_bot.url)
        #
        # # 設定排程器
        # scheduler = BackgroundScheduler()
        # scheduler.start()
        #
        # for schedule in config.preacher.schedules:
        #     scheduler.add_job(
        #         config.handle_schedule_task,
        #         CronTrigger.from_crontab(schedule, timezone=pytz.timezone(config.timezone))
        #     )

        with app.app_context():
            """設定 Jessiclient 相關路由"""
            blueprint = flask.Blueprint('jessigod', __name__, url_prefix='/api/jessigod')
            blueprint.add_url_rule('/origins',
                                   view_func=GetOriginView.as_view('get_origins', db),
                                   methods=['GET'])
            app.register_blueprint(blueprint)

        app.logger.info('啟動 Jessigod 成功')
