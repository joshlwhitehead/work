# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 17:25:04 2021

@author: josh
"""

import pandas as pd
import matplotlib.pyplot as plt


###CSV FILES###

whichplot = input('which graph would you like to print?\namp curve\nmelt curve\nmelt derivative\n')

filename = pd.read_csv(input('Name of file: '))

samp = int(input('# of samples: '))

numconc = int(input('# of primer concentrations: '))
c1 = input('C1: ')
c2 = input('C2: ')
c3 = input('C3: ')
c4 = input('c4: ')
c5 = input('c5: ')


plottitle = input('Name of Plot: ')
titlex = input('x axis label: ')
titley = input('y axis label: ')



lines = ['-','--',':','-.']
colors = ['b','g','r','c','k']

def datalist(nameoffile,con1,con2,con3,con4,con5):

    data = []
    conc = [con1,con2,con3,con4,con5]
    count = 0
   
    
    for i in range(1,samp+1):       
        data.append(nameoffile[str(i)+': '+str(conc[count])])
        
        if count != len(conc)-1:
            count += 1

        else:
            count = 0


    return data


def ampplot(nameoffile,con1,con2,con3,con4,con5,linelist,colorlist,conc,xname,yname,name):
    xaxis = nameoffile['Text']
    yaxis = datalist(nameoffile,con1,con2,con3,con4,con5)
    plt.close('all')
    fig, ax = plt.subplots()
    
    count = 0
    count2 = 0
    count3 = 0
    for i in yaxis:
        ax.plot(xaxis,i,lw=2,color=colorlist[count],linestyle=linelist[count3],label=str(nameoffile.columns[count+1]))
        count3 += 1
        if count == 0:
            count2 += 0
            prev = 0 
           
        elif count == conc-1:
            count2 += 1
            prev = count
        elif count - prev == conc:
            count2 += 1
        else:
            count2 += 0
        if count3 ==conc:
            count3 -= count3
        count += 1

    
    
    plt.title(str(name),size=40)
    ax.legend(prop={'size':40})
    ax.tick_params(labelsize=30)
    plt.xlabel(str(xname),size=40)
    plt.ylabel(str(yname),size=40)
    plt.xlim()
    plt.grid()
    plt.show()
#ampplot(filename,c1,c2,c3,lines,colors,numconc,titlex,titley,plottitle)


def meltplot(nameoffile,conc,name,xname,yname,colorlist,linelist):
    xvals = []
    yvals = []
    count = 0
    for i in nameoffile.columns:
        if count % 2 != 0:
            xvals.append(i)
        elif count % 2 == 0 and count != 0:
            yvals.append(i)
        count += 1
        
    plt.close('all')
    fig, ax=plt.subplots()
    
    count = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 2
    for i in yvals:
        ax.plot(nameoffile[xvals[count4]],nameoffile[i],lw=2,color=colorlist[count],linestyle=linelist[count3],label=str(nameoffile.columns[count5]))
        count4 += 1
        
        count3 += 1
        if count == 0:
            count2 += 0
            prev = 0 
           
        elif count == conc-1:
            count2 += 1
            prev = count
        elif count - prev == conc:
            count2 += 1
        else:
            count2 += 0
        if count3 ==conc:
            count3 -= count3
        count += 1
        count5 += 2
    
    plt.title(str(name),size=40)
    ax.legend(prop={'size':40})
    ax.tick_params(labelsize=30)
    plt.xlabel(str(xname),size=40)
    plt.ylabel(str(yname),size=40)
    plt.xlim()
    plt.grid()
    plt.show()
#meltplot(filename,numconc,plottitle,titlex,titley,colors,lines)
    

def meltderivplot(nameoffile,numsamp,conc,name,xname,yname,colorlist,linelist):
    xvals = []
    yvals = []
    count = 0
    for i in nameoffile.columns:
        if count % 2 == 0:
            xvals.append(i)
        elif count % 2 != 0:
            yvals.append(i)
        count += 1
        
    plt.close('all')
    fig, ax=plt.subplots()
    
    count = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 1
    for i in yvals:
        ax.plot(nameoffile[xvals[count4]],nameoffile[i],lw=2,color=colorlist[count],linestyle=linelist[count3],label=str(nameoffile.columns[count5]))
        if count == numsamp-1:
            break
        count4 += 1
        
        count3 += 1
        if count == 0:
            count2 += 0
            prev = 0 
           
        elif count == conc-1:
            count2 += 1
            prev = count
        elif count - prev == conc:
            count2 += 1
        else:
            count2 += 0
        if count3 ==conc:
            count3 -= count3
        count += 1
        count5 += 2
    
    plt.title(str(name),size=40)
    ax.legend(prop={'size':40})
    ax.tick_params(labelsize=30)
    plt.xlabel(str(xname),size=40)
    plt.ylabel(str(yname),size=40)
    plt.xlim()
    plt.grid()
    plt.show()
#meltderivplot(filename,samp,numconc,plottitle,titlex,titley,colors,lines)




if whichplot == 'amp curve':
    ampplot(filename,c1,c2,c3,c4,c5,lines,colors,numconc,titlex,titley,plottitle)
elif whichplot == 'melt curve':
    meltplot(filename,numconc,plottitle,titlex,titley,colors,lines)
elif whichplot == 'melt derivative':
    meltderivplot(filename,samp,numconc,plottitle,titlex,titley,colors,lines)

































