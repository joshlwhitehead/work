from datetime import datetime
import numpy as np

from lib.analysis_operation import AnalysisOperation
from lib.helpers import *


class MeanShiftNormalization(AnalysisOperation):
    name = 'meanShiftNormalization'

    def run(self, data):
        self.start = datetime.now()
        fluor = data['current']

        i = self.config.normalizationShiftMeanIndices[0]
        j = self.config.normalizationShiftMeanIndices[1]

        meanShiftNormalized = [np.subtract(c, np.mean(c[i:j])) for c in fluor]

        self.stop = datetime.now()

        return {
            'current': meanShiftNormalized,
            'meanShiftNormalized': meanShiftNormalized,
        }
