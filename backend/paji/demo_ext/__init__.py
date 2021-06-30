import flask

from paji.demo_ext.say_hello_view import SayHelloView


class DemoExt:

    @classmethod
    def init_app(cls, app: flask.Flask):
        with app.app_context():
            blueprint = flask.Blueprint('demo', __name__, url_prefix='/api/demo')
            blueprint.add_url_rule('/hello', view_func=SayHelloView.as_view('hello'), methods=['GET'])
            app.register_blueprint(blueprint)
