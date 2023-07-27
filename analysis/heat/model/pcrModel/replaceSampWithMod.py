import numpy as np
import matplotlib.pyplot as plt


with open('NEWBeta07_TT5_Run_1.txt','r') as f:
    file = f.readlines()



with open('newFile.txt','w') as f:
    modTot = []
    sampTot = []
    for indx,val in enumerate(file):
        if 'modeled' in val:
            modTot.append(val.split()[7].strip(','))
        if ('CHUBE:' or 'DATAQ:') in val:
            current = val.split()
            if len(modTot) > 0:
                new = modTot[-1]
            else:
                new = current[4]
            current[4] = new
            current = ''.join([current[0],' ',current[1],' ',current[2],' ',
                               current[3],' ',current[4],'  ',current[5],'\n'])
            f.writelines(current)
            

            
        else:
            f.writelines(val)
        