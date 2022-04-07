from datetime import datetime
import numpy as np
import scipy as scipy


from .analysis_operation import AnalysisOperation

def monoExp(x, m, t, b):
    return m * np.exp( -t * x ) + b

class InverseDerivative(AnalysisOperation):
    name = 'inverseDerivative'

    def run(self, data):
        self.start = datetime.now()

        t = data['smoothedT']
        fluor = data['expDiff']
        smoothFluor = data['smoothed']

        derivatives = [np.multiply(np.gradient(f), -1) for f in fluor]

        smoothDerivatives = [np.multiply(np.gradient(f), -1) for f in smoothFluor]

        self.stop = datetime.now()

        return {
            'derivatives': derivatives,
            'smoothDerivatives': smoothDerivatives,
        }
