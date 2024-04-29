import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from confidenceFun import CI,tukey
from pcr_fit import findLeastSquaresCq


folderMelt = 'raw/baselineMelt'
folderPCR = 'raw/baselinePCR'

nameConvention = {
    'melt start':['Initial Melt Value','RFU'],
    'melt stop':['Final Melt Value','RFU'],
    'melt range':['Melt Range','RFU'],
    'fmax':['Fmax','RFU'],
    'mean pcr':['445 Baseline','RFU'],
    'pcr start':['Initial PCR Value','RFU'],
    'pcr stop':['Final PCR Value','RFU'],
    'cq':['Cq','Cycle'],
    'reverse cq':['Reverse Cq','Cycle'],
    'pcr min':['Minimum PCR Value','RFU'],
    'instrument':'Instrument'
}

channels = [415,445,480,515,555,590,630,680,'NIR','CLR','DARK']
def readCsv(folder,file,chan):
    sheet = pd.read_csv('/'.join([folder,file]))
    return list(sheet[str(chan)])


def reverseCq(pcr):    
    cq = 25
    reversePCR = list(reversed(pcr[:cq]))

    cyclesReverse = np.arange(0,len(reversePCR))
    
    cqReverse = findLeastSquaresCq([cyclesReverse,reversePCR])[0]
    realCqReverse = len(reversePCR) - cqReverse
    return realCqReverse


def makeDF(chan):
    dataByInst = {}
    runInfo = pd.read_csv('raw/baseline.csv')
    cupInfo = list(runInfo['cons'])
    instInfo = list(runInfo['inst'])
    fmaxInfo = pd.read_csv('raw/fmax.csv')
    cqInfo = pd.read_csv('raw/cq.csv')
    dataByInst['cup id'] = cupInfo
    dataByInst['instrument'] = instInfo
    dataByInst['fmax'] = fmaxInfo[str(chan)]
    dataByInst['cq'] = cqInfo[str(chan)]


    dataByInst['melt start'] = []
    dataByInst['melt stop'] = []
    dataByInst['melt range'] = []
    dataByInst['pcr start'] = []
    dataByInst['pcr stop'] = []
    dataByInst['pcr min'] = []
    dataByInst['reverse cq'] = []
    dataByInst['mean pcr'] = []
    dataByInst['mean pcr 90% ci'] = []


    for i in os.listdir(folderMelt):
        meltData = readCsv(folderMelt,i,chan)
        dataByInst['melt start'].append(meltData[0])
        dataByInst['melt stop'].append(meltData[-1])
        dataByInst['melt range'].append(meltData[0] - meltData[-1])
    for i in os.listdir(folderPCR):
        pcrData = readCsv(folderPCR,i,chan)
        dataByInst['pcr start'].append(pcrData[0])
        dataByInst['pcr stop'].append(pcrData[-1])
        dataByInst['pcr min'].append(min(pcrData)) 
        dataByInst['reverse cq'].append(reverseCq(pcrData))
        dataByInst['mean pcr'].append(np.mean(pcrData))
        ci90 = CI(pcrData,0.1)
        dataByInst['mean pcr 90% ci'].append((ci90[1]-ci90[0])/2)


    df = pd.DataFrame(dataByInst)
    return df


def makeCsv(chan):
    df = makeDF(chan)
    df.to_csv(''.join(['parsedData/',str(chan),'.csv']))


def compare(chan,sortBy,compWhat,alpha):
    df = makeDF(chan)
    
    try:
        df = df.dropna()
        # print(compWhat)
        print(tukey(df,sortBy,compWhat,alpha))
    except:
        print('cannot do TUKEY')
    df.boxplot(compWhat,by=sortBy)
    plt.ylabel(nameConvention[compWhat][1])
    plt.suptitle('')
    plt.xlabel(nameConvention[sortBy])
    plt.title(nameConvention[compWhat][0])
    plt.savefig(''.join([compWhat,'_boxplot.png']))


def makeCompound(chan,sortBy,compWhat):
    df = makeDF(chan)
    smallDF = {}
    for indx,val in enumerate(df[sortBy]):
        if val not in smallDF:
            smallDF[val] = [df[compWhat][indx]]
        else:
            smallDF[val].append(df[compWhat][indx])
    print(smallDF)

makeCompound(515,'instrument','fmax')
