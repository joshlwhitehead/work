import pandas as pd
import openpyxl as op

file = 'test.xlsx'
sheet = 'full'
# writer = pd.ExcelWriter(file,engine='xlsxwriter')

wb = op.load_workbook('test.xlsx')

with pd.ExcelWriter('test.xlsx',engine='openpyxl') as writer:
    writer.book = wb
    ws = writer.sheets

    sheet = 'full'
    chart = ws.add_chart({'type':'line'})
    chart.add_series({
    'categories':[sheet,1,2,10,2],
    'values':[sheet,1,3,10,3]})
    writer.sheets.insert_chart('D2',chart)
    writer.save()








# writer.save()