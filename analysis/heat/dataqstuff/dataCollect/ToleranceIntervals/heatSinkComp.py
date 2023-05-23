import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from parsTxt import parsPCRTxt
import os
def test (x,a,b,c):
    return a*np.log(x+b)+c
for i in os.listdir('data'):
    x = np.array(parsPCRTxt(''.join(['data/',i]))[5][1])-parsPCRTxt(''.join(['data/',i]))[5][1][0]
    y = parsPCRTxt(''.join(['data/',i]))[5][0]
    popt,popc = curve_fit(test,x,y)

    plt.plot(x,y)
plt.show()