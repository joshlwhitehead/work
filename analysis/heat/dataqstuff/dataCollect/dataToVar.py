"""This is a space to organize data. getData function parses out csv produced by dave"""


import getData as gd
"""
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

uL600 = gd.getData('uL600.csv','20May2022')
uL700 = gd.getData('uL700.csv','20May2022')
uL800 = gd.getData('uL800.csv','20May2022')

uL600_b = gd.getData('uL600_b.csv','20May2022')
uL700_b = gd.getData('uL700_b.csv','20May2022')
uL800_b = gd.getData('uL800_b.csv','20May2022')

uL800_c = gd.getData('uL800_c.csv','20May2022')
uL700_c = gd.getData('uL700_c.csv','20May2022')
uL600_c = gd.getData('uL600_c.csv','20May2022')

uL600_d = gd.getData('uL600_d.csv','20May2022')
uL700_d = gd.getData('uL700_d.csv','20May2022')
uL800_d = gd.getData('uL800_d.csv','20May2022')

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


inflectNorm = gd.getData('inflectNormFill1.csv','08Aug2022')
inflectLow = gd.getData('inflectLowFill2.csv','08Aug2022')



###################INSERTS#################################
date = '16Aug2022'
a57 = gd.getData('3483fb_57.csv',date)
b57 = gd.getData('7791e4_57.csv',date)
c57 = gd.getData('07813a_57.csv',date)

a54 = gd.getData('54a.csv',date)
b54 = gd.getData('54b.csv',date)
c54 = gd.getData('54c.csv',date)
d54 = gd.getData('54d.csv',date)

a52 = gd.getData('3a0ee6_52.csv',date)
b52 = gd.getData('04fd99_52.csv',date)
c52 = gd.getData('5e924a_52.csv',date)
d52 = gd.getData('9cfadc_52.csv',date)
e52 = gd.getData('18c660_52.csv',date)

date = '17Aug2022'
toeUp = gd.getData('toeUpV08.csv',date)
toeDown = gd.getData('toeDownV08.csv',date)


###########             RECESSED       v04                 ###################
date = '18Aug2022'
v04r52a = gd.getData('17Aug2022_V04_251f37_p14_52_1.csv',date)
v04r52b = gd.getData('17Aug2022_V04_aa9aef_p14_52_4.csv',date)
v04r52c = gd.getData('17Aug2022_V04_2700e1e_p14_52_11.csv',date)
v04r52d = gd.getData('17Aug2022_V04_dbccb5_p14_52_12.csv',date)
v04r52e = gd.getData('17Aug2022_V04_03dc44_p14_52_13.csv',date)
v04r57a = gd.getData('17Aug2022_V04_80cb5d_p14_57_5.csv',date)
v04r57b = gd.getData('17Aug2022_V04_10e32b_p14_57_6.csv',date)
v04r57c = gd.getData('17Aug2022_V04_345c60_p14_57_9.csv',date)
v04r57d = gd.getData('17Aug2022_V04_b8675e_p14_57_10.csv',date)
v04r57e = gd.getData('17Aug2022_V04_a9ddad_p14_57_15.csv',date)
v04r46a = gd.getData('17Aug2022_V04_fbcb66_p14_46_2.csv',date)
v04r46b = gd.getData('17Aug2022_V04_5098de_p14_46_3.csv',date)
v04r46c = gd.getData('17Aug2022_V04_a6b508_p14_46_7.csv',date)
v04r46d = gd.getData('17Aug2022_V04_7077b1_p14_46_8.csv',date)
v04r46e = gd.getData('17Aug2022_V04_673ed5_p14_46_14.csv',date)



######################              v05                                 ##########################


date = '23Aug2022'
v05r57a = gd.getData('23Aug2022_V05_f3a134_p14.csv',date)
v05r57b = gd.getData('23Aug2022_V05_8b9de9_p14.csv',date)
v05r57c = gd.getData('23Aug2022_V05_8e73a1_p16.csv',date)
v05r57d = gd.getData('23Aug2022_V05_47a837_p16.csv',date)

v05r52a = gd.getData('23Aug2022_V05_41334e_p16.csv',date)
v05r52b = gd.getData('23Aug2022_V05_febd3e_p16.csv',date)
v05r52c = gd.getData('23Aug2022_V05_303d56_p16.csv',date)
v05r52d = gd.getData('23Aug2022_V05_21e174_p16.csv',date)



##############################                          v06                                             ###################

v06r52a = gd.getData('23Aug2022_V06_dc7ca8_p17.csv',date)
v06r52b = gd.getData('23Aug2022_V06_7b3b16_p17.csv',date)
v06r52c = gd.getData('23Aug2022_V06_104e83_p17.csv',date)
v06r52d = gd.getData('23Aug2022_V06_618257_p17.csv',date)
v06r52e = gd.getData('23Aug2022_V06_5aba63_p17.csv',date)
date = '24Aug2022'
v06r57a = gd.getData('23Aug2022_V06_49f0c0_p16.csv',date)
v06r57b = gd.getData('23Aug2022_V06_98da1a_p16.csv',date)
v06r57c = gd.getData('23Aug2022_V06_4589a5_p16.csv',date)
v06r57d = gd.getData('23Aug2022_V06_e571b7_p16.csv',date)







######################              BIG SLUG                #############################

slugV04r52a = gd.getData('23Aug2022_V04_ea8794_p18.csv',date)
slugV04r52b = gd.getData('23Aug2022_V04_70b0f6_p18.csv',date)
slugV04r52c = gd.getData('23Aug2022_V04_08b421_p18.csv',date)
slugV04r52d = gd.getData('23Aug2022_V04_ea0796_p18.csv',date)



#############               3.5 spring                      #######################

springV04r52a = gd.getData('23Aug2022_V04_919533_p183.csv',date)
springV04r52b = gd.getData('23Aug2022_V04_84ef51_p185.csv',date)
springV04r52c = gd.getData('23Aug2022_V04_f783fc_p184.csv',date)

springV05r52a = gd.getData('23Aug2022_V05_ef491a_p16.csv',date)
springV05r52b = gd.getData('23Aug2022_V05_03e30b_p16.csv',date)
springV05r52c = gd.getData('23Aug2022_V05_9b9705_p16.csv',date)


date = '25Aug2022'

###############             seal vs no seal             #################

f06FlatFilla = gd.getData('25Aug2022_V06_c3a27d_p16_52.csv',date)
f06FlatFillb = gd.getData('25Aug2022_V06_b618e1_p16_52.csv',date)
f06FlatFillc = gd.getData('25Aug2022_V06_485641_p16_52.csv',date)
f06FlatFilld = gd.getData('25Aug2022_V06_499bcc_p16_52.csv',date)
f06FlatFille = gd.getData('25Aug2022_V06_2fc6e5_p16_52.csv',date)

f06FlatFillSeala = gd.getData('25Aug2022_V06_e7455a_p16_sealed.csv',date)
f06FlatFillSealb = gd.getData('25Aug2022_V06_e96707_p16_sealed.csv',date)
f06FlatFillSealc = gd.getData('25Aug2022_V06_425567_p16_sealed.csv',date)






###############                 MODEL RETRAIN F.06              ############
date = '29Aug2022'
h50 = gd.getData('h50.csv',date)
h100 = gd.getData('h100.csv',date)
h90 = gd.getData('h90.csv',date)
h70 = gd.getData('h70.csv',date)




#########################           ACCEPTANCE                          #####################
date = '13Sep2022'
# adv01_1 = gd.getData('Adv01_P23_33425e_220908_Run1.csv',date)
# adv01_2 = gd.getData('Adv01_P16_5e621f_220908_Run2.csv',date)
# adv01_3 = gd.getData('Adv01_P16_a314fa_220908_Run3.csv',date)

# adv02_1 = gd.getData('Adv2_P23_21fef3_220907_Run1.csv',date)
# adv02_2 = gd.getData('Adv2_P23_ae5298_220907_Run2.csv',date)
# adv02_3 = gd.getData('Adv2_P23_9bd409_220907_Run3.csv',date)

# adv03_1 = gd.getData('Adv3_P20_220829_Run01.csv',date)
# adv03_2 = gd.getData('Adv3_P20_220829_Run021.csv',date)
# adv03_3 = gd.getData('Adv3_P20_220829_Run033.csv',date)

# adv04_1 = gd.getData('Adv4_P20_45275f_220829_Run01.csv',date)
# adv04_2 = gd.getData('Adv4_P21_220829_Run02.csv',date)
# adv04_3 = gd.getData('Adv4_P21_220829_Run03.csv',date)







# date = '14Sep2022'
# adv01_1 = gd.getPcrData('Adv01_DV03_220907_Run1.csv',date)
# adv01_2 = gd.getPcrData('Adv01_DV03_220907_Run2.csv',date)
# adv01_3 = gd.getPcrData('Adv01_DV03_220907_Run3.csv',date)

# adv02_1 = gd.getPcrData('Adv02_DV03_220907_Run1.csv',date)
# adv02_2 = gd.getPcrData('Adv02_DV03_220907_Run2.csv',date)
# adv02_3 = gd.getPcrData('Adv02_DV03_220907_Run3.csv',date)

# adv03_1 = gd.getPcrData('Adv3_DV03_220829_Run01.csv',date)
# adv03_2 = gd.getPcrData('Adv3_DV03_220829_Run02.csv',date)
# adv03_3 = gd.getPcrData('Adv3_DV03_220829_Run03.csv',date)

# adv04_1 = gd.getPcrData('Adv4_DV09_220829_Run01.csv',date)
# adv04_2 = gd.getPcrData('Adv4_DV09_220829_Run02.csv',date)
# adv04_3 = gd.getPcrData('Adv4_DV09_220829_Run03.csv',date)









# date = '15Sep2022'
# adv10_1 = gd.getPcrData('AdvB10_PCR_091422_Run1.csv',date)
# adv10_2 = gd.getPcrData('AdvB10_PCR_091522_Run2.csv',date)

# test = gd.test('test.csv',date)

# print(test[1][-10:])



# date = '23Sep2022'

# trip = gd.getData('tripleTCa.csv',date)
"""

date = '11Oct2022'

forward1 = gd.getData('forwardNew2.csv',date)
forward2 = gd.getData('forwardNew3.csv',date)
forward3 = gd.getData('forwardNew4.csv',date)
backward1 = gd.getData('backwardNew2.csv',date)
backward2 = gd.getData('backwardNew3.csv',date)
backward3 = gd.getData('backwardsJustChan1.csv',date)
backward4 = gd.getData('backwardsJustChan2.csv',date)

noInsert1 = gd.getData('noInsertNoBall1.csv',date)
noInsert2 = gd.getData('noInsertNoBall2.csv',date)


# date = '12Oct2022'

# small11 = gd.getData('ADV11SmallSlug1.csv',date)
# large11 = gd.getData('ADV11LargeSlug2.csv',date)
# large11_mp = gd.getData('ADV11LargeSlug4.csv',date)









date = '10Nov2022'

smallA = gd.getData('Adv02_P26_DualNormal_221109_Run1.csv',date)
smallB = gd.getData('Adv02_P26_DualNormal_221109_Run2.csv',date)
largeA = gd.getData('Adv08_P26_NewModel_221108_Run1.csv',date)
largeB = gd.getData('Adv08_P26_NewModel_221108_Run3.csv',date)
obroundA = gd.getData('Adv11_P26_DualNormal_221108_Run2.csv',date)
obroundB = gd.getData('Adv11_P26_DualNormal_221108_Run3.csv',date)


backSmallA = gd.getData('backwards/Adv02_P_Dual_OldModel_221110_Run1.csv',date)
backSmallB = gd.getData('backwards/Adv02_P_Dual_OldModel_221110_Run2.csv',date)
backLargeA = gd.getData('backwards/Adv11_P_Dual_NewModel_221110_Run1.csv',date)
backLargeB = gd.getData('backwards/Adv11_P_Dual_NewModel_221110_Run2.csv',date)
backObroundA = gd.getData('backwards/Adv08_P_Dual_NewModel_221110_Run1.csv',date)
backObroundB = gd.getData('backwards/Adv08_P_Dual_NewModel_221110_Run2.csv',date)