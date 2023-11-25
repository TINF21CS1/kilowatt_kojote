import random
from enum import Enum, auto

from .main import smartmeter

class production_type(Enum):
    solar = auto()
    wind = auto()
    gas = auto()

class feed_in(smartmeter):
    def __init__(self, seed, local=False):
        if(not local):
            super().__init__(seed, lambda: -1 * self.production())
            self.reading *= -1
            size = random.randint(300, 1000000000)
            self.production_type = random.choices(list(production_type), [0.7, 0.2, 0.1], 1)[0]
        else:
            self.reading -= random.uniform(300, 10000)
            size = random.randint(300, 1000)
            self.production_type = random.choices(list(production_type), [0.9, 0.1, 0], 1)[0]


    def production(self) -> float:
        match self.production_type:
            case production_type.solar:
                return self.size
            case production_type.wind:
                return self.size
            case production_type.gas:
                return self.size
            case _:
                return 0
            
    def string(self):
        return super().string() + " " + \
                str(f'production_type={self.production_type}') + " " + \
                str(f'size={self.size}')