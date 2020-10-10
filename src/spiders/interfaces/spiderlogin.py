from twocaptcha import TwoCaptcha

from src.spiders.interfaces.spider import BaseSpider
from src.core.login import LoginHandler
from src.core.captcha import CaptchaHandler
from src.settings import SPIDERS_SETTINGS, CAPTCHA
from src.core.tools import parse_cookies


class SpiderLoginInterface(BaseSpider, LoginHandler):
    start_url = None
    first_store = None
    session_cookies = {}
    login_params = {}

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

    async def consult_stores(self):
        headers = SPIDERS_SETTINGS["instacart"]["BASE_HEADERS"]
        headers['cookie'] = 'ftr_ncd=6; _gcl_au=1.1.622688012.1602194134; _fbp=fb.1.1602194134892.828217208; _pin_unauth=dWlkPU5EazNaRGRrTWpZdE5qSTBZUzAwWWprNUxUbGtOR1l0TkdWaVpXRTBOamcwTWpVMA; ab.storage.userId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d=%7B%22g%22%3A%22163399259%22%2C%22c%22%3A1602194535085%2C%22l%22%3A1602194535085%7D; ab.storage.deviceId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d=%7B%22g%22%3A%22d313a6bf-948c-f6c9-f71e-5561657d140d%22%2C%22c%22%3A1602194535092%2C%22l%22%3A1602194535092%7D; _instacart_logged_in=1; __stripe_mid=d2e0933c-7a0f-47b3-9a0d-e07593cb097064dab5; __ssid=196ce26e4325f73269820d5a011f86a; build_sha=90b58763437ebed8f2d1c23c8be63db51d994dd5; _dd_s=rum=0&expire=1602366442158; ajs_anonymous_id=%2238536cb9-84c2-47c1-adbe-f5cbb2c5f425%22; ahoy_visitor=488abf00-5bb0-4005-9b77-365dc849fe98; ahoy_visit=082c4865-437d-4c82-a037-0a15f07acd62; forterToken=6fd80940ab474eb38b4cfaf7cbfe1e95_1602365551379__UDF43_9ck; _uetsid=fdfcfa7009b011ebb082b31e12410666; _uetvid=fe01d8a009b011eb96ee377d75844165; _derived_epik=dj0yJnU9NXRWdWNENzRucUJxeGxrNFYzUU5ReUpoaHV0TjRKZ0cmbj1QdW1FajJ0WEJtVDlnODZoTEh6Z1F3Jm09MSZ0PUFBQUFBRi1DS0hJJnJtPTEmcnQ9QUFBQUFGLUNLSEk; signup_load_perf_date=1602365791750; __Host-instacart_sid=cc7db71362b06cc2002507163d39289d08225544afef915fbf4d22a37ed0aeb0; _instacart_session=UGQ5ODRGZTBVWDlOdDJ1RkkzV3lIQTRseSsvemtEVmZIYnFldG5uVG1aK1dHUzhIWDh1LzBuUFdWK0huY2ZESnZOM1BYSXNCZmIvYTBIMFF2YmZqQWx2cFE5V1pUbThWalJmMHNObWxWVWRwKzBPN2J4K3ZYamF4RU91UnJhQkszMTJDbk96SnNuM29NS0YzNTY0WnAvcHpCc1g3TWlXSTZnN3Zld0xIQzFmVmFGOE5ETElVa3FvaFVDV1J6d3JlZ29oWEJ0QzBWZXY3SXZJbWo2NkovZmJTUzkzTnJYMVpWMkJJdmVMakdJRjZSaXhkbEw5T3BpWmMvVDJRRmt5dkliVXNEdm9WcDNwcm83ZnU4czh3K1UvcnYyZzFCYWdVaGF1THBldHhoZWxIV29HMDZPMXNnNldEQzdmZDFFUVViT0NDVzlQaUVEUEsyaE1zUFpHV3VpNTc3NksrUkZjTTNZbEZrZWxxOXk3RE5ZMmZROGFYL0dVZ2gwTkorek5SWlJwSHV2dVNoSU04K3grMUxUZU5zTUV0N1hnbEN3MW9wV2JnUUV5OFZWc2VPbFdNVGllSkNDWmwybnh5dWdFNkxPa3RwQ0luelorbFRTVTZZUWhOZkxVVyttd1VveHFlWWx0Q0E5SlVwTHc9LS1VdDlOcWgzc1oveVFVTWNnMHU2Y3lBPT0%3D--fdf853f8150b967242719323ae5f12e42b7b2512; ab.storage.sessionId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d=%7B%22g%22%3A%2293cafc50-ffc3-f681-7892-0a29d44fc8a6%22%2C%22e%22%3A1602367597106%2C%22c%22%3A1602365797107%2C%22l%22%3A1602365797107%7D'
        headers['referer'] = 'https://www.instacart.com/onboarding'

        response = await self.make_request(
            method="GET",
            headers=headers,
            url=SPIDERS_SETTINGS['instacart']['STORES_URL']
        )
        json_response = await response['raw'].json()
        self.first_store = json_response['container']['tracking_params']['warehouse_id']

    async def extract_data(self):
        pass

    def save_items(self):
        pass

    async def start_crawl(self, response):
        self.start_login()
        await self.make_login()
        await self.consult_stores()
        await self.extract_data()
        self.save_items()
