import _pickle as cPickle
import matplotlib.pyplot as plt
import pickle
import numpy as np
#import seaborn as sns
import pandas as pd
#from seaborn import scatterplot
from plotter.plotScatterTwoTheta import plotScatterTwoTheta
from plotter.plotMeanSTD import plotMeanSTD
#from plotter.plotPairGrid import plotPairGrid
from plotter.plotRRMS import plotRRMS
from plotter.plotData import plotData
from plotter.createAnimation import createAnimation
from plotter.plotDistributionOfTheta import plotDistributionOfTheta
from h_measurement_eqn.h_measurement_eqn import h_measurement_eqn
import os

# load trace
with open('mytrace.pickle', 'rb') as handle1:
    mytrace = pickle.load(handle1)
# mytrace stage m:
# samples, likelihood, weights, next stage ESS, next stage beta, resampled sampletrueValues = [1e9, 1e9]
stages = np.arange(0, len(mytrace))
thetaName = np.array(("k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8"))
pickleFileName = 'mytrace.pickle'
trueValues = np.ones((8, 1), ) * 1e9

# plotData("result\\TrueResponse.npy", "result\\NoisyTrueResponse.npy", "result\\maxEig.npy")
# plt.savefig("data.png", dpi=800)
# plt.show()
createAnimation(mytrace, trueValues, stages, ["k1", "k2", "k3"],[0, 1, 2])
# plotScatterTwoTheta(mytrace, trueValues, stages, ["k1", "k2"])
# plt.show()

# thetaChoice = np.arange(0, 8)
#
# thetaName = thetaName[thetaChoice]
# stages = np.arange(0, 1)
# plotPairGrid(mytrace, stages, thetaChoice, thetaName)
# plt.savefig("pairgrid.png", dpi=800)
# plt.show()
# prior_mean = np.array([[1.14, 1.32, 0.35, 0.95, 0.87, 1.235, 0.935, 0.85]])
# plotDistributionOfTheta(mytrace, thetaName, 28, trueValues, rows=4, cols=2)
# plt.savefig("prior.png", dpi=800)
# plt.show()

# stages = np.arange(0, 29)
# mean, std, cov = plotMeanSTD(mytrace, thetaChoice, stages, trueValues, thetaName, 4, 2)
# plt.savefig("mean&std.png",dpi=800)
# plt.show()
#

# plot RRMS

# measure_vector = np.array([[0, 1, 2, 3, 4, 5, 6, 7]])
# k0 = 1e9
#
# stage = np.arange(15, 16)
# trueValues = np.ones((8, 1), ) * 1e9
# samples = np.arange(0, 250)
# rrms = plotRRMS(pickleFileName, stage, samples, trueValues, h_measurement_eqn, measure_vector, k0)
# print(rrms)
