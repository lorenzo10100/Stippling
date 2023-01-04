import cv2 as cv
import numpy as np

#The following function is used to generate the PDF (probability density function) of a given image (gray)
def makePDF(gray):
    img = cv.imread(gray)
    bounds = img.shape
    pdf = np.zeros((bounds[0], bounds[1]), dtype=np.float64)
    for x in range(bounds[0]):
        for y in range(bounds[1]):
            pdf[x][y] = 255 - np.float64(img[x][y][0])
    return pdf