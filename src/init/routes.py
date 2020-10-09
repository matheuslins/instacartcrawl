from aiohttp import web

from src.core.home import home


routes = [
    web.get('/', home)
]
