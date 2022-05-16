from dataq import DataQ
from time import sleep
import serial
from threading import Thread
import time
import os
date = '16May2022'
directory = ''.join(['data/',date])
folder = os.path.isdir(directory)
if folder == True:
    pass
else:
    os.mkdir(directory)


x = input('fileName: ')
f = open(''.join([directory,'/',x,'.txt']), "a")
start =time.time() 
def dataQThread(dataq, file):
    dataq.start()
    sleep(5)
    

    while True:
        liquid1 = dataq.getThermocouple(0)
        # stg1htsnk = dataq.getThermocouple(1)

        # liquidAvg = (liquid1 + liquid2) / 2
        line = "DATAQ: " + \
                    " | liquid = "   + str(round(liquid1, 2)) + \
                    " |"

                    # " | stg1htsnk = " + str(round(stg1htsnk, 2)) + \
                    # " | liquidAvg = "  + str(round(liquidAvg, 2)) + \
                    # " | liquid2 = "  + str(round(liquid2, 2)) + \
                    # " | laser = "    + str(round(dataq.getThermocouple(2), 2)) + \
                    # " | pcrhtsnk = " + str(round(dataq.getThermocouple(3), 2)) + \

                    # " | stg1htsnk = " + str(round(dataq.getThermocouple(4), 2)) + \
        end = time.time()
        print(line,'elapsed time ',round(end-start))
        file.write(line + "\n")
        file.flush()
        sleep(1)

dataq = DataQ([(1,'t')])#,(2,'t')])#,(3,'t'),(4,'t'),(5,'t')])
t = Thread(target=dataQThread, args=(dataq,f))
t.start()
ser = serial.Serial('COM6', 115200)


while (True):
    pass
    try:
        line = ser.readline().decode("latin1", "replace")
        print(line, end='')
        try:
            f.write(line)
            f.flush()
        except():
            pass
    except():
        pass