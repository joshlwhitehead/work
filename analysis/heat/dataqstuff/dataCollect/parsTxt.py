import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os



def parsPCRTxt(file):

    

    with open(file,'r') as readFile:
        file = readFile.readlines()


    heat = [[]]
    timeH = [[]]
    cool = [[]]
    timeC = [[]]
    heatCollect = False
    coolCollect = False
    start = False
    countLines = 0
    countH = 0
    countC = 0




    for u in file:
        if 'Start PCR' in u:
            start = True
        if 'goto' in u and 'Controlled' not in u and float(u.split()[-1]) > 85:
            heatCollect = True
            coolCollect = False
            # heat.append([])
        elif 'goto' in u and 'Controlled' not in u and float(u.split()[-1]) < 65:
            heatCollect = False
            coolCollect = True
        elif 'MELT' in u:
            start = False

        if start and 'DATAQ:' in u:

            try:
                if heatCollect and len(heat[countH]) != 0 and heat[countH][-1]-float(u.split()[4].strip(',')) > 10:
                    heat.append([])
                    timeH.append([])
                    countH+=1
                elif coolCollect and len(cool[countC]) != 0 and float(u.split()[4].strip(','))-cool[countC][-1] > 10:
                    cool.append([])
                    timeC.append([])
                    countC+=1
            except:
                pass
            
            
            if heatCollect:
                heat[countH].append(float(u.split()[4].strip(',')))
                timeH[countH].append(float(file[countLines-1].split()[0].strip('()'))/1000)

            elif coolCollect:
                cool[countC].append(float(u.split()[4].strip(',')))
                timeC[countC].append(float(file[countLines-1].split()[0].strip('()'))/1000)
        
        
        countLines += 1
    return (heat,timeH),(cool,timeC)



















