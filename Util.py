import math

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