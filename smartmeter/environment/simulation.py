from threading import Lock

from .main import shared_environment_wrapper
from smartmeter.util.nd_list import create_nd_list

class simulation():
    def __init__(self, environment: shared_environment_wrapper):
        self.environment = environment
        self.lock = Lock()
    
    def run(self):
        self.timestamp += 15*60
        with self.lock:
            pass
            #weather simulation

        #sleep(15 Minuten)



    