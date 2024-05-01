from fit445 import makeDf,fitCurves
import os
import pandas as pd
import matplotlib.pyplot as plt
from confidenceFun import tolArea,taPlot

def makeDf(folder):
    dict = {}
    for i in os.listdir(''.join([folder,'/'])):
        fold = i.split(' ')
        inst = i
        dict[inst] = fitCurves(''.join([folder,'/',i,'/']))


    newDict = {'inst':[],'r2':[]}
    for i in dict:
        for u in dict[i]:
            newDict['inst'].append(i)
            newDict['r2'].append(u)


    # print(newDict)


    df = pd.DataFrame(newDict)
    return df

def makeCompound(df,sortBy,compWhat):
    
    smallDF = {}
    for indx,val in enumerate(df[sortBy]):
        if val not in smallDF:
            smallDF[val] = [df[compWhat][indx]]
        else:
            smallDF[val].append(df[compWhat][indx])
    return list(smallDF.values())


no = makeCompound(makeDf('byInstNoThump'),'inst','r2')
yes = makeCompound(makeDf('byInstThump'),'inst','r2')



taPlot(no,0.1,0.9,'C0','no thump')
taPlot(yes,0.1,0.9,'g','thump')
plt.show()
