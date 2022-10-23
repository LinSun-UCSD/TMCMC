import _pickle as cPickle
import matplotlib.pyplot as plt
import pickle
import numpy as np
import seaborn as sns
import pandas as pd
from seaborn import scatterplot
from plotter.plotScatterTwoTheta import plotScatterTwoTheta
from plotter.plotMeanSTD import plotMeanSTD


# load trace
with open('mytrace.pickle', 'rb') as handle1:
    mytrace = pickle.load(handle1)
# mytrace stage m:
# samples, likelihood, weights, next stage ESS, next stage beta, resampled samples
trueValues = [1e9, 1e9]
stages = np.arange(0, 64)
labelsName = ["k1", "k2"]
pickleFileName ='mytrace.pickle'
# plotScatterTwoTheta(pickleFileName, trueValues, stages, labelsName)

# # model evidence
# evidence = 1
# for i in range(len(mytrace)):
#     Wm = mytrace[i][2]
#     evidence = evidence * (sum(Wm) / len(Wm))

# plot distribution\
plt.show()
sns.set_theme(style="white")
g = sns.PairGrid(pd.DataFrame(mytrace[-1][0][:, :8]), diag_sharey=False)
g.map_upper(sns.scatterplot, s=15)
g.map_lower(sns.kdeplot)
g.map_diag(sns.kdeplot, lw=12)
plt.show()
plt.close()
#
# mean, std, cov = plotMeanSTD(pickleFileName, np.array((1,2)), stages, trueValues)
