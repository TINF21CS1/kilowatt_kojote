from .residential import residential
from .feed_in import feed_in

class residential_feed_in(residential, feed_in):
    def __init__(self, seed):
        super().__init__(seed) #figure out behaivior with multiple parent classes
                                #need to change chances of production type in feed_in init

    def round(self):
        self.reading += self.usage_residential()
        self.reading -= self.production()
        self.send_reading()