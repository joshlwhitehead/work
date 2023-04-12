import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
from scipy.stats import t
from parsTxt import parsPCRTxt, meltRamp

folder = 'data/'

def combDenat(folder):
    peakSamp = []
    for file in os.listdir(folder):
        peakSampList = parsPCRTxt(''.join([folder,file]))[0][0]                                     #collect temperatures while heating
        for peak in peakSampList:
            peakSamp.append(max(peak))
    return peakSamp

def combAnneal(folder):
    peakSamp = []
    for file in os.listdir(folder):
        peakSampList = parsPCRTxt(''.join([folder,file]))[1][0]                                     #collect temperatures while heating
        for peak in peakSampList:
            peakSamp.append(min(peak))
    return peakSamp


def combMelt(folder):
    rampRates = []
    for i in os.listdir(folder):
        meltTemps = meltRamp(''.join([folder,i]))[0][0]
        meltTimes = meltRamp(''.join([folder,i]))[0][1]
        a,b = np.polyfit(meltTimes,meltTemps,1)
        rampRates.append(a)

    return rampRates


print(combAnneal(folder))



