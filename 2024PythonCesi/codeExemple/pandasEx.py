# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 21:55:49 2022

@author: droch
"""

produitsDict = {
    'smartphone':{'prix':1000,'enStock':True},
    'chaussures':{'prix':100,'enStock':False},
    'console':{'prix':400,'enStock':True}
}
print(produitsDict)
print

import pandas as pd

# dataframe à partir d'un dictionnaire
df = pd.DataFrame(produitsDict)

print(df)
print

# dataframe à partir d'une liste

pays = [
    [70, 55, 85],                          #Population en millions
    [0.901, 0.922, 0.936],                 #IDH
    [2091,2077,3045]                       #PIB
]
df = pd.DataFrame(pays, columns=['France','Angleterre','Allemagne'])

print(df)
print

#dataframe à partir d'un fichier
data = pd.read_csv('metal_bands_2017.csv',encoding='latin-1', sep=';')
print.data.head()