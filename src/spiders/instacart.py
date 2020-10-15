import json

from src.settings import SPIDERS_SETTINGS
from src.core.spiders.instacart import InstacartBusiness
from src.core.logging import log
from src.spiders.interfaces.spider import BaseSpider
from src.models.instacart.item import InstaCartFileItem


class InstaCartSpider(BaseSpider, InstacartBusiness):

    spider_name = 'instacart'
    start_url = SPIDERS_SETTINGS["instacart"]["START_URL"]

    def __init__(self, *args, **kwargs):
        super(InstaCartSpider, self).__init__(*args, **kwargs)
        self.set_extraction_keys()
        self.set_login_params()

    def get_start_url(self):
        return self.start_url

    async def get(self):
        return await self.run()

    def set_extraction_keys(self):
        self.keys_to_extract = {
            "site_key_captcha": {
                "params": {"name": "script", "attrs": {"id": "node-gon"}},
                "method_to_extract": self.get_by_json
            },
            "authenticity_token": {
                "params": {"name": "meta", "attrs": {"name": "csrf-token"}},
                "method_to_extract": self.get_by_meta
            }
        }

    def set_login_params(self):
        self.login_params = {
            "url": SPIDERS_SETTINGS["instacart"]["LOGIN_URL"],
            "json": {
                "scope": "",
                "grant_type": "password",
                "signup_v3_endpoints_web": None,
                "email": SPIDERS_SETTINGS["instacart"]["AUTH_USER"],
                "password": SPIDERS_SETTINGS["instacart"]["AUTH_PASSWORD"],
                "address": None,
                "captcha": None
            }
        }

    @staticmethod
    def get_by_json(data):
        if not data:
            return None
        raw_data = str(data[0].next)
        json_data = json.loads(raw_data)
        return json_data["landingContainer"]["container_payload"]["container"]["modules"][35]["data"]["sitekey"]

    @staticmethod
    def get_by_meta(data):
        if not data:
            return None
        return data[0]["content"]

    async def start_consult(self, response):
        log.info(msg=f"{self.spider_name} - Start consult spider")
        log.info(msg=f"{self.spider_name} - Spider with login")
        self.start_login()
        await self.make_login()

    async def start_extract(self):
        await self.consult_stores()
        await self.extract_data()
        self.save_item(file_name="instacart_items.json")

    def save_item(self, file_name):
        item = InstaCartFileItem(**self.item)
        item.save(file_name)

