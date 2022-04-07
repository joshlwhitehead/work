from datetime import datetime
import numpy as np
from tsmoothie.smoother import *

from lib.analysis_operation import AnalysisOperation


class Smooth(AnalysisOperation):
    name = 'smooth'

    def run(self, data):
        self.start = datetime.now()

        fluor = data['current']

        knots = self.config.smoothingKnots

        smoother = SplineSmoother(
            n_knots=knots, spline_type='natural_cubic_spline')
        smoother.smooth(fluor)
        low, up = smoother.get_intervals('prediction_interval')

        # diff = np.subtract(up, low)
        # adjusted = [np.divide(f, smoother.smooth_data[i]) for i, f in enumerate(diff)]
        # ave = [np.average(np.abs(f)) for f in adjusted]

        self.stop = datetime.now()

        return {
            'current': smoother.smooth_data,
            'smoothed': smoother.smooth_data,
            'smoothedLowerBounds': low,
            'smoothedUpperBounds': up,
        }
