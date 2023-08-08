import numpy as np
from parsTxt import parsPCRTxt, parsTCTxt, meltRamp
import matplotlib.pyplot as plt



file = 'oldButUseful/dataTC/Adv06_P11_2383ea_221220_Run1.txt'
tc = parsTCTxt(file)[0][1]
tcTemp = parsTCTxt(file)[0][0]

tc1 = parsTCTxt(file)[1][1]
tcTemp1 = parsTCTxt(file)[1][0]
# plt.plot(tc,tcTemp)
plt.plot(tc1,tcTemp1,'o')
plt.grid()
plt.show()