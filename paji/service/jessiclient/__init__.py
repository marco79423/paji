import flask

from paji.service.base import ServiceBase
from paji.service.jessiclient.routes import CreateSharingProjectView
from paji.service.jessiclient.routes import GetSharingProjectView


class JessiclientService(ServiceBase):

    def __init__(self, app, config, redis_client):
        self.app = app
        self.config = config

        self.redis_client = redis_client

    def start(self):
        with self.app.app_context():
            """設定 Jessiclient 相關路由"""
            blueprint = flask.Blueprint('jessiclient', __name__, url_prefix='/api/jessiclient')
            blueprint.add_url_rule('/sharing/projects',
                                   view_func=CreateSharingProjectView.as_view(
                                       'create_sharing_project',
                                       self.config,
                                       self.redis_client
                                   ),
                                   methods=['POST'])
            blueprint.add_url_rule('/sharing/projects/<project_code>',
                                   view_func=GetSharingProjectView.as_view(
                                       'get_sharing_project',
                                       self.config,
                                       self.redis_client
                                   ),
                                   methods=['GET'])
            self.app.register_blueprint(blueprint)

        self.app.logger.info('啟動 Jessiclient 成功')
