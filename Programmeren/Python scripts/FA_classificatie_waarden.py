# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 15:12:55 2017

@author: GudjonHelgi
"""
import pandas as pd
import numpy as np
from functies import normaliseren, data_vinden
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#data = pd.read_csv("FA_test_doordeweeks_overdag.csv",sep = ";",parse_dates={"Datum en tijd(uur)":[0,1]}, index_col = 0)
#data = pd.read_csv("2.008_jul14-jul15_schoon.csv",sep = ";",parse_dates={"Datum en tijd(uur)":[0,1]}, index_col = 0)
data = pd.read_csv("D2014_Jan14-Jan15_5min_schoon.csv",sep = ";",parse_dates={"Datum en tijd(uur)":[0,1]}, index_col = 0)
geb_colom = ["bedrijfstatus","valve actual pos","temperature 0","measairflow","lampenergy","objecttemp","ambienttemp","estimatedpresence","co2","air flow pressure difference","actual air flow"]
print(data.head())
data = data_vinden(data,geb_colom)
data = normaliseren(data)
#print(data)
#Voor elk hieronder situatie zijn de volgende variabelen bekeken:
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
luchtklep_niet_open_genoeg = [0.340667, -1.930618, 2.597218, -0.232039, -0.161661, -0.259005, -0.218329, 0.341457, -0.180115, -0.041821, -0.255754]
ventilatie_hoog = [-0.153679, 0.086212, 0.205857, 1.712752, -1.607076, 0.124783, -0.290010, -0.154372, -1.534846, -0.098678, 1.709057]
warm_niet_genoeg_aan_gedaan = [-0.423698, -1.038846, -0.399998, -0.284373, -0.528429, 1.894432, 2.253440, -0.423716, -0.353045, -0.411329, -0.284437]
indicatie_gebruik_lokaal = [-0.583982, 0.892874, 2.853171, -0.609231, -0.258862, -0.128524, 0.074861, -0.583983, -0.508339, -0.538752, -0.609233]
CO2_hoog_niet_genoeg_aan_gedaan = [-0.430441, -0.430441, -0.221076, -0.417481, -0.141993, -1.101215, 1.338662, -0.430441, 2.623672, -0.371864, -0.417383]
ventilatie_duidelijk_aan_zonder_bekende_aanwezigheid = [-1.071892, -1.071860, 0.014241, 1.900021, -0.164348, -0.097071, 0.102987, -1.071892, -0.075137, -0.397026, 1.931977]

geb_situaties = [luchtklep_niet_open_genoeg,ventilatie_hoog,warm_niet_genoeg_aan_gedaan,indicatie_gebruik_lokaal,CO2_hoog_niet_genoeg_aan_gedaan,ventilatie_duidelijk_aan_zonder_bekende_aanwezigheid]

test = pd.DataFrame(data =np.transpose(np.matrix(geb_situaties)))
#print(test)
lengte = len(data)
breede = len(test.columns)
oplossing = pd.DataFrame(np.random.randint(low=0,high=1,size = (lengte,breede)),index = data.index)#(range(len(data)),range(len(FA.columns)))))

for a in range(len(data)):
    for c in range(breede):
        som = 0
        for b in range(len(data.columns)):
            som = som + data.iloc[a,b] * test.iloc[b,c]
        oplossing.iloc[a,c] = som

#print(oplossing)
fig = plt.figure(4)
ax = fig.add_subplot(111,projection="3d")

#bekijken = data.iloc[:,8] >0.4
#print(oplossing[bekijken].iloc[:,0])
#oplossingN = oplossing[bekijken]
#kleur = normaliseren(data.iloc[:,8].values.reshape(-1,1)>0.4)
kleur = (data.iloc[:,8].values.reshape(-1,1) > 0.3)

#kleur = bekijken.values.reshape(-1,1)

#ax.scatter(data.iloc[:,6],data.iloc[:,5],data.iloc[:,1], c=kleur, cmap="autumn_r")
ax.scatter((oplossing.iloc[:,0] + np.abs(np.min(oplossing.iloc[:,0]))),(oplossing.iloc[:,2] + np.abs(np.min(oplossing.iloc[:,2]))),(oplossing.iloc[:,5] + np.abs(np.min(oplossing.iloc[:,5]))),c=kleur,cmap="autumn_r" )
#ax.scatter((oplossing[kleur][0] + np.abs(np.min(oplossing[kleur][0]))), (oplossing[kleur][2] + np.abs(np.min(oplossing[kleur][2]))), (oplossing[kleur][5] + np.abs(np.min(oplossing[kleur][5]))), c='y')
ax.set_xlabel('Luchtklep stand (0 = Open)')
ax.set_ylabel('Warm in lokaal, maar weinig aan gedaan')
ax.set_zlabel("Ventilatie aan zonder bekende aanwezigheid")
ax.set_title("CO2 waarden van lokaal D2.008 tussen jul 2014 en jul 2015")
plt.show()

fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.scatter((oplossing[kleur][0] + np.abs(np.min(oplossing[kleur][0]))), (oplossing[kleur][2] + np.abs(np.min(oplossing[kleur][2]))), c='r', s = 20)
ax.set_xlabel('Luchtklep stand (0 = Open)')
ax.set_ylabel('Warm in lokaal, maar weinig aan gedaan')
ax.set_title("Hoge(onder 1000ppm) CO2 waarden van lokaal D2.008 tussen jul 2014 en jul 2015")
plt.show()

fig = plt.figure(2)
ax = fig.add_subplot(111)
ax.scatter((oplossing[kleur][0] + np.abs(np.min(oplossing[kleur][0]))), (oplossing[kleur][5] + np.abs(np.min(oplossing[kleur][5]))), c='r', s=20)
ax.set_xlabel('Luchtklep stand (0 = Open)')
ax.set_ylabel('Ventilatie aan zonder bekende aanwezigheid')
ax.set_title("Hoge(boven 1000ppm) CO2 waarden van lokaal D2.008 tussen jul 2014 en jul 2015")
plt.show()

fig = plt.figure(3)
ax = fig.add_subplot(111)
ax.scatter(oplossing[kleur][2], oplossing[kleur][5], c='y', s=20)
ax.set_xlabel('Warm in lokaal, maar niet genoeg aan gedaan')
ax.set_ylabel('Ventilatie aan zonder bekende aanwezigheid')
ax.set_title("Normale(onder 1000ppm) CO2 waarden van lokaal D2.008 tussen jul 2014 en jul 2015")
plt.show()

gevonden = oplossing[kleur]
gevonden = gevonden[(gevonden[0] > 0) & (gevonden[0] < 0.5) & (gevonden[2] > 1)  & (gevonden[5] > 0) & (gevonden[5] < 0.5)]
#gevonden = gevonden[(gevonden[0] < -0.5) & (gevonden[2] > -1) & (gevonden[2]<1) & (gevonden[5] > -0.5) & (gevonden[5] < 1)]

for a in gevonden.index:
    print(a)
#==============================================================================
# for a in range(len(oplossing)):
#     if int(oplossing.iloc[a,0]+0.2) >0:
#         print(a, "  " , oplossing.iloc[a,0])
#==============================================================================