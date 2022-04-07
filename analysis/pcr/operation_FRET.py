from datetime import datetime
import numpy as np
from scipy.interpolate import make_interp_spline
from scipy.interpolate import interp1d

from lib.analysis_operation import AnalysisOperation


class Fret(AnalysisOperation):
    name = 'Fret'

    def run(self, data):
        self.start = datetime.now()

        raw = data['rawData']
        delta = []
        for i in raw:
            avgDiff = np.average(i[-5:])-np.average(i[:5])
            delta.append(avgDiff)
        
        
        channels = np.array([415,445,480,515,555,590,630,680])
        delta = np.array(delta[:8])
        X_Y_Spline = make_interp_spline(channels,delta)

        X_ = np.linspace(channels.min(), channels.max(), 500)
        Y_ = X_Y_Spline(X_)

        self.stop = datetime.now()

        return {
            'channels_smooth':X_,
            'fret_smooth':Y_,
            'fret':delta,
            'channels':channels
            }







