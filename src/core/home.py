from aiohttp import web


async def home(request):
    return web.Response(text="Welcome Crawl Framework!")
