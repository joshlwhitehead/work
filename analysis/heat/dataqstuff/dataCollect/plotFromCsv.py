import dataToVar as dat
import matplotlib.pyplot as plt
from thermalCompareQuant import listAvg


# plt.plot(dat.testb[2],label='current')
# plt.plot(dat.testa[2],label='proposed')
# plt.plot(dat.b[2],label='new mod')
# plt.plot(dat.uL700[2],label='700')
# plt.plot(dat.uL800[2],label='800')
# plt.plot(dat.uL900[2],label='900')
# plt.plot(dat.uL700[1],'--')

# plt.plot(dat.tight[2],label= 'tight')
# plt.plot(dat.loose[2],label='saggy')
# plt.plot(dat.loose[1])
# plt.plot(dat.uL600_b[2],label='600')


# plt.plot(dat.uL700[0][:len(dat.uL700[2])],dat.uL700[2],label='700')
# plt.plot(dat.uL700[0][:len(dat.uL700[1])],dat.uL700[1],label='700Thermister')
# plt.plot(dat.uL800[0][:len(dat.uL800[2])],dat.uL800[2],label='800')
# plt.plot(dat.uL800[0][:len(dat.uL800[1])],dat.uL800[1],label='800Thermister')
# plt.plot(dat.uL600[0][:len(dat.uL600[2])],dat.uL600[2],label='600')
# plt.plot(dat.uL600[0][:len(dat.uL600[1])],dat.uL600[1],label='600Thermister')
# plt.plot(dat.uL700_d[1],label='700')

# plt.plot(dat.uL800_d[1],label='800')

# plt.plot(dat.uL600[0][:len(dat.uL600[1])],dat.uL600[1],label='600Thermister')
# plt.plot(dat.uL700_b[1],label='700')
# plt.plot(dat.uL700[0][:len(dat.uL700[1])],dat.uL700[1],label='700Thermister')

# plt.plot(dat.f1[0],dat.f1[1])
# plt.plot(dat.f2[0],dat.f2[1])
# plt.plot(dat.f3[0],dat.f3[1])
# plt.plot(dat.f4[0],dat.f4[1])



# plt.plot(dat.h90_top[0][:len(dat.h90_top[2])],dat.h90_top[2])
# plt.plot(dat.h90_top[0][:len(dat.h90_top[2])],dat.h90_top[3])
# plt.plot(dat.h90_top[0][:len(dat.h90_top[1])],dat.h90_top[1])
# plt.plot(dat.h90[0][:len(dat.h90[2])],dat.h90[2])
# plt.plot(dat.h90[0][:len(dat.h90[2])],dat.h90[3])

# plt.plot(dat.full_noInsert[1])
# plt.plot(dat.full_noInsert[2],label='no insert')
# plt.plot(dat.full_insertD2_b[1])
# plt.plot(dat.full_insertD2_b[2],label='insert D')
# plt.plot(dat.full_insertF_c[1])
# plt.plot(dat.full_insertF_c[2],label='insert F')
# plt.plot(dat.full_insertB[1])
# plt.plot(dat.full_insertB[2],label='insert B')
# plt.plot(dat.full_insertB2[1])
# plt.plot(dat.full_insertB2[2],label='insert B')
# plt.plot(dat.full_insertC[1])
# plt.plot(dat.full_insertC[2],label='insert C')

# plt.plot(dat.h90_inf[2])
# plt.plot(dat.h90_inf[3])
# plt.plot(dat.h90_c[3])

# plt.plot(dat.full_forward [1])
# plt.plot(dat.full_forward[2],label='forward')
# plt.plot(dat.full_Backward[1])
# plt.plot(dat.full_Backward[2],label='backward')
# plt.plot(dat.full_x[1])
# plt.plot(dat.full_x[2],label='x')

# plt.plot(dat.double[1])
# plt.plot(dat.ramp1Cool[2],label='1')
# plt.plot(dat.ramp2Cool[2],label='2')
# plt.plot(dat.ramp3Cool[2],label='3')
# plt.xlabel('time')
# plt.ylabel('temp (c)')
# plt.plot(dat.holdDown[1])
# plt.plot(dat.noHoldDown[1])


# plt.plot(dat.a57[1],color='k')

# thick = 1.5
# plt.plot(dat.a52[2],lw=thick,color='green',label='5.2')
# plt.plot(dat.b52[2],lw=thick,color='green')
# plt.plot(dat.c52[2],lw=thick,color='green')
# plt.plot(dat.d52[2],lw=thick,color='green')
# plt.plot(dat.e52[2],lw=thick,color='green')
# plt.plot(dat.a54[2],lw=thick,color='red',label='5.4')
# plt.plot(dat.b54[2],lw=thick,color='red')
# plt.plot(dat.c54[2],lw=thick,color='red')
# plt.plot(dat.d54[2],lw=thick,color='red')
# plt.plot(dat.a57[2],lw=thick,color='blue',label='5.7')
# plt.plot(dat.b57[2],lw=thick,color='blue')
# plt.plot(dat.c57[2],lw=thick,color='blue')

# plt.ylabel('Temp (c)')
# plt.title('Non-recessed deck pedestal fill')


"""v04"""

plt.figure()
plt.plot(dat.v04r46a[0][:len(dat.v04r46a[2])],dat.v04r46a[2],color='blue',label='4.6 Recessed')
plt.plot(dat.v04r46b[0][:len(dat.v04r46b[2])],dat.v04r46b[2],color='blue')
plt.plot(dat.v04r46c[0][:len(dat.v04r46c[2])],dat.v04r46c[2],color='blue')
plt.plot(dat.v04r46d[0][:len(dat.v04r46d[2])],dat.v04r46d[2],color='blue')
plt.plot(dat.v04r46e[0][:len(dat.v04r46e[2])],dat.v04r46e[2],color='blue')


plt.plot(dat.v04r52a[0][:len(dat.v04r52a[2])],dat.v04r52a[2],color='green',label='5.2 Recessed')
plt.plot(dat.v04r52b[0][:len(dat.v04r52b[2])],dat.v04r52b[2],color='green')
plt.plot(dat.v04r52c[0][:len(dat.v04r52c[2])],dat.v04r52c[2],color='green')
plt.plot(dat.v04r52d[0][:len(dat.v04r52d[2])],dat.v04r52d[2],color='green')
plt.plot(dat.v04r52e[0][:len(dat.v04r52e[2])],dat.v04r52e[2],color='green')

plt.plot(dat.v05r52a[0][:len(dat.v05r52a[2])],dat.v05r52a[2],color='green')
plt.plot(dat.v05r52b[0][:len(dat.v05r52b[2])],dat.v05r52b[2],color='green')
plt.plot(dat.v05r52c[0][:len(dat.v05r52c[2])],dat.v05r52c[2],color='green')
plt.plot(dat.v05r52d[0][:len(dat.v05r52d[2])],dat.v05r52d[2],color='green')

plt.plot(dat.v06r52a[0][:len(dat.v06r52a[2])],dat.v06r52a[2],color='green')
plt.plot(dat.v06r52b[0][:len(dat.v06r52b[2])],dat.v06r52b[2],color='green')
plt.plot(dat.v06r52c[0][:len(dat.v06r52c[2])],dat.v06r52c[2],color='green')
plt.plot(dat.v06r52d[0][:len(dat.v06r52d[2])],dat.v06r52d[2],color='green')
plt.plot(dat.v06r52e[0][:len(dat.v06r52e[2])],dat.v06r52e[2],color='green')


plt.plot(dat.v04r57a[0][:len(dat.v04r57a[2])],dat.v04r57a[2],color='orange',label='5.7 Recessed')
plt.plot(dat.v04r57b[0][:len(dat.v04r57b[2])],dat.v04r57b[2],color='orange')
plt.plot(dat.v04r57c[0][:len(dat.v04r57c[2])],dat.v04r57c[2],color='orange')
plt.plot(dat.v04r57d[0][:len(dat.v04r57d[2])],dat.v04r57d[2],color='orange')
plt.plot(dat.v04r57e[0][:len(dat.v04r57e[2])],dat.v04r57e[2],color='orange')

plt.plot(dat.v05r57a[0][:len(dat.v05r57a[2])],dat.v05r57a[2],color='orange')
plt.plot(dat.v05r57b[0][:len(dat.v05r57b[2])],dat.v05r57b[2],color='orange')
plt.plot(dat.v05r57c[0][:len(dat.v05r57c[2])],dat.v05r57c[2],color='orange')
plt.plot(dat.v05r57d[0][:len(dat.v05r57d[2])],dat.v05r57d[2],color='orange')

plt.plot(dat.v04r46a[0][:len(dat.v04r46a[4])],dat.v04r46a[4],color='k')
plt.grid()
plt.title('Insert Height Comparison on Recessed Deck')
plt.ylabel('Temperature (C)')
plt.legend()


plt.figure() 
plt.plot(listAvg([dat.v04r46a[2][:len(dat.v04r46e[2])],
    dat.v04r46b[2][:len(dat.v04r46e[2])],
    dat.v04r46c[2][:len(dat.v04r46e[2])],
    dat.v04r46d[2][:len(dat.v04r46e[2])],
    dat.v04r46e[2]])[1],
    color='blue',label='4.6 Recessed')
plt.plot(listAvg([dat.v04r52a[2],
    dat.v04r52b[2][:len(dat.v04r52a[2])],
    dat.v04r52c[2][:len(dat.v04r52a[2])],
    dat.v04r52d[2][:len(dat.v04r52a[2])],
    dat.v04r52e[2][:len(dat.v04r52a[2])],
    dat.v05r52a[2][:len(dat.v05r52b[2])],
    dat.v05r52b[2][:len(dat.v05r52b[2])],
    dat.v05r52c[2][:len(dat.v05r52b[2])],
    dat.v05r52d[2][:len(dat.v05r52b[2])]])[1],
    color='green',label='5.2 Recessed')
plt.plot(listAvg([dat.v04r57a[2][:len(dat.v04r57e[2])],
    dat.v04r57b[2][:len(dat.v04r57e[2])],
    dat.v04r57c[2][:len(dat.v04r57e[2])],
    dat.v04r57d[2][:len(dat.v04r57e[2])],
    dat.v04r57e[2]])[1],
    color='orange',label='5.7 Recessed')
# plt.plot(dat.r46a[4],color='k')
plt.title('stdev by Insert')

plt.legend()
plt.grid()

plt.show()




# """v05"""

# plt.figure()
# # plt.plot(dat.r46a[2],color='blue',label='4.6 Recessed')
# # plt.plot(dat.r46b[2],color='blue')
# # plt.plot(dat.r46c[2],color='blue')
# # plt.plot(dat.r46d[2],color='blue')
# # plt.plot(dat.r46e[2],color='blue')
# plt.plot(dat.r52a[2],color='green',label='5.2 Recessed')
# plt.plot(dat.r52b[2],color='green')
# plt.plot(dat.r52c[2],color='green')
# plt.plot(dat.r52d[2],color='green')
# # plt.plot(dat.r52e[2],color='green')
# plt.plot(dat.r57a[2],color='orange',label='5.7 Recessed')
# plt.plot(dat.r57b[2],color='orange')
# plt.plot(dat.r57c[2],color='orange')
# plt.plot(dat.r57d[2],color='orange')
# # plt.plot(dat.r57e[2],color='orange')
# plt.plot(dat.r52a[4],color='k')
# plt.grid()
# plt.title('Insert Height Comparison on Recessed Deck')
# plt.ylabel('Temperature (C)')
# plt.legend()

# plt.figure() 
# # plt.plot(listAvg([dat.r46a[2][:len(dat.r46e[2])],dat.r46b[2][:len(dat.r46e[2])],dat.r46c[2][:len(dat.r46e[2])],dat.r46d[2][:len(dat.r46e[2])],dat.r46e[2]])[1],color='blue',label='4.6 Recessed')
# plt.plot(listAvg([dat.r52a[2],dat.r52b[2][:len(dat.r52a[2])],dat.r52c[2][:len(dat.r52a[2])],dat.r52d[2][:len(dat.r52a[2])]])[1],color='green',label='5.2 Recessed')
# plt.plot(listAvg([dat.r57a[2][:len(dat.r57a[2])],dat.r57b[2][:len(dat.r57a[2])],dat.r57c[2][:len(dat.r57a[2])],dat.r57d[2][:len(dat.r57a[2])]])[1],color='orange',label='5.7 Recessed')
# # plt.plot(dat.r46a[4],color='k')
# plt.title('stdev by Insert')

# plt.legend()
# plt.grid()

# plt.show()













