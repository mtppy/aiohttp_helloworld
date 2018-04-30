from aiohttp import web
from .view import handle


def setup_route(app):
    app.add_routes([web.get('/', handle),
                    web.get('/{name}', handle)])
