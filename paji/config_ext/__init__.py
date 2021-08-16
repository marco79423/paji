import flask
from omegaconf import OmegaConf


class ConfigExt:

    def __init__(self, app: flask.Flask):
        self.init_app(app)

    def init_app(self, app: flask.Flask):
        app.config.update({
            'app': OmegaConf.load('./config.yml'),
        })
