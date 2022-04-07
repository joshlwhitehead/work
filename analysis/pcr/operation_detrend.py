

from datetime import datetime
import numpy as np

from lib.analysis_operation import AnalysisOperation


class Detrend(AnalysisOperation):
    name = 'detrended'

    def run(self, data):
        self.start = datetime.now()

        fluor = data['current']
        cycles = np.arange(len(fluor[0]))
        fits = np.polyfit(cycles, np.asarray(fluor).T, 1)

        detrended = [
            np.subtract(f, np.polyval([fits[0][i], fits[1][i]], cycles))
            for i, f in enumerate(fluor)
        ]

        self.stop = datetime.now()

        return {
            'current': detrended,
            'tilted': detrended,
            'detrended': detrended,
        }
