import pandas as pd
from statsmodels.graphics.factorplots import interaction_plot
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

dF = pd.read_csv('newnew.csv')



fig = interaction_plot(dF.inst,dF.lot, dF.fill, ms=10)
plt.xticks(rotation=45)
plt.grid()
plt.show()


formula = 'fill ~ C(lot) + C(inst)'  
# don't include interaction term, ' + C(Filter):C(Day)', unless Kij > 1.
model = ols(formula, dF).fit()
aov_table = anova_lm(model, typ=2)
print(aov_table)
