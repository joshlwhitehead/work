import os

folderNom = 'injMold4_injMold5'
folderSwap = 'injMold4_injMold5_swap'

for i in os.listdir(folderSwap):
    if 'injMold4' in i:
        x = i.split('_')
        x.insert(-1,'LED-B')
        x = '_'.join(x)
        os.rename('/'.join([folderSwap,i]),'/'.join([folderSwap,x]))
    elif 'injMold5' in i:
        x = i.split('_')
        x.insert(-1,'LED-A')
        x = '_'.join(x)
        os.rename('/'.join([folderSwap,i]),'/'.join([folderSwap,x]))

