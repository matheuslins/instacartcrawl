import aiohttp


class TalkerInterface:
    def start_url(self):
        pass

    @staticmethod
    async def _initial_request(*, session, url):
        async with session.get(url) as response:
            return await response.text()

    async def run(self):
        async with aiohttp.ClientSession() as session:
            html = await self._initial_request(session=session, url=self.start_url())
