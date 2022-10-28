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

x0 = np.array([10.])
# Parameters of the proposal:
sigma = 0.1
# Number of steps
n = 100000

X, acceptance_rate = rwmetropolis(x0, log_h, n, sigma)
# How many samples do you want to burn?
burn = 400
# How many samples do you want to throw in between?
thin = 40 # Keep one every ten samples (k*)
# Here are the remaining samples:
X_rest = X[burn:X.shape[0]:thin]
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 12
fig, ax = plt.subplots()
ax.acorr(X_rest[:, 0], detrend=plt.mlab.detrend_mean, maxlags=100, color='k')
ax.set_xlim(0, 100)
ax.set_ylabel("$R_{xx}$(" + r'$\tau$' + ")")
ax.set_xlabel("Lags (samples)")
plt.grid("auto")
fig.set_size_inches(6,3)
fig.tight_layout()
# plt.savefig("autocorrelation.png",dpi=800)

fig, ax = plt.subplots()
ax.plot(X_rest, lw=1., color = 'k')
ax.set_xlabel('steps')
ax.set_ylabel('$X_{n+bk}$')
plt.grid("auto")
fig.set_size_inches(6,3)
fig.tight_layout()
plt.savefig("samples.png",dpi=800)

fig, ax = plt.subplots()
idx = np.arange(1, X_rest.shape[0] + 1)
X_ave = np.cumsum(X_rest) / idx
ax.plot(idx, X_ave, label='Sampling average of $\mathbb{E}[X_n]$')
ax.plot(idx, 0.10 * np.ones(idx.shape[0]), label='True $\mathbb{E}[X_n]$')
plt.legend(loc='best')
plt.grid("auto")
fig.set_size_inches(6,3)
fig.tight_layout()
# plt.savefig("mean.png",dpi=800)

fig, ax = plt.subplots()
X2_ave = np.cumsum(X_rest ** 2) / idx
X_var = X2_ave - X_ave ** 2
ax.plot(idx, X_var, label='Sampling average of $\mathbb{V}[X_n]$')
ax.plot(idx, 0.01 * np.ones(idx.shape[0]), label='True $\mathbb{V}[X_n]$')
plt.legend(loc='best')
ax.set_xlabel('$m$');
fig.set_size_inches(6,3)
fig.tight_layout()
plt.grid("auto")
plt.savefig("variance.png",dpi=800)

fig, ax = plt.subplots()
plt.hist(X_rest, density=True,alpha=0.25, bins=50);
xx = np.linspace(0, 1, 100)
ax.plot(xx, 10. * np.exp(-10. * xx), label="Analytical form")
plt.legend(loc='best')
ax.set_xlabel('$x$')
ax.set_ylabel('$\pi(x)$')
fig.set_size_inches(6,3)
fig.tight_layout()
plt.grid("auto")
plt.savefig("histogram.png",dpi=800)
plt.show()