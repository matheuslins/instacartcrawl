from twocaptcha import TwoCaptcha

from src.core.login import LoginHandler
from src.core.captcha import CaptchaHandler
from src.core.logging import log
from src.settings import SPIDERS_SETTINGS, CAPTCHA


class SpiderLoginInterface(LoginHandler):
    session_cookies = {}
    login_params = {}

    async def make_login(self):
        log.info(msg="Spider captcha detected")
        two_captcha = TwoCaptcha(**{
            'apiKey': CAPTCHA['2CAPTCHA_API_KEY'],
            'defaultTimeout': 60,
            'recaptchaTimeout': 200,
            'pollingInterval': 7
        })
        captcha_handler = CaptchaHandler(captcha_resolver=two_captcha)
        log.info(msg=f"Solving captcha - {self.login_data['site_key_captcha']}")

        captcha_result = await captcha_handler.broker_captcha(
            site_key=self.login_data["site_key_captcha"],
            site_url=SPIDERS_SETTINGS["instacart"]["START_URL"]
        )
        log.info(msg=f"Captcha solved: {captcha_result}")

        self.login_params["json"]["authenticity_token"] = self.login_data["authenticity_token"]
        self.login_params["json"]["captcha"] = captcha_result

        response = await self.make_session_request(
            method="POST",
            headers=SPIDERS_SETTINGS["instacart"]["BASE_HEADERS"],
            **self.login_params
        )
        self.session_cookies = response['raw'].cookies
        log.info(msg="Session cookies saved.")

