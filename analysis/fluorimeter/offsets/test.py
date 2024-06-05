from fit445 import makeDf,fitCurves
import os
import pandas as pd
import matplotlib.pyplot as plt
from confidenceFun import tolArea,taPlot,tukey,confArea,caPlot,anova

def makeDf(folder):
    dict = {}
    for i in os.listdir(''.join([folder,'/'])):
        fold = i.split(' ')
        miss1 = fold[1:]
        inst = ' '.join(miss1)
        dict[inst] = fitCurves(''.join([folder,'/',i,'/']))


    newDict = {'inst':[],'r2':[]}
    for i in dict:
        for u in dict[i]:
            newDict['inst'].append(i)
            newDict['r2'].append(u)


    # print(newDict)


    df = pd.DataFrame(newDict)
    # df.boxplot(by='inst')
    # plt.xticks(rotation=20)
    # plt.ylabel('R2 value')
    # plt.xlabel('Instrument')
    # plt.title('')
    # plt.suptitle('')
    # plt.show()
    return df



# makeDf('byInst')
print('THIS COMPARES ALL INSTRUMENT, PROTOCOL COMBOS')
print(tukey(makeDf('expandedTilt/byInst'),'inst','r2',0.1))
print(anova(makeDf('expandedTilt/byInst'),'inst','r2'))
def makeCompound(df,sortBy,compWhat):
    
    smallDF = {}
    for indx,val in enumerate(df[sortBy]):
        if val not in smallDF:
            smallDF[val] = [df[compWhat][indx]]
        else:
            smallDF[val].append(df[compWhat][indx])
    return list(smallDF.values())


noThumpTilt = makeCompound(makeDf('expandedTilt/byInstNoThump'),'inst','r2')
thumpTilt = makeCompound(makeDf('expandedTilt/byInstThump'),'inst','r2')
noThumpNoTilt = makeCompound(makeDf('expandedNominal/byInstNoThump'),'inst','r2')
thumpNoTilt = makeCompound(makeDf('expandedNominal/byInstThump'),'inst','r2')

dfNew = pd.DataFrame({
    'thump tilt':confArea(thumpTilt,0.1)[0][1],
    'no thump tilt':confArea(noThumpTilt,.1)[0][1],
    'thump no tilt':confArea(thumpNoTilt,0.1)[0][1],
    'no thump no tilt':confArea(noThumpNoTilt,0.1)[0][1]
    })

dictClean = {'pop':[],'r2':[]}
for i in dfNew:
    for u in dfNew[i]:
        dictClean['pop'].append(i)
        dictClean['r2'].append(u)
dfClean = pd.DataFrame(dictClean)
print('THIS COMPARES MEAN MEANS OR MEAN STDEVS')
print(tukey(dfClean,'pop','r2',.1))
print(anova(dfClean,'pop','r2'))

caPlot(thumpTilt,0.1,'C0','thump tilt')
caPlot(noThumpTilt,0.1,'C1','no thump tilt')
caPlot(thumpNoTilt,0.1,'C2','thump no tilt')
caPlot(noThumpNoTilt,0.1,'C3','no thump no tilt')
plt.grid()
plt.legend()
plt.show()
