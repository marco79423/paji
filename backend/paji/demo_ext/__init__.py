import flask

from paji.demo_ext.say_hello_view import SayHelloView


class DemoExt:

    def __init__(self, app: flask.Flask):
        self.init_app(app)

    def init_app(self, app: flask.Flask):
        with app.app_context():
            blueprint = flask.Blueprint('demo', __name__, url_prefix='/api/demo')
            blueprint.add_url_rule('/hello', view_func=SayHelloView.as_view('hello'), methods=['GET'])
            app.register_blueprint(blueprint)
