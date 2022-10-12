from numpy import full
import pandas as pd

def getData(file,date):
    fullSheet = pd.read_csv(''.join(['qdotData/',date,str(file)]))
    if 'PCR Modeled TempC' in fullSheet.columns():
        tempFull = fullSheet['PCR Modeled TempC']
    if 'timeSinceBoot' in fullSheet.columns():
        timeFull = fullSheet['timeSinceBoot']

    nm415 = fullSheet['415nm']
    nm445 = fullSheet['415nm']
    nm480 = fullSheet['415nm']
    nm515 = fullSheet['415nm']
    nm555 = fullSheet['415nm']
    nm590 = fullSheet['415nm']
    nm630 = fullSheet['415nm']
    nm680 = fullSheet['415nm']

    