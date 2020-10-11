from dataclasses import dataclass, field
from typing import Dict


@dataclass
class InstaCartItem:
    name: str = ''
    logoUrl: str = ''
    products:  Dict = field(default_factory=dict)

    def save(self, item):
        pass
