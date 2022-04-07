from .helpers import *

def getConfigMap(name):
    if name == 'lambda':
        return {
            'name': 'lambda',
            'backgroundCycles': [3,4,5],
            'dyeProfile0': [0.00195, 0.0632, 0.849, 0.332, 0.0716, 0.0218, 0.00493, 0.000901], # MavBlue
            'normalizingChannels': [nm415, nm445],
            'channelNormalizationImpactFactor': 0.75,
            'normalizationShiftMeanIndices': [3, 9],
            'smoothingKnots': 8,
            # Depth of the curve correlates to actual points risen x constant
            'testFluorChangeCurveMeasureToRise': 3.0,
            # Percent that the signal must rise above baseline
            'testFluorChangePosThreshold': 0.07,
            'testFluorChangeNegThreshold': 0.03,
            # Max noise to signal
            'testFluorChangePosNoiseRatioThreshold': 1.0,
            'testFluorChangeNegNoiseRatioThreshold': 0.5,
        }

    # default
    return {
        'name': 'default',
        'backgroundCycles': [3,4,5],
        'dyeProfile0': [0.00195, 0.0632, 0.849, 0.332, 0.0716, 0.0218, 0.00493, 0.000901], # MavBlue
        'normalizingChannels': [nm415, nm445],
        'channelNormalizationImpactFactor': 0.75,
        'normalizationShiftMeanIndices': [3, 9],
        'smoothingKnots': 8,
        # Depth of the curve correlates to actual points risen x constant
        'testFluorChangeCurveMeasureToRise': 3.0,
        # Percent that the signal must rise above baseline
        'testFluorChangePosThreshold': 0.07,
        'testFluorChangeNegThreshold': 0.03,
        # Max noise to signal
        'testFluorChangePosNoiseRatioThreshold': 1.0,
        'testFluorChangeNegNoiseRatioThreshold': 0.5,
    }
