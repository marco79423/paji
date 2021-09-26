class DBBackupConfig:
    def __init__(self, base_config, config):
        self._base_config = base_config
        self._config = config

    @property
    def timezone(self):
        return self._base_config.server.timezone

    @property
    def backup_plans(self):
        return [BackupPlanConfig(self._base_config, backup_plan_config) for backup_plan_config in
                self._config.backup_plans]


class BackupPlanConfig:
    def __init__(self, base_config, config):
        self._base_config = base_config
        self._config = config

    @property
    def name(self):
        return self._config.name

    @property
    def schedule(self):
        return self._config.schedule

    @property
    def source_database(self):
        return SourceDatabaseConfig(self._base_config, self._config.source_database)

    @property
    def backup_storage(self):
        return self._config.backup_storage


class SourceDatabaseConfig:
    def __init__(self, base_config, config):
        self._base_config = base_config
        self._config = config

    @property
    def type(self):
        return self._config.type

    @property
    def connection(self):
        return DatabaseConnectionConfig(self._base_config, self._config.connection)

    @property
    def database_names(self):
        return self._config.database_names

class DatabaseConnectionConfig:
    def __init__(self, base_config, config):
        self._base_config = base_config
        self._config = config

    @property
    def project_id(self):
        return self._config.project_id

    @property
    def zone(self):
        return self._config.zone

    @property
    def cluster_id(self):
        return self._config.cluster_id

    @property
    def service_account_file(self):
        return self._base_config.CONFIG_FOLDER / self._config.service_account_file

    @property
    def namespace(self):
        return self._config.namespace

    @property
    def pod_name_pattern(self):
        return self._config.pod_name_pattern

    @property
    def account(self):
        return self._config.account

    @property
    def password(self):
        return self._config.password
