import random
from enum import Enum
from smartmeter.io.filehandler import write_reading
import time

from smartmeter.constants import LOCATION_LIMITS_LATITUDE, LOCATION_LIMITS_LONGITUDE

class meter_type(Enum):
    residential = 0
    industry = 1
    feed_in = 2
    residential_feed_in = 3

    @classmethod
    def value(self, name):
        return(self.__dict__["__doc__"][str(name)])

class smartmeter:
    def __init__(self, seed, usage_func):
        print(self.__class__.__name__)
        random.seed(seed)
        self.reading = random.uniform(0, 1000000) #Verteilung der Startwerte noch anpassen
        self.location = (random.uniform(*LOCATION_LIMITS_LATITUDE), 
                         random.uniform(*LOCATION_LIMITS_LONGITUDE)) #random location
        self.timestamp = None #request time from environment
        self.datastore = list()
        self.usage = usage_func



    def run(self):
        while(True):
            self.reading += self.usage()
            write_reading(self.reading)
            time.sleep(20) #make continuous

    def usage(self):
        return 0 #will be overwritten by child classes

    def string(self):
        return str(self.__class__.__name__) + " " + \
                str(f'reading={self.reading}') + " " + \
                str(f'location={self.location}') + " " + \
                str(f'time={self.timestamp}')