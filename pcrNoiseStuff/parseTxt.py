"""This script reads a .txt file generated from the DAVE tool during thermal runs. The script then parses out the thermocouple data.
The first function returns lists of temps while heating and lists of temps while cooling during the PCR stage. The lists are embedded within
another list, clumped by cycle number (ie. each cycle has a seperate list of heating/cooling temps).
The second function returns a single list of heat kill temperatures and a single list of activation temperatures during the Treatment stage.
Both functions also return the set temps used."""
import numpy as np
def parsPCRTxt(file):                                                                                                       #read PCR data

    with open(file,'r') as readFile:                                                                                        #convert lines in file to list
        file = readFile.readlines()

    fullTemp = []
    fullTime = []
    full515 = []
    timeFluor = []

    start = False
    



    for i in file:
        if 'Start PCR' in i:
            start = True

        elif 'MELT -> FINISH' in i:
            start = False

        if start and 'modeled' in i:
            fullTemp.append(float(i.split()[7].strip(',')))
            fullTime.append(float(i.split()[0].strip('()')))

        elif start and '_performCapture:' in i:
            full515.append(float(i.split()[2].strip('[]').split(',')[6]))
            timeFluor.append(float(i.split()[0].strip('()')))





    return (np.array(fullTemp),np.array(fullTime)),(np.array(full515),np.array(timeFluor))





