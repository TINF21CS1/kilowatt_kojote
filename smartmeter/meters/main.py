import random
from enum import Enum
import uuid
from smartmeter.network.main import requests
import time

from smartmeter.constants import UPDATE_FREQUENCE

class meter_type(Enum):
    residential = 0
    industry = 1
    feed_in = 2
    residential_feed_in = 3

    @classmethod
    def value(self, name):
        return(self.__dict__["__doc__"][str(name)])

class smartmeter:
    def __init__(self, seed):
        random.seed(seed)
        self.reading = random.randint(0, 1000000) #Verteilung der Startwerte noch anpassen
        self.location = None
        self.timestamp = None #request time from environment
        self.datastore = list()
        self.uuid = uuid.uuid4() #is there a need to include the seed so the uuid is pseudo random?

        register = {"uuid": str(self.uuid),
                    "type": meter_type.value(type(self)),
                    "location": self.location}
        while(requests.register(register).status != '200'):
            pass

    def run(self):
        global UPDATE_FREQUENCE
        while(True):
            if(self.timestamp%UPDATE_FREQUENCE == 0):
                self.update()
            self.round()
            self.send_reading()
            time.sleep(15*60) #measure every 15 Minutes

    def update(self):
        pass
        #request update
        #download if available

    def round(self):
        pass

    def send_reading(self):
        data = {"timestamp": self.timestamp,
                "reading": self.reading}
        self.datastore.append(data)
        if((response := requests.send(self.datastore)).status == '200'):
            self.datastore = list()
        else:
            pass
            #error handling