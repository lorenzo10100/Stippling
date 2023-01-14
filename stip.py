
from Point import Point
import numpy as np
from scipy.spatial import *
import PDF as pd


def Centroids(sites, pd, bounds, step):
    siteCentroids = dict()
    siteIntensities = dict()
    sitePoints = dict()
    for _, site in enumerate(sites):
        site = site[0], site[1]
        siteCentroids[site] = Point(0, 0)
    kd = cKDTree(sites)
    x, y = np.meshgrid(np.arange(0, bounds[0], step), np.arange(0, bounds[1], step))
    points = np.c_[(y.ravel(), x.ravel())]
    for p in points:
        x, y = p[0], p[1]
        _, index = kd.query([[x, y]], p=2)
        index = index[0]
        nearest = sites[index][0], sites[index][1]
        weight = pd[int(x)][int(y)]
        centroid = siteCentroids[nearest]
        centroid.x += weight * x
        centroid.y += weight * y
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


