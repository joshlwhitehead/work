"""This is a space to organize data. getData function parses out csv produced by dave"""

from gc import get_debug
import getData as gd

# lid0Cons0_90 = gd.getData('lid0Cons0_90b.csv','31Mar2022')
# # lid0Cons0_70 = gd.getData('lid0Cons0_70.csv','31Mar2022')
# # lid0Cons0_50 = gd.getData('lid0Cons0_50.csv','31Mar2022')
# # lid0Cons0_100 = gd.getData('lid0Cons0_100.csv','31Mar2022')

# # b90 = gd.getData('lid0Cons0_90b.csv','01Apr2022')

# # lid0Cons0_fr = gd.getData('lid0Cons0_fullRun.csv','25Mar2022')
# # oldFr = gd.getData('lid0Cons0_fullRun1.csv','24Mar2022')
# # lid0Cons0_fr1 = gd.getData('lid0Cons0_fullRun1.csv','25Mar2022')
# # lid0Cons0_fr_ramp1 = gd.getData('lid0Cons0_fullRun_ramp1.csv','25Mar2022')

# # lid0Cons1_fr1_ramp1 = gd.getData('lid0Cons1_fullRun1_ramp1.csv','25Mar2022')


# # ###################         COOL            ##########################
# # cool100_80 = gd.getData('lid0Cons0Cool_100_80.csv','31Mar2022')
# # cool100_60 = gd.getData('lid0Cons0Cool_100_60.csv','31Mar2022')
# # cool100_40 = gd.getData('lid0Cons0Cool_100_40.csv','31Mar2022')




# # ##################                  FULL                        ############################
# # frS1 = gd.getData('lid0Cons0_fullRun.csv','31Mar2022')
# # testb = gd.getData('lid0Cons0_fullRunb.csv','01Apr2022')

# # testa = gd.getData('lidc_fullRun_115for20_100for180.csv','05Apr2022')


# # #######################                                 MOD                                                             ############################

# # b = gd.getData('lid0Cons1_v001_63_50_90_for200.csv','08Apr2022')

# # oil = gd.getData('lidC_mOil_peepshow.csv','14Apr2022')
# # wat = gd.getData('lidCCons2Peepshow_fullRun.csv','14Apr2022')



# # # import matplotlib.pyplot as plt
# # # plt.plot(testa[1])
# # # plt.plot(testa[2])
# # # plt.plot(b90[2])
# # # plt.grid()
# # # plt.show()




# # ########################            BREAK                       ########################
# # break115 = gd.getData('lid0_break_contAcq.csv','05Apr2022')
# # break105 = gd.getData('lid0_break_contAcq_105.csv','05Apr2022')





# # #######################         THERMO 001                              ###################

# # # uL700 = gd.getData('lidB700uL_sealed_c.csv','06May2022')
# # # uL800 = gd.getData('lidB800uL_sealed_c.csv','06May2022')
# # # uL900 = gd.getData('lidB900uL_sealed_b.csv','06May2022')

# # modRetrainData = gd.getData('N27_Stg1_High1.csv','16May2022')
# # modRetrainCool = gd.getData('Stage1_Model_Train_Final.csv','17May2022')



# # tight = gd.getData('tightTest.csv','18May2022')
# # loose = gd.getData('looseTest.csv','18May2022')


# ######################              V v T                           #########################

# uL600 = gd.getData('uL600.csv','20May2022')
# uL700 = gd.getData('uL700.csv','20May2022')
# uL800 = gd.getData('uL800.csv','20May2022')

# uL600_b = gd.getData('uL600_b.csv','20May2022')
# uL700_b = gd.getData('uL700_b.csv','20May2022')
# uL800_b = gd.getData('uL800_b.csv','20May2022')

# uL800_c = gd.getData('uL800_c.csv','20May2022')
# uL700_c = gd.getData('uL700_c.csv','20May2022')
# uL600_c = gd.getData('uL600_c.csv','20May2022')

# uL600_d = gd.getData('uL600_d.csv','20May2022')
# uL700_d = gd.getData('uL700_d.csv','20May2022')
# uL800_d = gd.getData('uL800_d.csv','20May2022')

# ###########################             break stuff                            #############################
# # f1 = gd.getData('f1.csv','19May2022')
# # f2 = gd.getData('f2.csv','19May2022')
# # f3 = gd.getData('f3.csv','19May2022')
# # f4 = gd.getData('f4.csv','19May2022')
# # f5 = gd.getData('f5.csv','19May2022')
# # f6 = gd.getData('f6.csv','19May2022')
# # f7 = gd.getData('f7.csv','19May2022')
# # f8 = gd.getData('f8.csv','19May2022')
# # f9 = gd.getData('f9.csv','19May2022')
# # f10 = gd.getData('f10.csv','19May2022')
# # f11 = gd.getData('f11.csv','19May2022')
# # f12 = gd.getData('f12.csv','19May2022')
# # f13 = gd.getData('f13.csv','19May2022')
# # f14 = gd.getData('f14.csv','19May2022')
# # f15 = gd.getData('f15.csv','19May2022')
# # f16 = gd.getData('f16.csv','19May2022')
# # f17 = gd.getData('f17.csv','19May2022')
# # f18 = gd.getData('f18.csv','19May2022')
# # f20 = gd.getData('f20.csv','19May2022')
# # f21 = gd.getData('f21.csv','19May2022')


# ###########################                         TWO THERMOCOUPLE                                    #########################################
# # h90 = gd.getData('hold90_noMod_twoThermo.csv','26May2022')
# # h90_b = gd.getData('hold90_noMod_twoThermo_b.csv','26May2022')
# h90_c = gd.getData('hold90_c.csv','26May2022')
# # h90_d = gd.getData('hold90_d.csv','26May2022')

# # h90_top = gd.getData('hold90_top.csv','26May2022')
# # h90_top_b = gd.getData('hold90_top_b.csv','26May2022')



# h90_inf = gd.getData('Tinf.csv','31May2022')

h70 = gd.getData('lidF_insertC_hold70.csv','01Jun2022')
h50 = gd.getData('lidF_insertC_hold50.csv','01Jun2022')
h100 = gd.getData('lidF_insertC_hold100_b.csv','01Jun2022')
h90 = gd.getData('lidF_insertC_hold90.csv','01Jun2022')

full_insertC = gd.getData('lidF_insertC_full.csv','01Jun2022')
# full_noInsert = gd.getData('lidF_noInsert_full.csv','01Jun2022')
# full_insertA = gd.getData('lidF_insertA_full.csv','01Jun2022')
# full_insertA2 = gd.getData('lidF_insertA2_full_b.csv','01Jun2022')
# full_insertB = gd.getData('lidF_insertB_full.csv','01Jun2022')
# full_insertB2 = gd.getData('lidF_insertB2_full.csv','01Jun2022')
# full_insertD = gd.getData('lidF_insertD_full.csv','02Jun2022')
# full_insertD2 = gd.getData('lidF_insertD2_full.csv','02Jun2022')
# full_insertD_b = gd.getData('lidF_insertD_full_c.csv','02Jun2022')
# full_insertD2_b = gd.getData('lidF_insertD2_full_b.csv','03Jun2022')
# full_insertF = gd.getData('lidF_insertF_full.csv','02Jun2022')
# full_insertF_b = gd.getData('lidF_insertF_full_b.csv','03Jun2022')
# full_insertF_c = gd.getData('lidF_insertF_full_c.csv','03Jun2022')

# h50_noInsert = gd.getData('lidF_noInsert_hold50.csv','01Jun2022')
# h70_noInsert = gd.getData('lidF_noInsert_hold70.csv','01Jun2022')
# h90_noInsert = gd.getData('lidF_noInsert_hold90.csv','01Jun2022')
# h100_noInsert = gd.getData('lidF_noInsert_hold100.csv','01Jun2022')

# h50_insertA = gd.getData('lidF_insertA2_hold50.csv','01Jun2022')
# h70_insertA = gd.getData('lidF_insertA2_hold70.csv','01Jun2022')
# h90_insertA = gd.getData('lidF_insertA2_hold90.csv','01Jun2022')
# h100_insertA = gd.getData('lidF_insertA2_hold100.csv','01Jun2022')

# h50_insertD = gd.getData('lidF_insertD_hold50.csv','02Jun2022')
# h70_insertD = gd.getData('lidF_insertD_hold70.csv','02Jun2022')
# h90_insertD = gd.getData('lidF_insertD_hold90.csv','02Jun2022')
h100_insertD = gd.getData('lidF_insertD_hold100.csv','02Jun2022')

h50_insert = gd.getData('lidG_insert_hold50_e.csv','07Jun2022')
h70_insert = gd.getData('lidG_insert_hold70_h.csv','07Jun2022')
h90_insert = gd.getData('lidG_insert_hold90_d.csv','07Jun2022')
h100_insert = gd.getData('lidG_insert_hold100_b.csv','07Jun2022')



# full_fat = gd.getData('lidF_insertF_fatBottom.csv','03Jun2022')
# full_flat = gd.getData('lidF_insertF_flatBottom.csv','03Jun2022')
# ##################################################          COOLING     ##########################################
c85_noInsert = gd.getData('lidF_noInsert_cool85.csv','02Jun2022')
c70_noInsert = gd.getData('lidF_noInsert_cool70.csv','02Jun2022')
c50_noInsert = gd.getData('lidF_noInsert_cool50.csv','02Jun2022')
c30_noInsert = gd.getData('lidF_noInsert_cool30.csv','02Jun2022')


# # c85_noInsert = gd.getData('lidF_noInsert_cool85.csv','02Jun2022')
c70_insert = gd.getData('lidG_insert_cool70.csv','07Jun2022')
c50_insert = gd.getData('lidG_insert_cool50.csv','07Jun2022')
c35_insert = gd.getData('lidG_insert_cool35.csv','07Jun2022')

# full_forward = gd.getData('lidG_insertForward_full_b.csv','06Jun2022')
# full_Backward = gd.getData('lidG_insertBackward_full_b.csv','06Jun2022')
# full_x = gd.getData('lidC_lumpCap_noInsert_fixKalman.csv','06Jun2022')

# first = gd.getData('lidG_lumpCap_firstRun.csv','07Jun2022')
# sec = gd.getData('lidG_lumpCap_secRun.csv','07Jun2022')
# third = gd.getData('lidG_lumpCap_thirdRun.csv','07Jun2022')


double = gd.getData('double1.csv','01Aug2022')
holdDown = gd.getData('holdDown.csv','03Aug2022')
noHoldDown = gd.getData('noHoldDown.csv','03Aug2022')

ramp1Cool = gd.getData('longCoolRamp1.csv','04Aug2022')
ramp2Cool = gd.getData('longCoolRamp2.csv','04Aug2022')
ramp3Cool = gd.getData('longCoolRamp3.csv','04Aug2022')
