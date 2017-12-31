# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 14:08:35 2017

@author: GudjonHelgi
"""
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Schoonmaken_v1.1.csv",sep = ";")
#data["Tijd"] = pd.to_datetime(data.iloc[:,1],format = "%H:%M:%S")
print(data["Tijd"])

plt.scatter(data.index,data[data.iloc[:,21]>0,22])
plt.show()
