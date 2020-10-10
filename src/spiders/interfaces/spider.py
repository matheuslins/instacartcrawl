import asyncio
from abc import ABCMeta, abstractmethod
from aiohttp import web
from aiohttp import ClientSession


class BaseSpiderInterface(web.View, metaclass=ABCMeta):
    response = None

    @abstractmethod
    def get_start_url(self):
        raise NotImplementedError

    @abstractmethod
    async def start_crawl(self, response):
        raise NotImplementedError

    @staticmethod
    async def _initial_request(*, session, url):
        async with session.get(url) as resp:
            return await resp.text()

    async def request_initial_page(self):
        async with ClientSession() as session:
            self.response = await asyncio.create_task(
                self._initial_request(
                    session=session, url=self.get_start_url()
                )
            )

    async def run(self, request):
        await self.request_initial_page()
        await self.start_crawl(self.response)
        return web.Response(text="Starting crawling...")
