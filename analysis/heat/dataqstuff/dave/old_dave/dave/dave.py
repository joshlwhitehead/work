import ntpath
import threading
from pathlib import Path
from time import sleep
from tkinter.filedialog import askdirectory
from tkinter.ttk import Progressbar

from time import sleep

import matplotlib.pyplot as plt
import tkinter as tk
import os
from tkinter import ttk, messagebox

from datetime import datetime
from ttkwidgets import CheckboxTreeview
from functools import partial
from tkinter import *
from tkinter import filedialog
import csv
import pandas as pd

OUTPUT_CSV = 1


import numpy as np
from PIL import ImageTk

import tkinter as tk

from . import version

root = tk.Tk()
root.title("Data Acquisition Visualizer/Evaluator (DAVE)" + version.DAVE_VERSION)
fullPath = StringVar()
filename = StringVar()
dlFullPath = StringVar()
dlFilename = StringVar()
totalData = pd.DataFrame()

dqPCR_selected = IntVar()
dqSTQ1_selected = IntVar()

timestamps = []


class ParsedValue():
    def __init__(self, name, color, parseValueFunc=None, filterValueFunc=None, mainY=True, step=False, linewidth=1.0):
        self.name = name

        self.mainY = mainY
        self.color = color
        self.step = step
        self.linewidth = linewidth
        self.filterValueFunc = filterValueFunc
        self.parseValueFunc = parseValueFunc
        self.values = {}
        self.ax = None
        self.active = True

    def setActive(self, active=True):
        self.active = active


class PlotGroup():
    def __init__(self, name):
        self.name = name
        self.active = True
        self.parsedValues = []

    def addParsedValue(self, parsedValue):
        self.parsedValues.append(parsedValue)

    def setActive(self, active=True):
        self.active = active


def wavelength_to_rgb(wavelength, gamma=0.8):
    ''' taken from http://www.noah.org/wiki/Wavelength_to_RGB_in_Python
    This converts a given wavelength of light to an 
    approximate RGB color value. The wavelength must be given
    in nanometers in the range from 380 nm through 750 nm
    (789 THz through 400 THz).

    Based on code by Dan Bruton
    http://www.physics.sfasu.edu/astro/color/spectra.html
    Additionally alpha value set to 0.5 outside range
    '''
    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 750:
        A = 1.
    else:
        A=0.5
    if wavelength < 380:
        wavelength = 380.
    if wavelength >750:
        wavelength = 750.
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    return (R,G,B,A)

#  I (42904) thermalControlTask: thermalControl-1 = 47.92, target = 50.00, output = 100.00, p=208.17, i=-47.20, d=-0.00, ff=10.92

def stage1TempCFunc(line):
    try:
        return float(line.split("thermalControl-0 = ")[1].split(",")[0])
    except:
        return None

def stage1ModeledTempCFunc(line):
    try:
        return float(line.split("thermalControl-0 = ")[1].split("modeled = ")[1].split(",")[0])
    except:
        return None

def stage1ExpectedTempCFunc(line):
    try:
        return float(line.split("thermalControl-0 = ")[1].split("expectedTempC = ")[1].split(",")[0])
    except:
        return None

def stage1TargetTempCFunc(line):
    try:
        return float(line.split("thermalControl-0 = ")[1].split("target = ")[1].split(",")[0])
    except:
        return None

def stage1ControlledRampTargetFunc(line):
    try:
        return float(line.split("thermalControl-0 = ")[1].split("controlledRampTarget = ")[1].split(",")[0])
    except:
        return None

def stage1ActualTecRampRateFunc(line):
    try:
        return float(line.split("thermalControl-0 = ")[1].split("actualTecRampRate = ")[1].split(",")[0])
    except:
        return None

def stage1PriorTargetTecRampRateFunc(line):
    try:
        return float(line.split("thermalControl-0 = ")[1].split("priorTargetTecRampRate = ")[1].split(",")[0])
    except:
        return None


def stage1ErrorTimeMs(line):
    try:
        return float(line.split("thermalControl-0 = ")[1].split("timeout = ")[1].split(",")[0])
        #return float(line.split("thermalControlTask: ")[1].split("timeout = ")[1].split(",")[0])
    except:
        return None


def stage1PTermFunc(line):
    try:
        return float(line.split("thermalControl-0 = ")[1].split("p=")[1].split(",")[0])
    except:
        return None

def stage1ITermFunc(line):
    try:
        return float(line.split("thermalControl-0 = ")[1].split("i=")[1].split(",")[0])
    except:
        return None

def stage1DTermFunc(line):
    try:
        return float(line.split("thermalControl-0 = ")[1].split("d=")[1].split(",")[0])
    except:
        return None

def stage1FFTermFunc(line):
    try:
        return float(line.split("thermalControl-0 = ")[1].split("ff=")[1].split(",")[0])
    except:
        return None

def stage1OutputFunc(line):
    try:
        return float(line.split("thermalControl-0 = ")[1].split("output = ")[1].split(",")[0])
    except:
        return None


def  stage1TargetRate(line):
    try:
        return float(line.split("thermalControl-0 = ")[1].split("targetTecRampRate = ")[1].split(",")[0])
    except:
        return None

def stage1TecRate(line):
    try:
        return float(line.split("thermalControl-0 = ")[1].split("actualTecRampRate = ")[1].split(",")[0])
    except:
        return None

def stage1HeatsinkRate(line):
    try:
        return float(line.split("thermalControl-0 = ")[1].split("HSrate = ")[1].split(",")[0])
    except:
        return None

def pcrTempCFunc(line):
    try:
        return float(line.split("thermalControl-1 = ")[1].split(",")[0])
    except:
        return None

def pcrModeledTempCFunc(line):
    try:
        return float(line.split("thermalControl-1 = ")[1].split("modeled = ")[1].split(",")[0])
    except:
        return None

def pcrExpectedTempCFunc(line):
    try:
        return float(line.split("thermalControl-1 = ")[1].split("expectedTempC = ")[1].split(",")[0])
    except:
        return None

def pcrTargetTempCFunc(line):
    try:
        return float(line.split("thermalControl-1 = ")[1].split("target = ")[1].split(",")[0])
    except:
        return None

def pcrControlledRampTargetFunc(line):
    try:
        return float(line.split("thermalControl-1 = ")[1].split("controlledRampTarget = ")[1].split(",")[0])
    except:
        return None

def pcrHeatSinkTempFunc(line):
    try:
        return float(line.split("thermalControl-1 = ")[1].split("HeatSinkTemp = ")[1].split(",")[0])
    except:
        return None

def pcrActualTecRampRateFunc(line):
    try:
        return float(line.split("thermalControl-1 = ")[1].split("actualTecRampRate = ")[1].split(",")[0])
    except:
        return None

def pcrPriorTargetTecRampRateFunc(line):
    try:
        return float(line.split("thermalControl-1 = ")[1].split("priorTargetTecRampRate = ")[1].split(",")[0])
    except:
        return None

def  pcrTargetRate(line):
    try:
        return float(line.split("thermalControl-1 = ")[1].split("targetTecRampRate = ")[1].split(",")[0])
    except:
        return None

def pcrTecRate(line):
    try:
        return float(line.split("thermalControl-1 = ")[1].split("actualTecRampRate = ")[1].split(",")[0])
    except:
        return None

def pcrHeatsinkRate(line):
    try:
        return float(line.split("thermalControl-1 = ")[1].split("HSrate = ")[1].split(",")[0])
    except:
        return None

def pcrPTermFunc(line):
    try:
        return float(line.split("thermalControl-1 = ")[1].split("p=")[1].split(",")[0])
    except:
        return None

def pcrITermFunc(line):
    try:
        return float(line.split("thermalControl-1 = ")[1].split("i=")[1].split(",")[0])
    except:
        return None

def pcrDTermFunc(line):
    try:
        return float(line.split("thermalControl-1 = ")[1].split("d=")[1].split(",")[0])
    except:
        return None

def pcrFFTermFunc(line):
    try:
        return float(line.split("thermalControl-1 = ")[1].split("ff=")[1].split(",")[0])
    except:
        return None

def pcrOutputFunc(line):
    try:
        return float(line.split("thermalControl-1 = ")[1].split("output = ")[1].split(",")[0])
    except:
        return None

def pcrErrorC(line):
    try:
        return float(line.split("thermalControl-1 = ")[1].split("error = ")[1].split(",")[0])
        #return float(line.split("thermalControlTask: ")[1].split("error = ")[1].split(",")[0])
    except:
        return None

def pcrErrorTimeMs(line):
    try:
        return float(line.split("thermalControl-1 = ")[1].split("timeout = ")[1].split(",")[0])
        #return float(line.split("thermalControlTask: ")[1].split("timeout = ")[1].split(",")[0])
    except:
        return None

#('DATAQ', '29.37', '29.59')
def dataQFunc1(line):
    try:
        return float(line.split("DATAQ")[1].split(",")[1].replace("'", "").split(")")[0])
    except:
        return None

def dataQFunc2(line):
    try:
        return float(line.split("DATAQ")[1].split(",")[2].replace("'", "").split(")")[0])
    except:
        return None

#DATAQ:  | liquid = 26.41 | liquid2 = 24.57 | laser = 29.8 | pcrhtsnk = 31.61 | stg1htsnk = 23.3 |
def dataQLiquid(line):
    try:
        return float(line.split("DATAQ:")[1].split("| dataQLiquidStg1 = ")[1].split("|")[0])
    except:
        return None

def dataQLaser(line):
    try:
        return float(line.split("DATAQ:")[1].split("| laser = ")[1].split("|")[0])
    except:
        return None

def dataQC1T(line):
    try:
        #return float(line.split("DATAQ:")[1].split("| C1T = ")[1].split("|")[0])
        return float(line.split("DATAQ:")[1].split("| dataQStage1PeltierTop = ")[1].split("|")[0])
    except:
        return None

def dataQC1B(line):
    try:
        #return float(line.split("DATAQ:")[1].split("| C1B = ")[1].split("|")[0])
        return float(line.split("DATAQ:")[1].split("| dataQStage1PeltierBottom = ")[1].split("|")[0])

    except:
        return None

def dataQPCRT(line):
    try:
        return float(line.split("DATAQ:")[1].split("| dataQPcrPeltierTop = ")[1].split("|")[0].replace("*", ""))
    except:
        return None

def dataQPCRB(line):
    try:
        return float(line.split("DATAQ:")[1].split("| dataQPcrPeltierBottom = ")[1].split("|")[0])
    except:
        return None

def dataQPcrHeatsink(line):
    try:
        return float(line.split("DATAQ:")[1].split("| PCRHS = ")[1].split("|")[0])
    except:
        return None


def rawTECModel(line):
    try:
        return float(line.split("TEC-1")[1].split("ModeledTempC: ")[1])
    except:
        return None


def dataQStage1Heatsink(line):
    try:
        return float(line.split("DATAQ:")[1].split("| stg1htsnk = ")[1].split("|")[0])
    except:
        return None

def dataQPcrSlug(line):
    try:
        return float(line.split("DATAQ:")[1].split("| dataQPcrSlug = ")[1].split("|")[0])
    except:
        return None

def dataQStg1Slug(line):
    try:
        return float(line.split("DATAQ:")[1].split("| dataQStg1Slug = ")[1].split("|")[0])
    except:
        return None

#I (891063) _performCapture: [881472,17,77.74,306,18000,2854,261,334,310,493,550,10814,211]

def fluorescenceFuncTemp(line):
    try:
        return float(line.split("_performCapture")[1].split(",")[2])
    except:
        return None

def fluorescenceFunc0(line):
    try:
        return float(line.split("_performCapture")[1].split(",")[3])
    except:
        return None

def fluorescenceFunc1(line):
    try:
        return float(line.split("_performCapture")[1].split(",")[4])
    except:
        return None

def fluorescenceFunc2(line):
    try:
        return float(line.split("_performCapture")[1].split(",")[5])
    except:
        return None

def fluorescenceFunc3(line):
    try:
        return float(line.split("_performCapture")[1].split(",")[6])
    except:
        return None

def fluorescenceFunc4(line):
    try:
        return float(line.split("_performCapture")[1].split(",")[7])
    except:
        return None

def fluorescenceFunc5(line):
    try:
        return float(line.split("_performCapture")[1].split(",")[8])
    except:
        return None

def fluorescenceFunc6(line):
    try:
        return float(line.split("_performCapture")[1].split(",")[9])
    except:
        return None

def fluorescenceFunc7(line):
    try:
        return float(line.split("_performCapture")[1].split(",")[10])
    except:
        return None

def fluorescenceFunc8(line):
    try:
        return float(line.split("_performCapture")[1].split(",")[11])
    except:
        return None

def fluorescenceFunc9(line):
    try:
        return float(line.split("_performCapture")[1].split(",")[12].split("]")[0])
    except:
        return None


def qDotRatioFunc(line):
    try:
        ch590nm = float(line.split("_performCapture")[1].split(",")[8])
        ch630nm = float(line.split("_performCapture")[1].split(",")[9])
        return ch590nm / ch630nm
    except:
        return None

def qDotPredictedTempCFunc(line):
    try:
        ch590nm = float(line.split("_performCapture")[1].split(",")[8])
        ch630nm = float(line.split("_performCapture")[1].split(",")[9])
        ratio = ch590nm / ch630nm
        # a = 2.6
        # b = -0.012
        # a = 2.75
        # b = -0.012
        # a = 2.615
        # b = -0.011
        # a = 2.1055
        # b = -0.009
        ### alpha cup
        # a = 3.494
        # b = -0.017
        # a = 4.0408
        # b = -0.0202
        # a = 4.371
        # b = -0.0216
        a = 5.015
        b = -0.0256
        return ((ratio - a) / b)
    except:
        return None

#"ExperimentStatePcr", "time: %d, state: %d", timerMs, _state);
def pcrDebugTimeMsFunc(line):
    try:
        return int(line.split("ExperimentStatePcr")[1].split("time: ")[1].split(",")[0])
    except:
        return None

def pcrDebugStateFunc(line):
    try:
        return int(line.split("ExperimentStatePcr")[1].split("state: ")[1])
    except:
        return None
       
#{'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'}
stage1Plot = PlotGroup("Stage1")
# stage1Plot.addParsedValue(ParsedValue("stage1TempC",         color='tab:cyan',   parseValueFunc=stage1TempCFunc))
# stage1Plot.addParsedValue(ParsedValue("stage1FilteredTempC", color='tab:red',    parseValueFunc=stage1FilteredTempCFunc))
# stage1Plot.addParsedValue(ParsedValue("stage1SetTempC",      color='tab:green',  parseValueFunc=stage1SetTempCFunc,     step=True))
# stage1Plot.addParsedValue(ParsedValue("stage1RampSetTempC",  color='tab:blue',   parseValueFunc=stage1RampSetTempCFunc, step=True))
# stage1Plot.addParsedValue(ParsedValue("dataQStage1Heatsink", color='tab:gray', parseValueFunc=dataQStage1Heatsink))
stage1Plot.addParsedValue(ParsedValue("dataQStage1PeltierTop", color='tab:pink', parseValueFunc=dataQC1T))
stage1Plot.addParsedValue(ParsedValue("dataQStage1PeltierBottom", color='tab:olive', parseValueFunc=dataQC1B))
stage1Plot.addParsedValue(ParsedValue("dataQLiquidStg1", color='tab:purple', parseValueFunc=dataQLiquid))
stage1Plot.addParsedValue(ParsedValue("dataQStg1Slug", color='tab:blue', parseValueFunc=dataQStg1Slug))

stage1Plot.addParsedValue(ParsedValue("Stage1 Temp",                            color = 'tab:cyan', parseValueFunc=stage1TempCFunc))
stage1Plot.addParsedValue(ParsedValue("Stage1 Modeled TempC",                   color='tab:orange', parseValueFunc=stage1ModeledTempCFunc))
stage1Plot.addParsedValue(ParsedValue("Stage1 Expected TempC",                  color='tab:green',  parseValueFunc=stage1ExpectedTempCFunc,     step=True))
stage1Plot.addParsedValue(ParsedValue("Stage1 Target TempC",                    color='tab:blue',   parseValueFunc=stage1TargetTempCFunc, step=True))
stage1Plot.addParsedValue(ParsedValue("Stage1 Controlled Ramp Target",          color='tab:red',    parseValueFunc=stage1ControlledRampTargetFunc))

# stage1Plot.addParsedValue(ParsedValue("dataQStage1Heatsink",                    color='tab:gray',   parseValueFunc=dataQStage1Heatsink))
# stage1Plot.addParsedValue(ParsedValue("dataQStage1PeltierTop",                  color='tab:pink',   parseValueFunc=dataQC1T))
# stage1Plot.addParsedValue(ParsedValue("dataQStage1PeltierBottom",               color='tab:olive',  parseValueFunc=dataQC1B))
# stage1Plot.addParsedValue(ParsedValue("dataQStg1Slug",                          color='tab:blue',   parseValueFunc=dataQStg1Slug))
# stage1Plot.addParsedValue(ParsedValue("dataQ Liquid Stg1",                        color='tab:purple', parseValueFunc=dataQLiquid))

stage1PidPlot = PlotGroup("Stage1Pid")
stage1PidPlot.addParsedValue(ParsedValue("Stage1 P Term",                       color='tab:red',    parseValueFunc=stage1PTermFunc))
stage1PidPlot.addParsedValue(ParsedValue("Stage1 I Term",                       color='tab:green',  parseValueFunc=stage1ITermFunc))
stage1PidPlot.addParsedValue(ParsedValue("Stage1 D Term",                       color='tab:blue',   parseValueFunc=stage1DTermFunc))
stage1PidPlot.addParsedValue(ParsedValue("Stage1 FF Term",                      color='tab:purple', parseValueFunc=stage1FFTermFunc, mainY=False))
stage1PidPlot.addParsedValue(ParsedValue("Stage1 Output",                       color='tab:orange', parseValueFunc=stage1OutputFunc, mainY=False))

stage1PidPlot.addParsedValue(ParsedValue("Stage1 Actual TEC Temp Rate",         color='tab:olive',  parseValueFunc=stage1ActualTecRampRateFunc))
stage1PidPlot.addParsedValue(ParsedValue("Stage1 Prior Target TEC Ramp Rate",   color='tab:pink',   parseValueFunc=stage1PriorTargetTecRampRateFunc))


# pcrPlot.addParsedValue(ParsedValue("pcrTempC",         color='tab:cyan',   parseValueFunc=pcrTempCFunc))
# pcrPlot.addParsedValue(ParsedValue("pcrFilteredTempC", color='tab:red',    parseValueFunc=pcrFilteredTempCFunc))
# pcrPlot.addParsedValue(ParsedValue("pcrModeledTempC",  color='tab:orange', parseValueFunc=pcrModeledTempCFunc))
# pcrPlot.addParsedValue(ParsedValue("pcrExpectedTempC", color='tab:brown',  parseValueFunc=pcrExpectedTempCFunc))
# pcrPlot.addParsedValue(ParsedValue("pcrLiquidTempC",   color='tab:purple', parseValueFunc=dataQFunc1))
# pcrPlot.addParsedValue(ParsedValue("pcrAboveTempC",    color='tab:pink',   parseValueFunc=dataQFunc2))
# pcrPlot.addParsedValue(ParsedValue("QDotRatioPredictedTempC", color='tab:olive', parseValueFunc=qDotPredictedTempCFunc))
# pcrPlot.addParsedValue(ParsedValue("pcrSetTempC",      color='tab:green',  parseValueFunc=pcrSetTempCFunc,     step=True))
# pcrPlot.addParsedValue(ParsedValue("pcrRampSetTempC",  color='tab:blue',   parseValueFunc=pcrRampSetTempCFunc, step=True))




errorMsPlot = PlotGroup("ErrorMs")
errorMsPlot.addParsedValue(ParsedValue("Stage1 Error Time Ms", color='tab:red', parseValueFunc= stage1ErrorTimeMs))
errorMsPlot.addParsedValue(ParsedValue("PCR Error Time Ms", color='tab:blue', parseValueFunc= pcrErrorTimeMs))


ratesPlot = PlotGroup("Rates")
ratesPlot.addParsedValue(ParsedValue("Stage1 Target Rate", color='tab:cyan', parseValueFunc= stage1TargetRate))
ratesPlot.addParsedValue(ParsedValue("Stage1 TEC Rate", color='tab:red', parseValueFunc= stage1TecRate))
ratesPlot.addParsedValue(ParsedValue("Stage1 Heatsink Rate", color='tab:orange', parseValueFunc= stage1HeatsinkRate))

ratesPlot.addParsedValue(ParsedValue("PCR Target Rate", color='tab:brown', parseValueFunc= pcrTargetRate))
ratesPlot.addParsedValue(ParsedValue("PCR TEC Rate", color='tab:purple', parseValueFunc= pcrTecRate))
ratesPlot.addParsedValue(ParsedValue("PCR Heatsink Rate", color='tab:pink', parseValueFunc= pcrHeatsinkRate))


#Temp
#Modeled
#Controlled Ramp Target
#Target
#Expcected Temp C
#Actual TEC Ramp RAte
#Priror Target Tec Ramp Rate

pcrPlot = PlotGroup("Pcr")
pcrPlot.addParsedValue(ParsedValue("dataQ Liquid PCR",                        color='tab:purple', parseValueFunc=dataQLiquid))
pcrPlot.addParsedValue(ParsedValue("PCR Temp",                            color = 'tab:cyan', parseValueFunc=pcrTempCFunc))
pcrPlot.addParsedValue(ParsedValue("PCR Modeled TempC",                   color='tab:orange', parseValueFunc=pcrModeledTempCFunc))
pcrPlot.addParsedValue(ParsedValue("PCR Expected TempC",                  color='tab:green',  parseValueFunc=pcrExpectedTempCFunc,     step=True))
pcrPlot.addParsedValue(ParsedValue("PCR Target TempC",                    color='tab:blue',   parseValueFunc=pcrTargetTempCFunc, step=True))
pcrPlot.addParsedValue(ParsedValue("PCR Controlled Ramp Target",          color='tab:red',    parseValueFunc=pcrControlledRampTargetFunc))
pcrPlot.addParsedValue(ParsedValue("PCR Heat Sink Temp",                  color='tab:gray',   parseValueFunc=pcrHeatSinkTempFunc))


# pcrPlot.addParsedValue(ParsedValue("pcrTempC",         color='tab:cyan',   parseValueFunc=pcrTempCFunc))






# pcrPlot.addParsedValue(ParsedValue("dataQLiquid",  color='tab:purple',       parseValueFunc=dataQLiquid))
# pcrPlot.addParsedValue(ParsedValue("dataQLiquid2",  color='tab:olive',       parseValueFunc=dataQLiquid2))
# pcrPlot.addParsedValue(ParsedValue("dataQLiquidAvg",  color='tab:olive',       parseValueFunc=dataQLiquidAvg))
# pcrPlot.addParsedValue(ParsedValue("dataQLaser",  color='tab:pink',          parseValueFunc=dataQLaser))

pcrPlot.addParsedValue(ParsedValue("dataQPcrSlug",     color='tab:red',   parseValueFunc= dataQPcrSlug))
pcrPlot.addParsedValue(ParsedValue("dataQPcrPeltierTop", color='tab:pink', parseValueFunc=dataQPCRT))
pcrPlot.addParsedValue(ParsedValue("dataQPcrPeltierBottom", color='tab:olive', parseValueFunc=dataQPCRB))
pcrPlot.addParsedValue(ParsedValue("dataQPcrHeatsink", color='tab:blue', parseValueFunc=dataQPcrHeatsink))
pcrPlot.addParsedValue(ParsedValue("rawTECModel", color='tab:blue', parseValueFunc=rawTECModel))

pcrPidPlot = PlotGroup("PcrPid")
pcrPidPlot.addParsedValue(ParsedValue("pcrPTerm",     color='tab:red',    parseValueFunc=pcrPTermFunc))
pcrPidPlot.addParsedValue(ParsedValue("pcrITerm",     color='tab:green',  parseValueFunc=pcrITermFunc))
pcrPidPlot.addParsedValue(ParsedValue("pcrDTerm",     color='tab:blue',   parseValueFunc=pcrDTermFunc))
pcrPidPlot.addParsedValue(ParsedValue("pcrFFTerm",    color='tab:purple', parseValueFunc=pcrFFTermFunc, mainY=False))
pcrPidPlot.addParsedValue(ParsedValue("pidOutput",    color='tab:orange', parseValueFunc=pcrOutputFunc))

# stage1PidPlot.addParsedValue(ParsedValue("PCR Actual TEC Temp Rate",         color='tab:olive',  parseValueFunc=pcrActualTecTempRate))
# stage1PidPlot.addParsedValue(ParsedValue("PCR Prior Target TEC Ramp Rate",   color='tab:pink',   parseValueFunc=pcrPriorTargetTecRampRate))


fluorescencePlot = PlotGroup("Fluorescence")
fluorescencePlot.addParsedValue(ParsedValue("415nm", color=wavelength_to_rgb(415), parseValueFunc=fluorescenceFunc0))
fluorescencePlot.addParsedValue(ParsedValue("445nm", color=wavelength_to_rgb(445), parseValueFunc=fluorescenceFunc1))
fluorescencePlot.addParsedValue(ParsedValue("480nm", color=wavelength_to_rgb(480), parseValueFunc=fluorescenceFunc2))
fluorescencePlot.addParsedValue(ParsedValue("515nm", color=wavelength_to_rgb(515), parseValueFunc=fluorescenceFunc3))
fluorescencePlot.addParsedValue(ParsedValue("555nm", color=wavelength_to_rgb(555), parseValueFunc=fluorescenceFunc4))
fluorescencePlot.addParsedValue(ParsedValue("590nm", color=wavelength_to_rgb(590), parseValueFunc=fluorescenceFunc5))
fluorescencePlot.addParsedValue(ParsedValue("630nm", color=wavelength_to_rgb(630), parseValueFunc=fluorescenceFunc6))
fluorescencePlot.addParsedValue(ParsedValue("680nm", color=wavelength_to_rgb(680), parseValueFunc=fluorescenceFunc7))
fluorescencePlot.addParsedValue(ParsedValue("Clear", color='tab:gray', parseValueFunc=fluorescenceFunc8))
fluorescencePlot.addParsedValue(ParsedValue("Nir", color=wavelength_to_rgb(720), parseValueFunc=fluorescenceFunc9))
fluorescencePlot.addParsedValue(ParsedValue("QDotRatio", color='tab:brown', parseValueFunc=qDotRatioFunc))
fluorescencePlot.addParsedValue(ParsedValue("FluorTemp", color='tab:brown', parseValueFunc=fluorescenceFuncTemp))
fluorescencePlot.addParsedValue(
    ParsedValue("qDotPredictedTempC", color='tab:pink', parseValueFunc=fluorescenceFuncTemp))

# debugPlot = PlotGroup("Debug")
# debugPlot.addParsedValue(ParsedValue("pcrDebugTimer",         color='tab:red',   parseValueFunc=pcrDebugTimeMsFunc))
# debugPlot.addParsedValue(ParsedValue("pcrDebugState",         color='tab:blue',  parseValueFunc=pcrDebugStateFunc, mainY=False, step=True))

plots = []
plots.append(stage1Plot)
plots.append(stage1PidPlot)
plots.append(pcrPlot)
plots.append(pcrPidPlot)
plots.append(errorMsPlot)
plots.append(ratesPlot)
plots.append(fluorescencePlot)
# plots.append(debugPlot)


def pickFile():
    fullPath.set(filedialog.askopenfilename(title="Select log file"))
    filename.set(os.path.basename(fullPath.get()))
    root.update_idletasks()


def parseLogFile(path):
    previousTimestamp = 0
    timestamps = []
    started = False
    with open(path, 'r') as file:
        line = file.readline()
        while line:
            try:
                try:

                    #put this back in if data recording start isnt consistent -Van Hoose
                    if not started:
                        if "TC:" in line:
                            started = True
                        else:
                            line = file.readline()
                            continue

                    timestamp = float(line.split("(")[1].split(")")[0])
                    timestamp = timestamp / 1000
                    timestamps.append(timestamp)
                except:
                    timestamp = previousTimestamp
                previousTimestamp = timestamp
                for plot in plots:
                    for parsedValue in plot.parsedValues:
                        if parsedValue.parseValueFunc != None:
                            value = parsedValue.parseValueFunc(line)
                            if value != None:
                                if parsedValue.filterValueFunc != None:
                                    if not parsedValue.filterValueFunc(value):
                                        pass
                                parsedValue.values[timestamp] = value
            except:
                pass

            line = file.readline()

    file.close()
    return timestamps

    # meltStartTimeKey = 0.0
    # for k,v in fluorescencePlot.parsedValues[11].values.items():
    #     if v < 55:
    #         meltStartTimeKey = k

    # meltPortionRatio = {key:value for key, value in fluorescencePlot.parsedValues[10].values.items() if key > meltStartTimeKey }
    # meltPortionTemps = {key:value for key, value in fluorescencePlot.parsedValues[11].values.items() if key > meltStartTimeKey }
    # secondOrder, firstOrder, constant = np.polyfit([meltPortionRatio[k] for k in meltPortionRatio], [meltPortionTemps[k] - 5 for k in meltPortionTemps], deg=2)

    # print(secondOrder, firstOrder, constant)

    # for k,v in fluorescencePlot.parsedValues[10].values.items():
    #     fluorescencePlot.parsedValues[12].values[k] = (secondOrder * v * v) + (firstOrder * v) + constant

def NewSubplot(singlePlot, axs, index, parsedValue):
    if singlePlot:
        obj = axs
    else:
        obj = axs[index]
    lists = sorted(parsedValue.values.items())
    if len(lists) >= 2:
        x, y = zip(*lists)

        if parsedValue.step:
            obj.step(x, y, where='post', color=parsedValue.color, label=parsedValue.name, linewidth=parsedValue.linewidth)
        else:
            obj.plot(x, y, color=parsedValue.color, label=parsedValue.name, linewidth=parsedValue.linewidth, clip_on=False)
        obj.tick_params(axis='y', labelcolor=parsedValue.color)


def AddToSubplotWithNewY(singlePlot, axs, index, parsedValue, newYIndex):
    if singlePlot:
        obj = axs
    else:
        obj = axs[index]
    if parsedValue.ax != None:
        parsedValue.ax.cla()
    ax = obj.twinx()
    parsedValue.ax = ax
    lists = sorted(parsedValue.values.items())
    if len(lists) >= 2:
        x, y = zip(*lists)
        ax.set_ylabel(parsedValue.name, color=parsedValue.color)
        if parsedValue.step:
            ax.step(x, y, where='post', color=parsedValue.color, label=parsedValue.name, linewidth=parsedValue.linewidth, clip_on=False)
        else:
            ax.plot(x, y, color=parsedValue.color, label=parsedValue.name, linewidth=parsedValue.linewidth, clip_on=False)

        ax.spines['right'].set_position(('outward', 40 * newYIndex))

        ax.tick_params(axis='y', labelcolor=parsedValue.color)


def AddToSubplot(singlePlot, axs, index, parsedValue):
    if singlePlot:
        obj = axs
    else:
        obj = axs[index]
    lists = sorted(parsedValue.values.items())
    if len(lists) >= 2:
        x, y = zip(*lists)
        if parsedValue.step:
            obj.step(x, y, where='post', color=parsedValue.color, label=parsedValue.name, linewidth=parsedValue.linewidth, clip_on=False)
        else:
            obj.plot(x, y, color=parsedValue.color, label=parsedValue.name, linewidth=parsedValue.linewidth, clip_on=False)


def RunPlot():
    singlePlot = False
    plotCount = 0
    for plot in plots:
        if plot.active:
            plotCount += 1
    if plotCount == 1:
        singlePlot = True
    elif plotCount < 1:
        return
    fig, axs = plt.subplots(plotCount, 1, sharex=True)

    largestNewYIter = 0
    plotIter = 0
    for plot in plots:
        if plot.active:
            if not singlePlot:
                axs[plotIter].cla()
            pvIter = 0
            newYIter = 0
            for parsedValue in plot.parsedValues:
                lists = sorted(parsedValue.values.items())
                if parsedValue.active and len(lists) > 1:
                    if pvIter == 0:
                        NewSubplot(singlePlot, axs, plotIter, parsedValue)
                    else:
                        if parsedValue.mainY:
                            AddToSubplot(singlePlot, axs, plotIter, parsedValue)
                        else:
                            AddToSubplotWithNewY(singlePlot, axs, plotIter, parsedValue, newYIter)
                            newYIter += 1
                pvIter += 1
            if singlePlot:
                axs.legend(bbox_to_anchor=(-.02, 1))
            else:
                axs[plotIter].legend(bbox_to_anchor=(-.02, 1))

            if newYIter > largestNewYIter:
                largestNewYIter = newYIter
            plotIter += 1
    plt.subplots_adjust(right=0.95 - 0.025 * largestNewYIter)
    figManager = plt.get_current_fig_manager()
    #figManager.window.state("zoomed")
    plt.show()


def setActives(checkboxTree):
    checkedItems = []
    for item in checkboxTree.get_checked():
        checkedItems.append(item)

    for plot in plots:
        anythingChecked = False
        for parsedValue in plot.parsedValues:
            if parsedValue.name in checkedItems:
                parsedValue.setActive(True)
                anythingChecked = True
            else:
                parsedValue.setActive(False)
        if not anythingChecked:
            plot.setActive(False)
        else:
            plot.setActive(True)


def graphData(checkboxTree):
    setActives(checkboxTree)
    if filename.get() != "":
        timestamps = parseLogFile(fullPath.get())
        # f = open("RunDictionaries_20210719_1017.txt", "w")
        # f.write("RawTempC\r\n")
        # f.write(str(pcrPlot.parsedValues[0].values))
        # f.write("\r\nFilteredTempC\r\n")
        # f.write(str(pcrPlot.parsedValues[1].values))
        # f.write("\r\n415nm\r\n")
        # f.write(str(fluorescencePlot.parsedValues[0].values))
        # f.write("\r\n445nm\r\n")
        # f.write(str(fluorescencePlot.parsedValues[1].values))
        # f.write("\r\n480nm\r\n")
        # f.write(str(fluorescencePlot.parsedValues[2].values))
        # f.write("\r\n515nm\r\n")
        # f.write(str(fluorescencePlot.parsedValues[3].values))
        # f.write("\r\n555nm\r\n")
        # f.write(str(fluorescencePlot.parsedValues[4].values))
        # f.write("\r\n590nm\r\n")
        # f.write(str(fluorescencePlot.parsedValues[5].values))
        # f.write("\r\n630nm\r\n")
        # f.write(str(fluorescencePlot.parsedValues[6].values))
        # f.write("\r\n680nm\r\n")
        # f.write(str(fluorescencePlot.parsedValues[7].values))
        # f.write("\r\nClear\r\n")
        # f.write(str(fluorescencePlot.parsedValues[8].values))
        # f.write("\r\nNir\r\n")
        # f.write(str(fluorescencePlot.parsedValues[9].values))
        # f.write("\r\nLiquidTempC\r\n")
        # f.write(str(pcrPlot.parsedValues[2].values))
        # f.write("\r\nAboveTempC\r\n")
        # f.write(str(pcrPlot.parsedValues[3].values))
    
    columns = ["timeSinceBootSeconds"]
    dicts = []

    for plot in plots:
        for parsedValue in plot.parsedValues:
            columns.append(parsedValue.name)
            dicts.append(parsedValue.values)

    if OUTPUT_CSV:
        with open(datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv", 'w', newline='') as ofile:
            writer = csv.writer(ofile, delimiter=',')
            writer.writerow(columns)
            for timestamp in timestamps:
                row = [timestamp]
                foundAnyAtTimestamp = False
                for d in dicts:
                    try:
                        row += [d[timestamp]]
                        foundAnyAtTimestamp = True
                    except:
                        row += ['']
                if foundAnyAtTimestamp:
                    writer.writerow(row)
        ofile.close()

    RunPlot()

    #timestamps = []

    # Xl = []
    # Yl = []
    # Zl = []
    # wavelengths = [415, 445, 480, 515, 555, 590, 630, 680, 700, 720]
    # i = 0
    # for _ in wavelengths:
    #     Xl.append([])
    #     Yl.append([])
    #     Zl.append([])
    # i = 0
    # f = open("fullRunContinuousAcquisition.csv", "w")
    # f.write('Time(s), 415nm, 445nm, 480nm, 515nm, 555nm, 590nm, 630nm, 680nm, Clear, Nir, \n')
    # for wavelength in fluorescencePlot.parsedValues:
    #     # if i == 8:
    #     #     continue
    #     firstVal = None
    #     for value in wavelength.values:
    #         # if firstVal == None:
    #         #     Zl[i].append(1)
    #         #     firstVal = wavelength.values[value]
    #         # else:
    #         Zl[i].append(wavelength.values[value])# / firstVal)
    #         Xl[i].append(value)
    #         Yl[i].append(wavelengths[i])
    #     i+=1

    # X = np.array(Xl)
    # Y = np.array(Yl)
    # Z = np.array(Zl)

    # i = 0
    # for timeStamp in Xl[0]:
    #     f.write(str(timeStamp)+", ")
    #     for wavelength in Zl:
    #         f.write(str(wavelength[i])+", ")
    #     f.write("\n")
    #     i+=1

    # f.close()

    # fig = plt.figure()
    # ax = fig.gca(projection='3d')
    # # Plot the surface.
    # surf = ax.plot_surface(X, Y, Z, cmap=plt.cm.gnuplot,
    #                     linewidth=0)
    # plt.show()


def autoProcessData(checkboxTree):

    # values = ['MODEL_TUNING', 'MODELED_PLOT', 'TEC_THERMO_DATA']
    # dataType = OptionDialog(root, 'Data Selection', "What are you trying to process?", values)

    setActives(checkboxTree)
    # if filename.get() != "":
    #     parseLogFile()

    columns = ["timeSinceBootSeconds"]
    dicts = []

    for plot in plots:
        for parsedValue in plot.parsedValues:
            columns.append(parsedValue.name)
            dicts.append(parsedValue.values)
    # newFileName = filename.get()[0:-4] + "RAW" + ".csv"
    # with open(datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv", 'w', newline='') as ofile:

    directoryPath = askdirectory(
        title='Select Folder Containing Only Viable Log txt Files')  # shows dialog box and return the path
    if directoryPath == "":
        return

    # pop up progress bar init
    popup = tk.Toplevel()
    tk.Label(popup, text="Processing Files").grid(row=0, column=0)
    progress_var = tk.DoubleVar()
    progress_bar = Progressbar(popup, variable=progress_var, maximum=100)
    progress_bar.grid(row=1, column=0, padx = 10, pady = 5)  # .pack(fill=tk.X, expand=1, side=tk.BOTTOM)
    popup.pack_slaves()

    i = 0
    fileCount = len(os.listdir(directoryPath))
    file = ""
    for file in os.listdir(directoryPath):
        #dicts = []


        i += 1
        progress_var.set(i / fileCount * 100)

        # skip files that aren't .txt files
        if file[-3:len(file)] != "txt":
            continue

        fPath = os.path.join(directoryPath, file)

        # check if it is a file
        if os.path.isfile(fPath):
            timestamps = parseLogFile(fPath)
            file = file.split('.')[0]
            outfile = file + "RAW" + ".csv"

            if not os.path.exists("Output_Files"):
                os.makedirs("Output_Files")

            with open("Output_Files/" + outfile, 'w', newline='') as ofile:
                writer = csv.writer(ofile, delimiter=',')
                writer.writerow(columns)
                for timestamp in timestamps:
                    row = [timestamp]
                    foundAnyAtTimestamp = False
                    for d in dicts:
                        try:
                            row += [d[timestamp]]
                            foundAnyAtTimestamp = True
                        except:
                            row += ['']
                    if foundAnyAtTimestamp:
                        writer.writerow(row)
            ofile.close()
            daveOutputToPaddedData(os.path.join(os.path.curdir, "Output_Files", outfile))

    popup.destroy()

    sfile = file.split("_")
    sfile = sfile[0:-1]
    newFile = ""
    for seg in sfile:
       newFile += seg + "_"
    newFile = newFile[0:-1]

    global totalData
    totalData.to_csv("Output_Files/" + newFile + ".csv")
    totalData = pd.DataFrame()
    #messagebox.showinfo("AUTO DAVE","Files have been successfully daved")


def daveOutputToPaddedData(fullFilePath): #, dataType):

    df = pd.read_csv(fullFilePath)

    timestampKey = 'timeSinceBootSeconds'
    thermistorTempKey1 = 'stage1TempC'
    thermistorTempKey2 = 'pcrTempC'
    measuredTempKey1 = 'dataQStg1Slug'
    measuredTempKey2 = 'dataQPcrSlug'
    modeledTempC = 'pcrModeledTempC'
    peltierTop = 'dataQPcrPeltierTop'
    peltierBot = 'dataQPcrPeltierBottom'

    paddedData = df[
        [timestampKey, thermistorTempKey1, thermistorTempKey2, measuredTempKey1, measuredTempKey2, modeledTempC,
         peltierTop, peltierBot]]

    # if data in file is not the specified type then ignore
    try:
        paddedData = paddedData[
            paddedData[timestampKey] > paddedData[timestampKey][paddedData[thermistorTempKey1].first_valid_index()]]
        paddedData = paddedData[
            paddedData[timestampKey] < paddedData[timestampKey][paddedData[thermistorTempKey2].last_valid_index()]]
    except:
        try:
            paddedData = paddedData[
                paddedData[timestampKey] > paddedData[timestampKey][paddedData[thermistorTempKey2].first_valid_index()]]
            paddedData = paddedData[
                paddedData[timestampKey] < paddedData[timestampKey][paddedData[thermistorTempKey2].last_valid_index()]]
        except:
            return

    paddedData[timestampKey] = (paddedData[timestampKey] - paddedData[timestampKey].min())

    # trim before first pcrTempC and after last pcrTempC

    dict = {}
    dict[timestampKey] = []
    dict[thermistorTempKey1] = []
    dict[measuredTempKey1] = []
    dict[thermistorTempKey2] = []
    dict[measuredTempKey2] = []

    dict['padded'] = []

    for i in np.arange(paddedData[timestampKey].min(), paddedData[timestampKey].max(), 0.05):
        dict[timestampKey].append(i)
        dict[thermistorTempKey1].append(np.NaN)
        dict[measuredTempKey1].append(np.NaN)
        dict[thermistorTempKey2].append(np.NaN)
        dict[measuredTempKey2].append(np.NaN)

        dict['padded'].append(True)
    # print(i)
    paddedData = pd.concat([paddedData, pd.DataFrame.from_dict(dict)], ignore_index=True)
    paddedData.set_index(timestampKey, inplace=True)
    paddedData = paddedData.sort_index()
    paddedData[thermistorTempKey1].interpolate(method='linear', limit_direction='both', inplace=True)
    paddedData[thermistorTempKey2].interpolate(method='linear', limit_direction='both', inplace=True)
    paddedData[measuredTempKey1].interpolate(method='linear', limit_direction='both', inplace=True)
    paddedData[measuredTempKey2].interpolate(method='linear', limit_direction='both', inplace=True)
    paddedData[modeledTempC].interpolate(method='linear', limit_direction='both', inplace=True)
    paddedData[peltierTop].interpolate(method='linear', limit_direction='both', inplace=True)
    paddedData[peltierBot].interpolate(method='linear', limit_direction='both', inplace=True)

    paddedData = paddedData[paddedData["padded"].notna()]

    try:
        paddedData = paddedData[[thermistorTempKey1, measuredTempKey1, thermistorTempKey2, measuredTempKey2]]
    except:
        try:
            paddedData = paddedData[[thermistorTempKey1, measuredTempKey1]]
        except:
            paddedData = paddedData[[thermistorTempKey2, measuredTempKey2]]

    global dqPCR_selected
    global dqSTQ1_selected

    fullNameOfFile = os.path.basename(fullFilePath)
    nameOfFile = fullNameOfFile[0:-7] + ".csv"
    paddedData.to_csv(os.path.join("Output_Files", nameOfFile))  # create single files also

    strFile = nameOfFile[0:-7]
    fileArr = strFile.split("_")

    # one file with all selected checkbox data
    if dqPCR_selected.get() and dqSTQ1_selected.get():
        groupedData = paddedData[[measuredTempKey1, measuredTempKey2]].copy(deep=True)
        groupedData.rename(columns={measuredTempKey1: "stg1_" + fileArr[-1], measuredTempKey2: "pcr_" + fileArr[-1]}, inplace=True)
    elif dqSTQ1_selected.get():
        groupedData = paddedData[[measuredTempKey1]].copy(deep=True)
        groupedData.rename(columns={measuredTempKey1: fileArr[-1]}, inplace=True)
    else:
        groupedData = paddedData[[measuredTempKey2]].copy(deep=True)
        groupedData.rename(columns={measuredTempKey2: fileArr[-1]}, inplace=True)

    global totalData
    totalData = pd.concat([totalData, groupedData], axis=1)

    # delete temp raw data files
    for file in os.listdir("Output_Files"):
        if "RAW" in file:
            os.remove("Output_Files/" + file)


class Dave:
    def __init__(self):
        pass

    def run(self):

        # spacing for format
        spacer1 = tk.Label(text="", font=('Times New Roman', 5))
        spacer1.pack()

        selectFileButton = Button(text="Select Log File", command=pickFile, bg='#fcfcfc')
        selectFileButton.pack()

        filenameLabel = Label(textvariable=filename, bg='#fcfcfc')
        filenameLabel.pack()

        # checkboxTreeview
        tree = CheckboxTreeview(root)
        tree.pack()
        for plot in plots:
            item = tree.insert("", "end", plot.name, text=plot.name + " Plot")
            tree.change_state(item, 'checked')
            for parsedValue in plot.parsedValues:
                tree.insert(plot.name, "end", parsedValue.name, text=parsedValue.name)

        # progress = Progressbar(root, orient=HORIZONTAL,
        #                        length=100, mode='determinate')
        # progress.pack()

        # spacing for format
        spacer2 = tk.Label(text="", font=('Times New Roman', 1))
        spacer2.pack()

        # generate graph
        generateGraphButton = Button(text="Generate Graph", command=partial(graphData, tree), bg='#96ffb8')
        generateGraphButton.pack()

        # spacing for format
        spacer3 = tk.Label(text="", font=('Times New Roman', 1))
        spacer3.pack()

        frame1 = Frame(root, highlightbackground="#a1d6ff", highlightthickness=2)
        frame1.pack(padx=20, pady=20)

        # spacing for format
        spacer4 = tk.Label(text="", font=('Times New Roman', 1))
        spacer4.pack()

        global dqPCR_selected
        dqPCR_selected.set(1)
        c = Checkbutton(frame1, text="dataqPCR", variable=dqPCR_selected)
        c.pack()

        c1 = Checkbutton(frame1, text="dataqSTG1", variable=dqSTQ1_selected)
        c1.pack()

        # auto process entire directory
        autoDaveButton = Button(frame1,text="AUTO DAVE", command=partial(autoProcessData, tree), bg='#a1d6ff')
        autoDaveButton.pack()

        # spacing for format
        spacer5 = tk.Label(frame1, text="", font=('Times New Roman', 1))
        spacer5.pack()



        root.mainloop()
