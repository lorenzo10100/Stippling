import numpy as np 
from scipy.spatial import cKDTree
import samp as sp
import gray as gr
import time

class KDTree:
    def __init__(self, points):
        self.tree = cKDTree(points)
        
    def find_nearest_neighbor(self, point):
        dist, index = self.tree.query(point, p=2)
        return self.tree.data[index], dist




    


if __name__ == "__main__":
    nPoints = 20000
    threshold = 200
    inPath = 'data/images/colosseo.jpeg'
    gray = gr.gray(inPath)
    bounds = gray.shape
    sites = sp.sampling(nPoints, gray, threshold, np.random.default_rng(seed=int(time.time())))
    x, y = np.meshgrid(np.arange(0, bounds[0], 1), np.arange(0, bounds[1], 1))
    points = np.c_[(x.ravel(), y.ravel())]
    kd = KDTree(sites)
    for p in points:
        nearest, _ = kd.find_nearest_neighbor(p)
        print(nearest)