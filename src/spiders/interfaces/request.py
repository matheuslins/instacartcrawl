from aiohttp import web

import asyncio
from aiohttp import ClientSession


class SpiderInterface:
    def start_url(self):
        pass

    @staticmethod
    async def _initial_request(*, session, url):
        async with session.get(url) as resp:
            return await resp.text()

    async def run(self, request):
        async with ClientSession() as session:
            response = await asyncio.create_task(
                self._initial_request(session=session, url=self.start_url())
            )
            with open("dump.html", "w") as file:
                file.write(response)
            return web.Response(text="Baixou o site!")
