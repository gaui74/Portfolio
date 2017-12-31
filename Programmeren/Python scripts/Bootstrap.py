# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 15:18:49 2017

@author: GudjonHelgi
"""

import numpy as np

def bootstrap(data, num_samples, alpha):
    """Returns bootstrap estimate of 100.0*(1-alpha) CI for statistic."""
    n = len(data)
    print(n)
    tot_matrix = []
    for i in range(num_samples):
        idx = np.random.randint(0,n,n)
        print(idx)
        matrix = data[idx]
        print(matix)
#==============================================================================
#         eigenw=np.linalg.eig(matrix)[0]
#         tot_matrix = tot_matrix + eigenw
#         print(tot_matrix)
#==============================================================================
    
    
#==============================================================================
#     idx = np.random.randint(0, n, (num_samples, n))
#     samples = data[idx]   
#     stat = np.sort(statistic(samples, 1))
#     return (stat[int((alpha/2.0)*num_samples)],
#             stat[int((1-alpha/2.0)*num_samples)])
#==============================================================================
