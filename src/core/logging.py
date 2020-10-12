import logging


class LoggerHandler:
    log = None
    spider_name = None

    def set_base_config(self):
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        self.log = logging.getLogger(f"Spider: {self.spider_name}")

    def info(self):
        return self.log.info

    def warning(self):
        return self.log.warning
