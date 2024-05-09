import os
import shutil
def moveFiles():
    parent = 'expandedNominal/byInst'
    for i in os.listdir(parent):
        if 'no thump' in i:
            for u in os.listdir('/'.join([parent,i])):
                shutil.copy('/'.join([parent,i,u]),'/'.join(['expandedNominal','official no thump',u]))
        elif 'thump' in i:
            for u in os.listdir('/'.join([parent,i])):
                shutil.copy('/'.join([parent,i,u]),'/'.join(['expandedNominal','official thump',u]))



