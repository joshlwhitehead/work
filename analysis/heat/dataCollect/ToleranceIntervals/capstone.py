from parsTxt import parsPCRTxt
file = 'capstoneGradThermals\B45_gradThermals_1.txt'
fun = parsPCRTxt(file)
heat,th = fun[0]
cool,tc = fun[1]
modH,mth = fun[-2]
modC,cth = fun[-1]
thermH,tth = fun[4]
thermC,ttc = fun[6]



import matplotlib.pyplot as plt
for indx,val in enumerate(heat):
    if indx == 0:
        plt.plot(th[indx],val,'tab:green',label='Top of Sample')
    else:
        plt.plot(th[indx],val,'tab:green')
for indx,val in enumerate(cool):
    plt.plot(tc[indx],val,'tab:green')

for indx,val in enumerate(modH):
    if indx == 0:
        plt.plot(mth[indx],val,'tab:orange',label='Model')
    else:
        plt.plot(mth[indx],val,'tab:orange')
for i,val in enumerate(modC):
    plt.plot(cth[i],val,'tab:orange')


for indx,val in enumerate(thermC):
    thermC[indx].insert(0,thermH[indx][-1])
    ttc[indx].insert(0,tth[indx][-1])
for indx,val in enumerate(thermH):
    if indx == 0:
        plt.plot(tth[indx],val,'tab:blue',label='Bottom of Sample')
    else:
        plt.plot(tth[indx],val,'tab:blue')
for indx,val in enumerate(thermC):
    plt.plot(ttc[indx],val,'tab:blue')
# plt.plot(fun[3][1],fun[3][0])
plt.legend()
plt.grid()
plt.show()