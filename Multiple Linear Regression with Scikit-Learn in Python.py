# -*- coding: utf-8 -*-
"""
Created on Thu May  6 01:56:48 2021

@author: abc
"""

#Multiple Linear Regression 

#In linear regression we work with one independent variable
#But in Multiple regression we work with multiple independent variable

# In linear for example : Y= MX + C  (One independent variable)

# In above equation M is our one independent variable and in multiple linear regression
# there more variables like M

# In Multiple linear regression there are some variables are also dependent


#Step : 1 import dataset
import pandas as pd

df = pd.read_excel('images_analyzed.xlsx')
print(df.head())


#Step : 2 Plot this dataset 

import seaborn as sns
sns.lmplot(x='Time', y='Images_Analyzed',data=df, hue='Age')
sns.lmplot(x='Coffee', y='Images_Analyzed', data=df, hue='Age')

#############################################################################
# Multiple Linear Regression concept

import pandas as pd

df = pd.read_excel('images_analyzed.xlsx')

import numpy as np
from sklearn import linear_model

#step : 1 Create an linear object

reg = linear_model.LinearRegression()

#Step : 2 Fit our dataset
#here x is Time,Coffee and Age are independent variable
# And y is Images_Analyzed it is dependent variable          
reg.fit(df[['Time', 'Coffee', 'Age']], df.Images_Analyzed)  

#Step : 3 Predict our dataset

print(reg.coef_)
print(reg.predict([[13,2,23]]))


                                                            






 

