import math
from collections import namedtuple

from .operation_background_subtraction import BackgroundSubtraction
from .operation_deconvolution import Deconvolution
from .operation_channel_normalization import ChannelNormalization
from .operation_smooth import Smooth
from .operation_mean_shift_normalization import MeanShiftNormalization
from .operation_detrend import Detrend
from .operation_noise import Noise
from .operation_curve_depth import CurveDepth
from .operation_cp_intracycle import IntracycleCp

from .test_fluor_change import TestFluorChange

def merge(incoming, existing):
    mr = existing.copy()
    for i, v in enumerate(incoming):
        current = existing[i]
        if current == None or math.isnan(current) or current == 0:
            mr[i] = v
    return mr

class PCRAnalysis:
    results = {}
    operations = []

    def __init__(self, configuration):
        self.config = namedtuple(
            'Config', configuration.keys())(**configuration)

        self.buildOperations()

    def callPCR(self, data):
        self.results = {}
        self.results['rawData'] = data.copy()
        self.results['current'] = data.copy()

        for operation in self.operations:
            res = operation.run(self.results)
            self.results.update(res)

            # print(operation.name, operation.stop - operation.start)

        self.mergeCalls()

    def mergeCalls(self):
        pcrCalls = [0] * len(self.results['scoresFluorChangePos'])
        
        pcrCalls = merge(self.results['scoresFluorChangePos'], pcrCalls)
        pcrCalls = merge(self.results['scoresFluorChangeNeg'], pcrCalls)

        self.results['pcrCalls'] = pcrCalls


    def buildOperations(self):
        self.operations = []
        # self.operations.append(ChannelNormalization(self.config))
        self.operations.append(BackgroundSubtraction(self.config))
        self.operations.append(Smooth(self.config))
        # self.operations.append(Deconvolution(self.config))
        self.operations.append(Noise(self.config))
        self.operations.append(MeanShiftNormalization(self.config))
        self.operations.append(Detrend(self.config))
        self.operations.append(CurveDepth(self.config))
        self.operations.append(IntracycleCp(self.config))

        # Tests
        self.operations.append(TestFluorChange(self.config))
