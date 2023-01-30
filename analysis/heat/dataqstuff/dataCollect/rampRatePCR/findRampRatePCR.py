import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy import stats
import pandas as pd
import os


def rr(temps,times):
    derivs = []
    for i in range(len(temps)):
        a,b = np.polyfit(times[i],temps[i],1)
        derivs.append(a)
        plt.plot(times[i],temps[i],'o')
        plt.plot(times[i],a*np.array(times[i])+b)
    plt.show()
    return derivs

folder = 'data/'


derivTotH = []
derivTotNameH = []
derivTotC = []
derivTotNameC = []
for i in os.listdir(folder):


    

    with open(''.join([folder,i]),'r') as readFile:
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


    for u in file:
        if 'Start PCR' in u:
            start = True
        if 'goto' in u and 'Controlled' not in u and float(u.split()[-1]) > 85:
            heatCollect = True
            coolCollect = False
            # heat.append([])
        elif 'goto' in u and 'Controlled' not in u and float(u.split()[-1]) < 65:
            heatCollect = False
            coolCollect = True
        elif 'MELT' in u:
            start = False

        if start and 'DATAQ:' in u:

            try:
                if heatCollect and len(heat[countH]) != 0 and heat[countH][-1]-float(u.split()[4].strip(',')) > 10:
                    heat.append([])
                    timeH.append([])
                    countH+=1
                elif coolCollect and len(cool[countC]) != 0 and float(u.split()[4].strip(','))-cool[countC][-1] > 10:
                    cool.append([])
                    timeC.append([])
                    countC+=1
            except:
                pass
            
            
            if heatCollect:
                heat[countH].append(float(u.split()[4].strip(',')))
                try:
                    timeH[countH].append(float(file[countLines-1].split()[0].strip('()'))/1000)
                except:
                    timeH[countH].append(float(file[countLines+1].split()[0].strip('()'))/1000)

            elif coolCollect:
                cool[countC].append(float(u.split()[4].strip(',')))
                try:
                    timeC[countC].append(float(file[countLines-1].split()[0].strip('()'))/1000)
                except:
                    timeC[countC].append(float(file[countLines+1].split()[0].strip('()'))/1000)
      
        
        countLines += 1

    count = 0
    for j in range(len(heat)):
        if len(heat[count]) <= 2:
            heat.remove(heat[count])
            timeH.remove(timeH[count])
            count += 1
    count = 0      
    for j in range(len(cool)):
        if len(cool[count]) <= 2:
            cool.remove(cool[count])
            timeC.remove(timeC[count])
            count += 1


    for k in rr(heat,timeH):
        derivTotH.append(k)
        derivTotNameH.append(i)
    for k in rr(cool,timeC):
        derivTotC.append(k)
        derivTotNameC.append(i)


    
    print(timeH[1])



dfHeat = pd.DataFrame({'run':derivTotNameH,'rr':derivTotH})
dfCool = pd.DataFrame({'run':derivTotNameC,'rr':derivTotC})

dfHeat.boxplot('rr',by='run')
plt.show()
dfCool.boxplot('rr',by='run')
plt.show()
# dF.boxplot('rr',by='type')
# plt.show()























# def testNorm(dist,dF,label):                            #data must be dataframe
#     if stats.anderson(dF.rr,dist=dist)[0] < stats.anderson(dF.rr,dist=dist)[1][2]:
#         print(''.join([label,' data ',dist]))
#     else:
#         print(''.join([label,' data not ',dist]))|
#         print(stats.anderson(dF.rr,dist=dist))
#         x = np.linspace(min(dF.rr),max(dF.rr))
#         dF.hist('rr',density=True)
#         plt.plot(x,stats.norm.pdf(x,loc=np.mean(dF.rr),scale=np.std(dF.rr)))
#         plt.show()

# testNorm('norm',dFB,'')

# m_compMM = pairwise_tukeyhsd(endog=dF.rr, groups=dF.type, alpha=.05)
# print(m_compMM)

# formula = 'rr ~ type' 
# model = ols(formula, dF).fit()
# aov_table = anova_lm(model, typ=2)
# print(aov_table)