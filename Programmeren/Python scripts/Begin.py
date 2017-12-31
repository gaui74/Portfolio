# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import FactorAnalysis
from Varimax import ortho_rotation as rotatie
from functies import data_vinden, normaliseren
import seaborn as sns

#data = pd.read_csv("SportData.csv",sep=";")
#data = pd.read_csv("overlast.csv",sep=";")
#data = pd.read_csv("Schoonmaken_v1.1.csv",sep=";",parse_dates = {"Datum en tijd(uur)" : [0,1]}, index_col = 0)
#data = pd.read_csv("FA_test_doordeweeks_overdag.csv",sep = ";",parse_dates={"Datum en tijd(uur)":[0,1]}, index_col = 0)
data = pd.read_csv("D2008jul2014jul2015-6min_schoon_overdag.csv",sep = ";",parse_dates={"Datum en tijd(uur)":[0,1]}, index_col = 0).dropna()
colommen = ["bedrijfsstatus","valve","temperature 0", "measairflow","lampenergy","objecttemp","ambienttemp","presence","co2","air flow pressure difference","actual air flow"]
# 0: Bedrijfstatus
# 1: Luchtklep
# 2: Temp0
# 3: measAirFlow
# 4: lampEnergie
# 5: ObjTemp
# 6: AmbTemp
# 7: aanwezigheid
# 8: Co2
# 9: Airflow difference
# 10: Actual airflow 
data = normaliseren(data_vinden(data,colommen))
#data = normaliseren(data)
#==============================================================================
# corrmat = data.corr()
# 
# colommen = ["bedrijfsstatus","valve","temperature 0", "measairflow","lightstate","objecttemp","lampenergy","ambienttemp","voltage switch","presence","co2","airflow diff","actualdim","actual airflow"]
# 
# 
# f, ax = plt.subplots(figsize=(12, 9))
# ax = sns.heatmap(corrmat, vmax=.8, square=True, xticklabels = colommen, yticklabels = colommen)
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 60)
# ax.set_yticklabels(ax.get_yticklabels(), rotation = 0)
#==============================================================================
#print(data.iloc[:,0],"  " , data.iloc[:,1])
#data = data.iloc[960:1920,:]  #week 2
#data = data.iloc[1920:2880,:] #week 3
#data = data.iloc[2880:3840,:] #week 4
#data = data.iloc[3840:4800,:] #week 5

#==============================================================================
# for a in range(len(data)):
#     if a < len(data):
#         data.iloc[a,4] = data.iloc[a,4] - data.iloc[a+1,4]
#         print(data.iloc[a,4], "  " , a)
#==============================================================================
#==============================================================================
# for a in range(len(data)):
#     data.iloc[a,1]=int(data.iloc[a,1][:2] + data.iloc[a,1][3:5] + data.iloc[a,1][6:8]) / 100
#==============================================================================
#data1 = data
#data = data.iloc[0:1679,:] #week 1
#data = data.iloc[960:1920,:]  #week 2
#data = data.iloc[1920:2880,:] #week 3
#data = data.iloc[2880:3840,:] #week 4
#data = data.iloc[3840:4800,:] #week 5
#==============================================================================
#     if data.iloc[:,b].max() < verschil:
#         data1 = pd.concat([data1, np.abs(data.iloc[:,b]/data.iloc[:,b].max())],axis = 1)
#     elif data.iloc[:,b].min() < -1:
#         data1 = pd.concat([data1,np.abs(data.iloc[:,b]/data.iloc[:,b].min())],axis = 1)
#     else:
#         data1 = pd.concat([data1, data.iloc[:,b]],axis=1)
#==============================================================================
    #data1 = pd.concat([data1,np.log(np.abs(data.iloc[:,b])+1)],axis=1)
    #print(data1.iloc[:,b].head())
#==============================================================================
# covar_matrix = pd.DataFrame(np.cov(data.astype(float),rowvar = False))          #covariantiematrix maken
# #for b in range(len(covar_matrix.columns)):
#     #print(covar_matrix.iloc[:,b].head())
# #print(covar_matrix)
# eigen_values = np.linalg.eig(covar_matrix)[0]
# eigen_values = sorted(eigen_values,reverse = True)  #sorteren van hoog naar laag
# #print(eigen_values)
# totvar = np.sum(eigen_values)                       #variaties sommeren
# #print(totvar)
# std = np.sqrt(eigen_values)                         #standarddeviaties berekenen
# #print(std)
# propvar = (eigen_values/totvar)                     #proportie van variatie per element ten opzichte van totaal variatie
# #print(propvar)
# cumpropvar = np.cumsum(propvar)                     #propvar cumulatief opsommen
# #print(cumpropvar)
# factoren1 = sum(i<0.8 for i in cumpropvar)          #Aantal factoren gebaseerd op p=0.6(variatiecriterium)
# #print(factoren1)
# factoren2 = sum(i>1 for i in eigen_values)          #aantal factoren gebaseerd op Kaiser
# #print(factoren2)
# plt.plot(eigen_values)                              #Screeplot geeft overduidelijk 3 factoren weer
# plt.show()
#==============================================================================


#FA = FactorAnalysis(n_components = 3).fit(data)
#FA = pd.DataFrame(FA.components_)
#print(np.transpose(FA))
#print(rotatie(np.transpose(FA)))
FA = FactorAnalysis(n_components = 8).fit_transform(np.transpose(data))
FA = pd.DataFrame(FA,index=colommen)
print(FA)
#print(rotatie(FA))

#print(data.iloc[:,0])
#print(FA.iloc[:,0])
#print(np.transpose(data.iloc[0,:]))
#print(np.transpose(data.iloc[0,:]) * FA.iloc[:,0])
#oplossing = np.multiply(data, FA)
#print(oplossing)

                #Data vermenigvuldigen met FA
#########################################################################################
#data = data1

#==============================================================================
# lengte = len(data)
# breede = len(FA.columns)
# oplossing = pd.DataFrame(np.random.randint(low=0,high=1,size = (lengte,breede)),index = data.index)#(range(len(data)),range(len(FA.columns)))))
# for a in range(lengte):
#     for c in range(breede):
#         som = 0
#         for b in range(len(data.columns)):
#             som = som + data.iloc[a,b] * FA.iloc[b,c]
#         oplossing.iloc[a,c] = round(som)
# 
# #==============================================================================
# # for a in range(int(len(oplossing)/2),len(oplossing)):
# #     print(a+2880,"  ",oplossing.iloc[a,3]>0)
# #==============================================================================
# #print(oplossing[oplossing.iloc[:,3] > 1])
# for a in range(int(len(oplossing)/2)):
#     print(a+3840,"  ",oplossing.iloc[a,2]>0)
#==============================================================================
#==============================================================================
# for b in range(len(oplossing)):
#     if oplossing.iloc[b,3] > 0: 
#         print(oplossing.iloc[b,:])
#==============================================================================
#==============================================================================
# for a in range(6):
#     for b in range(24):
#         if FA[b][a]<1 and FA[b][a]>-1:
#             FA[b][a]=0
#==============================================================================
#print(np.transpose(FA))
#haha = FA.fit_transform(np.transpose(data))
#print(pd.DataFrame(np.transpose(FA.components_)))

#==============================================================================
# FA = FactorAnalysis(n_components = 6).fit(np.transpose(data1.iloc[:,2:]))
# print(pd.DataFrame(FA.components_))
#==============================================================================
