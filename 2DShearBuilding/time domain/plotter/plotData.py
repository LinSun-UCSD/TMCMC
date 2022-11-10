import numpy as np
import matplotlib.pyplot as plt


def plotData(trueResponseFileName, noisyResponseFileName):
    trueResponse = np.load(trueResponseFileName)
    noisyResponse = np.load(noisyResponseFileName)
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams["font.size"] = 12
    plt.figure(figsize=(12,6))
    time = np.arange(0, trueResponse.shape[0], 1) / 50
    for i in range(trueResponse.shape[1]):
        plt.subplot(4, 2, i + 1)
        plt.plot(time, trueResponse[:, i],label='True', color="b")
        plt.plot(time, noisyResponse[:, i], label='Polluted', color="r",linestyle='--')
        plt.xlabel("Time [sec]")
        plt.ylabel("Normal. Accel.")

        plt.grid("auto")
        plt.xlim(0, time.max())
        plt.ylim(-1, 1)
    plt.tight_layout()