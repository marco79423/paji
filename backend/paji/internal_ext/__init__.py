import flask

from paji.internal_ext.get_all_routes import GetAllRoutesView


class InternalExt:

    @classmethod
    def init_app(cls, app: flask.Flask):
        with app.app_context():
            """設定內部相關路由"""
            blueprint = flask.Blueprint('internal', __name__, url_prefix='/api/internal')
            blueprint.add_url_rule('/routes',
                                   view_func=GetAllRoutesView.as_view('get_all_routes'),
                                   methods=['GET'])
            app.register_blueprint(blueprint)
