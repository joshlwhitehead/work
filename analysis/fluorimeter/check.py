import pandas as pd
import os

folder = 'covidInjMold/baselineRaw'
consList = list(pd.read_csv('/'.join([folder,'inst.csv']))['cons'])
cqData = pd.read_csv('/'.join([folder,'cq.csv']))
fmaxData = pd.read_csv('/'.join([folder,'fmax.csv']))


inCq = list(cqData['consumableId'])
inFmax = list(fmaxData['consumableId'])

for i in consList:
    if i not in inCq:
        print(i)