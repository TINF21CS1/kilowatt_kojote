from .main import smartmeter

class industry(smartmeter):
    def __init__(self, seed):
        super().__init__(seed)

    def round(self):
        self.reading += self.usage_industrial()
        self.send_reading()

    def usage_industrial(self):
        #get simulation
        #calculate usage
        pass