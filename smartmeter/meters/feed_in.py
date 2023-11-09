import random
from enum import Enum, auto

from .main import smartmeter

class production_type(Enum):
    solar = auto()
    wind = auto()
    gas = auto()

class feed_in(smartmeter):
    def __init__(self, seed):
        super().__init__(seed)
        self.reading *= -1
        random.seed(seed)
        size = random.randint(300, 1000000000)
        self.production_type = random.choices(list(production_type), [0.7, 0.2, 0.1], 1)[0]

    def round(self):
        self.reading -= self.production()
        self.send_reading()

    def production(self):
        #get simulation
        #calculate usage
        pass