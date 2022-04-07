from datetime import datetime
import numpy as np

from lib.analysis_operation import AnalysisOperation

class ChannelNormalization(AnalysisOperation):
    name = 'channelNormalization'

    def run(self, data):
        self.start = datetime.now()

        normalizingChannels = self.config.normalizingChannels
        fluor = data['current']

        def ave(channel):
            c = fluor[channel]
            initial = c[0]
            return [((v - initial) / initial) for v in c]

        averageChanges = [ave(channel) for channel in normalizingChannels]

        averageNormVector = np.multiply(
            np.mean(averageChanges, axis=0), self.config.channelNormalizationImpactFactor)

        def norm(rf):
            initial = rf[0]
            normVector = np.multiply(averageNormVector, initial)
            return np.subtract(rf, normVector)

        channelNormalized = [norm(r) for r in fluor]

        self.stop = datetime.now()

        return {
            'current': channelNormalized,
            'channelNormalized': channelNormalized,
        }
