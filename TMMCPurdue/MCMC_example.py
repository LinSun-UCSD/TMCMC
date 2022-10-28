import numpy as np
import matplotlib.pyplot as plt


def rwmetropolis(x0, log_h, n, sigma, args=()):
    """
    Random walk metropolis.

    :param x0:     The initial point (numpy array).
    :param log_h:  The logartihm of the function that is proportional to the density you want to sample from (function).
    :param n:      The maximum number of steps you want to take.
    :param sigma:  The standard deviation of the random walk proposal.
    :param args:   Any parameters to log_h.

    :returns:  X, acceptance_rate
    """
    x0 = np.array(x0)
    assert x0.ndim == 1
    # Dimensionality of space
    d = x0.shape[0]
    # A place to store the samples
    X = np.ndarray((n + 1, d))
    X[0, :] = x0
    # Previous value of log(h(x))
    log_h_p = log_h(x0, *args)
    # Keep track of how many samples are accepted
    count_accepted = 0
    # Start the simulation
    for t in range(1, n + 1):
        # Generation
        x = X[t - 1, :] + sigma * np.random.randn(d)
        # Calculation
        log_h_c = log_h(x, *args)  # Current value of log(h(x))
        alpha = min(1, np.exp(log_h_c - log_h_p))
        # Accept/Reject
        u = np.random.rand()
        if u <= alpha:  # Accept
            X[t, :] = x
            log_h_p = log_h_c
            count_accepted += 1
        else:  # Reject
            X[t, :] = X[t - 1, :]
    # Empirical acceptance rate
    acceptance_rate = count_accepted / (1. * n)
    return X, acceptance_rate


def log_h(x):
    if x[0] < 0:
        return -1e99  # Negative values are not allowed - Give back something very negative
    return -10. * x[0]  # The log of h(x)


# Initialiazation:
x0 = np.array([10.])
# Parameters of the proposal:
sigma = [ 0.1]
# Number of steps
n = 10000
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 12
plt.figure(figsize=(6, 3.5))
for i in range(len(sigma)):
    X, acceptance_rate = rwmetropolis(x0, log_h, n, sigma[i])
    plt.subplot(len(sigma), 1, i+1)
    plt.plot(range(n + 1), X, lw=1, color='black')
    plt.xlabel('$n$ (steps)')
    plt.ylabel('$X_n$')
    plt.xlim(-100, n)
    plt.grid("auto")
    plt.title("$\sigma$" + "=" + str(sigma[i]) + " " + 'Acceptance rate: %1.2f' % acceptance_rate)
    print('Acceptance rate: %1.2f' % acceptance_rate)
plt.tight_layout()
plt.savefig("samples.png", dpi=700)
plt.show()
