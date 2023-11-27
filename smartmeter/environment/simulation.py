from threading import Lock
import time
import random
from enum import Enum, auto

from .main import shared_environment_wrapper
from .util.time import month_add
from .constants import MAX_WIDTH, MAX_HEIGHT
from .preasure_areas import pressure_map

#wind an ht grenze
#sonne im h
#regen im t
#temperatur 

class season(Enum):
    winter = auto()
    spring = auto()
    summer = auto()
    fall = auto()



class simulation():
    def __init__(self, environment: shared_environment_wrapper, seed):
        self.environment = environment
        self.lock = Lock()
        self.season, self.next_season = self.get_season()
        random.seed(seed)
        self.pressure_map = pressure_map()

        for i in range(MAX_WIDTH):
            for j in range(MAX_HEIGHT):
                self.environment.sun[i][j] = self.get_sun(i, j)

    def get_sun(self, i, j):
        #calculate distance to closest low pressure area
        pass

    def get_season(self):
        with self.lock:
            x = self.environment.timestamp
        offset = random.randint(-15, 15)
        if (x.month, x.day) < (end := month_add((3,20), offset)) or \
            (x.month, x.day) > (end_fall := month_add((12,20), offset)): 
            return season.winter, end
        elif (x.month,x.day) < (end := month_add((6,21), offset) ): 
            return season.spring, end
        elif (x.month,x.day) < (end := month_add((9,23), offset)):     
            return season.summer, end
        else: 
            return season.fall, end_fall
    
    def run(self):
        self.environment.timestamp += 15*60
        with self.lock:
            pass
            #weather simulation
        time.sleep(15*60)
        #sleep(15 Minuten)



    