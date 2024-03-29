import copy
import datetime as dt
import os

import pytz
from apscheduler.triggers.cron import CronTrigger
from paji_sdk.base.exceptions import DataError

from paji.service.base import ServiceBase
from paji.service.db_backup.gke_mysql_client import GKEMysqlClient
from paji.service.db_backup.storage import DropboxStorage


class DBBackupService(ServiceBase):

    def setup(self):
        for backup_plan in self.config.services.db_backup.backup_plans:
            trigger = CronTrigger.from_crontab(backup_plan.schedule, timezone=pytz.timezone(self.config.server.timezone))
            self.scheduler.add_job(
                self.handle_backup_task,
                trigger,
                [self.config, backup_plan]
            )
            self.logger.info(f'啟動 Backup Plan {backup_plan.name} ({trigger}) 成功')

        self.logger.info('啟動 DB Backup 成功')

    def handle_backup_task(self, config, backup_plan):
        self.logger.info(f'開始執行 backup_plan {backup_plan.name} ...')

        # 取得資料庫客戶端
        db_client = self._get_database_client(backup_plan.source_database)

        # 取得對應儲存庫客戶端
        backup_storage = self._get_storage_client(backup_plan.backup_storage)
        for database_name in backup_plan.source_database.database_names:
            # 抓取要備份的資料庫的 SQL
            raw_sql = db_client.get_database_sql(database_name)

            if not raw_sql:
                raise DataError('資料庫內容不應為空')

            # 將備份上傳到備份地點
            backup_path = self._generate_backup_path(config, backup_plan, database_name)
            backup_storage.upload(
                path=backup_path,
                data=raw_sql.encode('utf-8'),
            )

    def _get_database_client(self, source_database):
        """取得對應的資料庫客戶端"""
        if source_database.type == 'gke':
            connection_info = copy.deepcopy(source_database.connection)
            connection_info.service_account_file = os.path.join(
                self.config.app.config_folder,
                connection_info.service_account_file,
            )
            return GKEMysqlClient(connection_info)
        else:
            raise ValueError(f'不支援的資料庫 Client {source_database.type}')

    @staticmethod
    def _get_storage_client(backup_storage):
        """取得對應的儲存庫客戶端"""
        if backup_storage.provider == 'dropbox':
            return DropboxStorage(token=backup_storage.token)
        else:
            raise ValueError(f'不支援的儲存庫 {backup_storage.provider}')

    @staticmethod
    def _generate_backup_path(config, backup_plan, database_name):
        """產生備份的檔案名稱"""
        backup_path = backup_plan.backup_storage.file_pattern

        # 取代變數
        backup_path = backup_path.replace('{database_name}', database_name)

        # 取代時間 (處理 strftime 不支援中文編碼的問題)
        now = dt.datetime.now(pytz.timezone(config.server.timezone))
        backup_path = now.strftime(backup_path.encode('unicode_escape').decode('utf-8')).encode('utf-8').decode('unicode_escape')

        return backup_path
