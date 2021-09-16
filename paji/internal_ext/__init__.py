import flask

from paji.internal_ext.get_all_routes import GetAllRoutesView


class InternalExt:

    def __init__(self, app: flask.Flask):
        self.init_app(app)

    def init_app(self, app: flask.Flask):
        with app.app_context():
            """設定內部相關路由"""
            blueprint = flask.Blueprint('internal', __name__, url_prefix='/_')
            blueprint.add_url_rule('/routes',
                                   view_func=GetAllRoutesView.as_view('get_all_routes'),
                                   methods=['GET'])
            app.register_blueprint(blueprint)
