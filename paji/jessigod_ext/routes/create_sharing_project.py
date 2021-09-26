import hashlib
import json

import flask.views


class CreateSharingProjectView(flask.views.MethodView):

    def __init__(self, config, redis_client):
        super().__init__()

        self._config = config
        self._redis_client = redis_client

    def post(self):
        request_body = flask.request.data

        m = hashlib.md5()
        m.update(request_body)
        project_code = m.hexdigest()

        self._redis_client.set(f'jessiclient:projects:{project_code}', request_body, self._config.sharing.project.expired_time)
        return {
            'data': {
                'projectCode': project_code,
            },
        }
