# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 12:12:38 2021

@author: josh
"""


import pandas as pd
import matplotlib.pyplot as plt


filename = input('Name of file? ')
file_data = pd.read_csv(filename)
column_name = file_data.columns                              #list of column names
num_samp = int(input('How many samples? '))                  #number of samples tested
num_conc = int(input('How many concentrations? '))


colors = ['b','r','g','orange','k']
lines = ['solid','dashed','dotted','dashdot']

def amp_plot():
    plt.close('all')
    count = 0
    count2 = 0
    for i in range(num_samp):
        plt.plot(file_data[column_name[0]],file_data[column_name[i+1]],color=colors[count2],linestyle=lines[count],label=str(column_name[i+1]))
        if count != num_conc-1:
            count += 1
        elif count == num_conc-1:
            count2 += 1
            count = 0
        else:
            count2 = 0
            
        
            
    plt.ylabel('Relative Fluorescence',size=30)
    plt.xlabel('Cycle',size=30)
    plt.title('Amplification Curve (After Color Comp.)',size=30)
    plt.tick_params(labelsize=30)
    plt.legend(prop={'size':20})
    plt.grid()
    plt.show()
    
#amp_plot()   
    
    
    
    
    
def melt_plot():
    plt.close('all')
    count = 0
    count2 = 0
    countx = 1
    county = 2
    for i in range(num_samp):
        plt.plot(file_data[column_name[countx]],file_data[column_name[county]],color=colors[count],linestyle=lines[count2],label=str(column_name[county]))
        if count != num_conc-1:
            count += 1
        elif count == num_conc-1:
            count2 += 1
            count = 0
        else:
            count2 = 0
        countx += 2
        county += 2
            
        
            
    plt.ylabel('Relative Fluorescence',size=30)
    plt.xlabel('Temperature (C)',size=30)
    plt.title('Melting Curve',size=30)
    plt.tick_params(labelsize=30)
    plt.legend(prop={'size':20})
    plt.grid()
    plt.show()
    
    
def deriv_plot():
    plt.close('all')
    count = 0
    count2 = 0
    countx = 20
    county = 21
    for i in range(10,num_samp):
        plt.plot(file_data[column_name[countx]],file_data[column_name[county]],color=colors[count],linestyle=lines[1],label=str(column_name[county]))
        if count != num_conc-1:
            count += 1
        elif count == num_conc-1:
            count2 += 1
            count = 0
        else:
            count2 = 0
        countx += 2
        county += 2
            
        
            
    plt.ylabel('-dF/dT',size=30)
    plt.xlabel('Temperature (C)',size=30)
    plt.title('Melting Peak (Third Set)',size=30)
    plt.tick_params(labelsize=30)
    plt.legend(prop={'size':20})
    plt.grid()
    plt.show() 
#deriv_plot() 








def trip_plots(col,num,curve):
    plt.close('all')
    count = 7
    for i in range(num):
        plt.plot(file_data[column_name[count-1]],file_data[column_name[count]],color=col,linestyle=lines[i],lw=3,label=str(column_name[count]))
        count += 10
    plt.grid() 
    plt.show()
    
    plt.ylabel('-dF/dT',size=30)
    plt.xlabel('Temperature (C)',size=30)
    plt.title(curve,size=30)
    plt.tick_params(labelsize=30)
    plt.legend(prop={'size':20})
        

def sing_plot(inp,inp2,col):
    plt.close('all')
    
    plt.plot(file_data['Text'],file_data[inp],color=col,lw=4,label=str(inp[3:]))
    plt.plot(file_data['Text'],file_data[inp2],color=col,linestyle='--',lw=4,label=str(inp2[3:]))
    plt.title('Amplification Curve of '+inp[3:len(inp)-1],size=30)
    plt.xlabel('Cycle',size=30)
    plt.ylabel('Relative Fluorescence',size=30)
    #plt.ylim(.85,1.05)
    plt.tick_params(labelsize=30)
    plt.legend(prop={'size':20})
    plt.grid()
    plt.show()

sing_plot('7: NAM+','8: NAM-','g')
        
        
        
    