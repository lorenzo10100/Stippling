import numpy as np 
from Point2 import Point
import cv2 as cv

def sampling(sample, gray, threshold, rng=np.random.default_rng()):
    pts = [Point(0,0) for _ in range(sample)]
    bounds = gray.shape
    hist = dict()
    roulette = np.zeros(threshold+1)
    for x in range(0, bounds[0]):
        for y in range(0, bounds[1]):
            intensity = np.uint8(gray[x][y])
            if intensity <= threshold:
                if intensity in hist:
                    hist[intensity].append(Point(np.float64(x),np.float64(y)))
                else:
                    hist[intensity] = [Point(np.float64(x),np.float64(y))]
    roulette[0] = 256*len(hist[0])
    for i in range(1, len(roulette)):
        roulette[i] = roulette[i-1] + (256-i)*len(hist[np.uint8(i)])
    for i in range(len(pts)):
        ball = rng.integers(0, len(roulette)-1)
        bucket = np.uint8(np.searchsorted(roulette, ball))
        p = hist[bucket][rng.integers(0, len(hist[bucket]))]
        p.x += rng.random(dtype=np.float64)
        p.y += rng.random(dtype=np.float64)
        pts[i] = p
    return pts      


