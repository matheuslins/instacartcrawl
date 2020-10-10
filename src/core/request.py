

class RequestHandler:
    headers = {}
    cookies = {}

    async def post_request(self, session, url):
        async with session.post(url, cookies=self.cookies, headers=self.headers) as resp:
            return await resp.text()

    async def make(self, session, url, method=None):
        if method and method == "post":
            await self.post_request(session, url)
        else:
            async with session.get(url, cookies=self.cookies, headers=self.headers) as resp:
                return await resp.text()
