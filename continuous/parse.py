import pandas as pd
import matplotlib.pyplot as plt



file = open('SNP alpha06.txt','r')
capt = []
for i in file:
    if '_performCapture' in i:
        capt.append(i)
file.close()


file = open('SNP alpha06.txt','w')
for i in capt:
    file.write(i)
file.close



data = pd.read_csv('Book1.csv')['T']
plt.plot(data)
plt.grid()
plt.xlim()
plt.ylim()
plt.savefig('test.png')