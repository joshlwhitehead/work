import os
import pandas as pd

base = list(pd.read_csv('covidContData/swapRaw/inst.csv')['cons'])

toChange = pd.read_csv('covidContData/swapRaw/fmax.csv')
changed = {}
for i in toChange.columns:
    changed[i] = []

toChange = toChange.to_dict('list')


for indx,val in enumerate(toChange['consumableId']):
    if val in base:
        for i in changed.keys():
            changed[i].append(toChange[i][indx])


df = pd.DataFrame(changed)
df.to_csv('covidContData/swapRaw/fmax.csv')
