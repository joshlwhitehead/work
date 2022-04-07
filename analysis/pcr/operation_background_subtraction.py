from datetime import datetime
import numpy as np

from lib.analysis_operation import AnalysisOperation


class BackgroundSubtraction(AnalysisOperation):
    name = 'backgroundSubtraction'

    def run(self, data):
        self.start = datetime.now()

        backgroundCycles = self.config.backgroundCycles
        # Normal vector for the first few runs averaged
        # row by row multiple to the max and subtract

        # [3,4]

        fluor = data['current']
        
        background = np.average(np.array(fluor)[:, backgroundCycles], axis=1).astype(int)

        backgroundSubtracted = [np.subtract(f, background[i]) for i,f in enumerate(fluor)]

        # backgroundSubtracted = np.add(backgroundSubtracted, abs(np.min(backgroundSubtracted)))

        self.stop = datetime.now()

        return {
            'current': backgroundSubtracted,
            'background': background,
            'backgroundSubtracted': backgroundSubtracted,
        }
