import flask.views


class GetRootView(flask.views.MethodView):

    def get(self):
        return '啪……啪唧！'
