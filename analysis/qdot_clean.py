"""
Created on Wed Jun 16 12:14:39 2021

@author: JoshWhitehead
"""

######################  IMPORT PCKGS    ############################
import lib.add_lib_path
import lib.api_auth as auth
import lib.graphql_queries as qry
import matplotlib.pyplot as plt
import numpy as np
from lib.consumable_config import getConfigMap
from melt.melt import MeltAnalysis


################### ADJUST THIS SECTION ##########################
consumableId = '4e9c4219-3a73-4099-a7cf-44f118f84aa8'

toPlot = 1                                                                       # which run to use



#########################   PULL DATA FROM BASE     #########################################
api = auth.getApiClient()

where = {
'id': {
    '_eq': consumableId
}
}

response = api.execute(query=qry.consumableWhere,variables={'where':where})

meltData = response['data']['consumable'][0]['experiments'][toPlot]['experimentResult']['meltData']['sensor']
mData = np.array(meltData).T.tolist()

t = response['data']['consumable'][0]['experiments'][toPlot]['experimentResult']['meltData']['temperature']
tData = np.array(t)



#######################     CONFIGURE       #############################################################
consumableName = 'lambda'
configuration = getConfigMap(consumableName)

meltAnalysis = MeltAnalysis(configuration)
meltAnalysis.callMelt(tData, mData)



########################    CALCULATE RATIO  ###################################
ratio = np.divide(mData[5],mData[6])                                                            #take ratio of 590nm/630nm

a,b = np.polyfit(tData,ratio,1)                                                                 #fit line
print('a',a,'\n','b',b)



##########################      PLOT    ##############################
plt.scatter(tData,ratio,s=.5,color='orange',lw=1.6,label= 'qdot')                               #plot scatterplot of ratio
plt.plot(tData,a*tData+b,label='linear fit')                                                    #plot fit line
plt.grid()
plt.legend()
plt.title('Ratio of 590nm & 630nm '+consumableId[:6])
plt.xlabel('Temperature (C)')
plt.ylabel('Ratio')
plt.savefig('qdot_ratio.png')



#######################     R^2 VALUE    #######################
sT = 0
xx = np.average(ratio)

s = (np.square(ratio-xx))
sT = sum(s)

r = (np.square(ratio-(a*tData+b)))
sR = sum(r)

print('R^2:',(sT-sR)/sT)










