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
# NTC = '68bed1a4367b4e35861518cd5c087b67'
# gBlock = 'cf7a8a80ebea4b7d8b149a78774d1d2f'
# LAM = '58bf7643d2594413a5d1f8fb5e64bae2'
# both = '34c2122c10344bd4aaca7e4e0399360c'
# NTC = 'b0385e486c9e4d34bcee26fc601ecc99'
# both = 'fd533fec012f4af0af0c90b24a76067b'
# gBlock = 'c2107e1d5c794a3795c75b23850180e7'
# LAM = '91bcb5150763442794ef2406ce4a54d8'
NTC = '161a047a1d7443ebad73970ea1c865f1'
LAM = '8a07685b-d8bb-48ee-acf8-cbbaf386ae6c'
gBlock = '881a41ef-7e5c-466f-9ad3-d5107b33f401'
both = '6079ae48-7278-4b61-bfdc-71be2f4dc689'


a = '5ebfd5e9bf964c9180ee8fc6c00c9581'
b = '6368587234f94cbfbd641fab28bc8355'
c = 'e1025099cbbb4a60b5ffed465250c441'
d = '6f6e07c509f84ae6a240b9e26d70ebb6'

# cons2 = 'd9104f4c1ea84abd805dd4dc53448066'
# cons1 = 'b107b8670ebf4e058769885e7ea99575'
label=['Dried Template','NTC']

cons_list = [a,b,c,d]
lab = ['2.5uM','5.0uM','10um','20uM']

channels_to_plot = [3]
channels_to_melt = {
    3:(.2,.7,.9)}
styles = {
    NTC:':',
    gBlock:'o-',
    LAM:'--',
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
    plt.title('MavBlue Titration ACTB Q670')
    plt.ylabel('-dF/dT')
    plt.xlabel('Temperature (C)')
    plt.legend()
    plt.ylim()
    plt.savefig('MavBlue_deriv.png')


def meltRaw():
    plt.figure()
    for i in cons_list:
        for u in channels_to_melt:
            meltAnalysis.callMelt(where(i)[2],where(i)[1])
            plt.plot(meltAnalysis.results['smoothedT'][50:],
            meltAnalysis.results['smoothed'][u][50:])
    plt.grid()
    plt.savefig('Duplex_melt.png')



def ampCurve():
    plt.figure
    count = 0
    for i in cons_list:
        pcrAnalysis.callPCR(where(i)[0])
        plt.plot(pcrAnalysis.results['backgroundSubtracted'][3],label=''.join([str(lab[count]),' ',str(channels[3]),'nm']))
        count += 1
    plt.grid()
    plt.title('MavBlue Titration ACTB Q670')
    plt.ylabel('Fluorescence')
    plt.xlabel('Cycle')
    plt.legend()
    plt.savefig('mavBlue.png')

def other():
    count = 0
    for i in cons_list:
        pcrAnalysis.callPCR(where(i)[0])
        cp = pcrAnalysis.results['cqs'][3]

        plt.plot(pcrAnalysis.results['backgroundSubtracted'][3],label=''.join([label[count],', Cp ',str(cp)]))
        count += 1
    plt.grid()
    plt.title('FD MS2 Qscript')
    plt.xlabel('Cycle')
    plt.ylabel('Fluorescence')
    plt.legend()
    plt.savefig('FD MS2.png')


def fret():
    delta = []
    for u in cons_list:
        for i in [0,2,3,4,5,6,7]:
            delta.append(np.average(where(u)[0][i][-5:])-np.average(where(u)[0][i][:5]))
    # print(len(delta))
    # print(delta)
    channels = [415,480,515,555,590,630,680]

    from scipy.interpolate import make_interp_spline
    tot = sum(delta)
    a = (delta[6]/tot)
    b = (delta[13]/tot)
    c = (delta[20]/tot)
    d = (delta[27]/tot)
    print(a,b,c,d)
    # Dataset
    x = np.array(channels)
    y1 = np.array(delta[:7])-delta[0]
    y2 = np.array(delta[7:14])-delta[7]
    y3 = np.array(delta[14:21])-delta[14]
    y4 = np.array(delta[21:])-delta[21]



    X_Y_Spline1 = make_interp_spline(x, y1)
    X_Y_Spline2 = make_interp_spline(x, y2)

    X_Y_Spline3 = make_interp_spline(x, y3)

    X_Y_Spline4 = make_interp_spline(x, y4)


    # Returns evenly spaced numbers
    # over a specified interval.
    X_ = np.linspace(x.min(), x.max(), 500)
    Y_1 = X_Y_Spline1(X_)
    Y_2 = X_Y_Spline2(X_)
    Y_3 = X_Y_Spline3(X_)
    Y_4 = X_Y_Spline4(X_)

    # Plotting the Graph
    plt.figure()
    plt.plot(X_, Y_1,'-',label='2.5uM MavBlue')
    plt.plot(X_, Y_2,'-',label='5.0uM MavBlue')
    plt.plot(X_, Y_3,'-',label='10uM MavBlue')
    plt.plot(X_, Y_4,'-',label='20uM MavBlue')
    plt.plot(x,y1,'o')
    plt.plot(x,y2,'o')
    plt.plot(x,y3,'o')
    plt.plot(x,y4,'o')
    plt.title("ActB Q670 MavBlue Titration End-Point Curve")
    plt.xlabel("Channel (nm)")
    plt.ylabel("Fluorescence")
    plt.xticks((415,445,480,515,555,590,630,680),('415','445','480','515','555','590','630','680'))
    plt.grid()
    plt.legend()
    # plt.text('aaa')
    plt.savefig(''.join(['fret.png']))
# other()

# ampCurve()
# melt_deriv()
# meltRaw()
fret()








end = time()

print(round(end-begin,2), ' sec')









