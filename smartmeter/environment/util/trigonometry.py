import math

from ..constants import MAX_WIDTH, MAX_HEIGHT

def calc_point_angle(x, d, theta_degrees):
    # Convert angle from degrees to radians
    theta_radians = math.radians(theta_degrees)
    
    # Calculate new coordinates
    x2 = x[0] + d * math.cos(theta_radians)
    y2 = x[1] + d * math.sin(theta_radians)
    
    return (x2, y2)

def calc_point_point(x, y, d1, d2):
    x1, y1 = x
    x2, y2 = y

    # Distance between points X and Y
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Check if there is no solution (circles don't intersect)
    if d > d1 + d2 or d < abs(d1 - d2) or d == 0 and d1 != d2:
        return []

    # Find a and h
    a = (d1**2 - d2**2 + d**2) / (2 * d)
    h = math.sqrt(d1**2 - a**2)

    # Find P, the point where the line through the circle intersection points crosses the line between the circle centers
    px = x1 + a * (x2 - x1) / d
    py = y1 + a * (y2 - y1) / d

    # Find the intersection points
    intersection1 = (px + h * (y2 - y1) / d, py - h * (x2 - x1) / d)
    intersection2 = (px - h * (y2 - y1) / d, py + h * (x2 - x1) / d)

    if(intersection1 == intersection2):
        return [intersection1]
    else:
        return [intersection1, intersection2]

def point_inside(point):
    if point[0] < 0 or point[0] > MAX_WIDTH:
        return False
    if point[1] < 0 or point[1] > MAX_HEIGHT:
        return False
    return True

def shared_neighbours(list1, list2):
    amount = 0
    for elem in list2:
        if elem in list1:
            amount += 1
    return amount

def calc_angle(x, y):
    """
    Calculate the angle from y to x using atan2, then adjust it so that:
    - 0 degrees when y is above x,
    - 90 degrees when y is to the right of x,
    - 180 degrees when y is below x,
    - 270 degrees when y is to the left of x.
    """
    angle_radians = math.atan2(x[1] - y[1], x[0] - y[0])
    # Adding π/2 radians (90 degrees) to adjust the zero point
    adjusted_angle_radians = angle_radians + math.pi / 2
    # Converting to degrees and adjusting the range to [0, 360)
    adjusted_angle_degrees = math.degrees(adjusted_angle_radians) % 360
    return adjusted_angle_degrees

def calc_dist(x: int | float, y: int | float) -> list():
    return ((abs(x[0] - y[0]) ** 2 )+ (abs(x[1] - y[1])**2))**0.5