import pandas as pd

data5 = pd.read_excel('qDotJosh.xlsx',sheet_name=1)

print(data5['q7'][0])
