import logging

import flask

from paji.server.domain import helpers


class WSGIServerHelper(helpers.WSGIServerHelperBase):

    def serve(self, app, host: str, port: int, is_dev: bool):
        if is_dev:
            if isinstance(app, flask.Flask):
                app.logger.setLevel(logging.DEBUG)
                app.run(host=host, port=port, debug=True)
            else:
                raise NotImplementedError
        else:
            raise NotImplementedError
