from .residential import residential
from .feed_in import feed_in

class residential_feed_in(residential, feed_in):
    def __init__(self, seed):
        super().__init__(seed, lambda: self.usage_residential() - self.production()) #figure out behaivior with multiple parent classes
                                #need to change chances of production type in feed_in init

    def string(self):
        super(residential, self).string() + " " + super(feed_in, self).string()