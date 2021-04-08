import math
import Config as cf

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getValue(self):
        return (self.x, self.y)

    def addDelta(self, deltaX, deltaY):
        self.x += deltaX
        self.y += deltaY
        return self

def normalize(vector):
    dis = math.sqrt(vector.x * vector.x + vector.y * vector.y)
    x = vector.x / dis
    y = vector.y / dis
    return Point(x, y)

def rotateVector(vector, angle, clockWise = True):
    radian = angle * cf.DEGREE_TO_RADIAN
    if (not clockWise):
        radian = -radian

    x = vector.x * math.cos(radian) - vector.y * math.sin(radian)
    y = vector.x * math.sin(radian) + vector.y * math.cos(radian)
    return Point(x, y)

def getAngleBetweenVector(vector1, vector2):
    vec1 = normalize(vector1)
    vec2 = normalize(vector2)

    return math.acos(vec1.x * vec2.x + vec1.y * vec2.y) * cf.RADIAN_TO_DEGREE