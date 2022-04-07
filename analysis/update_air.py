# from cp import mainTableVal
from airtable import Airtable
# import matplotlib.pyplot as plt

baseId = 'appNSxNY9azGBJsld'
apiKey = 'keyWE1cKBVZqYhNMi'

tableName = 'Experiments'
print(1)
mainTableVal = Airtable(baseId,tableName,apiKey)
print(2)
print(mainTableVal('Experiments')[0])
# records = mainTableVal.get_all()

# print(len(records))
# def wetDry():
#     for i in range(len(records)):
#         if 'FD' in records[i]['fields']['Description']:
#             rec = records[i]['id']
#             fields = {'Wet/Dry':'Dry'}
#             mainTableVal.update(rec,fields)
#         elif 'End to End' in records[i]['fields']['Description']:
#             rec = records[i]['id']
#             fields = {'Wet/Dry':'Dry'}
#             mainTableVal.update(rec,fields)
#         elif 'Dry' in records[i]['fields']['Description']:
#             rec = records[i]['id']
#             fields = {'Wet/Dry':'Dry'}
#             mainTableVal.update(rec,fields)
#         elif 'dry' in records[i]['fields']['Description']:
#             rec = records[i]['id']
#             fields = {'Wet/Dry':'Dry'}
#             mainTableVal.update(rec,fields)
#         elif 'fd' in records[i]['fields']['Description']:
#             rec = records[i]['id']
#             fields = {'Wet/Dry':'Dry'}
#             mainTableVal.update(rec,fields)
#         elif 'end-end' in records[i]['fields']['Description']:
#             rec = records[i]['id']
#             fields = {'Wet/Dry':'Dry'}
#             mainTableVal.update(rec,fields)
#         elif 'Saliva' in records[i]['fields']['Description']:
#             rec = records[i]['id']
#             fields = {'Wet/Dry':'Dry'}
#             mainTableVal.update(rec,fields)
#         elif 'saliva' in records[i]['fields']['Description']:
#             rec = records[i]['id']
#             fields = {'Wet/Dry':'Dry'}
#             mainTableVal.update(rec,fields)
#         elif 'Amplified' in records[i]['fields']['Description']:
#             rec = records[i]['id']
#             fields = {'Wet/Dry':'Wet'}
#             mainTableVal.update(rec,fields)
#         elif 'amplified' in records[i]['fields']['Description']:
#             rec = records[i]['id']
#             fields = {'Wet/Dry':'Wet'}
#             mainTableVal.update(rec,fields)
#         else:
#             rec = records[i]['id']
#             fields = {'Wet/Dry':'Wet'}
#             mainTableVal.update(rec,fields)

