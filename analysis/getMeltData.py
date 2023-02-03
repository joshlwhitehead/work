import lib.add_lib_path
import lib.api_auth as auth
import lib.graphql_queries as qry
import matplotlib.pyplot as plt
from pcr import pcr
import numpy as np
from lib.consumable_config import getConfigMap
from melt.melt import MeltAnalysis
from scipy.interpolate import make_interp_spline
import time
import pandas as pd
from scipy import stats


consumableId = ['cb33b22a-492a-4efa-83bf-6b232bc406c1','9b3a4660-7514-4d36-86a5-6ab76d427bc1','1eb72362-7fc4-4028-b294-027eb64cd4a9','054efdec-1dae-4c57-8c6b-48748f69b514','eaf107b4-36aa-463d-8270-6191e2128ed3']
def getMelt(consumableId,memoForRep):

    
    


    api = auth.getApiClient()

    where = {
    'id': {
        '_eq': consumableId
    }
    }
    channels = np.array([515,555,590,630,680])



    response = api.execute(query=qry.consumableWhere,variables={'where':where})


    # print(response)
    repMem = {}
    for i in range(len(response['data']['consumable'][0]['experiments'])):
        repMem[response['data']['consumable'][0]['experiments'][i]['memo']] = i
    
    rep = repMem[memoForRep]

    # melts = []

    rawData = response['data']['consumable'][0]['experiments'][rep]['experimentResult']['pcrData']['sensor']
    
    data = np.array(rawData).T.tolist()
    meltData = response['data']['consumable'][0]['experiments'][rep]['experimentResult']['meltData']['sensor']
    data_melt = np.array(meltData).T.tolist()
    # melts.append(data_melt)
    # print(meltData.keys())
    if len(data_melt) > 0:
        tData = response ['data']['consumable'][0]['experiments'][rep]['experimentResult']['meltData']['temperature']
        mData = data_melt

    consumableName = 'lambda'
    configuration = getConfigMap(consumableName)
    meltAnalysis = MeltAnalysis(configuration)
    if len(data_melt) > 0:
        meltAnalysis.callMelt(tData, mData)

    return data_melt



LED = []
detect = []
both = []
y = {}
nominal = []
flip = []
memos = ['filter flip 0','filter flip 1 LED','filter flip 2 detector','filter flip 3 both']
wave = 3
count = 0

for j in memos:
    for l in consumableId:
        # print(l)
        x445 = max(getMelt(l,j)[wave])/min(getMelt(l,j)[wave])
        # x445 = (max(getMelt(l,j)[wave])-min(getMelt(l,j)[wave]))/np.mean(getMelt(l,j)[wave])
        # x445 = max(getMelt(l,j)[wave])
        nominal.append(x445)
        flip.append(count)
    y['flip'] = flip
    y['baseline'] = nominal
    count += 1
print(y)
dF = pd.DataFrame(y)

# dF.hist('baseline')
# plt.show()



