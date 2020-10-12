import asyncio
from abc import ABCMeta, abstractmethod
from aiohttp import web
from http import HTTPStatus

from src.core.request import RequestHandler
from src.core.logging import LoggerHandler


class BaseSpider(LoggerHandler, web.View, metaclass=ABCMeta):
    response = None

    def __init__(self, *args, **kwargs):
        super(BaseSpider, self).__init__(*args, **kwargs)
        self.set_base_config()

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
        self.log.info("Initial page request...")
        request_handler = RequestHandler()
        response = await request_handler.make_session_request(
            method="GET",
            url=self.get_start_url()
        )
        self.response = response["text"]
        self.log.info("Got initial page text")

    async def run(self):
        await self.request_initial_page()
        await self.start_consult(self.response)

        _ = asyncio.create_task(self.start_extract())

        return web.json_response({
            "task": f"extract-data-{self.spider_name}",
            "status": HTTPStatus.OK
        })
