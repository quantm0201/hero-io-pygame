import math

from Component import Point

def normalize(vector):
    dis = math.sqrt(vector.x * vector.x + vector.y * vector.y)
    x = vector.x / dis
    y = vector.y / dis
    return Point(x, y)