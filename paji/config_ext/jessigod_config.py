class JessigodConfig:
    def __init__(self, base_config, config):
        self._base_config = base_config
        self._config = config

    @property
    def timezone(self):
        return self._base_config.server.timezone

    @property
    def database_url(self):
        return self._config.database_url

    @property
    def admin_token(self):
        return self._config.database_url

    @property
    def bots(self):
        return self._config.bots

    @property
    def preacher(self):
        return self._config.preacher
