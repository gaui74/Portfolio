# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 12:22:17 2017

@author: GudjonHelgi
"""
import pandas as pd
from sklearn.linear_model import Lasso
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

filenames = ["2.008_jul12-jul13_schoon.csv","2.008_jul13-jul14_schoon.csv","2.008_jul14-jul15_schoon.csv","2.008_jul15-apr16_schoon.csv"]
combined_csv = pd.concat( [ pd.read_csv(f,sep=";",parse_dates={"Datum en tijd(uur)":[0,1]}, index_col = 0) for f in filenames ] ).dropna()

x= combined_csv.drop("2.008 (B2.06a) Spreekkamer-CO2 Level  OG0B3B {307351} average",axis = 1)
y= round(combined_csv["2.008 (B2.06a) Spreekkamer-CO2 Level  OG0B3B {307351} average"]/250)*250
print(y)

X_train, y_train, X_test, y_test = train_test_split(x, y, test_size = 0.3, stratify = y)

lasso = Lasso(alpha = 0.1)
#lasso.fit(X_train,y_train)
#lasso_pred = lasso.predict(X_test)
#print(lasso.score(X_test,y_test))

lasso_coeff = lasso.fit(x,y).coef_
print(lasso_coeff)
#_ = plt.plot(range(len(x.columns)),lasso_coeff)
#_ = plt.xticks(range(len(x.columns)),x.columns, rotation = 90)
#_ = plt.ylabel("Coefficients")
#plt.show()

