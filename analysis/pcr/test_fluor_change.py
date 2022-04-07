

from datetime import datetime
import numpy as np

from lib.analysis_operation import AnalysisOperation


class TestFluorChange(AnalysisOperation):
    name = 'testFluorChange'

    def run(self, data):
        self.start = datetime.now()

        posChangeThreshold = self.config.testFluorChangePosThreshold
        negChangeThreshold = self.config.testFluorChangeNegThreshold
        posNoiseThreshold = self.config.testFluorChangePosNoiseRatioThreshold
        negNoiseThreshold = self.config.testFluorChangeNegNoiseRatioThreshold

        riseRatios = data['curveRiseRatio']
        curveToNoiseRatios = data['curveToNoiseRatio']

        scoresFluorChangePos = []
        for i in range(len(curveToNoiseRatios)):
            if (
                riseRatios[i] >= posChangeThreshold
                and curveToNoiseRatios[i] >= posNoiseThreshold
            ):
                scoresFluorChangePos.append(1)
            else:
                scoresFluorChangePos.append(float('nan'))

        scoresFluorChangeNeg = []
        for i in range(len(curveToNoiseRatios)):
            if (
                riseRatios[i] < negChangeThreshold
                or curveToNoiseRatios[i] < negNoiseThreshold
            ):
                scoresFluorChangeNeg.append(-1)
            else:
                scoresFluorChangeNeg.append(float('nan'))

        self.stop = datetime.now()

        return {
            'scoresFluorChangePos': scoresFluorChangePos,
            'scoresFluorChangeNeg': scoresFluorChangeNeg,
        }
