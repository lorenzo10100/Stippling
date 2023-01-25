import numpy as np 
from Point import Point

def sampling(sample, gray, threshold, rng=np.random.default_rng()):
    pts = np.zeros([sample], dtype=(np.float64, 2))
    bounds = gray.shape
    hist = {key : [] for key in range(0, threshold+1)}
    roulette = np.zeros(threshold+1)
    for x in range(0, bounds[0]):
        for y in range(0, bounds[1]):
            intensity = np.uint8(gray[x][y])
            if intensity in hist:
                hist[intensity].append(Point(np.float64(x),np.float64(y)))
    roulette[0] = 256*len(hist[0])
    for i in range(1, len(roulette)):
        roulette[i] = roulette[i-1] + (256-i)*len(hist[np.uint8(i)])

    for i in range(len(pts)):
        ball = rng.integers(0, len(roulette)-1)
        bucket = np.uint8(np.searchsorted(roulette, ball))
        if hist[bucket] != []:
            p = hist[bucket][rng.integers(0, len(hist[bucket]))]
            p.x += rng.random(dtype=np.float64)
            p.y += rng.random(dtype=np.float64)
            pts[i] = (p.x, p.y)
    return pts