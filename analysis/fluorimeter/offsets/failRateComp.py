import pandas as pd
from confidenceFun import tukey



df = {
    'thump':['off','off','off','on','on','on'],
    'fail':[5/6,4/5,5/7,2/5,2/5,1/3]
    }

print(tukey(df,'thump','fail',.1))

