import numpy as np
import matplotlib.pyplot as plt
import pickle


def plotMeanSTD(pickleFileName, thetaChoice, stageNum, trueValues):
    with open(pickleFileName, 'rb') as handle1:
        mytrace = pickle.load(handle1)
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
    for i in range(len(thetaChoice)):
        plt.figure()
        upper = temp1[:, i] / trueValues[i]
        lower = temp2[:, i] / trueValues[i]
        plt.fill_between(stageNum, lower, upper, color=[0.75, 0.75, 0.75])
        plt.plot(stageNum, np.array(mean)[:, i]/trueValues[i], color="b")
        plt.grid("auto")
        plt.xlabel("Stage")
        plt.ylabel("theta")
        plt.xlim((stageNum[0], stageNum[-1]))
    plt.show()
    return mean, std, cov
