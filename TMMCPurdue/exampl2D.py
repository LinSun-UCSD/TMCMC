import matplotlib.pyplot as plt
import numpy as np
# lin Sun
# email: lsun@ucsd.edu
# Pick a starting point for your random walk
x0 = np.zeros((2,))
# Pick a standard deviation for your random walk
sigma1 = 0.1
sigma2 = 0.1
Sigma = np.diag([sigma1 ** 2, sigma2 ** 2])
A = np.linalg.cholesky(Sigma)
# Pick the number of steps you want to simulate
n = 10000
# How many different sample paths of the process do you want to simulate
n_paths = 1
# We will be plotting in here:
fig, ax = plt.subplots()
# Loop over the paths
for _ in range(n_paths):
    # Simulate a single path
    X = np.ndarray((n + 1, 2))
    X[0, :] = x0
    for t in range(1, n + 1):
        Zt = np.random.randn(2)
        X[t, :] = X[t-1] + np.dot(A, Zt)
    # Let's plot it
    ax.plot(X[:, 0], X[:, 1], lw=1)
ax.set_xlabel('$X_{n1}$')
ax.set_ylabel('$X_{n2}$')
plt.show()