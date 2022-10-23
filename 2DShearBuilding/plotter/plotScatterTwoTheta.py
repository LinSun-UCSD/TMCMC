import _pickle as cPickle
import matplotlib.pyplot as plt
import pickle

"""
@Author: Lin Sun
INPUT:
pickleFileName: picke file name
trueValues: list of two
stages: numpy array of stage to plot the stages scatter plot
labelsName: list of string to name xlabel and ylabel
"""


def plotScatterTwoTheta(pickleFileName, trueValues, stages, labelsName):
    with open(pickleFileName, 'rb') as handle1:
        mytrace = pickle.load(handle1)

    for i in stages:
        plt.figure(figsize=(6, 5), dpi=100)
        plt.rc('xtick', labelsize=16)
        plt.rc('ytick', labelsize=16)
        plt.plot(trueValues[1], trueValues[0], 'ro', label='True')
        Sm = mytrace[i][0]
        Wm = mytrace[i][2]
        if i == 0:
            betap = 0
        else:
            betap = mytrace[i - 1][-2]
        plt.scatter(Sm[:, 1], Sm[:, 0], s=(Wm / sum(Wm)) * 1000, zorder=2)
        plt.xlim([0.8 * (trueValues[1]), 1.2 * (trueValues[1])])
        plt.ylim([0.8 * (trueValues[0]), 1.2 * (trueValues[0])])
        plt.title(r'$ \beta_{%d} $ = %.5f' % (i, betap), fontsize=16)
        plt.ylabel(labelsName[0], fontsize=16)
        plt.xlabel(labelsName[1], fontsize=16)
        plt.tight_layout()
    plt.show()
    plt.close('all')