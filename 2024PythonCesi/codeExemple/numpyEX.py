# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 18:13:56 2022

@author: droch
"""
import numpy as np

pays = np.array([ 
    ['France', 'Angleterre', 'Allemagne'], #Nom pays
    [70, 55, 85],                          #Population en millions
    [0.901, 0.922, 0.936],                 #IDH indice de developpement humain
    [2091,2077,3045]                       #PIB
])
print(pays)

# afficher la population en millions

# afficher la population en millions pour l'Angleterre

# afficher toutes les infos de l'Angleterre

# afficher tout sauf le nom des pays



dataPays = pays[1:,:] 

# essayer la ligne suivante
#dataPays[1,1] - 1

# essayer alors la ligne suivante
dataPays = dataPays.astype(float)
dataPays[1,1] - 1
print(dataPays)

#la ligne suivante améliore l'affichage
np.set_printoptions(suppress=True)
print(dataPays)

# usage des fonctions sum(), min(), max, mean()

# réaliser la somme des éléments de dataPays


# somme des PIB


# min, max, moyenne des PIB

# l'index du plus haut pib utiliser argmax()


# le nom du pays correspondant


# arange 

# définir une liste de 1 à 100 non compris par pas de 2


# linspace
# définir une graduation de 0 à 1 par pas de 0.1

