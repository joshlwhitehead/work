import matplotlib.pyplot as plt
import numpy as np

### LED
ledInst = [5,6,7,10,13,25,26,27]
lasInst = [1,2,8,11,12,15]

ledRat = [3.12,3.46,2.28,2.49,2.37,1.84,3.13,2.41]
lasRat = [4.65,2.43,1.92,2.06,2.99,3.98]

led = {}
for i in range(len(ledInst)):
    led[ledInst[i]] = ledRat[i]

las = {}
for i in range(len(lasInst)):
    las[lasInst[i]] = lasRat[i]

fmaxSnp = {1:3370.333,2:3440.1,10:2676.5,12:3352.778,26:2557.333}
noiseSnp = {1:.0433,2:0.055,10:0.055,12:0.023,26:0.025}




for i in noiseSnp:
    if i in ledInst:
        plt.scatter(led[i],noiseSnp[i],color='blue',label='led')
    elif i in lasInst:
        plt.scatter(las[i],noiseSnp[i],color='red',label='laser')

plt.legend()
plt.ylabel('pcr noise')
plt.xlabel('qdot ratio')
plt.grid()
plt.show()



