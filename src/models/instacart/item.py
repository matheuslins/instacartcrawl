import json

from dataclasses import dataclass, field
from itemadapter import ItemAdapter
from typing import Dict


@dataclass
class InstaCartFileItem:
    storeName: str = ''
    storeUrl: str = ''
    products:  Dict = field(default_factory=dict)

    def save(self, file_name):
        with open(file_name, "a") as file:
            item = ItemAdapter(self).asdict()
            json.dump(item, file, indent=4)


@dataclass
class InstaCartDbItem:
    name: str
    department: str
    storeName: str = ''
    storeUrl: str = ''

    def save(self, db_instance):
        item = ItemAdapter(self).asdict()
        db_instance.save(item)
