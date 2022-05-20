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
        # return float(line.split("thermalControlTask: ")[1].split("timeout = ")[1].split(",")[0])
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

def stage1TargetRate(line):
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

def pcrTargetRate(line):
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
        # return float(line.split("thermalControlTask: ")[1].split("error = ")[1].split(",")[0])
    except:
        return None

def pcrErrorTimeMs(line):
    try:
        return float(line.split("thermalControl-1 = ")[1].split("timeout = ")[1].split(",")[0])
        # return float(line.split("thermalControlTask: ")[1].split("timeout = ")[1].split(",")[0])
    except:
        return None

# ('DATAQ', '29.37', '29.59')
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

# DATAQ:  | liquid = 26.41 | liquid2 = 24.57 | laser = 29.8 | pcrhtsnk = 31.61 | stg1htsnk = 23.3 |
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
        # return float(line.split("DATAQ:")[1].split("| C1T = ")[1].split("|")[0])
        return float(line.split("DATAQ:")[1].split("| dataQStage1PeltierTop = ")[1].split("|")[0])
    except:
        return None

def dataQC1B(line):
    try:
        # return float(line.split("DATAQ:")[1].split("| C1B = ")[1].split("|")[0])
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

# I (891063) _performCapture: [881472,17,77.74,306,18000,2854,261,334,310,493,550,10814,211]

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

# "ExperimentStatePcr", "time: %d, state: %d", timerMs, _state);
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


