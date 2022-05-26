import pandas as pd
import matplotlib.pyplot as plt

def read(data):
    file = open(''.join(['dave_local_test_data/26May2022/',data,'.txt']),'r')
    temps = []
    for line in file:
        temps.append(float(line[28:33]))
    plt.plot(temps)
    plt.grid()
    plt.title('topFilm')
    plt.ylabel('temp (c)')
    plt.savefig(''.join(['dave_local_test_data/26May2022/','topFilmA']))
    
    file.close()

read('testa_top')