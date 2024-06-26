import pandas as pd
import os
import shutil

masterDir = 'covidContData'
masterBaselineDir = '/'.join([masterDir,'baselineRaw'])
masterSwapDir = '/'.join([masterDir,'swapRaw'])

posDir = 'covidContPosData'
posBaselineDir = '/'.join([posDir,'baselineRaw'])
posSwapDir = '/'.join([posDir,'swapRaw'])

negDir = 'covidContNegData'
negBaselineDir = '/'.join([negDir,'baselineRaw'])
negSwapDir = '/'.join([negDir,'swapRaw'])

baselinePCR = 'baselinePCR'
baselineMelt = 'baselineMelt'
swapPCR = 'swapPCR'
swapMelt = 'swapMelt'

inst = 'inst.csv'
fmax = 'fmax.csv'
cq = 'cq.csv'

def makeStuff(metric,swapOrBase):
    if metric == inst:
        cons = 'cons'
    else:
        cons = 'consumableId'
    if swapOrBase == 'swap':
        master = masterSwapDir
        pos = posSwapDir
        neg = negSwapDir
    else:
        master = masterBaselineDir
        pos = posBaselineDir
        neg = negBaselineDir

    full = pd.read_csv('/'.join([master,metric]))
    posFull = list(pd.read_csv('/'.join([pos,metric]))[cons])

    negFull = {}
    for i in full.columns:
        negFull[i] = []

    for indx,val in enumerate(full[cons]):
        if val not in posFull:
            for i in negFull.keys():
                negFull[i].append(full[i][indx])

    df = pd.DataFrame(negFull)
    df.to_csv('/'.join([neg,metric]))


def copyFiles(masterDir,posDir,negDir):
    allFilesList = os.listdir(masterDir)
    posFilesList = os.listdir(posDir)
    for i in allFilesList:
        if i not in posFilesList:
            shutil.copy('/'.join([masterDir,i]),'/'.join([negDir,i]))

copyFiles('/'.join([masterBaselineDir,baselineMelt]),'/'.join([posBaselineDir,baselineMelt]),'/'.join([negBaselineDir,baselineMelt]))

