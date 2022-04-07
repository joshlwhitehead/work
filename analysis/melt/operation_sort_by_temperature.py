from datetime import datetime
import numpy as np

from .analysis_operation import AnalysisOperation

class SortByTemperature(AnalysisOperation):
    name = 'sortByTemperature'

    def run(self, data):
        self.start = datetime.now()

        t = data['temperatures']
        fluor = data['current'].copy()

        fluor.insert(0, t)
        # print(fluor)
        sortIndex = 0
        a = np.array(fluor)
        # print(len(fluor[-1]),len(t))
        sorted = a[:,a[sortIndex,:].argsort()]

        sortedT = sorted[0]
        sortedD = sorted[1:]

        self.stop = datetime.now()

        return {
            'current': sortedD,
            'sortedT': sortedT,
            'sortedRawData': sortedD,
        }
