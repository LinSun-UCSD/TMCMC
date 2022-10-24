import numpy as np


# get the eigen values of Ac
def get_mode_state_space(Ac):
    D, T = np.linalg.eig(Ac)
    return T, D