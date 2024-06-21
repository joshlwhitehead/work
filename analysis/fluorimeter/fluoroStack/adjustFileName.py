import os

folderNom = 'injMold4_injMold5'
folderSwap = 'injMold4_injMold5_swap'
folderrr = 'im4_im5_lastTry'

for i in os.listdir(folderrr):
    if '11' in i or '12' in i or '13' in i:
        x = i.split('_')
        newName = x.insert(-1,'rebuild')
        x = '_'.join(x)
        os.rename('/'.join([folderrr,i]),'/'.join([folderrr,x]))

