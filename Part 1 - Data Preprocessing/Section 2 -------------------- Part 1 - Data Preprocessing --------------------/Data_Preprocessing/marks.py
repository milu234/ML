#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 10:21:18 2018

@author: milan
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('marks.csv')
X  = dataset.iloc[:,:+27].values 
Y = dataset.iloc[:,4].values

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN',strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:27])
X[:, 1:27] = imputer.transform(X[:, 1:27])
df = pd.DataFrame(X)


#df.to_excel('marks.xlsx', sheet_name='marks', index=True) for Exporting marks into Excel