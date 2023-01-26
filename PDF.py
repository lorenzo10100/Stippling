import cv2 as cv
import numpy as np


def makePDF(gray: str):
    """
    Funzione che crea la funzione di densita', data un'immagine grigia in input
    @param gray: Immagine grigia
    @return ndarray di toni di colori 
    """

    img = cv.imread(gray)
    bounds = img.shape
    pdf = np.zeros((bounds[0], bounds[1]), dtype=np.float64)
    for x in range(bounds[0]):
        for y in range(bounds[1]):
            pdf[x][y] = 255 - np.float64(img[x][y][0])
    return pdf
