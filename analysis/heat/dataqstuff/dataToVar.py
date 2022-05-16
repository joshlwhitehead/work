"""This is a space to organize data. getData function parses out csv produced by dave"""
import getData as gd

lid0Cons0_90 = gd.getData('lid0Cons0_90b.csv','31Mar2022')
lid0Cons0_70 = gd.getData('lid0Cons0_70.csv','31Mar2022')
lid0Cons0_50 = gd.getData('lid0Cons0_50.csv','31Mar2022')
lid0Cons0_100 = gd.getData('lid0Cons0_100.csv','31Mar2022')

b90 = gd.getData('lid0Cons0_90b.csv','01Apr2022')

lid0Cons0_fr = gd.getData('lid0Cons0_fullRun.csv','25Mar2022')
oldFr = gd.getData('lid0Cons0_fullRun1.csv','24Mar2022')
lid0Cons0_fr1 = gd.getData('lid0Cons0_fullRun1.csv','25Mar2022')
lid0Cons0_fr_ramp1 = gd.getData('lid0Cons0_fullRun_ramp1.csv','25Mar2022')

lid0Cons1_fr1_ramp1 = gd.getData('lid0Cons1_fullRun1_ramp1.csv','25Mar2022')


###################         COOL            ##########################
cool100_80 = gd.getData('lid0Cons0Cool_100_80.csv','31Mar2022')
cool100_60 = gd.getData('lid0Cons0Cool_100_60.csv','31Mar2022')
cool100_40 = gd.getData('lid0Cons0Cool_100_40.csv','31Mar2022')



##################                  FULL                        ############################
frS1 = gd.getData('lid0Cons0_fullRun.csv','31Mar2022')
testb = gd.getData('lid0Cons0_fullRunb.csv','01Apr2022')

testa = gd.getData('lidc_fullRun_115for20_100for180.csv','05Apr2022')


#######################                                 MOD                                                             ############################

b = gd.getData('lid0Cons1_v001_63_50_90_for200.csv','08Apr2022')

oil = gd.getData('lidC_mOil_peepshow.csv','14Apr2022')
wat = gd.getData('lidCCons2Peepshow_fullRun.csv','14Apr2022')



# import matplotlib.pyplot as plt
# plt.plot(testa[1])
# plt.plot(testa[2])
# plt.plot(b90[2])
# plt.grid()
# plt.show()




########################            BREAK                       ########################
break115 = gd.getData('lid0_break_contAcq.csv','05Apr2022')
break105 = gd.getData('lid0_break_contAcq_105.csv','05Apr2022')





#######################         THERMO 001                              ###################

uL700 = gd.getData('lidB700uL_sealed_c.csv','06May2022')
uL800 = gd.getData('lidB800uL_sealed_c.csv','06May2022')
uL900 = gd.getData('lidB900uL_sealed_b.csv','06May2022')

modRetrainData = gd.getData('N27_Stg1_High1.csv','16May2022')
modRetrainCool = gd.getData('Stg1_model_retrain_new_proto4.csv','16May2022')



