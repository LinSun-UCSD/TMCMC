import numpy as np
import matplotlib.pyplot as plt


def plotData(trueResponseFileName, noisyResponseFileName, maxEigName):
    trueResponse = np.load(trueResponseFileName)
    noisyResponse = np.load(noisyResponseFileName)
    maxEig = np.load(maxEigName)
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams["font.size"] = 12
    plt.figure(figsize=(6,5))
    time = range(1, trueResponse.shape[1]+1)
    plt.plot(time, np.multiply(trueResponse[0, :], maxEig), label='True', color="b", marker='o')
    for i in range(noisyResponse.shape[2]):
        plt.plot(time, np.multiply(noisyResponse[0,:,i], maxEig), label= str(i+1) + 'th Measured',linestyle='--', marker='o')
        plt.xlabel("Mode")
        plt.ylabel("Eigenvalues")
        plt.grid("auto")
    plt.legend()
    plt.tight_layout()
    plt.figure(figsize=(8,6))
    for mod in range(trueResponse.shape[1]):
        plt.subplot(4,2,mod+1)
        plt.plot(time, trueResponse[1:trueResponse.shape[0], mod], marker='o', color='b')
        for i in range(noisyResponse.shape[2]):
            plt.plot(time, noisyResponse[1:trueResponse.shape[0], mod, i], marker='o',linestyle='--')
        plt.axhline(y=0, color='r', linestyle='-')
        plt.grid("auto")
        plt.xlabel("DOF")
    plt.tight_layout()