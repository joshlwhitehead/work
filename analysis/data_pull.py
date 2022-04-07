"""
Created on Wed Jun 16 12:14:39 2021

@author: JoshWhitehead
"""

"""NO LONGER APPLICABLE"""

######################  IMPORT PCKGS    ############################
from time import time
begin = time()
import lib.add_lib_path
import lib.api_auth as auth
import lib.graphql_queries as qry
# from pcr import pcr
import numpy as np
# from lib.consumable_config import getConfigMap
# from melt.melt import MeltAnalysis
import pandas as pd

################### ADJUST THIS SECTION ##########################
consumableId = 'ddd76ad5-cfff-4323-81f2-c33469c6de1c'
fakeId = '00000000000000000000000000000000'



rep = 0




#########################   PULL DATA FROM BASE     #########################################
api = auth.getApiClient()

where = {'id':{'_neq':fakeId}}

response = api.execute(query=qry.consumableWhere,variables={'where':where})
cp = []
id = []
t = []
tm = []
# print(response)
# if 'smothed' in response['data']['consumable'][34]['experiments'][0]['experimentResult']['pcrResultData'].keys():
#     print('hi')
# print(response['data']['consumable'][1000]['experiments'][0]['experimentResult'])

for i in range(len(response['data']['consumable'])):
    # if 'tms' in response['data']['consumable'][i]['experiments'][rep]['experimentResult'].keys():
    #     print(response['data']['consumable'][i]['experiments'][rep]['experimentResult']['meltResultData']['tms'])
    if len(response['data']['consumable'][i]['experiments']) > 0:
        if response['data']['consumable'][i]['experiments'][0]['experimentResult'] != None:
            if response['data']['consumable'][i]['experiments'][0]['experimentResult']['pcrResultData'] != None:
                if 'cqs' in response['data']['consumable'][i]['experiments'][0]['experimentResult']['pcrResultData'].keys():
                    if response['data']['consumable'][i]['experiments'][0]['memo'] != None:
                        if len(response['data']['consumable'][i]['experiments'][0]['memo']) > 0:   
                            if 'dry' in response['data']['consumable'][i]['experiments'][0]['memo']:
                                if 'snp' in response['data']['consumable'][i]['experiments'][0]['memo']:                                    
                                    cp.append(response['data']['consumable'][i]['experiments'][rep]['experimentResult']['pcrResultData']['cqs'][3])
                                    id.append(response['data']['consumable'][i]['id'])
                                    if 'tms' in response['data']['consumable'][i]['experiments'][rep]['experimentResult']['meltResultData'].keys():
                                        tm.append(response['data']['consumable'][i]['experiments'][rep]['experimentResult']['meltResultData']['tms'][3])
                                    # if len(response['data']['consumable'][i]['experiments'][0]['experimentStartTime']) > 0:
                                    #     t.append(response['data']['consumable'][i]['experiments'][0]['experimentStartTime'])
                                elif 'SNP' in response['data']['consumable'][i]['experiments'][0]['memo']:
                                    cp.append(response['data']['consumable'][i]['experiments'][rep]['experimentResult']['pcrResultData']['cqs'][3])
                                    id.append(response['data']['consumable'][i]['id'])
                                    if 'tms' in response['data']['consumable'][i]['experiments'][rep]['experimentResult']['meltResultData'].keys():
                                        tm.append(response['data']['consumable'][i]['experiments'][rep]['experimentResult']['meltResultData']['tms'][3])
                                elif 'Snp' in response['data']['consumable'][i]['experiments'][0]['memo']:
                                    cp.append(response['data']['consumable'][i]['experiments'][rep]['experimentResult']['pcrResultData']['cqs'][3])
                                    id.append(response['data']['consumable'][i]['id'])
                                    if 'tms' in response['data']['consumable'][i]['experiments'][rep]['experimentResult']['meltResultData'].keys():
                                        tm.append(response['data']['consumable'][i]['experiments'][rep]['experimentResult']['meltResultData']['tms'][3])


                            elif 'Dry' in response['data']['consumable'][i]['experiments'][0]['memo']:
                                if 'snp' in response['data']['consumable'][i]['experiments'][0]['memo']:                                    
                                    cp.append(response['data']['consumable'][i]['experiments'][rep]['experimentResult']['pcrResultData']['cqs'][3])
                                    id.append(response['data']['consumable'][i]['id'])
                                    if 'tms' in response['data']['consumable'][i]['experiments'][rep]['experimentResult']['meltResultData'].keys():
                                        tm.append(response['data']['consumable'][i]['experiments'][rep]['experimentResult']['meltResultData']['tms'][3])
                                    # if len(response['data']['consumable'][i]['experiments'][0]['experimentStartTime']) > 0:
                                    #     t.append(response['data']['consumable'][i]['experiments'][0]['experimentStartTime'])
                                elif 'SNP' in response['data']['consumable'][i]['experiments'][0]['memo']:
                                    cp.append(response['data']['consumable'][i]['experiments'][rep]['experimentResult']['pcrResultData']['cqs'][3])
                                    id.append(response['data']['consumable'][i]['id'])
                                    if 'tms' in response['data']['consumable'][i]['experiments'][rep]['experimentResult']['meltResultData'].keys():
                                        tm.append(response['data']['consumable'][i]['experiments'][rep]['experimentResult']['meltResultData']['tms'][3])
                                elif 'Snp' in response['data']['consumable'][i]['experiments'][0]['memo']:
                                    cp.append(response['data']['consumable'][i]['experiments'][rep]['experimentResult']['pcrResultData']['cqs'][3])
                                    id.append(response['data']['consumable'][i]['id'])
                                    if 'tms' in response['data']['consumable'][i]['experiments'][rep]['experimentResult']['meltResultData'].keys():
                                        tm.append(response['data']['consumable'][i]['experiments'][rep]['experimentResult']['meltResultData']['tms'][3])


                            elif 'DRY' in response['data']['consumable'][i]['experiments'][0]['memo']:
                                if 'snp' in response['data']['consumable'][i]['experiments'][0]['memo']:                                    
                                    cp.append(response['data']['consumable'][i]['experiments'][rep]['experimentResult']['pcrResultData']['cqs'][3])
                                    id.append(response['data']['consumable'][i]['id'])
                                    if 'tms' in response['data']['consumable'][i]['experiments'][rep]['experimentResult']['meltResultData'].keys():
                                        tm.append(response['data']['consumable'][i]['experiments'][rep]['experimentResult']['meltResultData']['tms'][3])
                                    # if len(response['data']['consumable'][i]['experiments'][0]['experimentStartTime']) > 0:
                                    #     t.append(response['data']['consumable'][i]['experiments'][0]['experimentStartTime'])
                                elif 'SNP' in response['data']['consumable'][i]['experiments'][0]['memo']:
                                    cp.append(response['data']['consumable'][i]['experiments'][rep]['experimentResult']['pcrResultData']['cqs'][3])
                                    id.append(response['data']['consumable'][i]['id'])
                                    if 'tms' in response['data']['consumable'][i]['experiments'][rep]['experimentResult']['meltResultData'].keys():
                                        tm.append(response['data']['consumable'][i]['experiments'][rep]['experimentResult']['meltResultData']['tms'][3])
                                elif 'Snp' in response['data']['consumable'][i]['experiments'][0]['memo']:
                                    cp.append(response['data']['consumable'][i]['experiments'][rep]['experimentResult']['pcrResultData']['cqs'][3])
                                    id.append(response['data']['consumable'][i]['id'])
                                    if 'tms' in response['data']['consumable'][i]['experiments'][rep]['experimentResult']['meltResultData'].keys():
                                        tm.append(response['data']['consumable'][i]['experiments'][rep]['experimentResult']['meltResultData']['tms'][3])
                                


                           
print(len(cp),'\n',len(id),'\n',len(t))
print(len(tm))
while len(tm) < len(cp):
    tm.append(0)
# print(tm,'\n',cp)
# cp = np.array(cp)
# tm = np.array(tm)
# print(cp)


for i in range(len(cp)):
    # print(type(cp[i]))
    if type(cp[i]) != float:
        cp[i] = 0
        tm[i] = 40
    if type(tm[i]) != float:
        cp[i] = 0
        tm[i] = 40


spread = {'cp':cp,'tm':tm,'id':id}
dF = pd.DataFrame(spread)
dF.to_csv('Dry SNP.csv')




import matplotlib.pyplot as plt
maxTm = 86
minTm = 76
maxCp = 37
minCp = 23

plt.figure()
plt.title('Dry SNP')
plt.grid()
plt.scatter(cp,tm)
plt.hlines(maxTm,min(cp),max(cp),'k')
plt.hlines(minTm,min(cp),max(cp),'k')
plt.vlines(minCp,minTm,maxTm,'k','dashed')
plt.vlines(maxCp,minTm,maxTm,'k','dashed')
plt.xlabel('cp')
plt.ylabel('Tm')

plt.savefig('DrySnp.png')
plt.show()









end = time()
print(round(end-begin,2),' sec')



