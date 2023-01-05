import numpy as np


def rescaleFloat64s(float_array, new_Min, new_Max):
    """Rescale an array of float64s to a new range."""
    old_Min = np.max(float_array)
    rescaled = np.zeros(len(float_array), dtype=np.float64)
    for i, flo in enumerate(float_array):
        rescaled[i] = new_Min + (new_Max - new_Min) * flo/old_Min
    return rescaled