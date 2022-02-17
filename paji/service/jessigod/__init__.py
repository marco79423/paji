import pytz
import telegram
from apscheduler.triggers.cron import CronTrigger
from sqlalchemy import create_engine

from paji.service.base import ServiceBase
from paji.service.jessigod import core
from paji.service.jessigod.routes import admin, bots, sayings


class JessigodService(ServiceBase):

    def setup(self):
        # 設定 DB
        self._setup_db()

        # 設定機器人
        self._setup_telegram_bot()

        # 設定排程
        self._setup_scheduler()

        # 設定路由
        self._setup_routes()

        self.logger.info('啟動 Jessigod 成功')

    def _setup_db(self):
        jessigod_config = self.config.services.jessigod
        engine = create_engine(jessigod_config.database_url)
        models.Base.metadata.create_all(bind=engine)

    def _setup_telegram_bot(self):
        telegram_bot_config = self.config.services.jessigod.bots.telegram_bot
        if telegram_bot_config:
            bot = telegram.Bot(telegram_bot_config.token)
            bot.set_webhook(telegram_bot_config.url)

    def _setup_scheduler(self):
        jessigod_config = self.config.services.jessigod
        for schedule in jessigod_config.preacher.schedules:
            trigger = CronTrigger.from_crontab(schedule, timezone=pytz.timezone(self.config.server.timezone))
            self.scheduler.add_job(
                core.handle_schedule_task,
                trigger,
                [jessigod_config],
            )

    def _setup_routes(self):
        self.app.include_router(admin.router)
        self.app.include_router(sayings.router)
        self.app.include_router(bots.router)
