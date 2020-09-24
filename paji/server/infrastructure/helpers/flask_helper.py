from typing import List

import flask

from paji.server.domain import entities, helpers


class FlaskHelper(helpers.FlaskHelperBase):
    def __init__(self, flask_app: flask.Flask):
        self._flask_app = flask_app

    def get_all_routes(self) -> List[entities.Route]:
        routes = []
        for rule in self._flask_app.url_map.iter_rules():
            routes.append(entities.Route(
                methods=rule.methods,
                endpoint=rule.endpoint,
                path=rule.rule
            ))
        return routes
