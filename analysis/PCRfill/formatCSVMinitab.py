import pandas as pd

original = pd.read_csv('convertcsv (4).csv')

lot = original['consumable/lot']
fill = original['numericValue']

heads = {}
for i in lot:
    if i not in heads:
        heads[i] = []


for i in range(len(fill)):
    heads[lot[i]].append(fill[i])

x = []
for i in heads:
    x.append(len(heads[i]))

for i in heads:
    while len(heads[i]) < max(x):
        heads[i].append(None)

dF = pd.DataFrame(heads)
dF.to_csv('forMinitabByLot.csv')
