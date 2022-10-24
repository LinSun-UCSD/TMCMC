import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import pickle


def plotPairGrid(pickleFileName, stageNum, thetaChoice, thetaName):
    with open(pickleFileName, 'rb') as handle1:
        mytrace = pickle.load(handle1)
    for stage in stageNum:
        plt.show()
        sns.set_theme(style="white")
        data = pd.DataFrame(mytrace[stage][0][:, thetaChoice])
        data.columns = thetaName
        g = sns.PairGrid(data, diag_sharey=False)
        g.map_upper(sns.scatterplot, s=15)
        g.map_lower(sns.kdeplot, levels=4)
        g.map_diag(sns.kdeplot, lw=2)
        g.tight_layout()
        plt.show()

