import json

import flask.views


class GetSharingProjectView(flask.views.MethodView):

    def __init__(self, config, redis_client):
        super().__init__()

        self._config = config
        self._redis_client = redis_client

    def get(self, project_code):
        data = self._redis_client.get(f'jessiclient:projects:{project_code}')
        if not data:
            return flask.jsonify({
                'error': 'project 不存在'
            }), 404

        project = json.loads(data)
        return {
            'data': project,
        }
