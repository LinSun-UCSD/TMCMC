import numpy as np
import matplotlib.pyplot as plt
import pickle


def plotMeanSTD(mytrace, thetaChoice, stageNum, trueValues, xlabels, rows, cols):
    mean = []
    std = []
    cov = []
    for stage in stageNum:
        Sm = mytrace[stage][0][:, thetaChoice]
        stageMean = np.mean(Sm, axis=0)
        mean.append(stageMean)
        stageSTD = np.std(Sm, axis=0)
        std.append(stageSTD)
        cov.append(stageMean / stageSTD)

    temp1 = np.array(mean) - np.array(std)
    temp2 = np.array(mean) + np.array(std)
    plt.figure()
    plt.rcParams["font.family"] = "times new roman"
    plt.rcParams["font.size"] = 12
    plt.figure(figsize=(12,6.5))
    for i in range(len(thetaChoice)):
        plt.subplot(rows,cols,i+1)
        upper = temp1[:, i] / trueValues[i]
        lower = temp2[:, i] / trueValues[i]
        plt.fill_between(stageNum, lower, upper, color=[0.75, 0.75, 0.75])
        plt.plot(stageNum, np.array(mean)[:, i]/trueValues[i], color="b")
        plt.grid("auto")
        plt.xlabel("Stage")
        plt.axhline(y=1, color='r', linestyle='--', lw=1.5)
        plt.ylabel(xlabels[i] + " /" + xlabels[i] + "$_{true}$")
        plt.xlim((stageNum[0], stageNum[-1]))
    plt.tight_layout()
    return mean, std, cov
