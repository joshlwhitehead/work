import math
import random
from collections import namedtuple

# from .operation_channel_normalization import ChannelNormalization
from .operation_smooth_melt import Smooth
from .operation_sort_by_temperature import SortByTemperature
from .operation_exponential_fit import ExponentialFit
from .operation_inverse_derivative import InverseDerivative

# from .test_fluor_change import TestFluorChange

def merge(incoming, existing):
    mr = existing.copy()
    for i, v in enumerate(incoming):
        current = existing[i]
        if current == None or math.isnan(current) or current == 0:
            mr[i] = v
    return mr

class MeltAnalysis:
    results = {}
    operations = []

    def __init__(self, configuration):
        self.config = namedtuple(
            'Config', configuration.keys())(**configuration)

        self.buildOperations()

    def callMelt(self, temperatures, data):
        self.results = {}
        self.results['rawData'] = data.copy()
        self.results['current'] = data.copy()
        # print(self.results['rawData'])
        self.results['temperatures'] = []
        for t in temperatures:
            self.results['temperatures'].append(t + random.random() / 10000)
        

        for operation in self.operations:
            res = operation.run(self.results)
            self.results.update(res)

            # print(operation.name, operation.stop - operation.start)

        self.mergeCalls()

    def mergeCalls(self):
        pass
        # pcrCalls = [0] * len(self.results['scoresFluorChangePos'])
        
        # pcrCalls = merge(self.results['scoresFluorChangePos'], pcrCalls)
        # pcrCalls = merge(self.results['scoresFluorChangeNeg'], pcrCalls)

        # self.results['pcrCalls'] = pcrCalls


    def buildOperations(self):
        self.operations = []
        self.operations.append(SortByTemperature(self.config))
        self.operations.append(Smooth(self.config))
        self.operations.append(ExponentialFit(self.config))
        self.operations.append(InverseDerivative(self.config))
        # self.operations.append(Noise(self.config))
        # self.operations.append(MeanShiftNormalization(self.config))
        # self.operations.append(Tilt(self.config))
        # self.operations.append(CurveDepth(self.config))
        # self.operations.append(IntracycleCp(self.config))

        # # Tests
        # self.operations.append(TestFluorChange(self.config))
