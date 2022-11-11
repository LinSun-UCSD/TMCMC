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
from plotter.plotData import plotData
from plotter.createAnimation import createAnimation
from plotter.plotDistributionOfTheta import plotDistributionOfTheta
from h_measurement_eqn.h_measurement_eqn import h_measurement_eqn
import os
from tmcmc_mod import pdfs

# load trace
with open('mytrace.pickle', 'rb') as handle1:
    mytrace = pickle.load(handle1)
# mytrace stage m:
# samples, likelihood, weights, next stage ESS, next stage beta, resampled samples
trueValues = [1e9, 1e9, 1e9, 1e9, 1e9, 1e9, 1e9, 1e9, 0.05]
stages = np.arange(0, 52)
thetaName = np.array(("k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8", "R"))
# plotScatterTwoTheta(pickleFileName, trueValues, stages, labelsName=["k1", "k2"])

createAnimation(mytrace, trueValues, stages, thetaName, [5, 6, 7])

# thetaName = thetaName[thetaChoice]
# plotPairGrid(mytrace, stages, thetaChoice, thetaName)
# plt.savefig("pairgrid.png", dpi=800)
# plt.show()

# prior_mean = np.array([[1.14, 1.32, 0.35, 0.95, 0.87, 1.235, 0.935, 0.85]])
# plotDistributionOfTheta(mytrace, thetaName, 63, trueValues, rows=3, cols=3)
# plt.savefig("prior.png", dpi=800)
# plt.show()
# mean, std, cov = plotMeanSTD(mytrace, np.arange(0, 9), np.arange(0, len(mytrace)), trueValues,
#                              thetaName, rows=3, cols=3)
# plt.savefig("mean&std.png",dpi=800)
# plt.show()

# plot RRMS
# GMinput = {
#     "totalStep": 1000,  # earthquake record stpes
#     "fs": 50,  # sampling rate
#     "filename": 'NORTHR_SYL090',  # the earthquake file to load
#     "path": os.getcwd() + "\\earthquake record"  # earthquake record folder
# }
# measure_vector = np.array([[0, 1, 2, 3, 4, 5, 6, 7]])
# k0 = 1e9
# TrueResponse = np.load("TrueResponse.npy")
# stage = np.arange(0,1)
# trueValues = np.ones((8, 1), ) * 1e9
# samples = np.arange(0,250)
# rrms = plotRRMS(pickleFileName, stage,samples, trueValues, h_measurement_eqn, measure_vector, k0, GMinput)
