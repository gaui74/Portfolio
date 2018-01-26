# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 12:08:13 2017

@author: GudjonHelgi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.cluster as cluster
import time
import hdbscan

sns.set_context('poster')
sns.set_color_codes()
plot_kwds = {'alpha' : 0.25, 's' : 80, 'linewidths':0}

data = pd.read_csv("cluster.csv",index_col = 0, sep = ";")
print(data)

#Functie voor het weergeven van resultaten, vanuit verschillende cluserherkenning methoden
#Deze functie is niet zelf geschreven.
def plot_clusters(data, algorithm, args, kwds):
    start_time = time.time()
    labels = algorithm(*args, **kwds).fit_predict(data)
    end_time = time.time()
    palette = sns.color_palette('deep', np.unique(labels).max() + 1)
    colors = [palette[x] if x >= 0 else (0.0, 0.0, 0.0) for x in labels]
    plt.scatter(data.iloc[:,0], data.iloc[:,1], c=colors, **plot_kwds)
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    frame.axes.get_yaxis().set_visible(False)
    plt.title('Clusters found by {}'.format(str(algorithm.__name__)), fontsize=24)
    plt.text(-0.5, 0.7, 'Clustering took {:.2f} s'.format(end_time - start_time), fontsize=14)


plot_clusters(data, cluster.KMeans, (), {'n_clusters': 5})
plot_clusters(data, cluster.AffinityPropagation, (), {'preference':-5.0, 'damping':0.95})
plot_clusters(data, cluster.SpectralClustering, (), {'n_clusters':4})
plot_clusters(data, cluster.AgglomerativeClustering, (), {'n_clusters':4, 'linkage':'ward'})
plot_clusters(data, cluster.DBSCAN, (), {'eps':0.25})
plot_clusters(data, hdbscan.HDBSCAN, (), {'min_cluster_size':300})

haha = pd.DataFrame(hdbscan.HDBSCAN(300).fit(data).labels_,index = data.index)
data1 = pd.concat([data, haha], axis = 1)

print(data1[data1.iloc[:,2] == 0])

