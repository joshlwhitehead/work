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
from matplotlib.axes import Axes

NTC = 'b0385e486c9e4d34bcee26fc601ecc99'
both = 'fd533fec012f4af0af0c90b24a76067b'
gBlock = 'c2107e1d5c794a3795c75b23850180e7'
LAM = '91bcb5150763442794ef2406ce4a54d8'

label=['Dried Template','NTC']

cons_list = [NTC,gBlock,both,LAM]
lab = ['NTC','gBlock','both','LAM']

channels_to_plot = [3]
channels_to_melt = {
    3:(.2,.7,.9),
}



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

    meltData = response['data']['consumable'][0]['experiments'][0]['experimentResult']['meltData']['sensor']
    data_melt = np.array(meltData).T.tolist()
    tdata = np.array(response['data']['consumable'][0]['experiments'][0]['experimentResult']['meltData']['temperature'])
    return data,data_melt,tdata

# tData = where(consumableId1)[1][0]
# mData = where(consumableId1)[1][1:]





#######################     CONFIGURE       #############################################################
consumableName = 'lambda'
configuration = getConfigMap(consumableName)

meltAnalysis = MeltAnalysis(configuration)
# meltAnalysis.callMelt(tData, mData)



pcrAnalysis = pcr.PCRAnalysis(configuration)
# if len(where(consumableId1)[0]) > 0:
#     pcrAnalysis.callPCR(where(consumableId1)[0])


def melt_deriv():


    plt.figure()
    count = 0
    for i in cons_list:
        for u in channels_to_melt:
            meltAnalysis.callMelt(where(i)[2],where(i)[1])
            plt.plot(meltAnalysis.results['smoothedT'][50:],
            meltAnalysis.results['smoothDerivatives'][u][50:],label=''.join([str(lab[count]),' ',str(channels[u]),'nm']))
        count += 1
    
     
    plt.grid()
    plt.title('ACTB Lambda Duplex')
    plt.ylabel('-dF/dT')
    plt.xlabel('Temperature (C)')
    plt.legend()
    plt.ylim()
    plt.savefig('Duplex_deriv.png')


def meltRaw():
    plt.figure()
    for i in cons_list:
        for u in channels_to_melt:
            plt.plot(where(i)[1][0][50:],
            where(i)[1][u][50:])
    
    
    plt.savefig('Duplex_melt.png')





meltAnalysis.callMelt(where(both)[2],where(both)[1])
findFit = meltAnalysis.results['smoothDerivatives'][3][50:175]
T = meltAnalysis.results['smoothedT'][50:175]
plt.plot(T,findFit)
plt.grid()
plt.savefig('idea.png')







end = time()

print(round(end-begin,2), ' sec')









