import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from confidenceFun import CI,tukey,tolArea,taPlot,caPlot,anovaPrep,anova,confArea
from pcr_fit import findLeastSquaresCq
import time

contents = ['cq','fmax','mean pcr','melt range','melt start','melt stop','pcr min','pcr start','pcr stop','reverse cq']
# folderMelt = 'raw/baselineMelt'
# folderPCR = 'raw/baselinePCR'

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
    'instrument':'Instrument',
    'config':'Configuration'
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


def makeDF(chan,folderInst,folderPCR,folderMelt):
    
    dataByInst = {}
    if 'baseline' in folderInst:
        config = 0
    else:
        config = 1
    runInfo = pd.read_csv('/'.join([folderInst,'inst.csv']))
    cupInfo = list(runInfo['cons'])
    instInfo = list(runInfo['inst'])
    # print(instInfo)
    instInfo = [' - '.join([str(i),str(config)]) for i in instInfo]
    # print(instInfo)
    fmaxInfo = pd.read_csv('/'.join([folderInst,'fmax.csv']))
    cqInfo = pd.read_csv('/'.join([folderInst,'cq.csv']))
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
    dataByInst['config'] = []


    for i in os.listdir('/'.join([folderInst,folderMelt])):
        meltData = readCsv('/'.join([folderInst,folderMelt]),i,chan)
        dataByInst['melt start'].append(meltData[0])
        dataByInst['melt stop'].append(meltData[-1])
        dataByInst['melt range'].append(meltData[0] - meltData[-1])
    for i in os.listdir('/'.join([folderInst,folderPCR])):
        pcrData = readCsv('/'.join([folderInst,folderPCR]),i,chan)
        dataByInst['pcr start'].append(pcrData[0])
        dataByInst['pcr stop'].append(pcrData[-1])
        dataByInst['pcr min'].append(min(pcrData)) 
        dataByInst['reverse cq'].append(reverseCq(pcrData))
        dataByInst['mean pcr'].append(np.mean(pcrData))
        ci90 = CI(pcrData,0.1)
        dataByInst['mean pcr 90% ci'].append((ci90[1]-ci90[0])/2)
        dataByInst['config'].append(config)


    df = pd.DataFrame(dataByInst)
    return df


def makeCsv(chan):
    df = makeDF(chan)
    df.to_csv(''.join(['parsedData/',str(chan),'.csv']))


def compare(df,chan,sortBy,compWhat,alpha):
    
    try:
        df = df.dropna()
        # print(compWhat)
        print(tukey(df,sortBy,compWhat,alpha))
    except:
        print('cannot do TUKEY')
    df.boxplot(compWhat,by=sortBy)
    plt.ylabel(nameConvention[compWhat][1])
    plt.suptitle('')
    plt.xticks(rotation=30)
    plt.xlabel(nameConvention[sortBy])
    plt.title(nameConvention[compWhat][0])
    plt.savefig(''.join(['plots2/',str(chan),'_',compWhat,'_boxplot.png']))


def makeCompound(df,sortBy,compWhat):
    
    smallDF = {}
    for indx,val in enumerate(df[sortBy]):
        if val not in smallDF:
            smallDF[val] = [df[compWhat][indx]]
        else:
            smallDF[val].append(df[compWhat][indx])
    # print(df)
    # print(smallDF)
    compound = list(smallDF.values())
    for indx,val in enumerate(compound):
        new = [i for i in val if 0/i == 0]
        compound[indx] = new
    return compound


# makeCompound(415,'instrument','cq','baselineRaw','baselinePCR','baselineMelt')
def makeAllPlots():
    start = time.time()

    for i in channels:
        for u in contents:
            try:
                df = makeDF(i,'baselineRaw','baselinePCR','baselineMelt')
                df2 = makeDF(i,'swapRaw','swapPCR','swapMelt')
                dfComb = pd.concat([df,df2],ignore_index=1)
                compoundPop = makeCompound(df,'instrument',u)
                compoundPop2 = makeCompound(df2,'instrument',u)
              
                compare(dfComb,i,'instrument',u,0.1)
                # compare(515,'instrument','cq',0.1,'baselineRaw','baselinePCR','baselineMelt')
                plt.figure()
                plt.grid()
                caPlot(compoundPop,0.1,'b',u,i,0)
                caPlot(compoundPop2,.1,'g',u,i,1)
                
            except:
                print('cannot make',i,'-',u,'plots2')
            print(i,u)
            # time.sleep(10)

    end = time.time()
    print(end-start)

# makeAllPlots()
def compareAll():
    differences = []
    for i in channels:
        for u in contents:
            try:
                df1 = makeDF(i,'baselineRaw','baselinePCR','baselineMelt')
                com1 = makeCompound(df1,'instrument',u)
                ca1 = confArea(com1,0.1)[0][1]

                df2 = makeDF(i,'swapRaw','swapPCR','swapMelt')
                com2 = makeCompound(df2,'instrument',u)
                ca2 = confArea(com2,0.1)[0][1]

                prep = anovaPrep([ca1,ca2],[0,1],u,'config')
                tuk = tukey(prep,'config',u,0.1)
                if tuk.reject[0] == True:
                    if tuk.meandiffs[0] < 0:
                        differences.append([i,u,'new config is smaller'])
                    else:
                        differences.append([i,u,'new config is larger'])
                else:
                    print(i,u,'not different')
            except:
                print('could not do',i,u)
                print(ca1,ca2)
    for i in differences:
        print(i)
    
compareAll()
               