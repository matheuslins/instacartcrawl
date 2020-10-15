from decouple import config


CAPTCHA = {
    "2CAPTCHA_API_KEY": config("2CAPTCHA_API_KEY"),
    "2CAPTCHA_URL": config("2CAPTCHA_URL")
}

SPIDERS_SETTINGS = {
    "instacart": {
        "START_URL": "http://instacart.com",
        "LOGIN_URL": "https://www.instacart.com/v3/dynamic_data/authenticate/login?source=web&cache_key=undefined",
        "STORES_URL": "https://www.instacart.com/v3/containers/next_gen/onboarding?source=web&cache_key=undefined",
        "LINK_PATHS": "http://instacart.com/v3/containers/{}/ng/l/savings/all/_/modules".format,
        "SPECIFIC_STORE": "https://www.instacart.com/store/{}/storefront".format,
        "BASE_HEADERS": {
            'authority': 'www.instacart.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'x-client-identifier': 'web',
            'x-csrf-token': 'undefined',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
            'origin': 'https://www.instacart.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.instacart.com/',
            'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': 'ftr_ncd=6; _gcl_au=1.1.622688012.1602194134; _fbp=fb.1.1602194134892.828217208; _pin_unauth=dWlkPU5EazNaRGRrTWpZdE5qSTBZUzAwWWprNUxUbGtOR1l0TkdWaVpXRTBOamcwTWpVMA; ab.storage.userId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d=%7B%22g%22%3A%22163399259%22%2C%22c%22%3A1602194535085%2C%22l%22%3A1602194535085%7D; ab.storage.deviceId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d=%7B%22g%22%3A%22d313a6bf-948c-f6c9-f71e-5561657d140d%22%2C%22c%22%3A1602194535092%2C%22l%22%3A1602194535092%7D; _instacart_logged_in=1; __stripe_mid=d2e0933c-7a0f-47b3-9a0d-e07593cb097064dab5; __ssid=196ce26e4325f73269820d5a011f86a; ab.storage.sessionId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d=%7B%22g%22%3A%223c83e8c0-ecba-e95d-ea25-98749cbabd34%22%2C%22e%22%3A1602291216135%2C%22c%22%3A1602289410633%2C%22l%22%3A1602289416135%7D; __stripe_sid=fa0c3d48-b5cb-4bc4-99b2-8b79d35dc13c5ed314; _dd_s=rum=0&expire=1602290681404; ajs_anonymous_id=%226981ebb4-80d3-4155-9ec8-80ce06f12b6d%22; build_sha=b025575d4c43f8c0c1625a09fc224efb53606687; ahoy_visitor=c9a84ac2-c77d-447c-a1c4-f5bf64ec215f; ahoy_visit=cb93c8a1-f8fc-4886-8103-8147de0cfda7; _instacart_session=T0ZjSTdDRkJZNGt1cGlNT1pqNmhsTWJkVURqbXBIMGVJU3VYa0h6OW9KcDhySjdPZU10MjFROTFESVMyMWgwdGdXeWdVS0dDOU9HcSs0eC9jMmI3WXQzek41MFl3ejFHUmo5cmdlUXVYckR4N0JGRUNMeFJrbkpkR3ZZTnVqdlZmV2dzTXBWaWtKa1VjTmllVUJVQ1BjUEhkTXpSRkM4YkZKS0dXbk9wcXF3eUM1SEQ3UStEZnFPTG1lVTVEVzRaNEdkbC9BRDcySys1dGtnN2d3OFhvbFI3d1N3VFNSN2xCL1B3cTlhRnZIWklWR1dwMnh3YkhkTzk1ZVFIcXBHMmtHcHMrN1d6VmlKeXhIaHFaU29od3NCdFV3c3JLUzlDMk90MlVKWUg1T3c1ZUNpc2gxYlovRnAzYTdaSXFBcXpTN0ZyMFUwYU1ENFBnaXhOa0tEcEJLRUlPck9pcmxSUVAycWYrVnNZbHhURy84dEFZcVUrc0tNRG9ncElWRlZtR29XR24zSXZ4L0ZoRjFVZEFrNktDbU9qdjJPRU9ROXBEZWNkR0twVVhKMD0tLTVLRzlURFJWQUs2SUsvRVd1UmF4NXc9PQ%3D%3D--146307313fc70d42a43cea1fb82d241d39531b33; forterToken=6fd80940ab474eb38b4cfaf7cbfe1e95_1602289785096__UDF43_9ck; _uetsid=fdfcfa7009b011ebb082b31e12410666; _uetvid=fe01d8a009b011eb96ee377d75844165; _derived_epik=dj0yJnU9eDEySi0wTVRiNFNmb3dfQXVyV1lDTGY1TUtwRW51RmUmbj1vZWRiaFhaci1PRXVnVzl2TEFya3l3Jm09MSZ0PUFBQUFBRi1CQUhzJnJtPTEmcnQ9QUFBQUFGLUJBSHM; signup_load_perf_date=1602289808990; ahoy_visitor=324b02b7-329a-4fcb-9ebb-22fec7dfd495; ahoy_track=true; build_sha=9a1e23818a224998940b1f832aeb0fba13a7e333; _instacart_session=Wit4a0pOL1JlK0dnUkVET3hOencvWUs3M2lzY2ZSL0N0NjF3bU45QjF2akJ5cklUZS94U1NCTnBYcVRZZHpZVENJRXZ6ZVB0Q2gxV1VMYWlIV2xyRlJCSVBCUmxQNVBaNmYwU2o3Wm1rWmZmcURWNjc4UkZaTitEQ3ExQzRiODVlcWxjSUx6OVlHQUl5Snp1UXp4dlFSL1g0eHFhYUkzMkJsQmJSN29WdElWaG5UWVMwYVVXa0tKTDdxMFU0U0VBV0tETHF5MGIwR2V0L1BvZzJ3UVZwcjVtY0s0bGJreUdLRnlJSXdaRzBNdGsvMEZmU0ROcFdRenhZQmVrVURTUVdTM3R1dC9vOXVtRjNQT2lEcDd4WlBXdHVKUk9zNzBNaFE1YlV1OFRMQUZNZTRVRE9ubGFMWUk4RWZEV3B4VmVDei9STS9qTXpUNUVrSjRPdlJIMVdnRzlWWHVKeHNLTEFXNTA2eTM1OE1VK0xobkt3SnNKLzdXR0piaHk1YitRdGZMdnlYcU1BU01TbVZUWGo1S2JXL093NlJUMmpSTEdnYk0rU1VHaE02OD0tLWhTbVhkTkxjNHpGa2hPWGcybWlOVUE9PQ%3D%3D--c29111ee46a7b5587ee1a6eb2bdc487aec70221c',
            'Content-Type': 'application/json'
        },
        "STORE_COOKIE": 'ftr_ncd=6; _gcl_au=1.1.622688012.1602194134; _fbp=fb.1.1602194134892.828217208; _pin_unauth=dWlkPU5EazNaRGRrTWpZdE5qSTBZUzAwWWprNUxUbGtOR1l0TkdWaVpXRTBOamcwTWpVMA; ab.storage.userId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d=%7B%22g%22%3A%22163399259%22%2C%22c%22%3A1602194535085%2C%22l%22%3A1602194535085%7D; ab.storage.deviceId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d=%7B%22g%22%3A%22d313a6bf-948c-f6c9-f71e-5561657d140d%22%2C%22c%22%3A1602194535092%2C%22l%22%3A1602194535092%7D; _instacart_logged_in=1; __stripe_mid=d2e0933c-7a0f-47b3-9a0d-e07593cb097064dab5; __ssid=196ce26e4325f73269820d5a011f86a; build_sha=90b58763437ebed8f2d1c23c8be63db51d994dd5; _dd_s=rum=0&expire=1602366442158; ajs_anonymous_id=%2238536cb9-84c2-47c1-adbe-f5cbb2c5f425%22; ahoy_visitor=488abf00-5bb0-4005-9b77-365dc849fe98; ahoy_visit=082c4865-437d-4c82-a037-0a15f07acd62; forterToken=6fd80940ab474eb38b4cfaf7cbfe1e95_1602365551379__UDF43_9ck; _uetsid=fdfcfa7009b011ebb082b31e12410666; _uetvid=fe01d8a009b011eb96ee377d75844165; _derived_epik=dj0yJnU9NXRWdWNENzRucUJxeGxrNFYzUU5ReUpoaHV0TjRKZ0cmbj1QdW1FajJ0WEJtVDlnODZoTEh6Z1F3Jm09MSZ0PUFBQUFBRi1DS0hJJnJtPTEmcnQ9QUFBQUFGLUNLSEk; signup_load_perf_date=1602365791750; __Host-instacart_sid=cc7db71362b06cc2002507163d39289d08225544afef915fbf4d22a37ed0aeb0; _instacart_session=UGQ5ODRGZTBVWDlOdDJ1RkkzV3lIQTRseSsvemtEVmZIYnFldG5uVG1aK1dHUzhIWDh1LzBuUFdWK0huY2ZESnZOM1BYSXNCZmIvYTBIMFF2YmZqQWx2cFE5V1pUbThWalJmMHNObWxWVWRwKzBPN2J4K3ZYamF4RU91UnJhQkszMTJDbk96SnNuM29NS0YzNTY0WnAvcHpCc1g3TWlXSTZnN3Zld0xIQzFmVmFGOE5ETElVa3FvaFVDV1J6d3JlZ29oWEJ0QzBWZXY3SXZJbWo2NkovZmJTUzkzTnJYMVpWMkJJdmVMakdJRjZSaXhkbEw5T3BpWmMvVDJRRmt5dkliVXNEdm9WcDNwcm83ZnU4czh3K1UvcnYyZzFCYWdVaGF1THBldHhoZWxIV29HMDZPMXNnNldEQzdmZDFFUVViT0NDVzlQaUVEUEsyaE1zUFpHV3VpNTc3NksrUkZjTTNZbEZrZWxxOXk3RE5ZMmZROGFYL0dVZ2gwTkorek5SWlJwSHV2dVNoSU04K3grMUxUZU5zTUV0N1hnbEN3MW9wV2JnUUV5OFZWc2VPbFdNVGllSkNDWmwybnh5dWdFNkxPa3RwQ0luelorbFRTVTZZUWhOZkxVVyttd1VveHFlWWx0Q0E5SlVwTHc9LS1VdDlOcWgzc1oveVFVTWNnMHU2Y3lBPT0%3D--fdf853f8150b967242719323ae5f12e42b7b2512; ab.storage.sessionId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d=%7B%22g%22%3A%2293cafc50-ffc3-f681-7892-0a29d44fc8a6%22%2C%22e%22%3A1602367597106%2C%22c%22%3A1602365797107%2C%22l%22%3A1602365797107%7D',
        "AUTH_USER": config("AUTH_USER"),
        "AUTH_PASSWORD": config("AUTH_PASSWORD"),
        "SAVE_DB_ITEM": config("SAVE_DB_ITEM", cast=bool, default=True),
        "ES_INDEX": "instacart-products"
    }
}

DB_SETTINGS = {
    "ES": {
        "HOST": config("DB_HOST", default="http://localhost:9200")
    }
}
