import numpy as np 

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point(%s, %s)" % (self.x, self.y)

    def __repr__(self):
        return self.__str__()
    

    def __lt__(self, other):
        return self.x < other.x

def sortByX(array):
    return np.sort(array, axis=0)
    
def sortByY(array):
    return np.sort(array, axis=1)


if __name__ == "__main__":
    points = np.array([[4,9], [9,2], [8,3], [7,9], [10,5]])
    print(sortByX(points))
    print(sortByY(points))