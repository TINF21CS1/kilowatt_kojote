from .main import smartmeter
import random

from smartmeter.io.network import requests

class residential(smartmeter):
    def __init__(self, seed):
        super().__init__(seed, self.usage_residential)
        self.consumtion = [
			[250, 250], # 00:00
			[200, 200], # 01:00
			[200, 200], # 02:00
			[200, 200], # 03:00
			[200, 200], # 04:00
			[200, 200], # 05:00
			[400, 400], # 06:00
			[400, 400], # 07:00
			[400, 400], # 08:00
			[300, 350], # 09:00
			[300, 350], # 10:00
			[300, 350], # 11:00
			[300, 350], # 12:00
			[300, 350], # 13:00
			[300, 350], # 14:00
			[300, 350], # 15:00
			[300, 350], # 16:00
			[500, 500], # 17:00
			[500, 500], # 18:00
			[500, 500], # 19:00
			[500, 500], # 20:00
			[500, 500], # 21:00
			[250, 250], # 22:00
			[250, 250]  # 23:00
        ]
        match random.randint(0, 2):
            case 0: #low density
                self.households = random.randint(1, 2)
            case 1: #medium density
                self.households = random.randint(5, 10)
            case 2: #high density
                self.households = random.randint(20, 40)
        main_deviation = random.uniform(0.8, 1.2)
        for i in range(len(self.consumtion)):
            for j in range(len(self.consumtion[i])):
                self.consumtion[i][j] = self.consumtion[i][j] * main_deviation * random.uniform(0.9, 1.1) * self.households

    def usage_residential(self) -> float:
        self.timestamp = requests.get(['timestamp'])
        weekend = +(self.timestamp.weekday() > 4)
        return self.consumtion[self.timestamp.hour][weekend] / 4 * random.uniform(0.9, 1.1)
    
    def string(self):
        return super().string() + " " + \
                str(f'households={self.households}') + " " + \
                str(f'consumtion={self.consumtion}')