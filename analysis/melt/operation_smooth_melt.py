from datetime import datetime
import numpy as np
from math import ceil, floor
from csaps import csaps

from .analysis_operation import AnalysisOperation


class Smooth(AnalysisOperation):
    name = 'smooth'

    def run(self, data):
        self.start = datetime.now()

        t = data['sortedT']
        fluor = data['current']
        
        smoothing = 0.15
        dataPoints = 300
        minT = ceil(t[0])
        maxT = floor(t[-1])
        smoothedT = np.linspace(minT, maxT, dataPoints)

        smoothed = []
        for f in fluor:
            ys = csaps(t, f, smoothedT, smooth=smoothing)
            smoothed.append(ys)

        self.stop = datetime.now()

        return {
            'current': smoothed,
            'smoothed': smoothed,
            'smoothedT': smoothedT,
        }
