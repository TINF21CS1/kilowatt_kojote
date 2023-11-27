from threading import Thread
import random
import time
import platform
import datetime

from .simulation import simulation
from .api import api as env_api
from .util.nd_list import create_nd_list
from .constants import MAX_WIDTH, MAX_HEIGHT

class shared_environment_wrapper():
    def __init__(self, seed):
        random.seed(seed)
        empty_matrix = create_nd_list([MAX_WIDTH, MAX_HEIGHT], None)
        self.temperature = empty_matrix
        self.wind = empty_matrix
        self.sun = empty_matrix 
        self.rain = empty_matrix
        self.timestamp = datetime.fromtimestamp(random.randint(946681200000, int(time.time()))) #start is 01.01.2000

        #populate environment

class environment():
    def __init__(self, seed):

        #init environment
        shared_environment = shared_environment_wrapper(seed)

        #create instances of thread classes
        sim = simulation(shared_environment, seed)
        api = env_api(shared_environment)

        #Define thread tasks
        def sim_task():
            sim.run()

        def api_task():
            api.run()

        #create threads
        sim_thread = Thread(target=sim_task, args=())
        api_thread = Thread(target=api_task, args=())

        #start both threads
        sim_thread.start()
        api_thread.start()

        #necceassary? Threads wont finish
        sim_thread.join()
        api_thread.join()

def main(seed):
    environment(seed)

if __name__ == "__main__":
    seed = platform.node()
    main(seed)