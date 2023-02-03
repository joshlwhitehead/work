import lib.add_lib_path
import lib.api_auth as auth
import lib.graphql_queries as qry
import matplotlib.pyplot as plt
from pcr import pcr
import numpy as np
from lib.consumable_config import getConfigMap
from melt.melt import MeltAnalysis
from scipy.interpolate import make_interp_spline


consumableId = ['cb33b22a-492a-4efa-83bf-6b232bc406c1','9b3a4660-7514-4d36-86a5-6ab76d427bc1','1eb72362-7fc4-4028-b294-027eb64cd4a9','054efdec-1dae-4c57-8c6b-48748f69b514','eaf107b4-36aa-463d-8270-6191e2128ed3']
for i in consumableId:
    rep = 1


    api = auth.getApiClient()

    where = {
    'id': {
        '_eq': i
    }
    }
    channels = np.array([515,555,590,630,680])



    response = api.execute(query=qry.consumableWhere,variables={'where':where})
    # print(response)

    rawData = response['data']['consumable'][0]['experiments'][rep]['experimentResult']['pcrData']['sensor']
    data = np.array(rawData).T.tolist()
    meltData = response['data']['consumable'][0]['experiments'][rep]['experimentResult']['meltData']['sensor']
    data_melt = np.array(meltData).T.tolist()
    # print(meltData.keys())
    if len(data_melt) > 0:
        tData = response ['data']['consumable'][0]['experiments'][rep]['experimentResult']['meltData']['temperature']
        mData = data_melt

    consumableName = 'lambda'
    configuration = getConfigMap(consumableName)
    meltAnalysis = MeltAnalysis(configuration)
    if len(data_melt) > 0:
        meltAnalysis.callMelt(tData, mData)

    print(i[:6])
    for u in data_melt[1:3]:
        print('mean: ',np.mean(u))
        print('base: ',u[-1])
    # print('\n')











def derivSpec():
    x = channels
    y = []
    for i in [3,4,5,6,7]:
        y.append(max(meltAnalysis.results['smoothDerivatives'][i]))
    y = np.array(y)

    X_Y_Spline = make_interp_spline(channels,y)

   
    X_ = np.linspace(x.min(), x.max(), 500)
    Y_ = X_Y_Spline(X_)

    # plt.plot(meltAnalysis.results['smoothedT'],meltAnalysis.results['smoothDerivatives'][4])
    plt.figure()
    plt.plot(X_,Y_)
    plt.plot(channels,y,'o')
    plt.title(''.join(['Spectral Signature ',consumableId[:6]]))
    # plt.ylabel(''.join(["Melt Peak @ ",str(round(good_tm,1))]))
    plt.xlabel('Channel (nm)')
    # plt.ylim(-.15,2.2)
    plt.xticks((515,555,590,630,680),('515','555','590','630','680'))
    plt.grid()
    
    
    # plt.savefig(''.join(['specSigMadison/21Jul2022/',consumableId[:6]]))
    plt.show()
# derivSpec()