import asyncio

from abc import ABCMeta, abstractmethod
from aiohttp import web

from src.core.request import RequestHandler


class BaseSpider(web.View, metaclass=ABCMeta):
    response = None

    @abstractmethod
    def get_start_url(self):
        raise NotImplementedError

    @abstractmethod
    async def start_consult(self, response):
        raise NotImplementedError

    @abstractmethod
    async def start_extract(self):
        raise NotImplementedError

    @abstractmethod
    def save_item(self, file_name):
        raise NotImplementedError

    async def request_initial_page(self):
        request_handler = RequestHandler()
        task_response = await asyncio.create_task(
            request_handler.make_request(method="GET", url=self.get_start_url())
        )
        self.response = task_response["text"]

    async def run(self, request):
        await self.request_initial_page()
        await self.start_consult(self.response)
        await self.start_extract()
        return web.Response(text="Starting crawling...")
