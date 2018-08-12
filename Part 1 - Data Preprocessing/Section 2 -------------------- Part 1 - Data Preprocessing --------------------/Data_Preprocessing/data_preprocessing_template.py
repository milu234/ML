#import the librarires
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Get the dataset 
dataset = pd.read_csv('Data.csv')
X  = dataset.iloc[:,:-1].values 
Y = dataset.iloc[:,3].values

#Enter the values of the missing table using the meanof that column
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN',strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])


#Encoding /categorical data

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])

onehotencoder =  OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()


labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)

