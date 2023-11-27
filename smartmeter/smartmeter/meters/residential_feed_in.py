from .residential import residential
from .feed_in import feed_in

class residential_feed_in(residential, feed_in):
    def __init__(self, seed):
        residential.__init__(self, seed, lambda: self.usage_residential() - self.production()) #figure out behaivior with multiple parent classes
        feed_in.__init__(self, seed, local=True)

    def string(self):
        residential.string(self) + " " + feed_in.string(self)