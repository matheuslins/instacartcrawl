from src.spiders.interfaces.spiderlogin import SpiderLoginInterface
from src.settings import SPIDERS_CONSTANTS


class InstaCartSpider(SpiderLoginInterface):

    start_url = SPIDERS_CONSTANTS["instacart"]["START_URL"]

    def __init__(self, *args, **kwargs):
        super(InstaCartSpider, self).__init__(*args, **kwargs)
        self.set_extraction_keys()

    async def get(self):
        return await self.run(self.request)

    def set_extraction_keys(self):
        self.keys_to_extract = {
            "captcha": {
                "params": {"name": "script", "attrs": {"id": "node-gon"}},
                "method_to_extract": self.get_by_json
            },
            "authenticity_token": {
                "params": {"name": "meta", "attrs": {"name": "csrf-token"}},
                "method_to_extract": self.get_by_meta
            }
        }

    @staticmethod
    def get_by_json(data):
        return None

    @staticmethod
    def get_by_meta(data):
        if not data:
            return None
        return data[0]["content"]
