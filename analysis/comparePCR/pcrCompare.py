import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
import toleranceinterval as ti


data = pd.read_csv('BetaVAlpha.csv')
inst = data['inst']
cq = data['cq']
tm = data['tm']
fmax = data['fmax']
pcrNoise = data['pcr noise']
meltNoise = data['melt noise']
print(*set(inst))
dataOrg = {}
for indx,val in enumerate(inst):
    if val not in dataOrg.keys():
        dataOrg[val] = {
            'cq':[cq[indx]],
            'tm':[tm[indx]],
            'fmax':[fmax[indx]],
            'pcr noise':[pcrNoise[indx]],
            'melt noise':[meltNoise[indx]]
                        }     
    else:
        dataOrg[val]['cq'].append(cq[indx])
        dataOrg[val]['tm'].append(tm[indx])
        dataOrg[val]['fmax'].append(fmax[indx])
        dataOrg[val]['pcr noise'].append(pcrNoise[indx])
        dataOrg[val]['melt noise'].append(meltNoise[indx])

def sortByInstType(dataType):
    beta = []
    verif = []
    betaMean = []
    betaStd = []
    verifMean = []
    verifStd = []
    for i in dataOrg:
        if 'Beta' in i:
            beta.append(dataOrg[i][dataType])
            betaMean.append(np.mean(dataOrg[i][dataType]))
            betaStd.append(np.std(dataOrg[i][dataType]))
        else:
            verif.append(dataOrg[i][dataType])
            verifMean.append(np.mean(dataOrg[i][dataType]))
            verifStd.append(np.std(dataOrg[i][dataType]))
    
    meanTot = []
    instTot = []
    stdTot = []
    for indx,val in enumerate(betaMean):
        meanTot.append(val)
        instTot.append('Beta')
        stdTot.append(betaStd[indx])
    for indx,val in enumerate(verifMean):
        meanTot.append(val)
        instTot.append('Verif')
        stdTot.append(verifStd[indx])
    
    dF = {'instType':instTot,'mean':meanTot,'std':stdTot}

    return dF,(beta,verif),(betaMean,betaStd),(verifMean,verifStd)


def TI(sample):
    bound = ti.twoside.normal(sample,.9,.9)
    return bound[0]

def deliver(dataType):
    dF = sortByInstType(dataType)[0]
    betaX = sortByInstType(dataType)[2][0]
    betaY = sortByInstType(dataType)[2][1]
    verifX = sortByInstType(dataType)[3][0]
    verifY = sortByInstType(dataType)[3][1]

    alpha = 0.1

    formula = 'std ~ instType'
    model = ols(formula, dF).fit()
    aov_table = anova_lm(model, typ=1)
    # print(aov_table)


    m_compMult = pairwise_tukeyhsd(endog=dF['std'],groups=dF['instType'],alpha=alpha)
    print('stdev compare')
    print(m_compMult)
    m_compMult = pairwise_tukeyhsd(endog=dF['mean'],groups=dF['instType'],alpha=alpha)
    print('mean compare')
    print(m_compMult)




    betaMeanTI = TI(betaX)
    betaStdTI = TI(betaY)
    verifMeanTI = TI(verifX)
    verifStdTI = TI(verifY)

    plt.plot(betaX,betaY,'o',color='k',label='Beta')
    plt.plot(verifX,verifY,'o',color='g',label='Verification')
    
    plt.hlines(np.mean(betaY),betaMeanTI[0],betaMeanTI[1],lw=5)
    plt.vlines(np.mean(betaX),betaStdTI[0],betaStdTI[1],lw=5)
    plt.hlines(np.mean(verifY),verifMeanTI[0],verifMeanTI[1],lw=5)
    plt.vlines(np.mean(verifX),verifStdTI[0],verifStdTI[1],lw=5)
    plt.plot([np.mean(betaX),np.mean(verifX)],[np.mean(betaY),np.mean(verifY)],'o',color='r')
    
    plt.grid()
    plt.legend()
    plt.show()



deliver('cq')