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
    df.boxplot(by='inst')
    plt.xticks(rotation=20)
    plt.ylabel('R2 value')
    plt.xlabel('Instrument')
    plt.title('')
    plt.suptitle('')
    plt.show()
    return df



# makeDf('byInst')

print(tukey(makeDf('byInst'),'inst','r2',0.1))
print(anova(makeDf('byInst'),'inst','r2'))
def makeCompound(df,sortBy,compWhat):
    
    smallDF = {}
    for indx,val in enumerate(df[sortBy]):
        if val not in smallDF:
            smallDF[val] = [df[compWhat][indx]]
        else:
            smallDF[val].append(df[compWhat][indx])
    return list(smallDF.values())


# no = makeCompound(makeDf('byInstNoThump'),'inst','r2')
# yes = makeCompound(makeDf('byInstThump'),'inst','r2')

# dfNew = pd.DataFrame({'thump':confArea(yes,0.1)[0][1],
#                       'no thump':confArea(no,.1)[0][1]})
# dictClean = {'pop':[],'r2':[]}
# for i in dfNew:
#     for u in dfNew[i]:
#         dictClean['pop'].append(i)
#         dictClean['r2'].append(u)
# dfClean = pd.DataFrame(dictClean)

# print(tukey(dfClean,'pop','r2',.1))


# caPlot(no,0.1,'C0','no thump')
# caPlot(yes,0.1,'g','thump')
# plt.grid()
# plt.legend()
# plt.show()
