import dataToVar as dat
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

time = dat.h90[0]
therm = dat.h90[1]
samp = dat.h90[2]

dF = pd.DataFrame({'time':time,'therm':therm,'samp':samp})
dF.to_csv('test.csv')

# plt.plot(dat.h90[0],dat.h90[1])
# plt.plot(dat.h90[0],dat.h90[2])
# plt.show()