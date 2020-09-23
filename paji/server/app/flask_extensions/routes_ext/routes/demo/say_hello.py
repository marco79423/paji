import flask.views


class SayHelloView(flask.views.MethodView):

    def get(self):
        name = flask.request.args.get('name', '陌生人')
        return f'哈囉 {name}'
