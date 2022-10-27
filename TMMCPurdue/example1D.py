import time

import matplotlib.pyplot as plt
import numpy as np

# Pick a starting point for your random walk
x0 = 0.
# Pick a standard deviation for your random walk
sigma = [0.1, 1]
# Pick the number of steps you want to simulate
n = 10000
# How many different sample paths of the process do you want to simulate
n_paths = 5
# We will be plotting in here:
plt.figure(figsize=(7, 6))
for j in range(len(sigma)):
    sig = sigma[j]
    plt.subplot(2, 1, j + 1)
    # Loop over the paths
    for _ in range(n_paths):
        # Simulate a single path
        X = np.ndarray((n + 1,))
        X[0] = x0
        for t in range(1, n + 1):
            Zt = np.random.randn()
            X[t] = X[t - 1] + sig * Zt
        # Let's plot it
        plt.plot(range(n + 1), X)
    plt.xlabel('$n$ (steps)')
    plt.ylabel('$X_n$')
    legenName = []
    for i in range(n_paths):
        legenName.append("path " + str(i + 1))
    plt.legend(legenName, loc="upper left")
    plt.title(r'$\sigma$' + "=" + str(sig))

    plt.xlim(0, n)
    plt.grid("auto")

plt.tight_layout()
plt.savefig("1D example.png")
plt.show(block=True)
