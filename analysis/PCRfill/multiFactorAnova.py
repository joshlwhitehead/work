import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.graphics.factorplots import interaction_plot
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd


original = pd.read_csv('convertcsv (4).csv')

inst = original['instrument']
lot = original['consumable/lot']
fill = original['numericValue']



new = {}
for i in inst:
    new[i] = {}




