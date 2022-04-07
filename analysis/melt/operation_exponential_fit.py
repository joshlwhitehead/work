from datetime import datetime
import numpy as np
import scipy as scipy
from math import ceil, floor

from .analysis_operation import AnalysisOperation

def monoExp(x, m, t, b):
    return m * np.exp( -t * x ) + b

class ExponentialFit(AnalysisOperation):
    name = 'exponentialFit'

    def run(self, data):
        self.start = datetime.now()

        t = data['smoothedT']
        fluor = data['smoothed']

        cutoffDegree = 70.0
        cutoffIndex = next(x for x, val in enumerate(t) if val > cutoffDegree)
        
        cutT = t[:cutoffIndex]

        exp1 = []
        expDiff = []
        for f in fluor:
            # perform the fit
            cutF = f[:cutoffIndex]
            m0 = 100
            b0 = f[-1]
            tau0 = 0.01
            p0 = (m0, tau0, b0) # start with values near those we expect
            try:
                params, cv = scipy.optimize.curve_fit(monoExp, cutT, cutF, p0, bounds=(0, [5000, 1, 65000]))
                m, tau, b = params
            
                exponentialLine = monoExp(t, m, tau, b)
                exp1.append(exponentialLine)

                expDiff.append(np.subtract(f, exponentialLine))
            except:
                exp1.append(None)
                expDiff.append(None)

            # determine quality of the fit
            # squaredDiffs = np.square(ys - monoExp(xs, m, t, b))
            # squaredDiffsFromMean = np.square(ys - np.mean(ys))
            # rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)
            # print(f"R² = {rSquared}")


        self.stop = datetime.now()

        return {
            'leadExp': exp1,
            'expDiff': expDiff,
        }
