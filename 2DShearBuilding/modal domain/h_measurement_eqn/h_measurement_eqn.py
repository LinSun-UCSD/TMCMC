import numpy as np
from .get_mass import get_mass
from .get_stiffness import get_stiffness
from .modalAnalaysis import modalAnalaysis


def h_measurement_eqn(parameter_SP, measure_vector, k0, m0):
    # input K, M and C
    DOF = len(parameter_SP)

    M_global = get_mass(m0, DOF)
    K_global = get_stiffness(parameter_SP, DOF, k0)
    values, vectors = modalAnalaysis(K_global, M_global)
    values = values.reshape((1, len(values)))
    y = np.zeros((vectors.shape[0] + values.shape[0], vectors.shape[1]))
    y[0, :] = values[0, :]
    # max eigen
    maxEigen = y[0,-1]
    # y[0,:] = y[0,:]/maxEigen
    y[1:y.shape[0], :] = vectors
    maxEigenVec = np.zeros((y.shape[1],))
    for i in range(y.shape[1]):
        maxEigenVec[i] = np.linalg.norm(y[1:y.shape[0], i])
        # y[1:y.shape[0], i] = y[1:y.shape[0], i]/maxEigenVec[i]
    return y, maxEigen, maxEigenVec
