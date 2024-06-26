import pandas as pd
import os

masterDir = 'covidContData'
masterBaselineDir = '/'.join([masterDir,'baselineRaw'])
masterSwapDir = '/'.join([masterDir,'swapRaw'])

baselinePCR = 'baselinePCR'
baselineMelt = 'baselineMelt'
swapPCR = 'swapPCR'
swapMelt = 'swapMelt'

inst = 'inst.csv'
fmax = 'fmax.csv'
cq = 'cq.csv'


fullBaselineInst = pd.read_csv(masterBaselineDir)