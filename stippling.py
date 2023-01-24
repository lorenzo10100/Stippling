from Point import Point
import numpy as np
from KDTree import *
import PDF as pd

def Centroids(sites, pd, bounds, step):
    siteCentroids = dict()
    siteIntensities = dict()
    sitePoints = dict()
    for _, site in enumerate(sites):
        siteCentroids[site] = Point(0, 0)
    box = Rectangle(Point(np.float64(0),np.float64(0)), Point(np.float64(bounds[0]), np.float64(bounds[1])))
    kd = makeKDTree(sites, box)
    x, y = np.meshgrid(np.arange(box.min.x, box.max.x, step), np.arange(box.min.y, box.max.y, step))
    pts = np.c_[x.ravel(), y.ravel()]
    for p in pts:
        pt = Point(p[0], p[1])
        nearest, _ = kd.findNearest(pt)
        weight = pd
        weight = weight[int(p[0])][int(p[1])]
        centroid = siteCentroids[nearest]
        centroid.x += weight * pt.x
        centroid.y += weight * pt.y
        siteCentroids[nearest] = centroid
        if nearest in siteIntensities:
            siteIntensities[nearest] += weight
        else:
            siteIntensities[nearest] = weight
        if nearest in sitePoints:
            sitePoints[nearest] += 1
        else:
            sitePoints[nearest] = 1
    centroids = [Point(0, 0) for _ in range(len(sites))]
    densities = [np.float64(0) for _ in range(len(sites))]
    i = 0
    print(len(siteIntensities))
    print(len(siteCentroids))
    print(len(sitePoints))
    for site, density in siteIntensities.items():
        centroid = siteCentroids[site]
        centroid.x /= density
        centroid.y /= density
        centroids[i] = centroid
        densities[i] = siteIntensities[site] / sitePoints[site]
        i += 1
    print(centroids)
    print(densities)
    return centroids, densities