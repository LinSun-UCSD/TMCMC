import numpy as np


def normalize(vector):
    for i in range(vector.shape[1]):
        vector[:, i] = vector[:, i]/(np.sign(vector[0, i]) * np.sqrt(vector[0, i]**2))
    return vector
