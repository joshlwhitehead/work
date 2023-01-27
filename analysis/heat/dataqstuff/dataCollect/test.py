import numpy as np
import matplotlib.pyplot as plt
import dataToVar as dat
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy import stats
import pandas as pd
import os
raw = 'test.txt'

with open(raw,'r') as readFile:
    file = readFile.readlines()


heat = [[]]
timeH = [[]]
cool = [[]]
timeC = [[]]
heatCollect = False
coolCollect = False
start = False
countLines = 0
countH = 0
countC = 0


# print(file.readlines())


for i in file:
    if 'Start PCR' in i:
        start = True
    if 'goto' in i and 'Controlled' not in i and float(i.split()[-1]) == 95:
        heatCollect = True
        coolCollect = False
        # heat.append([])
    elif 'goto' in i and 'Controlled' not in i and float(i.split()[-1]) == 55:
        heatCollect = False
        coolCollect = True
    elif 'MELT' in i:
        start = False
    try:
        if heatCollect and start and len(heat[countH]) != 0 and heat[countH][-1]-float(i.split()[4].strip(',')) > 10:
            heat.append([])
            timeH.append([])
            countH+=1
    except:
        pass
    # if coolCollect and start and len(cool[countC]) != 0 and float(i.split()[4].strip(','))-cool[countC][-1] > 10:
    #     cool.append([])
    #     countC+=1
    
    if heatCollect and start and 'DATAQ:' in i:
        heat[countH].append(float(i.split()[4].strip(',')))
        timeH[countH].append(float(file[countLines-1].split()[0].strip('()'))/1000)

    elif coolCollect and start and 'DATAQ:' in i:
        cool[countC].append(float(i.split()[4].strip(',')))
        timeC[countC].append(float(file[countLines-1].split()[0].strip('()'))/1000)
    
    
    countLines += 1



# plt.plot(cool[0],'o-')
# plt.show()
        

def rr():
    derivs = []
    ramp = []
    for i in range(len(heat)):
        a,b = np.polyfit(timeH[i],heat[i],1)
        derivs.append(a)
        ramp.append((heat[i][-1]-heat[i][0])/(timeH[i][-1]-timeH[i][0]))
    #     plt.plot(timeH[i],heat[i],'o')
    #     plt.plot(timeH[i],a*np.array(timeH[i])+b)
    # plt.show()
    return derivs,ramp

# print(heat[0])
# rr = []
# for i in range(len(heat)):
#     rr.append((heat[i][-1]-heat[i][0])/(timeH[i][-1]-timeH[i][0]))

# plt.boxplot(rr())
# plt.show()
derivTot = []
derivTotName = []
for i in rr()[0]:
    derivTot.append(i)
    derivTotName.append('a')
for i in rr()[1]:
    derivTot.append(i)
    derivTotName.append('b')

dF = pd.DataFrame({'type':derivTotName,'rr':derivTot})
dFA = pd.DataFrame({'type':['a']*len(rr()[0]),'rr':rr()[0]})
dFB = pd.DataFrame({'type':['b']*len(rr()[1]),'rr':rr()[1]})



def testNorm(dist,dF,label):                            #data must be dataframe
    if stats.anderson(dF.rr,dist=dist)[0] < stats.anderson(dF.rr,dist=dist)[1][2]:
        print(''.join([label,' data ',dist]))
    else:
        print(''.join([label,' data not ',dist]))
        print(stats.anderson(dF.rr,dist=dist))
        x = np.linspace(min(dF.rr),max(dF.rr))
        dF.hist('rr',density=True)
        plt.plot(x,stats.norm.pdf(x,loc=np.mean(dF.rr),scale=np.std(dF.rr)))
        plt.show()

# testNorm('norm',dFB,'')

# m_compMM = pairwise_tukeyhsd(endog=dF.rr, groups=dF.type, alpha=.05)
# print(m_compMM)

formula = 'rr ~ type' 
model = ols(formula, dF).fit()
aov_table = anova_lm(model, typ=2)
print(aov_table)