import _pickle as cPickle
import matplotlib.pyplot as plt
import pickle
with open(r"mytrace.pickle", "rb") as input_file:
    post = cPickle.load(input_file)
k1_true = 1e9
k2_true = 1e9
#load trace
with open('mytrace.pickle', 'rb') as handle1:
    mytrace = pickle.load(handle1)

for i in range(len(mytrace)):
    plt.figure(figsize=(6, 5), dpi=100)
    plt.rc('xtick',labelsize=16)
    plt.rc('ytick',labelsize=16)
    plt.plot(k2_true,k1_true,'ro',label='True')
    Sm = mytrace[i][0]
    Wm = mytrace[i][2]
    if i == 0:
        betap = 0
    else:
        betap = mytrace[i-1][-2]
    plt.scatter(Sm[:,1],Sm[:,0],s=(Wm/sum(Wm))*1000,zorder=2)
    plt.xlim([0.4*(k2_true),1.2*(k2_true)])
    plt.ylim([0.8*(k1_true),2.2*(k1_true)])
    #plt.legend(fontsize=12)
    plt.title(r'$ \beta_{%d} $ = %.5f' % (i,betap),fontsize=16)
    plt.ylabel('$k_1$',fontsize=16)
    plt.xlabel('$k_2$',fontsize=16)
    plt.tight_layout()
    #plt.savefig(f"Plots/p{i}")
plt.show()
# model evidence
evidence = 1
for i in range(len(mytrace)):
    Wm = mytrace[i][2]
    evidence = evidence*(sum(Wm)/len(Wm))