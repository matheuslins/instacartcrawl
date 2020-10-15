from elasticsearch import Elasticsearch

from src.settings import DB_SETTINGS


def config_client():
    return Elasticsearch(hosts=DB_SETTINGS["ES"]["HOST"], timeout=25)
