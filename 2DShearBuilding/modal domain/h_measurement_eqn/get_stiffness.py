import numpy as np


# this is calculated the stiffness matrix of a 2D shear building
def get_stiffness(k, DOF, k0):
    if len(k) == DOF:
        temp = np.zeros((2, 2, k.shape[0]))
        for i in range(len(k)):
            temp[:, :, i] = np.array([[k[i], -k[i]], [-k[i], k[i]]]).reshape((2, 2))


    K_global = np.zeros((DOF, DOF))
    for i in range(DOF - 1):
        K_global[i:i + 2, i:i + 2] = K_global[i:i + 2, i:i + 2] + temp[:, :, i + 1]
    K_global[0, 0] = K_global[0, 0] + temp[0, 0, 0]
    return K_global
