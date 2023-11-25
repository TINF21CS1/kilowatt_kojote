import random

from .main import smartmeter
from smartmeter.io.network import requests

class industry(smartmeter):
    def __init__(self, seed, usage_func=None):
        if(usage_func==None): usage_func=self.usage_industrial
        super().__init__(seed, usage_func)
        self.size = random.randint(1000, 1000000)
        match a:=random.random():
            case _ if a < 0.5:
                self.shifts = 1
            case _ if a < 0.8:
                self.shifts = 2
            case _:
                self.shifts = 3
        self.weekend_shift = False
        if(self.shifts > 1):
            self.weekend_shift = (random.random() > 0.8)
        self.fluctuation = random.random()

    def usage_industrial(self) -> float:
        self.timestamp = requests.get(['timestamp'])
        if(self.timestamp.weekday() > 4 and not self.weekend_shift):
            return 0
        match self.shifts:
            case 1:
                if(self.timestamp.hour < 7 or self.timestamp.hour > 15):
                    return 0
            case 2:
                if(self.timestamp.hour < 6 or self.timestamp.hour > 22):
                    return 0
        return self.size * random.uniform(0.5, 1.5) * (1+self.fluctuation)
        return 0
    
    def string(self):
        return super().string() + " " + \
                str(f'size={self.size}') + " " + \
                str(f'shifts={self.shifts}') + " " + \
                str(f'fluctuation={self.fluctuation}')