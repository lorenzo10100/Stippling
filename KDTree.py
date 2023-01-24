import numpy as np 
from Point import Point, sortByX, sortByY
import sampling as sp
import gray as gr
import time

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
    if node == None:
        return None, maxDistSqd
    if node.splitByX:
        leftBox = Rectangle(r.min, Point(node.p.x, r.max.y))
        rightBox = Rectangle(Point(node.p.x, r.min.y), r.max)
        leftTarget = target.x <= node.p.x
    else:
        leftBox = Rectangle(r.min, Point(r.max.x, node.p.y))
        rightBox = Rectangle(Point(r.min.x, node.p.y), r.max)
        leftTarget = target.y <= node.p.y
    if leftTarget:
        nearestNode, nearestBox = node.left, leftBox
        furtherNode, furtherBox = node.right, rightBox
    else:
        nearestNode, nearestBox = node.right, rightBox
        furtherNode, furtherBox = node.left, leftBox
    nearest, distSqd = search(nearestNode, target, nearestBox, maxDistSqd)
    if node.splitByX:
        distance = abs(node.p.x - target.x)
    else:
        distance = abs(node.p.y - target.y)
    distance *= distance
    if distance > maxDistSqd:
        return nearest, maxDistSqd
    distance = node.p.getDistance(target)
    if distance < distSqd:
            nearest = node.p
            distSqd = distance
            maxDistSqd = distSqd
    temp_nearest, temp_distSqd = search(furtherNode, target, furtherBox, maxDistSqd)
    if temp_distSqd < distSqd:
        nearest = temp_nearest
        distSqd = temp_distSqd
    return nearest, np.float64(distSqd)
        
