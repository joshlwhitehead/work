"""
Created on Wed Jun 16 12:14:39 2021

@author: JoshWhitehead
"""

######################  IMPORT PCKGS    ############################
from time import time
begin = time()
import lib.add_lib_path
import lib.api_auth as auth
import lib.graphql_queries as qry
# from IPython.display import clear_output
import matplotlib.pyplot as plt
# import pcr.add_pcr_path
from pcr import pcr
import numpy as np
from lib.consumable_config import getConfigMap
from melt.melt import MeltAnalysis

################### ADJUST THIS SECTION ##########################
consumableId1 = 'dfede594-9409-4bb4-a3a5-d434b289c61f'
consumableId2 = 'df9087ec-73e0-4bc5-9b2c-bfe2904c9086'
consumableId3 = 'e48382c9-0cd4-4596-8c81-472cb6535d61'
consumableId4 = 'b12b473c-eef8-4461-b97a-d7cafde8018c'
consumableId5 = 'cd509f1e-89f2-44ea-a7b9-7da077e5e745'
consumableId6 = 'b20f0b5a-4cd5-4c2d-a54c-dd468eb727b6'
consumableId7 = 'adf78feb6fc94c219f982aefc406d3a2'
consumableId8 = 'eb2ba98c-1c40-4df8-9671-0048dfe0a3a4'
consumableId9 = 'c355895f-514d-4de6-bc64-2bd2a45914c1'
consumableId10 = 'bdcb2a4f-ad6a-4803-a6e5-2ec6525277ed'

cons_list = [consumableId1,consumableId2,consumableId3,consumableId4,consumableId5,consumableId6,consumableId7,consumableId8,consumableId9,consumableId10]
toPlot = 1

channels_to_plot = [4,5,6]
channels_to_melt = [4,5,6]


##################### GENERAL CONSTANTS #########################
channels = [415,445,480,515,555,590,630,680,'CLR','NIR']



#########################   PULL DATA FROM BASE     #########################################
def where(consumableId):
    api = auth.getApiClient()

    where = {
    'id': {
        '_eq': consumableId
    }
    }
    response = api.execute(query=qry.consumableWhere,variables={'where':where})
    rawData = response['data']['consumable'][0]['experiments'][0]['experimentResult']['pcrData']['sensor']
    data = np.array(rawData).T.tolist()

    meltData = response['data']['consumable'][0]['experiments'][1]['experimentResult']['meltData']['sensor']
    data_melt = np.array(meltData).T.tolist()
    t = response['data']['consumable'][0]['experiments'][1]['experimentResult']['meltData']['temperature']
    return data,data_melt,t

if len(where(consumableId10)[1]) > 0:
    # print(data_melt)
    tData = where(consumableId10)[2]
    mData = where(consumableId10)[1]
    # print(mData)
# print(data_melt)




#######################     CONFIGURE       #############################################################
consumableName = 'lambda'
configuration = getConfigMap(consumableName)

meltAnalysis = MeltAnalysis(configuration)
if len(where(consumableId10)[1]) > 0:
    meltAnalysis.callMelt(tData, mData)


# clear_output(wait=True)

pcrAnalysis = pcr.PCRAnalysis(configuration)
if len(where(consumableId10)[0]) > 0:
    pcrAnalysis.callPCR(where(consumableId1)[0])





cons = consumableId10
ratio = np.divide(where(cons)[1][5],where(cons)[1][6])

# listOfR = []
# for i in cons_list[9]:
#     div = np.divide(where(i)[1][6],where(i)[1][7])
#     listOfR.append(div)
# # print('hi',listOfR[0])
# av = []
# for i in range(len(where(consumableId10)[1][0])):
#     avi = np.average([listOfR[0][i],listOfR[1][i],listOfR[2][i]])
#     av.append(avi)
# # print(av)



# # for i in cons_list[6:]:
# #     print(len(where(i)[1][6]))


x = np.array(where(consumableId10)[2])


a,b = np.polyfit(x,np.array(ratio),1)
print('a',a,'\n','b',b)



plt.figure()

plt.scatter(where(consumableId10)[2],ratio,s=.5,color='orange',lw=1.6,label= 'qdot')



plt.plot(x,a*x+b,label='linear fit')

plt.grid()
plt.legend()
plt.title('Ratio of 590nm & 630nm '+consumableId10[:6])
plt.xlabel('Temperature (C)')
plt.ylabel('Ratio')
plt.savefig('qdot_ratio.png')
sT = 0
xx = np.average(ratio)


s = (np.square(ratio-xx))
sT = sum(s)
# print(sT)

r = (np.square(ratio-(a*x+b)))
sR = sum(r)
# print(sR)

print('r2',(sT-sR)/sT)

end = time()

print(round(end-begin,2), ' sec')









