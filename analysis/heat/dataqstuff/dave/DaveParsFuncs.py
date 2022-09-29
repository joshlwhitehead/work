def stage1TempCFunc(line):
    try:
        return float(line.split("TC-0 = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-0 = ")[1].split(",")[0])
        except:
            return None


def stage1ModeledTempCFunc(line):
    try:
        return float(line.split("TC-0 = ")[1].split("modeled = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-0 = ")[1].split("modeled = ")[1].split(",")[0])
        except:
            return None


def stage1ExpectedTempCFunc(line):
    try:
        return float(line.split("TC-0 = ")[1].split("exptTempC = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-0 = ")[1].split("exptTempC = ")[1].split(",")[0])
        except:
            return None


def stage1TargetTempCFunc(line):
    try:
        return float(line.split("TC-0 = ")[1].split("target = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-0 = ")[1].split("target = ")[1].split(",")[0])
        except:
            return None


def stage1ControlledRampTargetFunc(line):
    try:
        return float(line.split("TC-0 = ")[1].split("controlledRampTarget = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-0 = ")[1].split("controlledRampTarget = ")[1].split(",")[0])
        except:
            return None


def stage1ActualTecRampRateFunc(line):
    try:
        return float(line.split("TC-0 = ")[1].split("actualTecRampRate = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-0 = ")[1].split("actualTecRampRate = ")[1].split(",")[0])
        except:
            return None


def stage1ErrorTimeMs(line):
    try:
        return float(line.split("TC-0 = ")[1].split("timeout = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-0 = ")[1].split("timeout = ")[1].split(",")[0])
        except:
            return None


def stage1OutputFunc(line):
    try:
        return float(line.split("TC-0 = ")[1].split("output = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-0 = ")[1].split("output = ")[1].split(",")[0])
        except:
            return None


def stage1TargetRate(line):
    try:
        return float(line.split("TC-0 = ")[1].split("targetTecRampRate = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-0 = ")[1].split("targetTecRampRate = ")[1].split(",")[0])
        except:
            return None


def stage1TecRate(line):
    try:
        return float(line.split("TC-0 = ")[1].split("actualTecRampRate = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-0 = ")[1].split("actualTecRampRate = ")[1].split(",")[0])
        except:
            return None


def stage1HeatsinkRate(line):
    try:
        return float(line.split("TC-0 = ")[1].split("HSrate = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-0 = ")[1].split("HSrate = ")[1].split(",")[0])
        except:
            return None


def stage1HeatSinkTempFunc(line):
    try:
        return float(line.split("TC-0 = ")[1].split("heatSink = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-0 = ")[1].split("heatSink = ")[1].split(",")[0])
        except:
            return None



def pcrTempCFunc(line):
    try:
        return float(line.split("TC-1 = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-1 = ")[1].split(",")[0])
        except:
            return None


def pcrModeledTempCFunc(line):
    try:
        return float(line.split("TC-1 = ")[1].split("modeled = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-1 = ")[1].split("modeled = ")[1].split(",")[0])
        except:
            return None


def pcrExpectedTempCFunc(line):
    try:
        return float(line.split("TC-1 = ")[1].split("expectedTempC = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-1 = ")[1].split("expectedTempC = ")[1].split(",")[0])
        except:
            return None


def pcrTargetTempCFunc(line):
    try:
        return float(line.split("TC-1 = ")[1].split("target = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-1 = ")[1].split("target = ")[1].split(",")[0])
        except:
            return None


def pcrControlledRampTargetFunc(line):
    try:
        return float(line.split("TC-1 = ")[1].split("controlledRampTarget = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-1 = ")[1].split("controlledRampTarget = ")[1].split(",")[0])
        except:
            return None


def pcrHeatSinkTempFunc(line):
    try:
        return float(line.split("TC-1 = ")[1].split("heatSink = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-1 = ")[1].split("heatSink = ")[1].split(",")[0])
        except:
            return None


def pcrActualTecRampRateFunc(line):
    try:
        return float(line.split("TC-1 = ")[1].split("actualTecRampRate = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-1 = ")[1].split("actualTecRampRate = ")[1].split(",")[0])
        except:
            return None


def pcrTargetRate(line):
    try:
        return float(line.split("TC-1 = ")[1].split("TecRate = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-1 = ")[1].split("TecRate = ")[1].split(",")[0])
        except:
            return None


def pcrTecRate(line):
    try:
        return float(line.split("TC-1 = ")[1].split("actualTecRampRate = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-1 = ")[1].split("actualTecRampRate = ")[1].split(",")[0])
        except:
            return None


def pcrHeatsinkRate(line):
    try:
        return float(line.split("TC-1 = ")[1].split("HSrate = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-1 = ")[1].split("HSrate = ")[1].split(",")[0])
        except:
            return None


def pcrOutputFunc(line):
    try:
        return float(line.split("TC-1 = ")[1].split("output = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-1 = ")[1].split("output = ")[1].split(",")[0])
        except:
            return None


def pcrErrorC(line):
    try:
        return float(line.split("TC-1 = ")[1].split("error = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-1 = ")[1].split("error = ")[1].split(",")[0])
        except:
            return None


def pcrErrorTimeMs(line):
    try:
        return float(line.split("TC-1 = ")[1].split("timeout = ")[1].split(",")[0])
    except:
        try:
            return float(line.split("thermalControl-1 = ")[1].split("timeout = ")[1].split(",")[0])
        except:
            return None


# DATAQ:  | liquid = 26.41 | liquid2 = 24.57 | laser = 29.8 | pcrhtsnk = 31.61 | stg1htsnk = 23.3 |
def dataQLiquid(line):
    try:
        return float(line.split("DATAQ:")[1].split("| LiquidStg1 = ")[1].split("|")[0])
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
        return float(line.split("DATAQ:")[1].split("| Stage1PeltierTop = ")[1].split("|")[0])
    except:
        return None


def dataQC1B(line):
    try:
        # return float(line.split("DATAQ:")[1].split("| C1B = ")[1].split("|")[0])
        return float(line.split("DATAQ:")[1].split("| Stage1PeltierBottom = ")[1].split("|")[0])

    except:
        return None


def dataQPCRT(line):
    try:
        return float(line.split("DATAQ:")[1].split("| PcrPeltierTop = ")[1].split("|")[0].replace("*", ""))
    except:
        return None


def dataQPCRB(line):
    try:
        return float(line.split("DATAQ:")[1].split("| PcrPeltierBottom = ")[1].split("|")[0])
    except:
        return None


def dataQPcrHeatsink(line):
    try:
        return float(line.split("DATAQ:")[1].split("| PcrHeatsink = ")[1].split("|")[0])
    except:
        return None


def rawTECModel(line):
    try:
        return float(line.split("TEC-1")[1].split("ModeledTempC: ")[1])
    except:
        return None


def dataQStage1Heatsink(line):
    try:
        return float(line.split("CHUBE:")[1].split("| Stage1Heatsink = ")[1].split("|")[0])
    except:
        try:
            return float(line.split("DATAQ:")[1].split("| Stage1Heatsink = ")[1].split("|")[0])
        except:
            return None


def measuredPcrTempC(line):
    try:
        return float(line.split("CHUBE:")[1].split("| PcrThermoTempC = ")[1].split("|")[0])
    except:
        try:
            return float(line.split("DATAQ:")[1].split("| PcrThermoTempC = ")[1].split("|")[0])
        except:
            try:
                return float(line.split("DATAQ:")[1].split("| dataQPcrSlug = ")[1].split("|")[0])
            except:
                return None


def measuredStg1TempC(line):
    try:
        return float(line.split("CHUBE:")[1].split("| Stg1ThermoTempC = ")[1].split("|")[0])
    except:
        try:
            return float(line.split("DATAQ:")[1].split("| dataQLiquidStg1 = ")[1].split("|")[0])
        except:
            try:
                return float(line.split("DATAQ:")[1].split("| dataQStg1Slug = ")[1].split("|")[0])
            except:
                try:
                    return float(line.split("DATAQ:")[1].split("| Stg1ThermoTempC = ")[1].split("|")[0])
                    # return 2
                except:
                    return None
def measuredStg1TempC2(line):
    return float(line.split("DATAQ:")[1].split("| stg1AltThermoTempC2 = ")[1].split("|")[0])
def measuredStg1TempC3(line):
    return float(line.split("DATAQ:")[1].split("| stg1AltThermoTempC3 = ")[1].split("|")[0])



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
