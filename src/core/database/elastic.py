import pytz
import hashlib
from datetime import datetime
from elasticsearch.helpers import bulk
from elasticsearch.helpers.errors import BulkIndexError
from elasticsearch.exceptions import ConnectionError
from urllib3.exceptions import NewConnectionError

from src.settings import SPIDERS_SETTINGS
from src.core.database import config_client


class ElasticSearchDBHandler:

    bulk_list = []
    bulk_size = 100

    def __init__(self):
        self.es_index = SPIDERS_SETTINGS['instacart']['ES_INDEX']
        self.tz = pytz.timezone('America/Sao_Paulo')
        self.client = config_client()

    @staticmethod
    def generate_id(item):
        return hashlib.sha1(
            f"{item['name']}_{item['storeName']}".encode()
        ).hexdigest()[:40]

    def insert_items(self):
        date_timezone = datetime.now(tz=self.tz).date()
        for item in self.bulk_list:
            yield {
                "_index": f"{self.es_index}-{date_timezone}",
                "_type": "product",
                "_id": self.generate_id(item),
                '_op_type': 'create',
                '_source': item
            }

    def save(self, item):
        item.update({
            "dateTime": datetime.now(tz=self.tz).isoformat(),
        })
        self.bulk_list.append(item)
        if len(self.bulk_list) >= self.bulk_size:
            try:
                bulk(client=self.client, actions=self.insert_items())
            except (BulkIndexError, NewConnectionError, ConnectionError):
                pass
            self.bulk_list = []

    def save_left_items(self):
        try:
            bulk(client=self.client, actions=self.insert_items(), raise_on_exception=False)
        except (BulkIndexError, NewConnectionError, ConnectionError):
            pass


elastic_instance = ElasticSearchDBHandler()
