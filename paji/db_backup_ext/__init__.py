import flask
from apscheduler.schedulers.background import BackgroundScheduler


class DBBackupExt:

    def __init__(self, app: flask.Flask):
        self.init_app(app)

    def init_app(self, app: flask.Flask):
        scheduler = BackgroundScheduler()
        scheduler.start()

        print('aaaaa', app.config['app'].db_backup.backup_plan.schedules)

    def backup_mysql_to_backup_storage(self):
        pass
