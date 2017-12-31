# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("d2008apr-jun2015_geen_data_redundantie.xlsx")

data1 = pd.read_csv("d2008apr-jun2015.csv",sep=";")

data1["2.008 (B2.06a) Spreekkamer-CO2 Level  OG0B3B {307351} average"] = pd.to_numeric(data1["2.008 (B2.06a) Spreekkamer-CO2 Level  OG0B3B {307351} average"].str.replace(",","."))

co2 = data1["2.008 (B2.06a) Spreekkamer-CO2 Level  OG0B3B {307351} average"]

temp_a = data1["2.008 (B2.06a) Spreekkamer-Temperature 0 OG0221 {55374} average"]

i = data1["Datum (dd/MMM/yy)"]

co2_verschil=[]

#print(co2.describe())
b=0
for a in co2:
    c=a-b
    b=a
    co2_verschil.append(c)

co2_verschil = pd.DataFrame(co2_verschil)
print(co2_verschil.describe())
aha=co2_verschil>co2_verschil.std()*2
aha = aha.as_matrix()
print(data[aha])

#print(data1["2.008 (B2.06a) Spreekkamer-CO2 Level  OG0B3B {307351} average"].describe())
#print(data1.info())
#plt.scatter(i,co2)
#plt.show()