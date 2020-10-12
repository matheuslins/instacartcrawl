import logging


class LoggerHandler:
    log = None

    def set_base_config(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
            datefmt='%d-%b-%y %H:%M:%S'
        )
        self.log = logging.getLogger()

    def info(self):
        return self.log.info

    def warning(self):
        return self.log.warning
