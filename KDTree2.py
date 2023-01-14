import numpy as np 
from Point import Point, sortByX, sortByY

class Rectangle:
    def __init__(self, min: Point, max: Point):
        self.min = min
        self.max = max
    

class kdNode:
    def __init__(self, p: Point, splitByX: bool, left=None, right=None):
        self.p = p
        self.splitByX = splitByX
        self.left = left
        self.right = right


class KDTree:
    def __init__(self, root, rectangle):
        self.root = root
        self.rectangle = rectangle

    def findNearest(self, p: Point):
        return search(self.root, p, self.rectangle, np.inf)


def split(pts, splitByX):
    if len(pts) == 0:
       return None
    if splitByX:
        pts = sortByX(pts)
    else:
        pts = sortByY(pts)
    mid = len(pts)//2
    return kdNode(pts[mid], splitByX, split(pts[:mid], not(splitByX)), split(pts[mid+1:], not(splitByX)))
    
def makeKDTree(pts, rectangle):
    root = split(pts, True)
    return KDTree(root, rectangle)

def search(node : kdNode, target: Point, r: Rectangle, maxDistSqd: np.float64()):
    stack = [(node, r)]
    nearest = None
    distSqd = np.inf
    while stack:
        curr_node, curr_r = stack.pop()
        if curr_node is None:
            continue
        if curr_node.splitByX:
            leftBox = Rectangle(curr_r.min, Point(curr_node.p.x, curr_r.max.y))
            rightBox = Rectangle(Point(curr_node.p.x, curr_r.min.y), curr_r.max)
            leftTarget = target.x <= curr_node.p.x
        else:
            leftBox = Rectangle(curr_r.min, Point(curr_r.max.x, curr_node.p.y))
            rightBox = Rectangle(Point(curr_r.min.x, curr_node.p.y), curr_r.max)
            leftTarget = target.y <= curr_node.p.y
        if leftTarget:
            nearestNode, nearestBox = curr_node.left, leftBox
            furtherNode, furtherBox = curr_node.right, rightBox
        else:
            nearestNode, nearestBox = curr_node.right, rightBox
            furtherNode, furtherBox = curr_node.left, leftBox
        stack.append((nearestNode, nearestBox))
        if curr_node.splitByX:
            distance = abs(curr_node.p.x - target.x)
        else:
            distance = abs(curr_node.p.y - target.y)
        distance *= distance
        if np.isclose(distance, maxDistSqd, rtol=1e-5, atol=1e-8):
            continue
        distance = curr_node.p.getDistance(target)
        if distance < distSqd:
            nearest = curr_node.p
            distSqd = distance
            maxDistSqd = np.min([maxDistSqd, distSqd])
        stack.append((furtherNode, furtherBox))
    return nearest, np.float64(distSqd)

"""
The stack variable in the code is a list that is used to keep track of the nodes that need to be visited during the search. 
The pop() method is used to remove and return the last element from the list. 
This element is then assigned to the node and r variables, which are used in the search algorithm.

In the search function, the stack is initialized with the root node of the tree and the rectangle associated with that node. 
The algorithm then enters a loop that continues as long as there are elements in the stack. 
Inside the loop, the node and r variables are set to the last element in the stack, and that element is removed from the stack using the pop() method. 
The algorithm then checks whether the node is None and, if it is, continues to the next iteration of the loop. 
If the node is not None, the algorithm performs the search operations as usual.

At the end of each iteration, the algorithm adds the nearest child node and the corresponding rectangle to the stack. 
This ensures that the algorithm will visit all of the nodes in the tree, from left to right and from top to bottom. 
When the stack is empty, the search is complete.

"""