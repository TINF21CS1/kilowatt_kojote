import random
import math
import numpy as np

from .constants import MAX_WIDTH, MAX_HEIGHT
from .util.trigonometry import calc_point_angle, calc_point_point, point_inside, shared_neighbours, calc_angle, calc_dist

class pressure_area():
    def __init__(self, center: (float, float), size: int, id: int, neighbors: list()):
        self.size = size
        self.center = center
        self.neighbours = neighbors
        self.type = random.choice(['high', 'low'])
        self.center = (int(center[0]), int(center[1]))
        self.last_grow = (center[0]+1, center[1])
        self.id = id

    def calculate_chance(self, size, distance, adjacend) -> float:
        x = distance/size
        k = 9 #steepness
        adjacend_factor = (((adjacend+4)/8)**0.25)
        logistical_decrease =  (1/(1+math.e**(k*(x-1))))
        return logistical_decrease * adjacend_factor

    def rotate_left(self, lst, amount):
        return lst[amount:] + lst[:amount]

    def get_angle(self, center, start):
        angle_radians = math.atan2(center[1] - start[1], center[0] - start[0])
        angle = (angle_radians / (math.pi / 4))+0.1
        angle_rounded = int(round(angle))
        angle_adjusted = (6-angle_rounded)%8
        return angle_adjusted

    #def find_next_pixel(matrix, start, center, direction='clockwise'):
    def find_next_pixel(self, map, start, center, direction='clockwise'):
        """
        Find the next pixel to color in the clockwise direction.
        This function needs to identify the next pixel that is 0 (uncolored) but adjacent to at least one 1 (colored pixel).
        `start` is the starting point for the search.
        """
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # Right, Down, Left, Up
        if direction != 'clockwise':
            directions = directions[::-1]

        x_start, y_start = start
        for dx, dy in self.rotate_left(directions, self.get_angle(start, center)):
            x, y = x_start + dx, y_start + dy
            if 0 <= x < map.shape[0] and 0 <= y < map.shape[1]:
                if map[x, y] == None:
                    return (x, y)
        return None

    def grow(self, map):
    #def grow_shape(matrix, center, initial_radius, steps):
        """
        Grow the shape from its center by coloring one pixel at a time in a clockwise direction.
        """

        # Starting point for the growth
        start = self.center

        next_pixel = self.find_next_pixel(map, start, self.center)
        if next_pixel is None:
            return False  # No more pixels to color
        if(random.random() < 0.75):
            map[next_pixel] = self.id
            #print(matrix)
        start = next_pixel
        return





        match calc_angle(self.center, self.last_grow):
            case angle if angle < 90:
                angle_offset = 0
            case angle if angle >= 90 and angle < 180:
                angle_offset = 1
            case angle if angle >= 180 and angle < 270:
                angle_offset = 2
            case angle if angle >= 270:
                angle_offset = 3
        
        for i in range(20): #limit unnecessary?
            limit_error = False
            match (angle_offset)%4:
                case 0:
                    if(self.last_grow[1]<=1):
                        limit_error = True
                    else:
                        next_grow = (self.last_grow[0], self.last_grow[1]-1)
                case 1:
                    if(self.last_grow[0]>=MAX_WIDTH-2):
                        limit_error = True
                    else:
                        next_grow = (self.last_grow[0]+1, self.last_grow[1])
                case 2:
                    if(self.last_grow[1]>=MAX_HEIGHT-2):
                        limit_error = True
                    else:
                        next_grow = (self.last_grow[0], self.last_grow[1]+1)
                case 3:
                    if(self.last_grow[0]<=1):
                        limit_error = True
                    else:
                        next_grow = (self.last_grow[0]-1, self.last_grow[1])
            if(limit_error):
                angle_offset = (angle_offset + 1)%4
            else:
                match map[next_grow[0], next_grow[1]]:
                    case None:
                        adjacend = 0
                        for j in range(3):
                            for k in range(3):
                                
                                if(first:=(next_grow[0] -1 +j) in range(MAX_WIDTH) and \
                                   (second:=(next_grow[1] -1 +k) in range(MAX_HEIGHT)) and \
                                    map[next_grow[0] -1 +j][next_grow[1] -1 +k] == self.id):
                                    adjacend += 1
                        if(random.random() < (chance := self.calculate_chance(self.size, calc_dist(self.center, next_grow), adjacend))):
                            map[next_grow[0]][next_grow[1]] = self.id
                        if(chance < 0.01):
                            return False
                        self.last_grow = (next_grow[0], next_grow[1])
                        return True
                    case self.id:
                        angle_offset = (angle_offset + 1)%4
                    case _:
                        self.last_grow = (next_grow[0], next_grow[1])

        
class pressure_map():
    def __init__(self) -> None:
        self.list = list()
        #self.map = create_nd_list([MAX_WIDTH, MAX_HEIGHT], None)
        self.map = np.full((MAX_WIDTH, MAX_HEIGHT), None)
        threshold = float(1)
        while sum([math.pi*obj.size**2 for obj in self.list]) / (MAX_HEIGHT*MAX_WIDTH) < threshold:
            if self.add_circle() == False:
                threshold *= 0.99
        for i, area in enumerate(self.list):
            area.id = i
            self.map[area.center[0], area.center[1]] = area.id

        active_areas = self.list.copy()
        while(len(active_areas) > 0):
            if(active_areas[0].grow(self.map) == False):
                active_areas.pop(0)
            else:
                active_areas.append(active_areas.pop(0))

        print("pressure areas populated")
        print(self.map)

    def random_size(self):
        return random.randint(2, 5)
        #return random.randint(1000, 10000)
    
    def add_circle(self):
        match(old_len:=len(self.list)):
            case 0:
                center = (random.randint(0, MAX_WIDTH), random.randint(0, MAX_HEIGHT))
                size = self.random_size()
                self.list.append(pressure_area(center, size, len(self.list), list()))
            case 1:
                neighbor = self.list[0]
                size = self.random_size()
                angle = random.randint(0, 360)
                center = calc_point_angle(neighbor.center, neighbor.size + size, angle)
                if(point_inside(center)):
                    self.list.append(pressure_area(center, size, len(self.list), [neighbor]))
                    neighbor.neighbours.append(self.list[-1])
                    return True
                else:
                    return False
            case _:
                size = self.random_size()
                weights = [len(obj.neighbours) for obj in self.list]
                weights_sum = sum(weights)
                weights = [weight/weights_sum for weight in weights]
                while True:
                    neighbor1: pressure_area = random.choices(self.list, weights ,k=1)[0]
                    neighbor2: pressure_area = random.choice(neighbor1.neighbours)
                    if shared_neighbours(neighbor1.neighbours, neighbor2.neighbours) < 2 or len(self.list) <= 3:
                        break
                center = calc_point_point(neighbor1.center, neighbor2.center, neighbor1.size + size, neighbor2.size + size)
                if(len(center) == 0):
                    return False
                else:
                    center = center[0] #Fix: With two results need to select the result that does not overlap
                if(point_inside(center)):
                    self.list.append(pressure_area(center, size, len(self.list), [neighbor1, neighbor2]))
                    neighbor1.neighbours.append(self.list[-1])
                    neighbor2.neighbours.append(self.list[-1])
                    return True
                else:
                    return False