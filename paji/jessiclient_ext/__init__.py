import flask
import redis

from paji.jessiclient_ext.routes import GetSharingProjectView
from paji.jessiclient_ext.routes.create_sharing_project import CreateSharingProjectView


class JessiclientExt:

    def __init__(self, app: flask.Flask):
        self.app = None

        self.init_app(app)

    def init_app(self, app: flask.Flask):
        self.app = app

        config = app.config['config'].jessiclient
        if not config:
            app.logger.info('放棄啟動 Jessiclient： 不存在必要的設定檔')
            return

        redis_client = redis.Redis(
            host=config.redis.host,
            port=config.redis.port,
        )

        with app.app_context():
            """設定 Jessiclient 相關路由"""
            blueprint = flask.Blueprint('jessiclient', __name__, url_prefix='/api/jessiclient')
            blueprint.add_url_rule('/sharing/projects',
                                   view_func=CreateSharingProjectView.as_view('create_sharing_project', config, redis_client),
                                   methods=['POST'])
            blueprint.add_url_rule('/sharing/projects/<project_code>',
                                   view_func=GetSharingProjectView.as_view('get_sharing_project', config, redis_client),
                                   methods=['GET'])
            app.register_blueprint(blueprint)

        app.logger.info('啟動 Jessiclient 成功')
