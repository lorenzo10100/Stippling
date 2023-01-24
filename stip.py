from Point import Point
import numpy as np
from KDTree2 import *
import PDF as pd


def Centroids(sites, pd, bounds, step):
    siteCentroids = dict()
    siteIntensities = dict()
    sitePoints = dict()
    for _, site in enumerate(sites):
        site = site[0], site[1]
        siteCentroids[site] = Point(0, 0)
    kd = KDTree(sites)
    x, y = np.arange(0, bounds[0], step), np.arange(0, bounds[1], step)
    for i in x:
        for j in y:
            p = np.array([i, j])
            nearest, dist = kd.find_nearest_neighbor(p)
            nearest = tuple(nearest)
            weight = pd[int(i)][int(j)]
            centroid = siteCentroids[nearest]
            centroid.x += weight * i
            centroid.y += weight * j
            siteCentroids[nearest] = centroid
            if nearest in siteIntensities:
                siteIntensities[nearest] += weight
            else:
                siteIntensities[nearest] = weight
            if nearest in sitePoints:
                sitePoints[nearest] += 1
            else:
                sitePoints[nearest] = 1
    centroids = np.zeros((len(sites), 2), dtype=np.float64)
    densities = np.zeros(len(sites))
    i = 0
    for site, density in siteIntensities.items():
        centroid = siteCentroids[site]
        centroid.x /= density
        centroid.y /= density
        centroids[i] = np.array([centroid.x, centroid.y])
        densities[i] = siteIntensities[site] / sitePoints[site]
        i += 1
    return centroids, densities