import logging


class LoggerHandler:
    log = None

    def __init__(self):
        self.set_log_config()

    def set_log_config(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
            datefmt='%d-%b-%y %H:%M:%S'
        )
        self.log = logging.getLogger(name=self.__class__.__name__)

    def info(self, msg, *args, **kwargs):
        return self.log.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        return self.log.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        return self.log.error(msg, *args, **kwargs)


log = LoggerHandler()
