import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl as op
import xlsxwriter
from scipy import stats
import statsmodels.api as sm

newFile = 'PCR.xlsx'
timeTo = []
fullTemp = []
fullTime = []
fullDerivTemp = []
tempc = np.arange(40,115,10)
for k in os.listdir('data'):
    fileName = k#'Thermalboat 20221207 Rebuilt Run 3.txt'
    file = open(''.join(['data/',fileName]),'r')
    # tempC = 90
    time = []
    temp = []
    absDif = []
    count =0
    
    for u in file:
        if 'TC-' in u:
            u = u.split()
            if float(u[4][:-1]) >= 25:
                time.append(float(u[0][1:-1])/1000)
                temp.append(float(u[4][:-1]))
                # absDif.append(abs(tempC-float(u[5][:-1])))
                
    

                


    time = np.array(time)-time[0]


    
    for u in tempc:
        absDif = []
        indx = []
        for i in temp:
            absDif.append(abs(u-i))

        indx = absDif.index(min(absDif))
        # print(time[indx])

        timeTo.append(time[indx])
    fullTemp.append(temp)
    fullTime.append(time)

    timeTemp = np.array([time,temp]).T
    # wb = op.load_workbook(newFile)
    a,b,c = np.polyfit(time,temp,2)
    fullDerivTemp.append(2*a*time+b)
# fullTemp = np.array(fullTemp)
# fullTime = np.array(fullTime)
print(file.read())
dFTest = pd.DataFrame({'time':fullTime[0],'temp':fullTemp[0]})

formula = 'temp ~ time'
model = sm.formula.ols(formula,dFTest)
model_fitted = model.fit()
# print(model_fitted.summary())
    
timeTo = [timeTo[i:i+len(tempc)] for i in range(0,len(timeTo),len(tempc))]
timeTo = np.array(timeTo).T

lens = []
for i in range(len(fullTime)):
    lens.append(len(fullTime[i]))

sameLenTime = []
sameLenTemp = []
sameLenDeriv = []
longest = max(lens)
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

timeTo2.insert(0,os.listdir('data'))
# print(timeTo)
timeTo2 = np.array(timeTo2)


def toExcel():
    it = np.arange(0,len(timeTo))



    fullDict = {}
    for i in range(len(os.listdir('data'))):
        x = [os.listdir('data')[i]]
        while len(x) < longest:
            x.append(None)
        fullDict[''.join(['file name ',str(it[i])])] = x
        fullDict[''.join(['normalized time (sec) ',str(it[i])])] = sameLenTime[i]
        fullDict[''.join(['temp (c) ',str(it[i])])] = sameLenTemp[i]


    dFTot = pd.DataFrame(fullDict)
    writer = pd.ExcelWriter(newFile,engine='xlsxwriter')
    dFTot.to_excel(writer,sheet_name='full')
    wb = writer.book
    ws = writer.sheets['full']
    chart = wb.add_chart({'type':'line'})

    count = 2
    for i in range(len(sameLenTemp)):
        chart.add_series({
            'categories':['full',1,count,len(sameLenTemp[0]),count],
            'values':['full',1,count+1,len(sameLenTemp[0]),count+1],
            'name':['full',1,count-1]
            })
        count += 3
    chart.set_x_axis({'name':'Time (sec)'})
    chart.set_y_axis({'name':'Temp (c)'})

    ws.insert_chart('D2',chart)
    writer.save()









    wb = op.load_workbook(newFile)
    tempc2 = tempc.tolist()
    tempc2.insert(0,'file name')
    tempc2 = np.array(tempc2)
    with pd.ExcelWriter(newFile,engine='openpyxl') as writer:
        writer.book = wb
        writer.sheets = {worksheet.title:worksheet for worksheet in wb.worksheets}
        dF = pd.DataFrame(timeTo2.T,columns=tempc2)
        dF.to_excel(writer,'time to temp')
        writer.save()


    fullDict = {}
    for i in range(len(os.listdir('data'))):
        x = [os.listdir('data')[i]]
        while len(x) < longest:
            x.append(None)
        fullDict[''.join(['file name ',str(it[i])])] = x
        fullDict[''.join(['normalized time (sec) ',str(it[i])])] = sameLenTime[i]
        fullDict[''.join(['dTdt ',str(it[i])])] = sameLenDeriv[i]


    with pd.ExcelWriter(newFile,engine='openpyxl') as writer:
        writer.book = wb
        writer.sheets = {worksheet.title:worksheet for worksheet in wb.worksheets}
        dF = pd.DataFrame(fullDict)
        dF.to_excel(writer,'deriv')
        writer.save()

toExcel()
# print(timeTo[0])
# x = np.linspace(min(timeTo[-3]),max(timeTo[-3]))
# plt.hist(timeTo[-3],bins=10,density=True)
# plt.plot(x,stats.norm.pdf(x,loc=np.mean(timeTo[-3]),scale=np.std(timeTo[-3])))
# plt.show()

# print(stats.anderson(timeTo[-3]))



