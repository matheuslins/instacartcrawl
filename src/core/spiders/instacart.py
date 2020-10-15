import asyncio
from bs4 import BeautifulSoup
from aiohttp import ClientSession

from src.core.tools import remove_special_chars
from src.core.logging import log
from src.settings import SPIDERS_SETTINGS
from src.spiders.interfaces.spiderlogin import SpiderLoginInterface
from src.models.instacart.item import InstaCartDbItem
from src.core.database.elastic import elastic_instance


class InstacartBusiness(SpiderLoginInterface):

    item = {}
    spider_headers = SPIDERS_SETTINGS["instacart"]["BASE_HEADERS"]
    first_store = None

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
            fs=await self.get_all_products_tasks(store_name)
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
                log.info(msg=f"Path: {path}")
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

            await self.open_tasks(tasks)

        return tasks

    async def open_tasks(self, tasks):
        tasks_response = await asyncio.gather(*tasks)
        products_items = {}

        for _task in tasks_response:
            json_response = _task['json']
            try:
                department = json_response['module_data']['header_label_action']['label']
            except KeyError:
                department = json_response['module_data']['tracking_params']['source_value']

            log.info(msg=f"Department: {department}")

            products = json_response['module_data']['items']

            if SPIDERS_SETTINGS['instacart']['SAVE_DB_ITEM']:
                await self.send_item_to_db(products, department)

            await self.save_file_item(products_items, products, department)

    async def send_item_to_db(self, products, department):

        for count, product in enumerate(products):
            item = {
                "name": product["name"],
                "department": department,
                "storeName": self.item['storeName'],
                "storeUrl": self.item['storeUrl']
            }
            log.info(msg=f"Product {count}: {product['name']}")

            db_item = InstaCartDbItem(**item)
            db_item.save(elastic_instance)
            log.info(msg=f"Sent to ElasticSearch")

        elastic_instance.save_left_items()

    async def save_file_item(self, products_items, products, department):
        for count, product in enumerate(products):
            products_items.setdefault(department, []).append({
                'name': product['name']
            })
            log.info(msg=f"Product {count}: {product['name']}")

        self.item['products'] = products_items
