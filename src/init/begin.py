from aiohttp import web

from src.init.routes import routes
from src.spiders.instacart import InstaCartSpider


def run():
    app = web.Application()
    app.add_routes(routes=routes)
    app.router.add_view("/instacart", InstaCartSpider)
    web.run_app(app)



