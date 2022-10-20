import matplotlib.pyplot as plt
import numpy as np
# Pick a starting point for your random walk
x0 = 0.
# Pick a standard deviation for your random walk
sigma = 0.1
# Pick the number of steps you want to simulate
n = 10000
# How many different sample paths of the process do you want to simulate
n_paths = 10
# We will be plotting in here:
fig, ax = plt.subplots()
# Loop over the paths
for _ in range(n_paths):
    # Simulate a single path
    X = np.ndarray((n + 1,))
    X[0] = x0
    for t in range(1, n + 1):
        Zt = np.random.randn()
        X[t] = X[t-1] + sigma * Zt
    # Let's plot it
    ax.plot(range(n+1), X)
ax.set_xlabel('$n$ (steps)')
ax.set_ylabel('$X_n$');
plt.show()