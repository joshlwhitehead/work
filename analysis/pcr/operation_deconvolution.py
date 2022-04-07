from datetime import datetime
import numpy as np
import scipy as scipy

from lib.analysis_operation import AnalysisOperation


class Deconvolution(AnalysisOperation):
    name = 'deconvolution'

    def run(self, data):
        self.start = datetime.now()

        dye0 = self.config.dyeProfile0
        channelsOfInterest = [0,1,2,3,6,7,8,9]

        fluor = np.array(data['current'])

        def dye0Fitter(dyeProfile, m, b):
            return np.multiply(np.add(np.multiply(dyeProfile, m), b), dyeProfile)
        
        dye0Signal = []
        dye1Signal = []
        dye0Deconvoluted = []
        dye1Deconvoluted = []

        for i in range(len(fluor[0])):
            # get this cycle
            cycle = fluor[:, i][channelsOfInterest]

            fitToCurve = np.multiply(cycle, dye0)
            params, cv = scipy.optimize.curve_fit(dye0Fitter, dye0, fitToCurve, (1, 1), bounds=([0, -65000], [65000, 65000]))
            m, b = params

            signal = np.add(np.multiply(dye0, m), b)
            dye0Signal.append(signal)
            dye0Sum = np.sum(signal)
            dye0Deconvoluted.append(dye0Sum)
            
            signal1 = np.subtract(cycle, signal)
            dye1Signal.append(signal1)
            dye1Deconvoluted.append(np.sum(signal1))








        # # want 10 and 0 out.
        # params, cv = scipy.optimize.curve_fit(dye0Fitter, dye0, np.multiply(backgroundSubtracted, dye1), (20, 10), bounds=([0, -65000], [65000, 65000]))
        # # params, cv = scipy.optimize.curve_fit(dye1MultipleExp, cycles, backgroundSubtracted, (20, 10))
        # m, b = params
        # print('want 10 and 0', m, b)

        # dye1Signal = np.add(np.multiply(dye0Profile, m), b)
        # dye2Signal = np.subtract(backgroundSubtracted, dye1Signal)


        

        self.stop = datetime.now()

        return {
            # 'current': channelNormalized,
            'dye0Signal': dye0Signal,
            'dye0Deconvoluted': dye0Deconvoluted,
            'dye1Signal': dye1Signal,
            'dye1Deconvoluted': dye1Deconvoluted,
        }
