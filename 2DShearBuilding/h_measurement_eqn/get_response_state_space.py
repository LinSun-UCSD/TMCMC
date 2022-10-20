import numpy as np
from get_mode_state_space import get_mode_state_space


# state space model:
# x(t) = Ac*x_dot(t) + Bc*u(t)
# y(t) = Cc*x(t) + Dc*u(t)

def get_response_normalized_modal_eq(S, Bc, T, Cc, Dc, u):
    temp = np.linalg.lstsq(T, Bc, rcond=None)[0]
    Gamma = np.diag(temp.reshape((temp.shape[0],)))
    X = np.real(np.matmul(np.matmul(T, Gamma), S))
    y = np.real(np.matmul(np.matmul(np.matmul(Cc, T), Gamma), S) + np.matmul(Dc, u.reshape((1, len(u)))))
    return y, X, Gamma


# this is to get the response from state-space
def get_response_state_space(Ac, Bc, Cc, Dc, u, t):
    DOF = len(Ac[0]) / 2
    T, Lambda = get_mode_state_space(Ac)
    n2 = Lambda.shape[0]  # state space dimension
    # initialize
    N = len(u)
    s = np.zeros((n2, N), dtype=complex)
    s_dot = np.zeros((n2, N), dtype=complex)
    # calculate the normalized complex modal response ‘s'
    for j in range(n2):
        for m in range(N - 1):
            c2 = (u[m + 1] - u[m]) / (t[m + 1] - t[m])
            c1 = u[m] - c2 * t[m]
            tau = t[m + 1] - t[m]
            temp = s[j, m] + c2 / Lambda[j] * t[m] + c1 / Lambda[j] + c2 / (Lambda[j] ** 2)
            s[j, m + 1] = temp * np.exp(Lambda[j] * tau) \
                          - c2 / Lambda[j] * t[m + 1] \
                          - (c1 / Lambda[j] + c2 / (Lambda[j] ** 2))
            s_dot[j, m + 1] = temp * np.exp(Lambda[j] * tau) * Lambda[j] - c2 / Lambda[j]
    y, X, Gamma = get_response_normalized_modal_eq(s, Bc, T, Cc, Dc, u)
    return y, X, s, s_dot, T, Gamma
