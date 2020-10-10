from src.core.request import RequestHandler


class CaptchaHandler(RequestHandler):

    def __init__(self, captcha_resolver):
        super(CaptchaHandler, self).__init__()
        self.captcha_resolver = captcha_resolver

    async def broker_captcha(self, *, site_key, site_url):
        captcha_response = self.captcha_resolver.recaptcha(sitekey=site_key, url=site_url)
        return captcha_response['code']
