from aiohttp import ClientSession


class RequestHandler:
    headers = {}
    cookies = {}

    def __init__(self, headers=None, cookies=None):
        self.headers = headers
        self.cookies = cookies

    @staticmethod
    async def make_request(**kwargs):
        async with ClientSession() as session:
            async with session.request(**kwargs) as resp:
                return {
                    "status": resp.status,
                    "text": await resp.text(),
                    "raw": resp
                }
