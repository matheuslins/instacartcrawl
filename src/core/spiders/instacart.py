import asyncio
from bs4 import BeautifulSoup
from aiohttp import ClientSession

from src.core.tools import remove_special_chars
from src.settings import SPIDERS_SETTINGS
from src.spiders.interfaces.spiderlogin import SpiderLoginInterface


class InstacartBusiness(SpiderLoginInterface):
    first_store = None
    spider_headers = SPIDERS_SETTINGS["instacart"]["BASE_HEADERS"]

    async def consult_stores(self):
        self.spider_headers['cookie'] = SPIDERS_SETTINGS["instacart"]["STORE_COOKIE"]

        response = await self.make_session_request(
            method="GET",
            headers=self.spider_headers,
            url=SPIDERS_SETTINGS['instacart']['STORES_URL']
        )
        json_response = await response['raw'].json()
        self.first_store = json_response['container']['tracking_params']['warehouse_id']

    async def extract_data(self):
        self.spider_headers['cookie'] = SPIDERS_SETTINGS["instacart"]["STORE_COOKIE"]

        url = SPIDERS_SETTINGS['instacart']['SPECIFIC_STORE'](self.first_store)
        response = await self.make_session_request(
            method="GET",
            headers=self.spider_headers,
            url=url
        )

        soup = BeautifulSoup(response['text'], 'html.parser')
        store = soup.find(name="div", attrs={"data-identifier": "store_logo"})
        store_name = store.img.attrs['alt']

        self.item = {
            "storeName": store_name,
            "storeUrl": store.img.attrs['src']
        }

        await asyncio.wait(
            await self.get_all_products_tasks(store_name)
        )

    async def get_links_paths(self, store_name):
        links_paths = []

        self.spider_headers['cookie'] = SPIDERS_SETTINGS["instacart"]["STORE_COOKIE"]

        clean_store_name = remove_special_chars(store_name)
        url = SPIDERS_SETTINGS["instacart"]["LINK_PATHS"](clean_store_name)

        response = await self.make_session_request(
            method="GET",
            headers=self.spider_headers,
            url=url
        )
        json_response = await response['raw'].json()

        for module in json_response['container']['modules']:
            module_id = module['id']
            if "savings_items" in module_id:
                links_paths.append(module['async_data_path'])

        return links_paths

    async def get_all_products_tasks(self, store_name):
        tasks = []
        self.spider_headers['cookie'] = SPIDERS_SETTINGS["instacart"]["STORE_COOKIE"]
        links_paths = await self.get_links_paths(store_name)

        async with ClientSession() as session:
            for path in links_paths:
                print(f"Path: {path}")
                url = f'{SPIDERS_SETTINGS["instacart"]["START_URL"]}{path}'
                task = asyncio.ensure_future(
                    self.make_raw_request(
                        session=session,
                        method="GET",
                        headers=self.spider_headers,
                        url=url
                    )
                )
                tasks.append(task)

            await self.save_all_products(tasks)

        return tasks

    async def save_all_products(self, tasks):
        tasks_response = await asyncio.gather(*tasks)
        all_products = {}
        count = 0

        for _task in tasks_response:
            json_response = _task['json']
            department = json_response['module_data']['tracking_params']['source_value']

            print(f"Department: {department}")

            products = json_response['module_data']['items']

            for product in products:
                count = count + 1
                all_products.setdefault(department, []).append({
                    'name': product['name']
                })
                print(f"Product {count}: {product['name']}")

        self.item['products'] = all_products
