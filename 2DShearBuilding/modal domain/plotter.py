import _pickle as cPickle
import matplotlib.pyplot as plt
import pickle
import numpy as np
import seaborn as sns
import pandas as pd
from seaborn import scatterplot
from plotter.plotScatterTwoTheta import plotScatterTwoTheta
from plotter.plotMeanSTD import plotMeanSTD
from plotter.plotPairGrid import plotPairGrid
from plotter.plotRRMS import plotRRMS
from h_measurement_eqn.h_measurement_eqn import h_measurement_eqn
import os

# load trace
with open('mytrace.pickle', 'rb') as handle1:
    mytrace = pickle.load(handle1)
# mytrace stage m:
# samples, likelihood, weights, next stage ESS, next stage beta, resampled samples
trueValues = [1e9, 1e9]
stages = np.arange(0, 64)
thetaName = np.array(("k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8"))
pickleFileName ='mytrace.pickle'
# plotScatterTwoTheta(pickleFileName, trueValues, stages, labelsName=["k1", "k2"])

# # model evidence
# evidence = 1
# for i in range(len(mytrace)):
#     Wm = mytrace[i][2]
#     evidence = evidence * (sum(Wm) / len(Wm))

# stages = np.array((0,))
thetaChoice = np.array((1,2,3))

thetaName = thetaName[thetaChoice]
# plotPairGrid(pickleFileName, stages, thetaChoice, thetaName)
#
# mean, std, cov = plotMeanSTD(pickleFileName, np.array((1,2)), stages, trueValues)
#

# plot RRMS
GMinput = {
    "totalStep": 1000,  # earthquake record stpes
    "fs": 50,  # sampling rate
    "filename": 'NORTHR_SYL090',  # the earthquake file to load
    "path": os.getcwd() + "\\earthquake record"  # earthquake record folder
}
measure_vector = np.array([[0, 1, 2, 3, 4, 5, 6, 7]])
k0 = 1e9
TrueResponse = h_measurement_eqn(mytrace[60][0][1,:], GMinput, 1, GMinput["totalStep"], measure_vector,
                                 k0)
stage = np.arange(63,64)
trueValues = np.ones((8, 1), ) * 1e9
samples = np.array((1,2))
rrms = plotRRMS(pickleFileName, stage,samples, trueValues, h_measurement_eqn, measure_vector, k0, GMinput)