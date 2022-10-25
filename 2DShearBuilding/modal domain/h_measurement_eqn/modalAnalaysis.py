import numpy as np
import scipy.linalg as la
from .normalize import normalize as normalize

# this is to get the damping matrix
def modalAnalaysis(K, M):
    values, vectors = la.eig(K, M)
    values = np.real(values)
    index = np.argsort(values)
    values = values[index]
    vectors = vectors[:, index]
    vectors = normalize(vectors)
    return values, vectors
