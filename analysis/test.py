from cProfile import label
from tkinter import *
import lib.add_lib_path
import lib.api_auth as auth
import lib.graphql_queries as qry
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from pcr import pcr
import numpy as np
from lib.consumable_config import getConfigMap
from melt.melt import MeltAnalysis
from scipy.interpolate import make_interp_spline

root = Tk()
root.geometry("600x400")
root.title("Josh's Super-Duper Cool Spectral Analysis Machine")

def analyze():
    consumableId = str(inputtxt.get("1.0", "end-1c"))
    # consumableId = '7ff89494-acf3-4c01-a053-22b54ca99349'

    note = ''

    refChan = int(refChanBox.get('1.0','end-1c'))
    api = auth.getApiClient()

    where = {
    'id': {
        '_eq': consumableId
    }
    }
    channels = [480,515,555,590,630,680]
    channelString = []


    for i in channels:
        channelString.append(str(i))


    rep = 0
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

    pcrAnalysis = pcr.PCRAnalysis(configuration)
    if len(data) > 0:
        pcrAnalysis.callPCR(data)
        anneal = response['data']['consumable'][0]['experiments'][rep]['experimentResult']['pcrData']['temperature']




    # def pcrplot():
    if varPCR.get() == 1 and varMelt.get() == 0:
        delta = []
        for i in [2,3,4,5,6,7]:
            delta.append(np.average(data[i][-2:])-np.average(data[i][:2]))

        # print(delta)
        

        x = np.array(channels)
        y = np.array(delta[:len(channels)])
        frac = []
        tot = sum(delta)
        for i in delta:
            frac.append(i/tot)


        X_Y_Spline = make_interp_spline(x, y)

        # Returns evenly spaced numbers
        # over a specified interval.
        X_ = np.linspace(x.min(), x.max(), 500)
        Y_ = X_Y_Spline(X_)

        # Plotting the Graph
        plt.figure()
        plt.plot(X_, Y_,'-',x,y,'o')
        plt.title(''.join([note,' ',consumableId[:6]]))
        plt.xlabel("Channel (nm)")
        plt.ylabel("Fluorescence")
        
        plt.xticks(channels,channelString)
        plt.grid()
        plt.savefig(''.join([consumableId[:6]]))
        plt.show()




    elif varMelt.get() == 1 and varPCR.get() == 0:
        x = np.array(channels)

    
        maxFluor = max(meltAnalysis.results['smoothDerivatives'][refChan])
        maxFluor = max(meltAnalysis.results['smoothDerivatives'][refChan][100:])
        tmIndx = list(meltAnalysis.results['smoothDerivatives'][refChan]).index(maxFluor)
        good_tm = meltAnalysis.results['smoothedT'][tmIndx]
        fluor = []
        for i in [2,3,4,5,6,7]:
            fluor.append(meltAnalysis.results['smoothDerivatives'][i][tmIndx])
        y = np.array(fluor)



        X_Y_Spline = make_interp_spline(x,y)

    
        X_ = np.linspace(x.min(), x.max(), 500)
        Y_ = X_Y_Spline(X_)

        # plt.plot(meltAnalysis.results['smoothedT'],meltAnalysis.results['smoothDerivatives'][4])
        plt.figure()
        plt.plot(X_,Y_)
        plt.plot(np.array(channels),fluor,'o')
        plt.title(''.join(['Spectral Signature ',consumableId[:6]]))
        plt.ylabel(''.join(["Melt Peak @ ",str(round(good_tm,1))]))
        plt.xlabel('Channel (nm)')
        # plt.ylim(-.15,2.2)
        plt.xticks((480,515,555,590,630,680),('480','515','555','590','630','680'))
        plt.grid()
        
        
        plt.savefig(''.join([consumableId[:6]]))
        plt.show()












varPCR = IntVar()
varMelt = IntVar()
checkPCR = Checkbutton(root,text='PCR',variable=varPCR,onvalue=1,offvalue=0)
checkMelt = Checkbutton(root,text='Melt',variable=varMelt,onvalue=1,offvalue=0)




















l = Label(text='Cup ID')


inputtxt = Text(root, height = 10,width = 25)
l2 = Label(text='Reference Channel')
refChanBox = Text(root,height=2,width=4)

quit = Button(text="Quit", command=root.destroy)
run = Button(root,height=2,width=20,text='Analyze',command=lambda:analyze())

# b.place(x=50,y=500)

l.pack()

inputtxt.pack()
run.pack()
l2.pack()
refChanBox.pack()
checkPCR.pack()
checkMelt.pack()

quit.pack(side='bottom',pady=50)




mainloop()