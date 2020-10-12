import json

from dataclasses import dataclass, field
from itemadapter import ItemAdapter
from typing import Dict


@dataclass
class InstaCartItem:
    storeName: str = ''
    storeUrl: str = ''
    products:  Dict = field(default_factory=dict)

    def save(self, file_name):
        with open(file_name, "a") as file:
            item = ItemAdapter(self).asdict()
            json.dump(item, file, indent=4)
