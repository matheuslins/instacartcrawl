from src.talkers.interfaces.request import TalkerInterface
from src.settings import TALKER_SETTINGS


class InstaCartTalker(TalkerInterface):

    def start_url(self):
        return TALKER_SETTINGS["instacart"]["START_URL"]

