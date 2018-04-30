from aiohttp import web
import asyncio
from .route import setup_route


loop = asyncio.get_event_loop()
app = web.Application(loop=loop)
setup_route(app)
web.run_app(app, port=8080)