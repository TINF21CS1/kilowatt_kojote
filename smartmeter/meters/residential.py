from .main import smartmeter

class residential(smartmeter):
    def __init__(self, seed):
        super().__init__(seed)

    def round(self):
        self.reading += self.usage_residential()
        self.send_reading()

    def usage_residential(self):
        #get simulation
        #calculate usage
        pass