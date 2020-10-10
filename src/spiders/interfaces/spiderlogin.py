from src.spiders.interfaces.spider import BaseSpiderInterface
from src.core.login import LoginHandler


class SpiderLoginInterface(BaseSpiderInterface, LoginHandler):
    start_url = None

    def get_start_url(self):
        return self.start_url

    async def start_crawl(self, response):
        self.start_login()
        print(self.login_data)
