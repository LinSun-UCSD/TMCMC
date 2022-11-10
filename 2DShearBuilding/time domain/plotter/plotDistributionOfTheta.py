import numpy as np
import matplotlib.pyplot as plt
import pickle


def plotDistributionOfTheta(mytrace, xlabels, stage, trueValues, rows, cols):
    samples = mytrace[stage][0]
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams["font.size"] = 12
    plt.figure(figsize=(12, 6.5))
    for i in range(samples.shape[1]):
        plt.subplot(rows, cols, i + 1)
        plt.hist(samples[:, i], facecolor='b', alpha=0.7,rwidth=0.5, bins=25)
        plt.xlabel(xlabels[i])
        plt.ylabel("Num. of Samples")
        plt.axvline(trueValues[i], color='r',linestyle='--', lw=2)
        plt.grid("auto")
    plt.tight_layout()

