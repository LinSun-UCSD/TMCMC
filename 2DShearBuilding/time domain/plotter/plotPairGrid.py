import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import scipy.stats as stats
import numpy as np


def stdfunc(x, **kws):
    r = np.std(x) / np.mean(x)
    ax = plt.gca()
    ax.annotate("$\delta$ = %.2E" % r, xy=(.1, .9), xycoords=ax.transAxes, fontsize=10)


def corrfunc(x, y, **kws):
    r, _ = stats.pearsonr(x, y)
    ax = plt.gca()
    ax.annotate("r = {:.2f}".format(r), xy=(.1, .9), xycoords=ax.transAxes, fontsize=10)


def plotPairGrid(mytrace, stageNum, thetaChoice, thetaName):
    for stage in stageNum:
        plt.figure()
        plt.rcParams["font.family"] = "Times New Roman"
        plt.rcParams["font.size"] = 10
        sns.set(style="white", font_scale=0.8, font="Times New Roman")

        data = pd.DataFrame(mytrace[stage][0][:, thetaChoice])
        data.columns = thetaName
        g = sns.PairGrid(data, diag_sharey=False)
        plt.ticklabel_format(style='sci', axis='both', scilimits=(0, 0))

        g.map_upper(sns.scatterplot, s=10, color='b')
        g.fig.set_size_inches(12, 6.5)
        g.map_lower(sns.kdeplot, cmap='Blues_d')
        # g.map_diag(sns.kdeplot, lw=2)
        g.map_diag(sns.histplot, kde_kws={'color': 'k'}, bins=25)
        g.map_diag(stdfunc)
        g.map_lower(corrfunc)
        g.map_upper(corrfunc)
        g.tight_layout()
