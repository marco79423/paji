import flask.views
from flask import current_app

from paji.internal_ext import entities


class GetAllRoutesView(flask.views.MethodView):

    def get(self):
        routes = []
        for rule in current_app.url_map.iter_rules():
            routes.append(entities.Route(
                methods=rule.methods,
                endpoint=rule.endpoint,
                path=rule.rule
            ))

        return flask.jsonify([
            route.serialize() for route in routes
        ])
