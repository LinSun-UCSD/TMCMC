import numpy as np

# this is calculate the stiffness matrix of a 2D shear building
def get_stiffness(k, DOF, measure_vector, k0):
    if len(k) == DOF:
        temp = np.zeros((2, 2, k.shape[0]))
        for i in range(len(k)):
            temp[:, :, i] = np.array([[k[i], -k[i]], [-k[i], k[i]]]).reshape((2,2))
    elif len(k) < DOF:
        temp_k = np.ones((DOF,))*k0
        for i in range(len(measure_vector[0])):
            temp_k[measure_vector[0,i]] = k[i]
        temp = np.zeros((2, 2, temp_k.shape[0]))
        for i in range(len(temp_k)):
            temp[:, :, i] = np.array([[temp_k[i], -temp_k[i]], [-temp_k[i], temp_k[i]]]).reshape((2, 2))

    K_global = np.zeros((DOF, DOF))
    for i in range(DOF-1):
        K_global[i:i+2, i:i+2] = K_global[i:i+2, i:i+2] + temp[:, :, i+1]
    K_global[0, 0] = K_global[0,0] + temp[0, 0, 0]
    return K_global
