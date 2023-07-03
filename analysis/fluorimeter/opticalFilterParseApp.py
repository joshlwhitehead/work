##################### IMPORTS   ##########################
import pandas as pd                
import numpy as np
from tkinter import *

######################  FUNCTION TO ANALYZE BANDPASS FILTER ###############################
def bandPass(): 
    data = str(inputtxt3.get("1.0", "end-1c")).split()              # get data from inputs
    fileName = str(inputtxt.get("1.0", "end-1c"))
    notes = str(inputtxt2.get("1.0", "end-1c"))

    x1 = []                             # parse x,y data from input
    y1 = []
    count = 0
    for i in data[1:]:
        if count%2 == 0:
            x1.append(float(i))
        else:
            y1.append(float(i))
        count += 1
    x1 = np.array(x1)
    y1 = np.array(y1)

    start = min(abs(400-x1))
    try:
        startIndx = list(x1).index(400-start)
    except:
        startIndx = list(x1).index(400+start)
    end = min(abs(500-x1))              # find closest value to 500
    try:
        cutIndx = list(x1).index(500-end)   
    except:
        cutIndx = list(x1).index(500+end)

    x1 = x1[startIndx:cutIndx]           # cutoff data at 500 nm
    y1 = y1[startIndx:cutIndx]

    max90 = 0.9*max(y1)                     
    maxList = [i for i in y1 if i >= max90]
    maxim = np.mean(maxList)            # take average of all points above 0.9*max

    halfMax = maxim*0.5         # half of max
    difs = abs(halfMax-y1)      
    onOff1 = min(difs)          # find value closest to halfmax

    difs = list(difs)           #find value second closest to halfmax
    difs.remove(onOff1)
    onOff2 = min(difs)

    try:
        onOffIndx1 = list(y1).index(halfMax-onOff1)
    except:
        onOffIndx1 = list(y1).index(halfMax+onOff1)
    try:
        onOffIndx2 = list(y1).index(halfMax-onOff2)
    except:
        onOffIndx2 = list(y1).index(halfMax+onOff2)


    cutOn50 = min(x1[onOffIndx1],x1[onOffIndx2])        #halfway up to max
    cutOff50 = max(x1[onOffIndx1],x1[onOffIndx2])       #halfway down to min

    fwhm = cutOff50 - cutOn50           #full width half max
    center = fwhm*0.5 + cutOn50         #center wavelength

    maxim = [round(maxim)]              # round values
    halfMax = [round(halfMax)]
    cutOn50 = [round(cutOn50)]
    cutOff50 = [round(cutOff50)]
    fwhm = [round(fwhm)]
    center = [round(center)]
    notes = [notes]
    for i in range(len(x1)-1):          #make values a list with same len as x,y
        maxim.append(None)
        halfMax.append(None)
        cutOn50.append(None)
        cutOff50.append(None)
        fwhm.append(None)
        center.append(None)
        notes.append(None)
    outPut = {                          #save data in dict
        'Wavelength (nm)':x1,
        'Transmission (%)':y1,
        'Max (%)':maxim,
        'Half Max (%)':halfMax,
        '50% Cut-On (nm)':cutOn50,
        '50% Cut-Off (nm)':cutOff50,
        'FWHM (nm)':fwhm,
        'Center Wavelength (nm)':center,
        'Notes':notes
    }
    dF = pd.DataFrame(outPut)
    dF.to_csv(''.join([fileName,'.csv']))               #save dataframe to csv
    return maxim,halfMax,cutOn50,cutOff50,fwhm,center



############################### FUNCTION TO ANALYZE LONGPASS FILTER #######################################
def longPass():
    data = str(inputtxt3.get("1.0", "end-1c")).split()          # get data from inputs
    fileName = str(inputtxt.get("1.0", "end-1c"))
    notes = str(inputtxt2.get("1.0", "end-1c"))
    x1 = []                                                     #parse x,y
    y1 = []
    count = 0
    for i in data[1:]:
        if count%2 == 0:
            x1.append(float(i))
        else:
            y1.append(float(i))
        count += 1
    x1 = np.array(x1)
    y1 = np.array(y1)
    start = min(abs(400-x1))
    try:
        startIndx = list(x1).index(400-start)
    except:
        startIndx = list(x1).index(400+start)
    end = min(abs(500-x1))
    try:
        cutIndx = list(x1).index(500-end)
    except:
        cutIndx = list(x1).index(500+end)

    x1 = x1[startIndx:cutIndx]                                           #end x,y at 500nm
    y1 = y1[startIndx:cutIndx]

    max90 = 0.9*max(y1)
    maxList = [i for i in y1 if i >= max90]
    maxim = np.mean(maxList)                                    #average data points over 0.90*max

    halfMax = maxim*0.5                                         #half of max

    halfMaxDif = min(abs(halfMax-y1))
    # print(halfMaxDif)
    try:
        halfMaxIndx = list(y1).index(halfMax-halfMaxDif)
    except:
        halfMaxIndx = list(y1).index(halfMax+halfMaxDif)
    cutOn50 = x1[halfMaxIndx]                                   # halfway up to max
    
    maxim = [round(maxim)]                      #round values
    halfMax = [round(halfMax)]
    cutOn50 = [round(cutOn50)]
    notes = [notes]
    for i in range(len(x1)-1):                  #make all values a list with same length of x,y
        maxim.append(None)
        halfMax.append(None)
        cutOn50.append(None)
        notes.append(None)
    outPut = {                                  #save data to dict
        'Wavelength (nm)':x1,
        'Transmission (%)':y1,
        'Max (%)':maxim,
        'Half Max (%)':halfMax,
        '50% Cut-On (nm)':cutOn50,
        'Notes':notes
    }
    dF = pd.DataFrame(outPut)
    dF.to_csv(''.join([fileName,'.csv']))   #save dataFrame to csv
    return maxim,halfMax,cutOn50

##############  BUILD UI    ####################################

root = Tk()                                                                                             #initialize user interface window
root.geometry("500x500")                                                                                #set size of window

root.title('Optical Filter Quantitation')                                                             #name ui window
inputtxt = Text(root, height = 1,width = 25)
inputtxt2 = Text(root, height = 8,width = 25)
inputtxt3 = Text(root, height = 8,width = 25)
run = Button(root,height=2,width=20,text='Bandpass',command=lambda:bandPass())                            #create button that runs the above code when pushed
run2 = Button(root,height=2,width=20,text='Longpass',command=lambda:longPass())                            #create button that runs the above code when pushed
label = Label(text='Filter ID')
label2 = Label(text='Notes')
label3 = Label(text='Raw Data')

def clear():
    inputtxt.delete('1.0','end')
    inputtxt2.delete('1.0','end')
    inputtxt3.delete('1.0','end')
clearButton = Button(root,text='Clear All',command=clear)
clearButton.place(x=5,y=5)
run.pack()
run2.pack()
label.pack()
inputtxt.pack()
label2.pack()
inputtxt2.pack()
label3.pack()
inputtxt3.pack()
clearButton.pack()
mainloop()


# plt.plot(x1,y1)
# plt.show()



