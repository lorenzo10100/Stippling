import cv2 as cv
import numpy as np


def gray(path: str) -> np.ndarray:
    """
    Funzione molto semplice, che prende un percorso in cui è presente un'immagine e la trasforma
    nella rispettiva scala di grigi
    """
    img = cv.imread(path)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_name = path.split('/')[2].split('.')[0]
    ext = path.split('/')[2].split('.')[1]
    cv.imwrite('data/gray_images/gray_' + img_name + '.' + ext, gray)
    return gray
