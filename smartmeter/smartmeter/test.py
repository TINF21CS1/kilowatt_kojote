import numpy as np
import math
import random

def rotate_left(lst, amount):
    return lst[amount:] + lst[:amount]

def initialize_shape(matrix, center, radius, id):
    """
    Initialize the shape in the matrix by setting the pixels within the given radius of the center to 1.
    """
    x_center, y_center = center
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            if (x - x_center) ** 2 + (y - y_center) ** 2 <= radius ** 2:
                matrix[x, y] = id
    return matrix

def get_angle(center, start):
    angle_radians = math.atan2(center[1] - start[1], center[0] - start[0])
    angle = (angle_radians / (math.pi / 4))+0.1
    angle_rounded = int(round(angle))
    angle_adjusted = (6-angle_rounded)%8
    return angle_adjusted

def find_next_pixel(matrix, start, center, id, path = [], direction='clockwise'):
    """
    Find the next pixel to color in the clockwise direction.
    This function needs to identify the next pixel that is 0 (uncolored) but adjacent to at least one 1 (colored pixel).
    `start` is the starting point for the search.
    """
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # Right, Down, Left, Up
    if direction != 'clockwise':
        directions = directions[::-1]

    x_start, y_start = start
    for dx, dy in rotate_left(directions, get_angle(start, center)):
        x, y = x_start + dx, y_start + dy
        if 0 <= x < matrix.shape[0] and 0 <= y < matrix.shape[1]:
            if matrix[x, y] == None:
                return (x, y)
            elif(matrix[x,y] != id and (x,y) not in path):
                #print(x,y)
                #print(matrix)
                path.append((x,y))
                return find_next_pixel(matrix, (x,y), center, id, path)
            elif((x,y) in path):
                print('')
        elif x<0:
            return find_next_pixel(matrix, (0,y-1), center, id)
        elif x>matrix.shape[0]:
            return find_next_pixel(matrix, (0,y+1), center, id)
        elif y<0:
            return find_next_pixel(matrix, (x-1,0), center, id)
        elif y>matrix.shape[1]:
            return find_next_pixel(matrix, (x+1,0), center, id)
    return None

def grow_shape(matrix, center, id):
    """
    Grow the shape from its center by coloring one pixel at a time in a clockwise direction.
    """
    # Initialize the shape

    # Starting point for the growth
    start = center

    #for _ in range(steps):
    next_pixel = find_next_pixel(matrix, start, center, id)
    if next_pixel is None:
        #break  # No more pixels to color
        return matrix, None
    if(random.random() < 0.75):
        matrix[next_pixel] = id
        #print(matrix)
    start = next_pixel

    return matrix, next_pixel
if False:
    print(get_angle((5,5), (5,6)))
    print(get_angle((5,5), (6,6)))
    print(get_angle((5,5), (6,5)))
    print(get_angle((5,5), (6,4)))
    print(get_angle((5,5), (5,4)))
    print(get_angle((5,5), (4,4)))
    print(get_angle((5,5), (4,5)))
    print(get_angle((5,5), (4,6)))

# Example usage
x, y = 10, 10  # Matrix size
matrix = np.full((x, y), None)
center1 = (4, 4)
center2 = (6, 7)
initial_radius = 0
steps = 40

#matrix[6,6] = 'MM'
#matrix[6,7] = 'MM'
#matrix[7,6] = 'MM'
#matrix[7,7] = 'MM'
#matrix[7,8] = 'MM'
#matrix[8,8] = 'MM'
#matrix[9,8] = 'MM'
#matrix[8,9] = 'MM'
#matrix[9,9] = 'MM'

matrix = initialize_shape(matrix, center1, initial_radius, 1)

matrix = initialize_shape(matrix, center2, initial_radius, 2)

for _ in range(steps):
    if(center1 != None):
        matrix, center1 = grow_shape(matrix, center1, 1)
    if(center2 != None):
        matrix, center2 = grow_shape(matrix, center2, 2)
print(matrix)