import numpy as np


def normalize(y):
    yNorm = np.zeros(y.shape)
    max = np.amax(np.abs(y), axis=0)
    for i in range(y.shape[1]):
        yNorm[:, i] = y[:, i]/max[i]
    return yNorm, max
