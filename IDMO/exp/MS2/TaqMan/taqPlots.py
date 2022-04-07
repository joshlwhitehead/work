# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt


filename = input('Name of file? ')
file_data = pd.read_csv(filename)
column_name = file_data.columns                              #list of column names
num_samp = int(input('How many samples? '))                  #number of samples tested
num_conc = int(input('How many concentrations? '))


colors = ['b','r','g','k','c','pink','k']
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
            
        
            
    plt.ylabel('Relative Fluorescence')
    plt.xlabel('Cycle')
    plt.title('MS2 Amplification Curve (Saliva Test)')
    plt.tick_params()
    plt.legend()
    plt.grid()
    plt.show()
    
amp_plot()   
    
    
    
    
    
def melt_plot():
    plt.close('all')
    count = 0
    count2 = 0
    countx = 1
    county = 2
    for i in range(num_samp):
        plt.plot(file_data[column_name[countx]],file_data[column_name[county]],color=colors[count2],linestyle=lines[count],label=str(column_name[county]))
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
    plt.title('Melting Curve (Trial 2 Temp 2)',size=30)
    plt.tick_params(labelsize=30)
    plt.legend(prop={'size':20})
    plt.grid()
    plt.show()
    
#melt_plot()   
 
def deriv_plot():
    plt.close('all')
    count = 0
    count2 = 0
    countx = 0
    county = 1
    for i in range(num_samp):
        plt.plot(file_data[column_name[countx]],file_data[column_name[county]],color=colors[count2],linestyle=lines[count],label=str(column_name[county]))
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
    plt.title('Melting Peak (Trial 2 Temp 2)',size=30)
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
        

def sing_plot(inp):
    plt.close('all')
    
    plt.plot(file_data['Text'],file_data[inp],lw=4)
    plt.title('Amplification Curve of '+inp,size=30)
    plt.xlabel('Cycle',size=30)
    plt.ylabel('Relative Fluorescence',size=30)
    plt.ylim(.91,2.4)
    plt.tick_params(labelsize=30)
    plt.grid()
    plt.show()

        
        
        
    