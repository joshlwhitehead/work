from cProfile import label
from distutils.cmd import Command
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
root.geometry("400x600")
root.title("Josh's Super-Duper Cool Spectral Analysis Machine")

def analyze():
    consumableId = str(inputtxt.get("1.0", "end-1c")).split()
    deltaList = []
    for Id in consumableId:

        note = ''

        
        api = auth.getApiClient()

        where = {
        'id': {
            '_eq': Id
        }
        }
        
        channels = drop.curselection()
        print(channels)
        
        channelTot = ['415','445','480','515','555','590','630','680']

        channelString = []
        for i in channels:
            channelString.append(channelTot[i])


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




        
        if varPCR.get() == 1 and varMelt.get() == 0:
            
            delta = []
            for i in channels:
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
            # plt.figure()
            if consumableId.index(Id) == 0:
                plt.plot(X_, Y_,'-',label=''.join([Id[:6],' ','LED']))
            else:
                plt.plot(X_, Y_,'-',label=''.join([Id[:6],' ','Laser']))
            plt.plot(x,y,'o')
            plt.title(''.join([str(inputtxt2.get("1.0", "end-1c"))]))
            plt.xlabel("Channel (nm)")
            plt.ylabel("Delta Fluorescence")
            
            plt.xticks(channels,channelString)
            
            plt.legend()
    plt.grid()
    plt.savefig(''.join(['specSigLEDlaserComp/',str(inputtxt2.get("1.0", "end-1c"))]))
    plt.show()



        
        # if varMelt.get() == 1 and varPCR.get() == 0:
        #     refChan = int(channelTot.index(str(refChanBox.get())))
        #     print(refChan)
        #     x = np.array(channels)

        
        #     maxFluor = max(meltAnalysis.results['smoothDerivatives'][refChan])
        #     maxFluor = max(meltAnalysis.results['smoothDerivatives'][refChan][100:])
        #     tmIndx = list(meltAnalysis.results['smoothDerivatives'][refChan]).index(maxFluor)
        #     good_tm = meltAnalysis.results['smoothedT'][tmIndx]
        #     fluor = []
        #     for i in channels:
        #         fluor.append(meltAnalysis.results['smoothDerivatives'][i][tmIndx])
        #     y = np.array(fluor)



        #     X_Y_Spline = make_interp_spline(x,y)

        
        #     X_ = np.linspace(x.min(), x.max(), 500)
        #     Y_ = X_Y_Spline(X_)

        #     # plt.plot(meltAnalysis.results['smoothedT'],meltAnalysis.results['smoothDerivatives'][4])
        #     plt.figure()
        #     plt.plot(X_,Y_)
        #     plt.plot(np.array(channels),fluor,'o')
        #     plt.title(''.join([Id[:6],' ',str(inputtxt2.get("1.0", "end-1c"))]))
        #     plt.ylabel(''.join(["Melt Peak @ ",str(round(good_tm,1))]))
        #     plt.xlabel('Channel (nm)')
        #     # plt.ylim(-.15,2.2)
        #     plt.xticks(channels,channelString)
        #     plt.grid()
            
            
        #     plt.savefig(''.join([Id[:6],' ',str(inputtxt2.get("1.0", "end-1c"))]))
        #     # plt.show()
        
    












varPCR = IntVar(value=1)
varMelt = IntVar()
# var415 = IntVar()
# var445 = IntVar()
# var480 = IntVar()
# var515 = IntVar()
# var555 = IntVar()
# var590 = IntVar()
# var630 = IntVar()
# var680 = IntVar()


checkPCR = Checkbutton(root,text='PCR',variable=varPCR,onvalue=1,offvalue=0)
checkMelt = Checkbutton(root,text='Melt',variable=varMelt,onvalue=1,offvalue=0)
# check415 = Checkbutton(root,text='415',variable=var415,onvalue=1,offvalue=0)
# check445 = Checkbutton(root,text='445',variable=var445,onvalue=1,offvalue=0)
# check480 = Checkbutton(root,text='480',variable=var480,onvalue=1,offvalue=0)
# check515 = Checkbutton(root,text='515',variable=var515,onvalue=1,offvalue=0)
# check555 = Checkbutton(root,text='555',variable=var555,onvalue=1,offvalue=0)
# check590 = Checkbutton(root,text='590',variable=var590,onvalue=1,offvalue=0)
# check630 = Checkbutton(root,text='630',variable=var630,onvalue=1,offvalue=0)
# check680 = Checkbutton(root,text='680',variable=var680,onvalue=1,offvalue=0)

options = ['415','445','480','515','555','590','630','680']

drop = Listbox(root,selectmode='multiple')

for i in options:
    drop.insert(END,i)
# drop.event_generate(5)
drop.select_set(2,7)








lCup = Label(text='Cup ID')
lTitle = Label(text='Title')
lRefChan = Label(text='Reference Channel')
lChan = Label(text='Channels to Use')


inputtxt = Text(root, height = 8,width = 25)
inputtxt2 = Text(root,height=5,width=25)

# refChanBox = Text(root,height=2,width=4)
# refChanBox.set('d')

refChanBox = Entry(root)
refChanBox.insert(0,'515')


quit = Button(text="Quit", command=root.destroy)
run = Button(root,height=2,width=20,text='Analyze',command=lambda:analyze())

# b.place(x=50,y=500)

lCup.pack()


inputtxt.pack()
lTitle.pack()
inputtxt2.pack()


checkPCR.pack()
checkMelt.pack()
lRefChan.pack()
refChanBox.pack()
lChan.pack()
drop.pack()
# check415.pack()
# check445.pack()
# check480.pack()
# check515.pack()
# check555.pack()
# check590.pack()
# check630.pack()
# check680.pack()
run.pack()
quit.pack(side='bottom',pady=50)




mainloop()