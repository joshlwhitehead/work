"""
Created on Wed Jun 16 12:14:39 2021

@author: JoshWhitehead
"""

######################  IMPORT PCKGS    ############################
from time import time
begin = time()
import os
from airtable import Airtable
import lib.add_lib_path
import lib.api_auth as auth
import lib.graphql_queries as qry
# from IPython.display import clear_output
import matplotlib.pyplot as plt
# import pcr.add_pcr_path
from pcr import pcr
# from pandas import DataFrame
import numpy as np
from lib.consumable_config import getConfigMap
from melt.melt import MeltAnalysis
import teams
import shutil
################### ADJUST THIS SECTION ##########################
consumableId = '47e8fed6766740e289adea4cd35ea166'


ampLow = -10
ampHigh = 100
derivLow = -0.2
derivHigh = 2.5

rep = 0

date = teams.date
fret = False

channels_to_plot = [3,6,7]
channels_to_melt = [3,4,5,6,7]
all_channels_to_plot = [3,4,5,6,7]



alphaRec = {'recr2mS95Dhl2T5b3':'Alpha: 01',
    'recjrmPNIUuSflnJK':'Alpha: 02',
    'rec5HYhNNN7VLCxd4':'Alpha: 03',
    'rec4rP17rdoKFl5j4':'Alpha: 04',
    'recgu1gKgbB473EtT':'Alpha: 06',
    'recGUbmGGQVVBh3tf':'Alpha: 07',
    'recwrvSqG3qXBssBn':'Alpha: 08',
    'rec8dSzBQbDFAyhsn':'Alpha: 09'
    }

##################### GENERAL CONSTANTS #########################
channels = [415,445,480,515,555,590,630,680,'NIR','CLR','Dark']
colors = ['pink','violet','blue','aqua','green',(1,.9,0),'orange','red','black','black','black']


#############   FOR AIRTABLE ACCESS     #################
baseId = 'appNSxNY9azGBJsld'
apiKey = 'keyWE1cKBVZqYhNMi'


def findAssay():
    tableName = 'Experiments'
    mainTable = Airtable(baseId,tableName,apiKey)

    record = mainTable.match('Barcode',consumableId)
    return record

# print(findAssay()['fields']['Instrument'])


NameOfFolder = ''.join([findAssay()['fields']['Description'],' ',consumableId[:6]])
# NameOfFolder = ''.join(['Qdot in Alpha Cup fullrun2'])
# ####

def textFile():
    f = open(''.join(['file_info.txt']),'a')
    f.truncate(0)
    f.write(''.join(['"PCR_some_backsub.png" is a plot of channels 515, 630, and 680 background subtracted off the average of the first 5 cycles.','\n','\n',
    '"PCR_all_backsub.png" is a plot of channels 515, 555, 590, 630, and 680 background subtracted off the average of the first 5 cycles.','\n','\n',
    '"melt_some_raw.png" is a plot of the raw melt data (Fluorescence vs. Temperature).','\n','\n',
    '"melt_deriv.png" is a plot of the negative derivative (-dF/dT) of the melt data after the data is smoothed with a cubic spline (-dF/dT vs. Temperature).','\n','\n',
    '"fret.png" is a plot comparing fluorescence to channel. The fluorescence is calculated by subtractin the average of the first 5 cycles from the average of the last 5 cycles.']))
    f.close()



#########################   PULL DATA FROM BASE     #########################################
api = auth.getApiClient()

where = {
'id': {
    '_eq': consumableId
}
}

response = api.execute(query=qry.consumableWhere,variables={'where':where})
# print(response)
rawData = response['data']['consumable'][0]['experiments'][rep]['experimentResult']['pcrData']['sensor']
data = np.array(rawData).T.tolist()
# print(data)
meltData = response['data']['consumable'][0]['experiments'][rep]['experimentResult']['meltData']['sensor']
data_melt = np.array(meltData).T.tolist()
# print(meltData)

if len(data_melt) > 0:
    tData = response ['data']['consumable'][0]['experiments'][rep]['experimentResult']['meltData']['temperature']
    mData = data_melt
    # print(tData)




#######################     CONFIGURE       #############################################################
consumableName = 'lambda'
configuration = getConfigMap(consumableName)
meltAnalysis = MeltAnalysis(configuration)
if len(data_melt) > 0:
    meltAnalysis.callMelt(tData, mData)



pcrAnalysis = pcr.PCRAnalysis(configuration)
# data = []
if len(data) > 0:
    pcrAnalysis.callPCR(data)
    anneal = response['data']['consumable'][0]['experiments'][rep]['experimentResult']['pcrData']['temperature']


    
######################  MAKE CSV    ##########################################
if os.path.isdir(NameOfFolder) == False:
    os.mkdir(''.join([NameOfFolder]))

# if len(data) > 0:
#     newPCR = {'T':anneal}
#     count = 0
#     for i in channels:
#         newPCR[i] = data[count]
#         count += 1

#     dF_PCR = DataFrame(newPCR)
#     dF_PCR.to_csv(''.join([NameOfFolder,'/Raw_PCR.csv']))

# if len(data_melt) > 0:
#     newMelt = {'T':tData}
#     count = 0
#     for i in channels:
#         newMelt[i] = mData[count]
#         count += 1
#     dF_Melt = DataFrame(newMelt)
#     dF_Melt.to_csv(''.join([NameOfFolder,'/Raw_Melt.csv']))


#################   PLOTS   ############################
def plotsomePCR():
    plt.figure()

    for i in channels_to_plot:
        cp = pcrAnalysis.results['cqs'][i]
        # cp = 1

        plt.plot(
            pcrAnalysis.results['backgroundSubtracted'][i],lw=2, color=colors[i], label=f'{channels[i]}, Cp {cp}')
    
    
    plt.title(findAssay()['fields']['Description'])
    plt.ylabel("F")
    plt.xlabel(''.join(['ID: ',consumableId[:6],'                                   ',
        'Cycle','                                      ',alphaRec[findAssay()['fields']['Instrument'][0]]]),loc='left')
    plt.legend()
    plt.grid()
    if 'NTC' in NameOfFolder:
        plt.ylim(ampLow,ampHigh)
    else:
        plt.ylim()
    plt.savefig(''.join([NameOfFolder,'/PCR_some_backsub']))


def plotallPCR():
    plt.figure()

    plt.close('all')
    for i in all_channels_to_plot:
        cp = pcrAnalysis.results['cqs'][i]
        # cp = 1

        plt.plot(pcrAnalysis.results['backgroundSubtracted'][i],lw=2,color=colors[i],label=f'{channels[i]}, Cp {cp}')
    plt.title(findAssay()['fields']['Description'])
    plt.ylabel("F")
    plt.xlabel(''.join(['ID: ',consumableId[:6],'                                   ',
        'Cycle','                                      ',alphaRec[findAssay()['fields']['Instrument'][0]]]),loc='left')
    plt.legend()
    plt.grid()
    if 'NTC' in NameOfFolder:
        plt.ylim(ampLow,ampHigh)
    else:
        plt.ylim()
    plt.savefig(''.join([NameOfFolder,'/PCR_all_backsub']))



def melt_some():
    plt.figure()
    plt.close('all')

    for i in channels_to_melt:
        plt.plot(tData,mData[i],lw=2,color=colors[i],label=str(channels[i]))
    plt.title(findAssay()['fields']['Description'])
    plt.ylabel('F')
    plt.xlabel(''.join(['ID: ',consumableId[:6],'                                   ',
        'Temp (C)','                                   ',alphaRec[findAssay()['fields']['Instrument'][0]]]),loc='left')
    plt.legend()
    plt.grid()
    plt.savefig(''.join([NameOfFolder,'/melt_some_raw']))



tm = max(meltAnalysis.results['smoothDerivatives'][3][120:])
tm2 = list(meltAnalysis.results['smoothDerivatives'][3]).index(tm)
good_tm = meltAnalysis.results['smoothedT'][tm2]

def melt_deriv():
    plt.figure()
    for i in channels_to_melt:
        
        plt.plot(
        meltAnalysis.results['smoothedT'],  
        meltAnalysis.results['smoothDerivatives'][i],color = colors[i],label = ''.join([str(channels[i])]))

    plt.title(findAssay()['fields']['Description'])
    plt.ylabel("-dF/dt")
    plt.xlabel(''.join(['ID: ',consumableId[:6],'                                   ',
        'Temp (C)','                                   ',alphaRec[findAssay()['fields']['Instrument'][0]]]),loc='left')
    plt.legend()
    plt.grid()
    
    if 'NTC' in NameOfFolder:
        plt.ylim(derivLow,derivHigh)
    else:
        plt.ylim()
    plt.savefig(''.join([NameOfFolder,'/melt_deriv']))
    # return good_tm


############################    XAMP    #######################################
if len(data) > 0:
    last = pcrAnalysis.results['rawData'][3][-1]
    first = np.average(pcrAnalysis.results['rawData'][3][:int(pcrAnalysis.results['cqs'][3])])
    # print(first)
    xamp = np.round(last/first,1)





########################    AIRTABLE UPLOAD     ########################






def uploadToAir():
    tableName = 'Experiments'

    mainTable = Airtable(baseId,tableName,apiKey)

    record = mainTable.match('Barcode',consumableId)
    fields = {
        'Data Location':
        ''.join(['https://teams.microsoft.com/_#/files/General?threadId=19%3A0b66ed3571b441938e00cbb11ede849a%40thread.tacv2&ctx=channel&context=',NameOfFolder,'&rootfolder=%252Fsites%252FMaverikProject%252FShared%2520Documents%252FGeneral%252FExperiments-MolBio%252FMaverick_',date,'%252F',NameOfFolder])
        }
    if len(data) > 0:
        fields['Cp'] = pcrAnalysis.results['cqs'][3]
        fields['x amp'] = xamp
        fields['Tm'] = good_tm
        
    mainTable.update(record['id'], fields)





print('Data Loaded')








########################    FINISHED PRODUCT    ############################
if len(data) > 0:
    plotsomePCR()
    plotallPCR()
    teams.upload(''.join([NameOfFolder,'/PCR_some_backsub.png']))
    teams.upload(''.join([NameOfFolder,'/PCR_all_backsub.png']))
    
    # teams.upload(''.join([NameOfFolder,'/Raw_PCR.csv']))
    if rep == 0:
        uploadToAir()

    print('PCR Done')

if len(data_melt) > 0:
    melt_some()
    melt_deriv()
    teams.upload(''.join([NameOfFolder,'/melt_some_raw.png']))
    # teams.upload(''.join([NameOfFolder,'/Raw_Melt.csv']))
    teams.upload(''.join([NameOfFolder,'/melt_deriv.png']))
    if rep == 0:
        uploadToAir()

    print('Melt Done')



if fret:
    delta = []
    for i in [0,2,3,4,5,6,7]:
        delta.append(np.average(data[i][-5:])-np.average(data[i][:5]))
    
    # print(delta)
    channels = [415,480,515,555,590,630,680]

    # channels.remove(445)
    # channels.remove(415)
    # channels.remove(480)

    from scipy.interpolate import make_interp_spline

    # Dataset
    x = np.array(channels)
    y = np.array(delta[:len(channels)])
    frac = []
    tot = sum(delta)
    for i in delta:
        frac.append(i/tot)
    # print(frac)


    X_Y_Spline = make_interp_spline(x, y)

    # Returns evenly spaced numbers
    # over a specified interval.
    X_ = np.linspace(x.min(), x.max(), 500)
    Y_ = X_Y_Spline(X_)

    # Plotting the Graph
    plt.figure()
    plt.plot(X_, Y_,'-',x,y,'o')
    plt.title("Fret Curve")
    plt.xlabel("Channel (nm)")
    plt.ylabel("Fluorescence")
    plt.xticks((415,445,480,515,555,590,630,680),('415','445','480','515','555','590','630','680'))
    plt.grid()
    # plt.text('aaa')
    plt.savefig(''.join([NameOfFolder,'/fret.png']))

    teams.upload(''.join([NameOfFolder,'/fret.png']))



textFile()
shutil.move('file_info.txt',NameOfFolder)
if len(data) >0 or len(data_melt) >0:
    teams.upload(''.join([NameOfFolder,'/file_info.txt']))
end = time()

print(round(end-begin,2), ' sec')









