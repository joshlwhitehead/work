import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from confidenceFun import CI,tukey,caPlot,anovaPrep,confArea
from pcr_fit import findLeastSquaresCq


study = 'covidContData'
contents = ['cq','fmax','mean pcr','melt range','melt start','melt stop','pcr min','pcr start','pcr stop','reverse cq']
# folderMelt = 'raw/baselineMelt'
# folderPCR = 'raw/baselinePCR'

nameConvention = {                                      #keys are shorthand labels, values contain the actual label and the unit of measurement
    'melt start':['Initial Melt Value','RFU'],
    'melt stop':['Final Melt Value','RFU'],
    'melt range':['Melt Range','RFU'],
    'fmax':['Fmax','RFU'],
    'mean pcr':['Baseline','RFU'],
    'pcr start':['Initial PCR Value','RFU'],
    'pcr stop':['Final PCR Value','RFU'],
    'cq':['Cq','Cycle'],
    'reverse cq':['Reverse Cq','Cycle'],
    'pcr min':['Minimum PCR Value','RFU'],
    'instrument':'Instrument',
    'config':'Configuration'
}

channels = [415,445,480,515,555,590,630,680,'NIR','CLR','DARK']




def readCsv(folder,file,chan):                      # reads a .csv of fluorescence data and returns the data from a specific channel
    sheet = pd.read_csv('/'.join([folder,file]))
    return list(sheet[str(chan)])


def reverseCq(pcr):                                     #estimates the cycle where the PCR curve drops down to baseline aka the reverse cq
    cq = 25             #need to eliminate PCR rise/plateau                                           
    reversePCR = list(reversed(pcr[:cq]))               # uses the cq algorithm on the PCR curve ordered from last to first cycle

    cyclesReverse = np.arange(0,len(reversePCR))
    
    cqReverse = findLeastSquaresCq([cyclesReverse,reversePCR])[0]
    realCqReverse = len(reversePCR) - cqReverse
    return realCqReverse




def makeDF(chan,folderInst,folderPCR,folderMelt,study):             #takes melt, pcr, cq, fmax data and organizes it by instrument in a dataframe 
    folderInst = '/'.join([study,folderInst])

    
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
        # print(folderInst,folderMelt,i,chan)
        # print(meltData)
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

    # print(dataByInst.keys())
    df = pd.DataFrame(dataByInst)
    # print(df)
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
    plt.title(' '.join([str(chan),nameConvention[compWhat][0]]))
    plt.savefig(''.join(['plotsCovidCont/',str(chan),'_',compWhat,'_boxplot.png']))


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
    

    for i in channels:
        for u in contents:
            try:
                df = makeDF(i,'baselineRaw','baselinePCR','baselineMelt',study)
                df2 = makeDF(i,'swapRaw','swapPCR','swapMelt',study)
                dfComb = pd.concat([df,df2],ignore_index=1)
                compoundPop = makeCompound(df,'instrument',u)
                compoundPop2 = makeCompound(df2,'instrument',u)
                
                compare(dfComb,i,'instrument',u,0.1)
                plt.figure()
                plt.grid()
                caPlot(compoundPop,0.1,'C0',u,i,0)
                caPlot(compoundPop2,.1,'C1',u,i,1)
                
            except:
                print('cannot make',i,'-',u,'plotsCovidCont')
            print(i,u)
            # time.sleep(10)

# makeAllPlots()


def makeOnePlot():
    chan = '515'
    metric = 'fmax'
    df = makeDF(chan,'baselineRaw','baselinePCR','baselineMelt',study)
    compoundPop = makeCompound(df,'instrument',metric)
    plt.grid()
    caPlot(compoundPop,.1,'C0',metric,chan,0)
    
# makeOnePlot()

def compareAll():

    final = {'channel':[],'metric':[],'mean diff':[],'sig diff mean':[],'std diff':[],'sig diff std':[],
             'config 0 std of means':[],'config 0 std of stds':[],'config 1 std of means':[],'config 1 std of stds':[]}

    for i in channels:
        for u in contents:
            try:
                df1 = makeDF(i,'baselineRaw','baselinePCR','baselineMelt',study)
                com1 = makeCompound(df1,'instrument',u)
                ca1 = confArea(com1,0.1)
                mean1 = ca1[0][0]
                std1 = ca1[0][1]
                # meanCi1 = ca1[2][0][1] - ca1[2][0][0]
                # stdCi1 = ca1[2][1][1] - ca1[2][1][0]
                # print(mean1)
                stdMean1 = np.std(mean1)
                stdStd1 = np.std(std1)

                df2 = makeDF(i,'swapRaw','swapPCR','swapMelt',study)
                com2 = makeCompound(df2,'instrument',u)
                ca2 = confArea(com2,0.1)
                mean2 = ca2[0][0]
                std2 = ca2[0][1]
                # meanCi2 = ca2[2][0][1] - ca2[2][0][0]
                # stdCi2 = ca2[2][1][1] - ca2[2][1][0]
                stdMean2 = np.std(mean2)
                stdStd2 = np.std(std2)

                prepMean = anovaPrep([mean1,mean2],[0,1],u,'config')
                tukMean = tukey(prepMean,'config',u,0.1)
                prepStd = anovaPrep([std1,std2],[0,1],u,'config')
                tukStd = tukey(prepStd,'config',u,0.1)

                sigDiffMean = tukMean.reject[0]
                sigDiffStd = tukStd.reject[0]
                meanDiff = tukMean.meandiffs[0]
                stdDiff = tukStd.meandiffs[0]


                final['channel'].append(i)
                final['metric'].append(u)
                final['sig diff mean'].append(sigDiffMean)
                final['mean diff'].append(meanDiff)
                final['sig diff std'].append(sigDiffStd)
                final['std diff'].append(stdDiff)
                final['config 0 std of means'].append(stdMean1)
                final['config 0 std of stds'].append(stdStd1)
                final['config 1 std of means'].append(stdMean2)
                final['config 1 std of stds'].append(stdStd2)
            except:
                print('could not do',i,u)
                print(ca1,ca2)
    dfFull = pd.DataFrame(final)
    dfFull.to_csv('allDataCovidCont.csv')
    
# compareAll()





def instInstVar(mean,chan,metric):
    data = pd.read_csv('allDataCovidCont.csv')
    if mean == 1:
        comp = 'means'
    else:
        comp = 'stds'
    config0Tot = list(data[''.join(['config 0 std of ',comp])])
    config1Tot = list(data[''.join(['config 1 std of ',comp])])
    if chan == 0 and metric == 0:
        config0Mean = config0Tot
        config1Mean = config1Tot
    elif chan != 0 and metric == 0:
        config0Mean = []
        config1Mean = []
        channelCol = list(data['channel'])
        for indx,val in enumerate(channelCol):
            if val == str(chan):
                config0Mean.append(config0Tot[indx])
                config1Mean.append(config1Tot[indx])
    elif chan == 0 and metric != 0:
        config0Mean = []
        config1Mean = []
        metricCol = list(data['metric'])
        for indx,val in enumerate(metricCol):
            if val == metric:
                config0Mean.append(config0Tot[indx])
                config1Mean.append(config1Tot[indx])
    config0 = [0]*len(config0Mean)
    config1 = [1]*len(config1Mean)

    means = config0Mean + config1Mean
    configs = config0 + config1

    dict = {comp:means,'config':configs}
    df = pd.DataFrame(dict)
    return tukey(df,'config',comp,0.1)


def instToInstVar():
    me = [0,1]
    for i in me:
        for u in channels:
            try:
                res = instInstVar(i,u,0)
                rej = res.reject[0]
                dif = res.meandiffs[0]
                if rej == 1:
                    if i == 1:
                        print('means of',u,'are different')
                    else:
                        print('stds of',u,'are different')
                    if dif < 0:
                        print('config 0 is more variable')
                    else:
                        print('config 1 is more variable')
                    print()
            except:
                pass

# instToInstVar()


def runRunVar(mean):
    
    data = pd.read_csv('allDataCovidCont.csv')
    chan = data['channel']
    res = {}
    if mean == 1:
        diffData = data['mean diff']
        col = 'sig diff mean'
    else:
        diffData = data['std diff']
        col = 'sig diff std'
    for i in channels:
        pf = []
        diff = []
        for indx,val in enumerate(data[col]):
            if chan[indx] == str(i):
                diff.append(diffData[indx])
                if val == 1:
                    pf.append(1)
                else:
                    pf.append(0)
        res[i] = [np.mean(pf),np.mean(diff),np.std(diff)]
    return res

test = runRunVar(0)
for i in test:
    if test[i][0] > 0.5:
        print(i,round(test[i][1],1),'+/-',round(test[i][2],1),test[i][0])



# print(runRunVar(1)['CLR'])
               