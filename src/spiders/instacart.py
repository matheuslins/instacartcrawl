from bs4 import BeautifulSoup
import json

from src.spiders.interfaces.spiderlogin import SpiderLoginInterface
from src.settings import SPIDERS_SETTINGS
from src.core.tools import remove_special_chars


class InstaCartSpider(SpiderLoginInterface):

    start_url = SPIDERS_SETTINGS["instacart"]["START_URL"]

    def __init__(self, *args, **kwargs):
        super(InstaCartSpider, self).__init__(*args, **kwargs)
        self.set_extraction_keys()
        self.set_login_params()

    async def get(self):
        return await self.run(self.request)

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
        headers = SPIDERS_SETTINGS["instacart"]["BASE_HEADERS"]
        headers['cookie'] = 'ftr_ncd=6; _gcl_au=1.1.622688012.1602194134; _fbp=fb.1.1602194134892.828217208; _pin_unauth=dWlkPU5EazNaRGRrTWpZdE5qSTBZUzAwWWprNUxUbGtOR1l0TkdWaVpXRTBOamcwTWpVMA; ab.storage.userId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d=%7B%22g%22%3A%22163399259%22%2C%22c%22%3A1602194535085%2C%22l%22%3A1602194535085%7D; ab.storage.deviceId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d=%7B%22g%22%3A%22d313a6bf-948c-f6c9-f71e-5561657d140d%22%2C%22c%22%3A1602194535092%2C%22l%22%3A1602194535092%7D; _instacart_logged_in=1; __stripe_mid=d2e0933c-7a0f-47b3-9a0d-e07593cb097064dab5; __ssid=196ce26e4325f73269820d5a011f86a; build_sha=90b58763437ebed8f2d1c23c8be63db51d994dd5; _dd_s=rum=0&expire=1602366442158; ajs_anonymous_id=%2238536cb9-84c2-47c1-adbe-f5cbb2c5f425%22; ahoy_visitor=488abf00-5bb0-4005-9b77-365dc849fe98; ahoy_visit=082c4865-437d-4c82-a037-0a15f07acd62; forterToken=6fd80940ab474eb38b4cfaf7cbfe1e95_1602365551379__UDF43_9ck; _uetsid=fdfcfa7009b011ebb082b31e12410666; _uetvid=fe01d8a009b011eb96ee377d75844165; _derived_epik=dj0yJnU9NXRWdWNENzRucUJxeGxrNFYzUU5ReUpoaHV0TjRKZ0cmbj1QdW1FajJ0WEJtVDlnODZoTEh6Z1F3Jm09MSZ0PUFBQUFBRi1DS0hJJnJtPTEmcnQ9QUFBQUFGLUNLSEk; signup_load_perf_date=1602365791750; __Host-instacart_sid=cc7db71362b06cc2002507163d39289d08225544afef915fbf4d22a37ed0aeb0; _instacart_session=UGQ5ODRGZTBVWDlOdDJ1RkkzV3lIQTRseSsvemtEVmZIYnFldG5uVG1aK1dHUzhIWDh1LzBuUFdWK0huY2ZESnZOM1BYSXNCZmIvYTBIMFF2YmZqQWx2cFE5V1pUbThWalJmMHNObWxWVWRwKzBPN2J4K3ZYamF4RU91UnJhQkszMTJDbk96SnNuM29NS0YzNTY0WnAvcHpCc1g3TWlXSTZnN3Zld0xIQzFmVmFGOE5ETElVa3FvaFVDV1J6d3JlZ29oWEJ0QzBWZXY3SXZJbWo2NkovZmJTUzkzTnJYMVpWMkJJdmVMakdJRjZSaXhkbEw5T3BpWmMvVDJRRmt5dkliVXNEdm9WcDNwcm83ZnU4czh3K1UvcnYyZzFCYWdVaGF1THBldHhoZWxIV29HMDZPMXNnNldEQzdmZDFFUVViT0NDVzlQaUVEUEsyaE1zUFpHV3VpNTc3NksrUkZjTTNZbEZrZWxxOXk3RE5ZMmZROGFYL0dVZ2gwTkorek5SWlJwSHV2dVNoSU04K3grMUxUZU5zTUV0N1hnbEN3MW9wV2JnUUV5OFZWc2VPbFdNVGllSkNDWmwybnh5dWdFNkxPa3RwQ0luelorbFRTVTZZUWhOZkxVVyttd1VveHFlWWx0Q0E5SlVwTHc9LS1VdDlOcWgzc1oveVFVTWNnMHU2Y3lBPT0%3D--fdf853f8150b967242719323ae5f12e42b7b2512; ab.storage.sessionId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d=%7B%22g%22%3A%2293cafc50-ffc3-f681-7892-0a29d44fc8a6%22%2C%22e%22%3A1602367597106%2C%22c%22%3A1602365797107%2C%22l%22%3A1602365797107%7D'
        headers['referer'] = f'https://www.instacart.com/store/{self.first_store}/storefront'

        url = SPIDERS_SETTINGS['instacart']['SPECIFIC_STORE'](self.first_store)
        response = await self.make_request(
            method="GET",
            headers=headers,
            url=url
        )

        soup = BeautifulSoup(response['text'], 'html.parser')
        store = soup.find(name="div", attrs={"data-identifier": "store_logo"})
        store_name = store.img.attrs['alt']

        self.item = {
            "storeName": store_name,
            "storeUrl": store.img.attrs['src']
        }

        await self.save_all_products(store_name)

    async def get_links_paths(self, store_name):
        links_paths = []

        headers = SPIDERS_SETTINGS['instacart']["BASE_HEADERS"]
        headers['cookie'] = 'ftr_ncd=6; _gcl_au=1.1.622688012.1602194134; _fbp=fb.1.1602194134892.828217208; _pin_unauth=dWlkPU5EazNaRGRrTWpZdE5qSTBZUzAwWWprNUxUbGtOR1l0TkdWaVpXRTBOamcwTWpVMA; ab.storage.userId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d=%7B%22g%22%3A%22163399259%22%2C%22c%22%3A1602194535085%2C%22l%22%3A1602194535085%7D; ab.storage.deviceId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d=%7B%22g%22%3A%22d313a6bf-948c-f6c9-f71e-5561657d140d%22%2C%22c%22%3A1602194535092%2C%22l%22%3A1602194535092%7D; _instacart_logged_in=1; __stripe_mid=d2e0933c-7a0f-47b3-9a0d-e07593cb097064dab5; __ssid=196ce26e4325f73269820d5a011f86a; build_sha=90b58763437ebed8f2d1c23c8be63db51d994dd5; _dd_s=rum=0&expire=1602366442158; ajs_anonymous_id=%2238536cb9-84c2-47c1-adbe-f5cbb2c5f425%22; ahoy_visitor=488abf00-5bb0-4005-9b77-365dc849fe98; ahoy_visit=082c4865-437d-4c82-a037-0a15f07acd62; forterToken=6fd80940ab474eb38b4cfaf7cbfe1e95_1602365551379__UDF43_9ck; _uetsid=fdfcfa7009b011ebb082b31e12410666; _uetvid=fe01d8a009b011eb96ee377d75844165; _derived_epik=dj0yJnU9NXRWdWNENzRucUJxeGxrNFYzUU5ReUpoaHV0TjRKZ0cmbj1QdW1FajJ0WEJtVDlnODZoTEh6Z1F3Jm09MSZ0PUFBQUFBRi1DS0hJJnJtPTEmcnQ9QUFBQUFGLUNLSEk; signup_load_perf_date=1602365791750; __Host-instacart_sid=cc7db71362b06cc2002507163d39289d08225544afef915fbf4d22a37ed0aeb0; _instacart_session=UGQ5ODRGZTBVWDlOdDJ1RkkzV3lIQTRseSsvemtEVmZIYnFldG5uVG1aK1dHUzhIWDh1LzBuUFdWK0huY2ZESnZOM1BYSXNCZmIvYTBIMFF2YmZqQWx2cFE5V1pUbThWalJmMHNObWxWVWRwKzBPN2J4K3ZYamF4RU91UnJhQkszMTJDbk96SnNuM29NS0YzNTY0WnAvcHpCc1g3TWlXSTZnN3Zld0xIQzFmVmFGOE5ETElVa3FvaFVDV1J6d3JlZ29oWEJ0QzBWZXY3SXZJbWo2NkovZmJTUzkzTnJYMVpWMkJJdmVMakdJRjZSaXhkbEw5T3BpWmMvVDJRRmt5dkliVXNEdm9WcDNwcm83ZnU4czh3K1UvcnYyZzFCYWdVaGF1THBldHhoZWxIV29HMDZPMXNnNldEQzdmZDFFUVViT0NDVzlQaUVEUEsyaE1zUFpHV3VpNTc3NksrUkZjTTNZbEZrZWxxOXk3RE5ZMmZROGFYL0dVZ2gwTkorek5SWlJwSHV2dVNoSU04K3grMUxUZU5zTUV0N1hnbEN3MW9wV2JnUUV5OFZWc2VPbFdNVGllSkNDWmwybnh5dWdFNkxPa3RwQ0luelorbFRTVTZZUWhOZkxVVyttd1VveHFlWWx0Q0E5SlVwTHc9LS1VdDlOcWgzc1oveVFVTWNnMHU2Y3lBPT0%3D--fdf853f8150b967242719323ae5f12e42b7b2512; ab.storage.sessionId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d=%7B%22g%22%3A%2293cafc50-ffc3-f681-7892-0a29d44fc8a6%22%2C%22e%22%3A1602367597106%2C%22c%22%3A1602365797107%2C%22l%22%3A1602365797107%7D'
        headers['referer'] = f'https://www.instacart.com/store/{store_name}/storefront'

        clean_store_name = remove_special_chars(store_name)
        url = f"{SPIDERS_SETTINGS['instacart']['START_URL']}/v3/containers/{clean_store_name}/ng/l/savings/all/_/modules"

        response = await self.make_request(
            method="GET",
            headers=headers,
            url=url
        )
        json_response = await response['raw'].json()

        for module in json_response['container']['modules']:
            module_id = module['id']
            if "savings_items" in module_id:
                links_paths.append(module['async_data_path'])

        return links_paths

    async def save_all_products(self, store_name):
        count = 0
        all_products = {}

        headers = SPIDERS_SETTINGS['instacart']["BASE_HEADERS"]
        headers['cookie'] = 'ftr_ncd=6; _gcl_au=1.1.622688012.1602194134; _fbp=fb.1.1602194134892.828217208; _pin_unauth=dWlkPU5EazNaRGRrTWpZdE5qSTBZUzAwWWprNUxUbGtOR1l0TkdWaVpXRTBOamcwTWpVMA; ab.storage.userId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d=%7B%22g%22%3A%22163399259%22%2C%22c%22%3A1602194535085%2C%22l%22%3A1602194535085%7D; ab.storage.deviceId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d=%7B%22g%22%3A%22d313a6bf-948c-f6c9-f71e-5561657d140d%22%2C%22c%22%3A1602194535092%2C%22l%22%3A1602194535092%7D; _instacart_logged_in=1; __stripe_mid=d2e0933c-7a0f-47b3-9a0d-e07593cb097064dab5; __ssid=196ce26e4325f73269820d5a011f86a; build_sha=90b58763437ebed8f2d1c23c8be63db51d994dd5; _dd_s=rum=0&expire=1602366442158; ajs_anonymous_id=%2238536cb9-84c2-47c1-adbe-f5cbb2c5f425%22; ahoy_visitor=488abf00-5bb0-4005-9b77-365dc849fe98; ahoy_visit=082c4865-437d-4c82-a037-0a15f07acd62; forterToken=6fd80940ab474eb38b4cfaf7cbfe1e95_1602365551379__UDF43_9ck; _uetsid=fdfcfa7009b011ebb082b31e12410666; _uetvid=fe01d8a009b011eb96ee377d75844165; _derived_epik=dj0yJnU9NXRWdWNENzRucUJxeGxrNFYzUU5ReUpoaHV0TjRKZ0cmbj1QdW1FajJ0WEJtVDlnODZoTEh6Z1F3Jm09MSZ0PUFBQUFBRi1DS0hJJnJtPTEmcnQ9QUFBQUFGLUNLSEk; signup_load_perf_date=1602365791750; __Host-instacart_sid=cc7db71362b06cc2002507163d39289d08225544afef915fbf4d22a37ed0aeb0; _instacart_session=UGQ5ODRGZTBVWDlOdDJ1RkkzV3lIQTRseSsvemtEVmZIYnFldG5uVG1aK1dHUzhIWDh1LzBuUFdWK0huY2ZESnZOM1BYSXNCZmIvYTBIMFF2YmZqQWx2cFE5V1pUbThWalJmMHNObWxWVWRwKzBPN2J4K3ZYamF4RU91UnJhQkszMTJDbk96SnNuM29NS0YzNTY0WnAvcHpCc1g3TWlXSTZnN3Zld0xIQzFmVmFGOE5ETElVa3FvaFVDV1J6d3JlZ29oWEJ0QzBWZXY3SXZJbWo2NkovZmJTUzkzTnJYMVpWMkJJdmVMakdJRjZSaXhkbEw5T3BpWmMvVDJRRmt5dkliVXNEdm9WcDNwcm83ZnU4czh3K1UvcnYyZzFCYWdVaGF1THBldHhoZWxIV29HMDZPMXNnNldEQzdmZDFFUVViT0NDVzlQaUVEUEsyaE1zUFpHV3VpNTc3NksrUkZjTTNZbEZrZWxxOXk3RE5ZMmZROGFYL0dVZ2gwTkorek5SWlJwSHV2dVNoSU04K3grMUxUZU5zTUV0N1hnbEN3MW9wV2JnUUV5OFZWc2VPbFdNVGllSkNDWmwybnh5dWdFNkxPa3RwQ0luelorbFRTVTZZUWhOZkxVVyttd1VveHFlWWx0Q0E5SlVwTHc9LS1VdDlOcWgzc1oveVFVTWNnMHU2Y3lBPT0%3D--fdf853f8150b967242719323ae5f12e42b7b2512; ab.storage.sessionId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d=%7B%22g%22%3A%2293cafc50-ffc3-f681-7892-0a29d44fc8a6%22%2C%22e%22%3A1602367597106%2C%22c%22%3A1602365797107%2C%22l%22%3A1602365797107%7D'
        headers['referer'] = f'https://www.instacart.com/store/{store_name}/storefront'

        links_paths = await self.get_links_paths(store_name)

        for path in links_paths:
            print(f"Path: {path}")
            url = f'{SPIDERS_SETTINGS["instacart"]["START_URL"]}{path}'
            response = await self.make_request(
                method="GET",
                headers=headers,
                url=url
            )
            json_response = await response['raw'].json()
            department = json_response['module_data']['tracking_params']['source_value']
            print(f"Department: {department}")

            products = json_response['module_data']['items']

            for product in products:
                count = count + 1
                all_products.setdefault(department, []).append({
                    'name': product['name']
                })
                print(f"Product {count}: {product['name']}")
                # if count > 10:
                #     self.item.update({
                #         pro
                #     })
                #     await self.save_item()
                #     count = 0
        self.item['products'] = all_products

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

    async def start_extract(self):
        await self.consult_stores()
        await self.extract_data()
        self.save_item()
