

from datetime import datetime
import numpy as np

from lib.analysis_operation import AnalysisOperation


class IntracycleCp(AnalysisOperation):
    name = 'intracycleCp'

    def run(self, data):
        self.start = datetime.now()

        fluor = data['tilted']
        cps = data['cps']


        pointsToUse = 4
        intracyleCp = []
        for i, d in enumerate(fluor):
            cp = cps[i]
            if cp > pointsToUse:
                # fit the polynomial
                cyc = [cp - pointsToUse + i for i in range(pointsToUse * 2 + 1)]
                # print(len(d[cp - pointsToUse:cp + pointsToUse + 1]))
                fit = np.polyfit(cyc, d[cp - pointsToUse:cp + pointsToUse + 1], 2)
                # take the derivative
                der = np.polyder(fit)
                r = np.roots(der)
                
                # Add one because the cycles are 0 indexed.
                intracyleCp.append(round(r[0] + 1.0, 2))
            else:
                intracyleCp.append(float('nan'))
                
        self.stop = datetime.now()

        return {
            'cqs': intracyleCp,
            'intracycleCps': intracyleCp,
        }
