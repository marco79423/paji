import flask.views

from paji.jessigod_ext import models


class GetOriginView(flask.views.MethodView):

    def __init__(self, db):
        super().__init__()
        self._db = db

    def get(self):
        origins = self._db.query(models.Origin).all()

        return flask.jsonify({
            'data': [
                {
                    'id': origin.id,
                    'name': origin.name,
                } for origin in origins
            ]
        })
