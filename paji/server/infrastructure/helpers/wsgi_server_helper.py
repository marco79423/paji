import logging
from typing import Callable

import flask
from paji.server.domain import helpers


class WSGIServerHelper(helpers.WSGIServerHelperBase):

    def __init__(self,
                 wsgi_application_prod_serve_func: Callable
                 ):
        self._wsgi_application_prod_serve_func = wsgi_application_prod_serve_func

    def serve(self, app, host: str, port: int, is_dev: bool):
        if is_dev:
            if isinstance(app, flask.Flask):
                app.logger.setLevel(logging.DEBUG)
                app.run(host=host, port=port, debug=True)
            else:
                raise NotImplementedError
        else:
            self._wsgi_application_prod_serve_func(app, host=host, port=port)
