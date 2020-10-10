import asyncio
from abc import ABCMeta, abstractmethod
from aiohttp import web
from aiohttp import ClientSession

from src.core.request import RequestHandler


class BaseSpider(web.View, metaclass=ABCMeta):
    response = None

    @abstractmethod
    def get_start_url(self):
        raise NotImplementedError

    @abstractmethod
    async def start_crawl(self, response):
        raise NotImplementedError

    @abstractmethod
    async def extract_data(self):
        raise NotImplementedError

    async def request_initial_page(self):
        request_handler = RequestHandler()

        async with ClientSession() as session:
            self.response = await asyncio.create_task(
                request_handler.make(session=session, url=self.get_start_url())
            )

    async def run(self, request):
        await self.request_initial_page()
        await self.start_crawl(self.response)
        return web.Response(text="Starting crawling...")
