# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 17:51:25 2021

@author: joshl
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


###CSV FILES###
filename = pd.read_csv(input('Name of file: '))
samp = int(input('# of samples: '))
plottitle = input('Title of plot: ')
labelx = input('x axis')
labely = input('y axis')



xaxis = filename['Text']



def removebad(nameoffile):              ###remove unnecesary columns
    count = 0
    count2 = 1
    for i in nameoffile.columns:
        if nameoffile.columns[count] != 'S'+str(count2):
            nameoffile.drop(columns=i,axis=1,inplace=True)
        elif nameoffile.columns[count] == 'S'+str(count2):
            count += 1
            count2 += 1
removebad(filename)



###DATA###

def datalist(x,y):

    data = []
    for i in range(1,7):
        data.append(x['S'+str(i)])


    return data


###MELT DERIVATIVE###
def deriv(xarray,yarray):
    new_list = [0]
    for i in range(len(yarray)):
        if i == len(yarray)-1:
            break
        else:
            new_list.append(-(yarray[i+1]-yarray[i])/(xarray[i+1]-xarray[i]))
    return new_list

#print(deriv(xaxis,datalist(filename,samp)))


def plotstuff(xvals,yvals,y,title,xlab,ylab):
    plt.close('all')
    fig, ax=plt.subplots()
    
    count = 0
    count2 = 1
    for i in y.columns:
        if y.columns[count] != 'S'+str(count2):
            y.drop(columns=i,axis=1,inplace=True)
        elif y.columns[count] == 'S'+str(count2):
            count += 1
            count2 += 1
    
    count = 0
    for i in yvals:
        ax.plot(xvals,i,lw=5,label=str(y.columns[count]))
        count += 1
        print(np.max(i))
    plt.title(str(title),size=40)
    ax.legend(prop={'size':40})
    ax.tick_params(labelsize=30)
    plt.xlabel(str(xlab),size=40)
    plt.ylabel(str(ylab),size=40)
    plt.xlim(61.5,95)
    plt.grid()
    plt.show()
    

plotstuff(xaxis,datalist(filename,samp),filename,plottitle,labelx,labely)


    
    
    
    
    
    
    

"""
###PLOTS###
def amp_plot():
    plt.close('all')
    fig, ax=plt.subplots()

    ax.plot(cycle,amp[0],lw=5)

    #plt.ylim(0,40,5)
    #ax.legend(prop={'size':40})
    plt.xlabel('Cycles',size=40)
    plt.ylabel('RFU',size=40)
    ax.tick_params(labelsize=30)
    ax.grid()

    plt.show()
    
amp_plot()

def melt_plot():
    plt.close('all')
    fig, ax=plt.subplots()

    ax.plot(xaxis,deriv(xaxis,a),lw=5)
    ax.plot(xaxis,deriv(xaxis,b),lw=5)
    ax.plot(xaxis,deriv(xaxis,c),lw=5)
    ax.plot(xaxis,deriv(xaxis,d),lw=5)
    ax.plot(xaxis,deriv(xaxis,e),lw=5)
    ax.plot(xaxis,deriv(xaxis,f),lw=5)

    #plt.ylim(0,40,5)
    #ax.legend(prop={'size':40})
    plt.xlabel('Temperature',size=40)
    plt.ylabel('RFU',size=40)
    ax.tick_params(labelsize=30)
    ax.grid()

    plt.show()



def HRM_plot():
    plt.close('all')
    fig, ax=plt.subplots()

    ax.plot(temp2,HRM2,lw=5)

    #plt.ylim(0,40,5)
    #ax.legend(prop={'size':40})
    plt.xlabel('Temperature',size=40)
    plt.ylabel('RFU',size=40)
    ax.tick_params(labelsize=30)
    ax.grid()

    plt.show()
    

    
    
melt_plot()  
 """   
    
    
    
    
    
    
    