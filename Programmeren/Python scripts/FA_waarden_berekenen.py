# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 11:32:55 2017

@author: GudjonHelgi
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import FactorAnalysis
from functies import data_vinden, normaliseren
import seaborn as sns
import math 
from mpl_toolkits.mplot3d import Axes3D
import csv

#print(data.head())
#print(data.iloc[17473:17600,2])
#data = pd.read_csv("D2008jul2014jul2015-6min_schoon_overdag.csv",sep = ";",parse_dates={"Datum en tijd(uur)":[0,1]}, index_col = 0)
data = pd.read_csv("D2014jan2014jan2015hour_schoon_overdag_TEST.csv",sep = ";",parse_dates={"Datum en tijd(uur)":[0,1]}, index_col = 0)
#data = pd.read_csv("Test.csv",sep = ";",parse_dates={"Datum en tijd(uur)":[0,1]}, index_col = 0)
#data = pd.read_csv("D2014_Jan14-Jan15_5min_schoon_.csv",sep = ";",parse_dates={"Datum en tijd(uur)":[0,1]}, index_col = 0)
colommen = ["bedrijfsstatus","valve","temperature0","temperature1","energysupplycool","energysupplyheat","measairflow","lampenergy","objecttemp","waterflow","ambienttemp","presence","co2","airflowpressuredifference","actualairflow"]
data = normaliseren(data_vinden(data,colommen))

#==============================================================================
# print(data.describe())
# for a in range(len(data)):
#     if data.iloc[a,2] == 0:
#         print(a)
#==============================================================================
        
for a in range(len(data.columns)):
    print(data.iloc[:,a].count(), len(data.iloc[:,a]))

#print(data.iloc[6216,:])
data = data.dropna()
print(data.shape)
data = data_vinden(data,colommen)
#print(data.head())
#data = normaliseren(data)

FA = FactorAnalysis(n_components = 5).fit_transform(np.transpose(data))
FA = np.transpose(pd.DataFrame(FA,index=data.columns))

lengte = len(data)
breede = len(FA)
print(breede)
oplossing = pd.DataFrame(np.random.randint(low=0,high=1,size = (lengte,breede)),index = data.index)

for a in range(lengte):
    for c in range(breede):
        som = 0
        for b in range(len(data.columns)):
            som = som + data.iloc[a,b] * FA.iloc[c,b]
        oplossing.iloc[a,c] = som

print(np.transpose(FA))

oplossing1 = oplossing[oplossing.iloc[:,1]>1]
#oplossing1 = oplossing[kleur]

fig = plt.figure(2)
ax = fig.add_subplot(111)#,projection='3d')
kleur = data['co2'].values.reshape(-1,1) > 0.247
#ax.scatter(oplossing[0],oplossing[2],oplossing[1])
ax.set_xlabel('FA 2')
ax.set_ylabel('FA 3')
ax.set_zlabel("FA 1")
ax.scatter(oplossing[4], oplossing[2],c='r')
plt.show()

fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.scatter(oplossing[kleur][1], oplossing[kleur][2])
plt.show()

gevonden = oplossing
gevonden = gevonden[ (gevonden[2] > -1) & (gevonden[2] < 0)]
#gevonden = gevonden[(gevonden[2] - gevonden[4] >3)]
#gevonden = gevonden[(gevonden[0] >-1) & (gevonden[0] <0) & (gevonden[1] < 3.5) & (gevonden[1] > 1) ]

bla = []
for a in gevonden.index:
    bla.append(a)
    
print(bla)

# screeplot
eigenwaarden = sorted(np.linalg.eig(pd.DataFrame(np.cov(data.astype(float),rowvar = False)))[0],reverse = True)
print(eigenwaarden)
plt.plot(eigenwaarden).show()

cluster = pd.concat([oplossing[kleur][1], oplossing[kleur][2]],axis = 1)
print(cluster)

cluster.to_csv("cluster.csv", sep=";")

#==============================================================================
# corrmat = data.corr()
# 
# f, ax = plt.subplots(figsize=(12, 9))
# ax = sns.heatmap(corrmat, vmax=.8, square=True, xticklabels = [data.columns], yticklabels = [data.columns])
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)
# ax.set_yticklabels(ax.get_yticklabels(), rotation = 0)
#==============================================================================


