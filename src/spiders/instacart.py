from aiohttp import web

from src.spiders.interfaces.request import SpiderInterface
from src.settings import TALKER_SETTINGS


class InstaCartSpider(SpiderInterface, web.View):

    async def get(self):
        return await self.run(self.request)

    def start_url(self):
        return TALKER_SETTINGS["instacart"]["START_URL"]

