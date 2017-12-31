# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 11:06:09 2017

@author: GudjonHelgi
"""
import pandas as pd
import numpy as np
from functies import normaliseren
#==============================================================================
# from functies import naar_float, Ckans_normaal
# import time
# from scipy.stats import norm
# import matplotlib.pyplot as plt
# import statsmodels.stats.api as sms
#==============================================================================

#data = pd.read_csv("FA_test.csv",sep = ";", parse_dates = {"Datum en tijd(uur)":[0,1]},index_col = 0)
#data = pd.read_csv("Schoonmaken_v1.3.csv",sep=";",parse_dates={"Datum en tijd(uur)":[0,1]}, index_col = 0)
data = pd.read_csv("FA_test_doordeweeks_overdag.csv",sep = ";", parse_dates = {"Datum en tijd(uur)":[0,1]},index_col = 0)
#print(np.transpose(data.iloc[4598,range(len(data.columns))],axes=0))
#filenames = ["2.008_jul12-jul13_schoon.csv","2.008_jul13-jul14_schoon.csv","2.008_jul14-jul15_schoon.csv","2.008_jul15-apr16_schoon.csv"]
#combined_csv = pd.concat( [ pd.read_csv(f,sep=";",parse_dates={"Datum en tijd(uur)":[0,1]}, index_col = 0) for f in filenames ] )
#print(combined_csv["07:00"])
#data = normaliseren(data)
oplossing = pd.DataFrame(index = data.columns, columns = ["Laag","Hoog"])

for a in range(len(data.columns)):
    gem = np.mean(data.iloc[:,a])
    laag = gem - gem*0.2
    hoog = gem + gem*0.8
    oplossing.iloc[a,0] = laag
    oplossing.iloc[a,1] = hoog
print(oplossing)
    
#==============================================================================
# colommen = ["high flow value", "low flow value", "Flow while PIR=0", "Flow frozen", "high CO2 value", "low CO2 value", "CO2_frozen", "CO2_neighbours non-identical", "PIR NaN"]
# uitkomst = pd.DataFrame(index = data.index, columns = colommen)
# 
# high_flow = data.iloc[:,10].max() * 0.8
# low_flow = data.iloc[:,10].min() * 1.2
# high_co2 = data.iloc[:,8].max() * 0.8
# low_co2 = data.iloc[:,8].min() * 1.2
# 
# for a in range(len(data)):
#     if data.iloc[a,10] > high_flow:
#         uitkomst.iloc[a,0] = 1
#     else:
#         uitkomst.iloc[a,0] = 0
#     
#     if data.iloc[a,10] < low_flow:
#         uitkomst.iloc[a,1] = 1
#     else:
#         uitkomst.iloc[a,1] = 0
#     
#     if data.iloc[a,10] > 0 and data.iloc[a,7] == 0:
#         uitkomst.iloc[a,2] = 1
#     else:
#         uitkomst.iloc[a,2] = 0
#     
#     std = np.std(data.iloc[range(a-20,a+20),10])
#     if std == 0:
#         uitkomst.iloc[a,3] = 1
#     else:
#         uitkomst.iloc[a,3] = 0
#     
#     if data.iloc[a,8] > high_co2:
#         uitkomst.iloc[a,4] = 1
#         uitkomst.iloc[a,5] = 0
#     elif data
#         uitkomst.iloc[a,4] = 0
#==============================================================================
    
    
    
    





























#print(combined_csv)
#uitkomst = Ckans_normaal(combined_csv,data.iloc[[4598,4599,4600],range(len(data.columns))])
#print(uitkomst)
#==============================================================================
# print(combined_csv.columns[20])
# print(combined_csv.shape)
# print(sms.DescrStatsW(combined_csv.iloc[:,20].dropna()).tconfint_mean())
#==============================================================================
#==============================================================================
# print(combined_csv.iloc[:,6].shape)
# print(combined_csv.iloc[:,6].describe())
# aanwezig = combined_csv.iloc[:,19]==1
# combined_csv = combined_csv[aanwezig]
# print(aanwezig)
# for i in range(len(combined_csv.columns)):
#     plt.hist(combined_csv.iloc[:,i].dropna(),bins = 100)
#     plt.title(combined_csv.columns[i])
#     plt.show()
#==============================================================================

