import asyncio

from src.talkers.sites.instacart import InstaCartTalker


def run():
    site_talker = InstaCartTalker()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(site_talker.run())


