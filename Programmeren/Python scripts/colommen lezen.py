# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 10:13:17 2017

@author: GudjonHelgi
"""
import pandas as pd

data = pd.read_csv("FA_test_doordeweeks_overdag.csv",sep = ";",parse_dates={"Datum en tijd(uur)":[0,1]}, index_col = 0)
geb_colommen = ["temperature 0", "measair", "estimatedpresence", "co2", "actual air"]
hoeveel_data = [0] * len(geb_colommen)
geb_data = pd.DataFrame(index = data.index, columns = geb_colommen).fillna(value = 0)

#==============================================================================
# for colom in data.columns:
#     #print(data.iloc[:,data.columns.get_loc(colom)])
#     if geb_colommen[3] in colom.lower():
#         geb_data .iloc[:,3] = (((geb_data.iloc[:,3] * hoeveel_data[3]) + data.iloc[:,data.columns.get_loc(colom)]) / (hoeveel_data[3] + 1))
#         hoeveel_data[3] =+ 1
#     elif "temperature 0" in colom.lower():
#         geb_data.iloc[:,0] = (geb_data.iloc[:,0]*hoeveel_data[0] + data.iloc[:,data.columns.get_loc(colom)]) / (hoeveel_data[0]+1)
#         hoeveel_data[0] =+ 1
#     elif "measairflow" in colom.lower():
#         geb_data.iloc[:,1] = (geb_data.iloc[:,1]*hoeveel_data[1] + data.iloc[:,data.columns.get_loc(colom)]) / (hoeveel_data[1]+1)
#         hoeveel_data[1] =+ 1
#     elif "estimatedpresence" in colom.lower():
#         geb_data.iloc[:,2] = (geb_data.iloc[:,2]*hoeveel_data[2] + data.iloc[:,data.columns.get_loc(colom)]) / (hoeveel_data[2]+1)
#         hoeveel_data[2] =+ 1
#     elif "actual air flow" in colom.lower():
#         geb_data.iloc[:,4] = (geb_data.iloc[:,4]*hoeveel_data[4] + data.iloc[:,data.columns.get_loc(colom)]) / (hoeveel_data[4]+1)
#         hoeveel_data[4] =+ 1
# print(geb_data)
#==============================================================================

for colom in data.columns:
    for a in range(len(geb_colommen)):
        if geb_colommen[a] in colom.lower():
            geb_data.iloc[:,a] = (geb_data.iloc[:,a]*hoeveel_data[a] + data.iloc[:,data.columns.get_loc(colom)]) / (hoeveel_data[a]+1)
            hoeveel_data[a] =+ 1
print(geb_data)