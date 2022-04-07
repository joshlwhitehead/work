

from datetime import datetime
import numpy as np

from lib.analysis_operation import AnalysisOperation


def rootIndices(f):
    border = 3
    roots = []
    for i in range(len(f)):
        if (
            i >= border
            and i < len(f) - border
            and f[i - 3] < 0
            and f[i - 2] < 0
            and f[i - 1] < 0
            and f[i] >= 0
            and f[i + 1] > 0
            and f[i + 2] > 0
        ):
            roots.append(i)
    return roots


class CurveDepth(AnalysisOperation):
    name = 'testFluorChange'

    def run(self, data):
        self.start = datetime.now()

        fluor = data['current'] # This is tilted
        smoothFluor = data['smoothed']
        noiseMagnitude = data['noiseMagnitude']

        depthToActualFactor = self.config.testFluorChangeCurveMeasureToRise

        firstDerivative = [np.gradient(f) for f in fluor]
        positiveRoots = [rootIndices(f) for f in firstDerivative]

        maxRoots = []
        rootMeasure = []
        rootDepthRatio = []
        for i, pr in enumerate(positiveRoots):
            if len(pr) == 1:
                maxRoots.append(pr[0])
                rootMeasure.append(fluor[i][pr[0]])
                rootDepthRatio.append(fluor[i][pr[0]]/smoothFluor[i][pr[0]])
            elif len(pr) == 0:
                maxRoots.append(float('nan'))
                rootMeasure.append(float('nan'))
                rootDepthRatio.append(float('nan'))
            else:
                mi = None
                m = 1e6
                for r in pr:
                    v = fluor[i][r]
                    if v < m:
                        m = v
                        mi = r
                maxRoots.append(mi)
                rootMeasure.append(fluor[i][mi])
                rootDepthRatio.append(fluor[i][mi]/smoothFluor[i][mi])

        rootMeasure = np.absolute(rootMeasure)
        # Estimation of how much the curve came up from baseline
        riseRatios = np.multiply(np.absolute(
            rootDepthRatio), depthToActualFactor)

        curveToNoiseRatios = np.divide(rootMeasure, noiseMagnitude)

        self.stop = datetime.now()

        return {
            'firstDerivative': firstDerivative,
            'cps': maxRoots,
            'curveDepth': rootMeasure,
            'curveRiseRatio': riseRatios,
            'curveToNoiseRatio': curveToNoiseRatios,
        }
