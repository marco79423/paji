class JessiclientConfig:
    def __init__(self, base_config, config):
        self._base_config = base_config
        self._config = config

    @property
    def redis(self):
        return self._config.redis

    @property
    def sharing(self):
        return self._config.sharing
