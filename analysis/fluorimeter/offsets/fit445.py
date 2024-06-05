"""fit an exponential decay to 445 PCR curve"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from scipy.optimize import curve_fit
from confidenceFun import r2,tukey
from scipy import stats
from findP import findP


colors = ['C0','C1','C2','C3','C4','C5','C6','C7','C8','C9']            #default list of matplotlib plot colors
instList = [604,608,609,610,617,619,620,622,623,625]                    #list of inst

def expon(x,a,b,c,d):                               #base exponential decay function
    return a*np.exp(-b*x+d)+c



def fitCurves(folder):                                      #loops through data in folder and fits expon decay to each 445 curve
                                                            #calculates r2 value and returns list of all r2
    rr = []
    for indx,val in enumerate(os.listdir(folder)):
        
        data = pd.read_csv(''.join([folder,val]))           #get data from file
        pcr445 = np.array(data['445'])
        cycle = np.arange(0,len(pcr445))
        try:
            popt,pcov = curve_fit(expon,cycle,pcr445)       #fit exponential
            rr.append(r2(pcr445,expon(cycle,*popt)))        #r2
        except:
            rr.append(0)
            pass
        
    return rr



def makeDf(data,popName):                       # 
    dict = {'pop':[],'r2 val':[]}
    for indx,val in enumerate(data):
        for u in val:
            dict['pop'].append(popName[indx])
            dict['r2 val'].append(u)
    df = pd.DataFrame(dict)
    return df

def byInst(folder,inst):
    inst = str(inst)
    thumpFold = ''.join([folder,'/official ',inst,' thump/'])
    noThumpFold = ''.join([folder,'/official ',inst,' no thump/'])
    thump = fitCurves(thumpFold)
    noThump = fitCurves(noThumpFold)

    df = makeDf([thump,noThump],[' '.join([inst,'thump']),' '.join([inst,'no thump'])])
    # df.boxplot(by='pop')
    # plt.show()
    print(inst)
    print(tukey(df,'pop','r2 val',0.1))

# for i in instList:
    
#     byInst('expandedTilt/byInst',i)
    # time.sleep(10)
def compR2():
    thumpTiltRR = fitCurves('expandedTilt/official thump/')
    noThumpTiltRR = fitCurves('expandedTilt/official no thump/')
    thumpRR = fitCurves('expandedNominal/official thump/')
    noThumpRR = fitCurves('expandedNominal/official no thump/')


    df = makeDf([thumpRR,noThumpRR],['thump','no thump'])
    # df.boxplot(by='pop')
    # plt.show()
    # print(df)
    print(np.mean(thumpRR))
    print(np.mean(noThumpRR))
    # print(np.mean(thumpBackRR))
    print('THIS COMPARES ALL THUMPER TO ALL NO THUMPER R2 VALUES')
    print(tukey(df,'pop','r2 val',0.1))
tilt = findP('expandedTiltData.xlsx')
noTilt = findP('expandedData.xlsx')
pThumpTilt = tilt[0][0]/tilt[0][1]
pNoThumpTilt = tilt[1][0]/tilt[1][1]
pThumpNoTilt = noTilt[0][0]/noTilt[0][1]
pNoThumpNoTilt = noTilt[1][0]/noTilt[1][1]
# pBack = 1/10

k = 1
n = 100
probThumpTilt = stats.binom.pmf(k,n,pThumpTilt)
probNoThumpTilt = stats.binom.pmf(k,n,pNoThumpTilt)
probThumpNoTilt = stats.binom.pmf(k,n,pThumpNoTilt)
probNoThumpNoTilt = stats.binom.pmf(k,n,pNoThumpNoTilt)


# print(probThump,probNoThump)

x = np.arange(0,n)
plt.bar(x,stats.binom.pmf(x,n,pThumpNoTilt),label='thumper no tilt')
plt.bar(x,stats.binom.pmf(x,n,pNoThumpNoTilt),label='no thumper no tilt')
plt.bar(x,stats.binom.pmf(x,n,pThumpTilt),label='thumper tilt')
plt.bar(x,stats.binom.pmf(x,n,pNoThumpTilt),label='no thumper tilt')
# plt.bar(x,stats.binom.pmf(x,n,pBack),label='thump tilt back')
plt.legend()
plt.ylabel('Probability of x Runs with Data Offsets')
plt.xlabel(''.join(['Number of Runs with Data Offsets']))
plt.grid()
plt.show()