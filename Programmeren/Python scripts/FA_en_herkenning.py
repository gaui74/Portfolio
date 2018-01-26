# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:53:15 2017

@author: GudjonHelgi
"""

import pandas as pd
import numpy as np
from sklearn.decomposition import FactorAnalysis
from functies import data_vinden, normaliseren
import hdbscan
import sklearn.cluster as cluster

lijst = ["D2014jan2014jan2015hour_schoon_overdag_TEST", "D2008jul2014jul2015-6min_schoon_overdag"]
for a in lijst:
    
    #Data inlezen
    file = a
    data = pd.read_csv((file + ".csv"),sep = ";",parse_dates={"Datum en tijd(uur)":[0,1]}, index_col = 0)
    colommen = ["bedrijfsstatus","valve","temperature0","temperature1","energysupplycool","energysupplyheat","measairflow","lampenergy","objecttemp","waterflow","ambienttemp","presence","co2","airflowpressuredifference","actualairflow"]
    data = normaliseren(data_vinden(data,colommen))
    data = data.dropna()
    
    #Factor analyse
    FA = FactorAnalysis(n_components = 5).fit_transform(np.transpose(data))
    FA = np.transpose(pd.DataFrame(FA,index=data.columns))
    
    #FA waarden berekenen per datarij
    lengte = len(data)
    breede = len(FA)
    oplossing = pd.DataFrame(np.random.randint(low=0,high=1,size = (lengte,breede)),index = data.index)
    for a in range(lengte):
        for c in range(breede):
            som = 0
            for b in range(len(data.columns)):
                som = som + data.iloc[a,b] * FA.iloc[c,b]
            oplossing.iloc[a,c] = som
    
    # Data filteren op basis van hoge CO2
    select = data['co2'].values.reshape(-1,1) > 0.25
    oplossing = oplossing[select]
    lengte = len(oplossing)
    breede = np.sum(range(len(FA.index)))
    clusters = pd.DataFrame(index = oplossing.index)
    
    #Clusters maken per 2 FA's
    for a in range(len(FA-1)):
        for b in range((a+1),len(FA)):
            geb_data = pd.concat([oplossing.iloc[:,a], oplossing.iloc[:,b]],axis = 1)
            labels = pd.DataFrame(hdbscan.HDBSCAN(300).fit(geb_data).labels_,index = geb_data.index,)
            aantal = str(labels.max() +1)
            labels.columns = ["clusters: " + aantal[5]]
            data1 = pd.concat([geb_data, labels], axis = 1)
            clusters = pd.concat([clusters, data1],axis = 1)
    
    print(clusters)
    clusters.to_csv((file + "_clusters.csv"), sep=";")
    
