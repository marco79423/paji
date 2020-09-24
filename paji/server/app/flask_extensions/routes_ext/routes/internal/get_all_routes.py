import flask.views

from paji.server.domain import use_cases


class GetAllRoutesView(flask.views.MethodView):

    def __init__(self, get_all_routes_use_case: use_cases.GetAllRoutesUseCase):
        self._get_all_routes_use_case = get_all_routes_use_case

    def get(self):
        return flask.jsonify([
            route.serialize() for route in self._get_all_routes_use_case.execute()
        ])
