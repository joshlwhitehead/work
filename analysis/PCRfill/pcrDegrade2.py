import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import t
from statsmodels.formula.api import ols



file = pd.read_csv('pcrFillData2.csv')

run = file['runs'][:5]
m = file['mass'][:5]
# thick = file['thickness (mm)']


alpha = 0.05
def CI():
    n = len(m)
    dof = n-2
    model = ols('mass ~ runs',file).fit()
    slope = model.params[1]
    se = np.sqrt(model.mse_resid)
    Sxx = np.var(m) * n
    t_star = t.ppf(1.0 - 0.5 * alpha, dof) # using t-distribution
    ciMin = slope-t_star*se/np.sqrt(Sxx)
    ciMax = slope+t_star*se/np.sqrt(Sxx)
    print(ciMin,ciMax)


# for i in thick:
CI()


