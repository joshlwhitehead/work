import matplotlib.pyplot as plt
# import pandas as pd
import numpy as np
import scipy.optimize as opt
import dataToVar as dat

tset = [50,70,90,100]

nin = dat.newCup90
fif = dat.newCup50
sev = dat.newCup70
one = dat.newCup100
fifTherm = np.array(fif[1][100:])
sevTherm = np.array(sev[1][100:])
ninTherm = np.array(nin[1][100:])
oneTherm = np.array(one[1][100:])





def part1(list,set):
    lessOne = []
    for i in list:
        if i <= set:
            # print(i)
            lessOne.append(i)
        else:
            break
    return np.array(lessOne)
fiff = part1(fifTherm,50)
sevv = part1(sevTherm,70)
ninn = part1(ninTherm,90)
onee = part1(oneTherm,100)

fifSamp = np.array(fif[0][100:len(fiff)])-np.min(fif[0])
sevSamp = np.array(sev[0][100:len(sevv)])-np.min(sev[0])
ninSamp = np.array(nin[0][100:len(ninn)])-np.min(nin[0])
oneSamp = np.array(one[0][100:len(onee)])-np.min(one[0])

def mesh(a,b):
    A,B = np.meshgrid(a,b)
    return A,B

coef3d,xxx = opt.curve_fit()


























def r2(y,fun):
    st = sum((y-np.average(y))**2)
    sr = sum((y-fun)**2)
    r2 = 1-sr/st
    return round(r2,3)

# print(*param)
# plt.figure()
# plt.plot(lessOne,ninSamp[:len(lessOne)])
# plt.plot(lessOne,fit(lessOne,*param))
# # plt.plot(lessOne,a*lessOne+b)
# plt.grid()
# plt.savefig('fitToOne')



