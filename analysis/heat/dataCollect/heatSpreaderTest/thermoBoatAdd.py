import os
import numpy as np
import pandas as pd
import openpyxl as op
from scipy import interpolate as interp
from openpyxl.chart import LineChart, Reference

newFile = 'TC.xlsx'
folder = 'dataTC'
alpha = 0.05
timeTo = []
fullTemp = []
fullTime = []
fullDerivTemp = []
tempc = np.arange(40,105,10)

for k in os.listdir(folder):
    fileName = k
    file = open(''.join([''.join([folder,'/']),fileName]),'r')
    filex = file.readlines()

    time = []
    temp = []
    absDif = []

    goodsTemp = []
    goodsTime = []
  
    for u in range(len(filex)):
        if 'TC-' in filex[u]:
            filex[u] = filex[u].split()
            goodsTemp.append(float(filex[u][4][:-1]))
            goodsTime.append(float(filex[u][0][1:-1])/1000)


    
    for j in range(len(goodsTemp)):
       
        if j != 0:
            if goodsTemp[j]-goodsTemp[j-1] >= 0.5 and goodsTemp[j] >=25:
                
                time.append(goodsTime[j])
                temp.append(goodsTemp[j])
            elif goodsTemp[j] >=50:
                time.append(goodsTime[j])
                temp.append(goodsTemp[j])
    
    time = np.array(time)-time[0]


    
    for u in tempc:
        absDif = []
        indx = []
        if max(temp) >= u:
            for i in temp:
         
                absDif.append(abs(u-i))

            indx = absDif.index(min(absDif))
         
            
            timeTo.append(time[indx])
        else:
            timeTo.append(0)
    fullTemp.append(temp)
    fullTime.append(time)

    timeTemp = np.array([time,temp]).T

    a,b,c = np.polyfit(time,temp,2)
    fullDerivTemp.append(2*a*time+b)




timeTo = [timeTo[i:i+len(tempc)] for i in range(0,len(timeTo),len(tempc))]
timeTo = np.array(timeTo).T

lens = []
for i in range(len(fullTime)):
    lens.append(len(fullTime[i]))
longest = max(lens)
longestTime = fullTime[lens.index(longest)]

sameLenTime = []
sameLenTemp = []
sameLenDeriv = []

for i in range(len(fullTime)):
    x = list(fullTime[i])
    y = list(fullTemp[i])
    z = list(fullDerivTemp[i])
    while len(x) < longest:
        
        x.append(None)
        y.append(None)
        z.append(None)
    sameLenTemp.append(y)
    sameLenTime.append(x)
    sameLenDeriv.append(z)

timeTo2 = timeTo.tolist()

timeTo2.insert(0,os.listdir(folder))

timeTo2 = np.array(timeTo2,dtype=object)


def addToExcel():

    wb = op.load_workbook(newFile)
    ws = wb['time to temp']
    
    tempc2 = tempc.tolist()
    tempc2.insert(0,"file name")
    tempc2.append('p/f')
    tempc2 = np.array(tempc2)
  
    timeToDict = {}
    for i in range(len(tempc2)):
        timeToDict[tempc2[i]] = list(timeTo2[i])
    dF = pd.DataFrame(timeTo2.T,columns=tempc2)
    tempc3 = []
    tempc2 = tempc2.tolist()
    for i in tempc2:
        try:
            tempc3.append(float(i))
        except:
            tempc3.append(i)

    ws.append(tempc3)
    timeTo3 = [ [] for _ in range(len(timeTo2.T))]
    for i in (range(len(timeTo2.T))):
        
        for u in timeTo2.T[i]:
            
            try:
                timeTo3[i].append(float(u))
            except:
                timeTo3[i].append(u)
    for i in timeTo3:

        ws.append(i)
        
    
    values = Reference(ws,min_col=1, min_row=2, max_col=len(tempc)+1, max_row=len(timeTo3)+1)
    labels = Reference(ws,min_col=2, min_row=1, max_col=len(tempc)+1, max_row=1)
  
    chart = LineChart()

    chart.add_data(values,titles_from_data=True,from_rows=True)
    chart.set_categories(labels=labels)
   
    
    ws.add_chart(chart,'K5')
  
   
    wb.save(newFile)

    
        

timesInterpNominal = []
x = interp.interp1d(fullTemp[0],fullTime[0])
for i in tempc:
    try:
        timesInterpNominal.append(x(i))
    except:
        timesInterpNominal.append(0)
pfTot = []
for j in range(len(fullTemp)):
    y = interp.interp1d(fullTime[j],fullTemp[j])
    tempsInterp = []
    for i in timesInterpNominal:
        try:
            tempsInterp.append(y(i))
        except:
            tempsInterp.append(0)

    count = 0
    pf = []
    for i in tempsInterp:
        if tempc[count]-i >= tempc[count]*(alpha):
            pf.append('p')
        else:
            pf.append('f')
        count += 1
    if 'f' not in pf:
        pfTot.append('pass')
    else:
        pfTot.append('fail')

timeTo2 = timeTo2.tolist()
timeTo2.append(np.array(pfTot))
timeTo2 = np.array(timeTo2)




addToExcel()


