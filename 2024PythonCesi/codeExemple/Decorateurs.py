# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 15:16:02 2022

@author: droch
"""

"""
Les décorateurs
Ce terme regroupe 2 notions distinctes en python :

- le design pattern qui permet d'ajouter des fonctionnalités à une fonction
- des annotations (terme Java) pour augmenter la définition d'une classe

"""

# décorateur au sens du design pattern
#%%

# principes utilisés 
# principe 1
# Une fonction peut être mise dans une variable (une fonction est à considérer comme un objet). 
# La variable permet ensuite d’exécuter la fonction.
# Exemple :
def sumab(a,b):
    summed = a + b
    print(summed)

maFonction=sumab
maFonction(5,3) # affiche 8

#%%

# Principe 2 : Une fonction peut retourner une fonction 
# Principe 3 : Une définition de fonction peur contenir une définition de fonction
def pretty_sumab(func):
    def inner(a,b):
        print(str(a) + " + " + str(b) + " fait ", end="")
        func(a,b)
        return
    return inner

# La fonction pretty_sumab retourne une fonction qui accepte deux paramètres a et b 
# (la fonction inner) et qui appèle en interne la fonction func

# Dans le code ci-dessous, maFonctionDecoree est en fait la fonction inner() qui va 
# décorer (« augmenter ») la fonction sumab()
maFonctionDecoree = pretty_sumab(sumab)
maFonctionDecoree(5,3) # affiche 5 + 3 fait 8

#%%

# Python va encore plus loin avec la directive @ pour faire en sorte que la fonction décorée se 
# fasse appeler comme la fonction originale 
# Ceci suppose cependant que l'on a accès au code de la fonction originale (pour y placer la décoration)
# Le code est celui-ci :
def pretty_sumab(func):
    def inner(a,b):
        print(str(a) + " + " + str(b) + " fait ", end="")
        func(a,b)
        return
    return inner

@pretty_sumab
def sumab(a,b):
    summed = a + b
    print(summed)

sumab(5,3) # appele en fait pretty_sumab(sumab), affiche donc 5 + 3 is 8 (essayez en mode debug ...)

"""
Décorateur de classe
Le mécanisme de décorateurs vu ci-dessus est appliqué pour des besoins spécifiques des classes
"""

"""
Le décorateur @property 
Il utilise en interne la fonction property()
Il est utilisé pour exposer un Attribut d'objet en tant que Propriété
Les syntaxes sont : 

@property: déclare la méthode en tant que Propriété en get
.setter: déclare la méthode en tant que Propriété en set
.deleter: déclare la méthode en tant que effaceur de l'attribut

https://www.tutorialsteacher.com/python/property-decorator
"""

#%%

# Getter
class Student:
    def __init__(self, name):
        self.__name = name              # __name est un attribut privé (commence par _ _ )

    @property
    def name(self):                     # name est un 'getter'  (accesseur en lecture) de __name : name est une Propriété
        return self.__name

st1=Student("George")
print(st1.name)
#print(st1.__name) # provoque une exception car attribut privé

#%%
# Setter protégé : le but d'un setter est de ne pas accepter n'importe quoi ...
class Student:
    def __init__(self, name):
        self.__name=name

    @property
    def name(self):
        return self.__name

    @name.setter                #property-name.setter decorator
    def name(self, value):
        if value != None and value !="":
            self.__name = value
        else:
            #print("Valeur interdite")
            raise Exception("Valeur invalide")

st1=Student("Alfred")
print(st1.name)
#st1.name = None
#st1.name = ""
print(st1.name)

