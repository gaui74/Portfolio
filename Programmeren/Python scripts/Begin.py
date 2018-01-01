# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import FactorAnalysis
from Varimax import ortho_rotation as rotatie
from functies import data_vinden, normaliseren
import seaborn as sns

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
#==============================================================================
                # Code voor verbanden tussen variabelen bekijken met behulp van een heatmap
# corrmat = data.corr() 
# 
# f, ax = plt.subplots(figsize=(12, 9))
# ax = sns.heatmap(corrmat, vmax=.8, square=True, xticklabels = colommen, yticklabels = colommen)
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 60)
# ax.set_yticklabels(ax.get_yticklabels(), rotation = 0)
#==============================================================================

#==============================================================================
                # poging tot date-time verwerken->werkte niet
# for a in range(len(data)):
#     data.iloc[a,1]=int(data.iloc[a,1][:2] + data.iloc[a,1][3:5] + data.iloc[a,1][6:8]) / 100
#==============================================================================

#==============================================================================
                # Voorereidende stappen voor de factor analyse. Hieruit wordt doormiddel van meerdere methoden het aantal factoren gevonden
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

