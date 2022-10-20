import numpy as np
import scipy.linalg as la


# this is to get the damping matrix
def get_classical_damping(K, M, damping, plot):
    values = la.eigvals(K, M)
    omega = np.sort(np.sqrt(np.real(values)))
    mode = damping["mode"]
    damping_ratio = damping["ratio"]
    temp = np.array([[1 / omega[mode[0] - 1], omega[mode[0] - 1]], [1 / omega[mode[1] - 1], omega[mode[1] - 1]]])
    a = 2 * np.matmul(np.linalg.inv(temp), np.transpose(np.array([[damping_ratio[0], damping_ratio[1]]])))
    C = a[0] * M + a[1] * K  # get the classical damping
    damping_mode = a[0] / 2 * np.true_divide(1, omega) + a[1] / 2 * omega
    return C, omega, a, damping_mode
