import numpy as np


# this is to get the system matrices in continuous time domain
def get_continuous_state_space(K, M, C, B, output_type):
    ndof = len(K[:, 1])
    temp1 = np.block([[np.zeros((ndof, ndof)), np.eye(ndof)]])
    temp2 = np.block([[np.linalg.lstsq(-M, K, rcond=None)[0], np.linalg.lstsq(-M, C, rcond=None)[0]]])
    Ac = np.block([[temp1], [temp2]])
    Bc = np.block([[np.zeros((ndof, 1))], [-B]])
    Cc = np.block([np.linalg.lstsq(-M, K, rcond=None)[0], np.linalg.lstsq(-M, C, rcond=None)[0]])
    if output_type == "abs":  # output is absolute acceleration
        Dc = np.zeros((ndof, 1))  # output is relative acceleration
    elif output_type == "rel":
        Dc = -B
    return Ac, Bc, Cc, Dc
