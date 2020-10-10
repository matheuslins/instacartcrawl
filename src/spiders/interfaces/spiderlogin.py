from aiohttp import ClientSession

from src.spiders.interfaces.spider import BaseSpider
from src.core.login import LoginHandler
from src.core.request import RequestHandler

from src.settings import SPIDERS_CONSTANTS


class SpiderLoginInterface(BaseSpider, LoginHandler):
    start_url = None

    def get_start_url(self):
        return self.start_url

    @staticmethod
    async def make_login():
        async with ClientSession() as session:
            request_handler = RequestHandler()
            response = await request_handler.make(
                session=session,
                url=SPIDERS_CONSTANTS["instacart"]["LOGIN_URL"],
                method="post"
            )
            print(response)

    async def extract_data(self):
        pass

    async def start_crawl(self, response):
        self.start_login()
        await self.make_login()
        await self.extract_data()
