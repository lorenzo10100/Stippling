import numpy as np


def rescaleFloat64s(float_array, new_Min, new_Max):
    """
    Funzione che scala un array di float64 in un range [new_Min, new_Max]
    @param float_array: array di float64
    @param new_Min: nuovo minimo a cui scalare
    @param new_Max: nuovo massimo a cui scalare
    @return: array scalato
    """
    old_Min = np.max(float_array)
    rescaled = np.zeros(len(float_array), dtype=np.float64)
    for i, flo in enumerate(float_array):
        rescaled[i] = new_Min + (new_Max - new_Min) * flo / old_Min
    return rescaled
