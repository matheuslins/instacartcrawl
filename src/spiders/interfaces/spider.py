import asyncio
from abc import ABCMeta, abstractmethod
from aiohttp import web
from http import HTTPStatus

from src.core.request import RequestHandler


class BaseSpider(web.View, metaclass=ABCMeta):
    response = None
    spider_name = None

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
        response = await request_handler.make_session_request(
            method="GET",
            url=self.get_start_url()
        )
        self.response = response["text"]

    async def run(self):
        await self.request_initial_page()
        await self.start_consult(self.response)

        _ = asyncio.create_task(self.start_extract())

        return web.json_response({
            "task": f"extract-data-{self.spider_name}",
            "status": HTTPStatus.OK
        })
