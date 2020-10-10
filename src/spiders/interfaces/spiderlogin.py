from twocaptcha import TwoCaptcha

from src.spiders.interfaces.spider import BaseSpider
from src.core.login import LoginHandler
from src.core.captcha import CaptchaHandler
from src.settings import SPIDERS_SETTINGS, CAPTCHA
from src.core.tools import parse_cookies
from src.models.instacart.item import InstaCartItem


class SpiderLoginInterface(BaseSpider, LoginHandler):
    start_url = None
    first_store = None
    session_cookies = {}
    login_params = {}
    item = {}

    def get_start_url(self):
        return self.start_url

    async def make_login(self):
        two_captcha = TwoCaptcha(**{
            'apiKey': CAPTCHA['2CAPTCHA_API_KEY'],
            'defaultTimeout': 60,
            'recaptchaTimeout': 200,
            'pollingInterval': 7
        })
        captcha_handler = CaptchaHandler(captcha_resolver=two_captcha)
        captcha_result = await captcha_handler.broker_captcha(
            site_key=self.login_data["site_key_captcha"],
            site_url=SPIDERS_SETTINGS["instacart"]["START_URL"]
        )

        self.login_params["json"]["authenticity_token"] = self.login_data["authenticity_token"]
        self.login_params["json"]["captcha"] = captcha_result

        response = await self.make_request(
            method="POST",
            headers=SPIDERS_SETTINGS["instacart"]["BASE_HEADERS"],
            **self.login_params
        )
        self.session_cookies = response['raw'].cookies

    def save_item(self):
        item = InstaCartItem()
        item.save(self.item)

    async def start_consult(self, response):
        self.start_login()
        await self.make_login()

    async def start_extract(self):
        pass
