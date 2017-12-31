# -*- coding: utf-8 -*-
"""
RAW .csv file to Rule .csv file
"""
import pandas as pd

TempRule = {"Normaal": [19, 23]}
PIRRule = {"Constant": [0.5, 1]}
CO2Rule = {"Normaal": [0, 1299], "Hoog": [1300, 1999], "Extreem": [2000], "Constant": 3}
AirRule = {"GoedeErvaring": [0, 0.15]}
#OccRule = {"NietAanwezig": 0, "Aanwezig": 1}

Readfile = "d2008apr-jun2015_MINIMALEDATA (2).csv"
Writefile = Readfile[:-4] + "_RULE" + Readfile[-4:]

RAWbestand = pd.read_csv(Readfile, sep = ";",index_col=0)

print(RAWbestand.info())
print(RAWbestand.head())

#==============================================================================
# for i in range(15840):
#     #j = RAWbestand.iloc[i,4]
#     RAWbestand.iloc[i,3] = float(RAWbestand.iloc[i,3].replace(",","."))
#     RAWbestand.iloc[i,2] = float(RAWbestand.iloc[i,2].replace(",","."))
#==============================================================================
    #print(j)
    #if type(float(RAWbestand.iloc[i,4])) == float :
        #print(RAWbestand.iloc[i,4])
#print(RAWbestand["2.008 (B2.06a) Spreekkamer-CO2 Level  OG0B3B {307351} average"])
#print(RAWbestand["Datum (dd/MMM/yy)"]+RAWbestand["Tijd"])

print("Bezig met bewerken...")    
for column in range(0, len(RAWbestand.columns)):
    for row in range(0, len(RAWbestand)):
        if column == 0:     #B
            if RAWbestand.iloc[row, column] in range(TempRule["Normaal"][0], TempRule["Normaal"][1]+1):
                RAWbestand.iloc[row, column] = 0
            else:
                RAWbestand.iloc[row, column] = 1
        if column == 1:     #C
            if RAWbestand.iloc[row, column]:
                RAWbestand.iloc[row, column] = 1
            else:
                RAWbestand.iloc[row, column] = 0
        if column == 2:     #D
            if RAWbestand.iloc[row, column] in range(CO2Rule["Normaal"][0], CO2Rule["Normaal"][1]+1):
                RAWbestand.iloc[row, column] = 0
            elif RAWbestand.iloc[row, column] in range(CO2Rule["Hoog"][0], CO2Rule["Hoog"][1]+1):
                RAWbestand.iloc[row, column] = 1
            else:
                RAWbestand.iloc[row, column] = 2
        if column == 3:     #E
            if float(RAWbestand.iloc[row, column]) > AirRule["GoedeErvaring"][1]:
                RAWbestand.iloc[row, column] = 1
            else:
                RAWbestand.iloc[row, column] = 0
        if column == 4:     #F
            if RAWbestand.iloc[row, column]:
                RAWbestand.iloc[row, column] = 0
            else:
                RAWbestand.iloc[row, column] = 1

print("Eerste vijf regels:")
print(RAWbestand.head())
RAWbestand.to_csv(Writefile)
