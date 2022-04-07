from datetime import datetime
import numpy as np

from .analysis_operation import AnalysisOperation

class RemoveDuplicates(AnalysisOperation):
    name = 'removeDuplicates'

    def run(self, data):
        self.start = datetime.now()

        t = data['smoothT']
        fluor = data['smoothed'].copy()

        fluor.insert(0, t)
    
        sortIndex = 0
        a = np.array(fluor)
        sorted = a[:,a[sortIndex,:].argsort()]

        sortedT = sorted[0]
        sortedD = sorted[1:]

        self.stop = datetime.now()

        return {
            'current': sortedD,
            'sortedT': sortedT,
            'sortedRawData': sortedD,
        }
