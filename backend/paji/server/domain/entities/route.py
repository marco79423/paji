from typing import Set

from paji.shared import base_types


class Route(base_types.Entity):

    def __init__(self, methods: Set[str], endpoint: str, path: str):
        self.methods = methods
        self.endpoint = endpoint
        self.path = path

    def serialize(self) -> dict:
        return {
            'methods': list(self.methods),
            'endpoint': self.endpoint,
            'path': self.path,
        }

    def __eq__(self, route):
        if not isinstance(self, route.__class__):
            return False
        return self.methods == route.methods and self.endpoint == route.endpoint and self.path == route.path
