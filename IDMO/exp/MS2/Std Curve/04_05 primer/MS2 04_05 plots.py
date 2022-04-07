# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 13:09:52 2021

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
lines = ['solid','dashed','dotted','dashdot','o']

def amp_plot():
    plt.close('all')
    count = 0
    count2 = 0
    for i in range(num_samp):
        plt.plot(file_data[column_name[0]],file_data[column_name[i+1]],color=colors[count],linestyle=lines[count2],label=str(column_name[i+1]))
        if count != num_conc-1:
            count += 1
        elif count == num_conc-1:
            count2 += 1
            count = 0
        else:
            count2 = 0
            
        
            
    plt.ylabel('Relative Fluorescence',size=30)
    plt.xlabel('Cycle',size=30)
    plt.title('Amplification Curve',size=30)
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
    countx = 0
    county = 1
    for i in range(num_samp,6):
        plt.plot(file_data[column_name[countx]],file_data[column_name[county]],color=colors[count],linestyle=lines[0],label=str(column_name[county]))
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
    plt.title('Melting Peak',size=30)
    plt.tick_params(labelsize=30)
    plt.legend(prop={'size':20})
    plt.grid()
    plt.show() 
    








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
        

        
        
        
        
        
    