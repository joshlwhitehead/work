import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from scipy.optimize import curve_fit
from confidenceFun import r2,tukey
from scipy import stats
import time


colors = ['C0','C1','C2','C3','C4','C5','C6','C7','C8','C9']
instList = [604,608,609,610,617,619,620,622,623,625]

def expon(x,a,b,c,d):
    return a*np.exp(-b*x+d)+c



def fitCurves(folder):
    
    rr = []
    for indx,val in enumerate(os.listdir(folder)):
        
        data = pd.read_csv(''.join([folder,val]))
        pcr445 = np.array(data['445'])
        cycle = np.arange(0,len(pcr445))
        try:
            popt,pcov = curve_fit(expon,cycle,pcr445)
            # plt.plot(cycle,expon(cycle,*popt),color=colors[indx])
            rr.append(r2(pcr445,expon(cycle,*popt)))
        except:
            rr.append(0)
            pass
    #     plt.plot(cycle,pcr445,'o',color=colors[indx])
        
    #     plt.grid()
    #     plt.ylabel('RFU')
    #     plt.xlabel('Cycle')

    # plt.savefig('test.png')
        
    return rr



def makeDf(data,popName):
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
for i in instList:
    
    byInst('expandedNominal/byInst',i)
    # time.sleep(10)
# thumpRR = fitCurves('expandedNominal/official thump/')
# noThumpRR = fitCurves('expandedNominal/official no thump/')
# # thumpBackRR = fitCurves('thumpBack/')


# df = makeDf([thumpRR,noThumpRR],['thump','no thump'])
# # df.boxplot(by='pop')
# # plt.show()
# # print(df)
# print(np.mean(thumpRR))
# print(np.mean(noThumpRR))
# # print(np.mean(thumpBackRR))
# print('THIS COMPARES ALL THUMPER TO ALL NO THUMPER R2 VALUES')
# print(tukey(df,'pop','r2 val',0.1))

# pThump = 32.5/69
# pNoThump = 67/70
# # pBack = 1/10

# k = 1
# n = 100
# probThump = stats.binom.pmf(k,n,pThump)
# probNoThump = stats.binom.pmf(k,n,pNoThump)
# # probBack = stats.binom.pmf(k,n,pBack)


# # print(probThump,probNoThump)

# x = np.arange(0,n)
# plt.bar(x,stats.binom.pmf(x,n,pThump),label='thumper')
# plt.bar(x,stats.binom.pmf(x,n,pNoThump),label='no thumper')
# # plt.bar(x,stats.binom.pmf(x,n,pBack),label='thump tilt back')
# plt.legend()
# plt.ylabel('Probability of x Runs with Data Offsets')
# plt.xlabel(''.join(['Number of Runs with Data Offsets (Out of ',str(n),')']))
# plt.grid()
# plt.show()