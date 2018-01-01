# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 11:26:10 2017

@author: GudjonHelgi
"""
import pandas as pd
# meerdere waarden tegelijker tijd naar floats
def naar_float(series):
    series = pd.DataFrame(series)
    for a in range(len(series.columns)):
        for b in range(len(series)):
            series.iloc[b,a] = float(series.iloc[b,a])
    return series

# Een ruige 95% betrouwbaarheidsinterval
from scipy.stats import norm
import numpy as np
def Ckans_normaal(df, test):
    #uitkomst = pd.DataFrame(np.empty(len(test)),columns = df.columns)
    for c in range(len(df.columns)):
        gebcolom = pd.DataFrame(sorted(df.iloc[:,c].dropna(),reverse = True))
        weglaten = int(len(gebcolom)-len(gebcolom)*0.95)
        gebcolom = gebcolom.iloc[weglaten:(len(gebcolom)-weglaten)]
        mu = np.mean(gebcolom)
        std = np.std(gebcolom)
        laag = mu - 2 * std
        hoog = mu + 2*std
        print(mu, "  " , std, "  " ,laag, "  " ,hoog, "  " , df.columns[c])
        test = pd.DataFrame(test)
        for a in range(len(test)):
            test.iloc[a,c] = norm(mu,std).cdf(test.iloc[a,c])
    return test

# min/max normalisatie
def normaliseren(data):
    data = pd.DataFrame(data)
    for b in range(0,len(data.columns)):
        verschil = data.iloc[:,b].max()-data.iloc[:,b].min()
        if verschil >0:
            data.iloc[:,b] = (data.iloc[:,b]-data.iloc[:,b].min())/verschil
    return data

# selectief data kiezen op basis van gegeven lijst aan colommen
def data_vinden(data, geb_colommen): 
    hoeveel_data = [0] * len(geb_colommen)
    geb_data = pd.DataFrame(index = data.index, columns = geb_colommen).fillna(value = 0)
    for colom in data.columns:
        if data[colom].count() < (len(data) / 2):
            data.drop(colom, axis = 1)
        else:
            colomN = colom.replace(" ","").lower()
            for a in range(len(geb_colommen)):
                if geb_colommen[a] in colomN:
                    geb_data.iloc[:,a] = ((geb_data.iloc[:,a]*hoeveel_data[a]) + data.iloc[:,data.columns.get_loc(colom)]) / (hoeveel_data[a]+1)
                    hoeveel_data[a] = hoeveel_data[a] + 1
    for b in geb_data.columns:
        if geb_data[b].max() == geb_data[b].min():
            geb_data.drop(b,axis = 1)
    
    return geb_data
