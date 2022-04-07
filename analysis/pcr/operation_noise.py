

from datetime import datetime
import numpy as np

from lib.analysis_operation import AnalysisOperation

def noZero(v):
    if v == 0:
        return 1
    return v

class Noise(AnalysisOperation):
    name = 'noise'

    def run(self, data):
        self.start = datetime.now()

        rawFluor = data['backgroundSubtracted']
        smoothFluor = data['smoothed']

        diff = [np.subtract(f, smoothFluor[i]) for i, f in enumerate(rawFluor)]
        adjusted = [np.divide(f, list(map(noZero, smoothFluor[i]))) for i, f in enumerate(diff)]
        ave = [np.average(np.abs(f)) for f in adjusted]

        noiseMagnitude = np.absolute([ave[i] * np.median(f) for i, f in enumerate(smoothFluor)])

        self.stop = datetime.now()

        return {
            'noise': ave,
            'noiseMagnitude': noiseMagnitude,
        }
