import numpy as np
import math

def findLeastSquaresCq(pcrData:np.ndarray):
    if len(set(pcrData[1])) == 1:
        return float('nan'), np.array([pcrData[0], [0]*len(pcrData[0])]).T, np.array([pcrData[0], [0]*len(pcrData[0])]).T # Cq*

    pcrData = np.array(pcrData)
    # pcrData = chopFirstTenCycles(pcrData) # protect against artifacts
    fits = findNPointFits(pcrData, n=7)
    firstDeriv = getFirstDeriv(fits)
    secondDeriv = findSecondDeriv(firstDeriv)
    extremes = findFunctionMinAndMax(secondDeriv)
    maxSecondDeriv = extremes[1]
    cq = maxSecondDeriv[0]
    cq = verifyIncreasing(cq, pcrData)

    if not math.isnan(cq) and cq <= 5:
        cq = float('nan')

    return cq, firstDeriv, secondDeriv





def chopFirstTenCycles(pcrData):
    cycles = pcrData[0]
    fluor = pcrData[1]
    return np.array([cycles[10:], fluor[10:]])

def findNPointFits(pcrData:np.ndarray, n:int=7):
    '''
    Finds least squares linear fit lines for seven consecutive points throughout the pcr curve.
    
    For each fit, returns the slope, intercept, standard deviation, and midpoint.
    '''
    if n < 3:
        raise ValueError('n must be greater than or equal to 3')
    pcrData = np.array(pcrData)
    halfN = n//2
    firstFits = []
    for i in range(halfN, len(pcrData[0]) - halfN):
        dataWindow = pcrData[0:2, i-halfN:i+halfN+1]
        x = dataWindow[0]
        y = dataWindow[1]
        coeff = np.polynomial.polynomial.polyfit(x, y, 1)
        slope = coeff[1]
        intercept = coeff[0]
        stdDev = getStandardDeviation(slope, intercept, dataWindow)
        firstFits.append([slope, intercept, stdDev, [x[halfN], y[halfN]]])
    return firstFits

def findAdaptivePointsFits(pcrData:np.ndarray):
    """
    Finds least square linear fit lines for seven consecutive points throughout the pcr curve
    Unless seven is too many, in which case it will do five, or three, whichever is largest. 
    The key difference here is that findNPointsFits by default does 7, and if you want to find 
    the 7 point fit of index 2 you cannot. This method will choose 7, or choose smaller n's when 
    needed.
    """
    pcrData = np.array(pcrData)
    firstFits = []
    for i in range(1, len(pcrData[0]) - 1):
        if i == 1 or i == len(pcrData[0]) - 2:
            n = 3
        elif i == 2 or i == len(pcrData[0]) - 3:
            n = 5
        else:
            n = 7
        halfN = n//2
        dataWindow = pcrData[0:2, i-halfN:i+halfN+1]
        x = dataWindow[0]
        y = dataWindow[1]
        coeff = np.polynomial.polynomial.polyfit(x, y, 1)
        slope = coeff[1]
        intercept = coeff[0]
        stdDev = getStandardDeviation(slope, intercept, dataWindow)
        firstFits.append([slope, intercept, stdDev, [x[halfN], y[halfN]]])
    return firstFits

def getStandardDeviation(slope:float, intercept:float, dataWindow:np.ndarray):
    ''' gets the standard devation of points (in the y-direction) from the line of best fit '''
    residualSum = 0
    N = 0
    for i, cycle in enumerate(dataWindow[0]):
        expectedPoint = slope * cycle + intercept
        actualPoint = dataWindow[1,i]
        difference = actualPoint - expectedPoint
        residualSum += (difference*difference) # root mean squared
        N += 1
    variance = residualSum / N
    stdDev = math.sqrt(variance)
    return stdDev   

def findAbsoluteMinimumFit(fits:list):
    ''' Finds the linear fit with the absolute minimum slope '''
    minimum = [float('inf'), float('inf'), float('inf'), [float('inf'), float('inf')]]
    for fit in fits:
        if fit[0] < minimum[0]:
            minimum = list.copy(fit)
    return minimum

def findLastCycle(pcrData:np.ndarray):
    ''' finds the cycle and fluorescence of the last cycle of pcr data '''
    pcrData = np.array(pcrData)
    lastCycle = pcrData[0, -1]
    lastFluor = pcrData[1, -1]
    return np.array([lastCycle, lastFluor])

def findFunctionMinAndMax(data:np.ndarray):
    ''' Finds the minimum and maximum dependent variable value in the data and returns first the minimum point and then the maximum point '''
    data = np.array(data)
    x = np.array(data).T[0]
    y = np.array(data).T[1]

    minDep = min(y)
    maxDep = max(y)

    minIndep = -1
    maxIndep = -1
    for i, val in enumerate(y):
        if val == minDep:
            minIndep = x[i]
        if val == maxDep:
            maxIndep = x[i]

    minDepVarPoint = [minIndep, minDep]
    maxDepVarPoint = [maxIndep, maxDep]
    return [minDepVarPoint, maxDepVarPoint]

def verifyIncreasing(cq:float, pcrData:np.ndarray):
    ''' Verifies that the cq is increasing throughout the pcr curve '''
    cqInd = np.where(pcrData[0] == cq)[0][0]
    prev = pcrData[1, cqInd-1]
    cqFluor = pcrData[1][cqInd]
    next = pcrData[1, cqInd+1]

    if prev > cqFluor and next < cqFluor:
        return float('nan')
    return cq

def getFirstDeriv(sevenPointFitInfo:list):
    ''' takes seven point fit info (as calculated in findSevenPointFits) and reformats into first derivative points '''
    firstDeriv = []

    for fit in sevenPointFitInfo:
        fluorPoint = fit[3]
        cycle = fluorPoint[0]
        slope = fit[0]
        intercept = fit[1]

        derivValue = slope
        derivPoint = [cycle, derivValue]
        firstDeriv.append(derivPoint)

    return np.array(firstDeriv)

def findSecondDeriv(firstDeriv:np.ndarray):
    ''' Use linear least squares of three points to find the second derivative of the data '''
    firstDeriv = np.array(firstDeriv)
    secondDeriv = []

    for i in range(1, len(firstDeriv) - 1):
        dataWindow = firstDeriv[i-1:i+2, 0:2]
        x = np.array(dataWindow).T[0]
        y = np.array(dataWindow).T[1]
        coeff = np.polynomial.polynomial.polyfit(x, y, 1)

        slope = coeff[1]
        cycle = x[1]

        derivValue = slope
        secondDeriv.append([cycle, derivValue])

    return np.array(secondDeriv)


