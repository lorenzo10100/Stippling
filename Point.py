import numpy as np 

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point(%s, %s)" % (self.x, self.y)

    def __repr__(self):
        return self.__str__()
    
    def getDistance(self, other):
        return np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

def sortByX(array):
    return sorted(array, key=lambda point: point.x)
    
def sortByY(array):
    return sorted(array, key=lambda point: point.y)
