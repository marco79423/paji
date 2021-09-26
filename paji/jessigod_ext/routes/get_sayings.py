import flask.views

from paji.jessigod_ext import models


class GetSayingsView(flask.views.MethodView):

    def __init__(self, db):
        super().__init__()
        self._db = db

    def get(self):
        # search_term = flask.request.openapi.parameters.query.get('searchTerm')
        # page_index = flask.request.openapi.parameters.query.get('pageIndex', 1)
        # page_size = flask.request.openapi.parameters.query.get('pageSize', None)

        q = self._db.query(models.Saying)

        if token and editor_only:
            editor = get_or_create_editor(db, token)
            q = q.filter_by(editor_id=editor.id)

        if origin:
            q = q.join(models.Saying.origin).filter(models.Origin.name == origin)

        q = q.order_by(models.Saying.created_at.desc())




        origins = self._db.query(models.Origin).all()

        return flask.jsonify({
            'data': [
                {
                    'id': origin.id,
                    'name': origin.name,
                } for origin in origins
            ]
        })
