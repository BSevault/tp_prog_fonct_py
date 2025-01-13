# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 14:46:40 2022

@author: droch
"""

#%%

# provient de https://www.tutorialsteacher.com/python/python-generator

def myGenerator():
    print('First item')
    yield 10        # yield remplace le return et fait que myGenerator devient un Generator

    print('Second item')
    yield 20

    print('Last item')
    yield 30

gen = myGenerator() 
print(type(gen))
value = next(gen)     # l'objet gen est toujours actif, prêt à un autre emploi. Une fonction ordinaire, sans yield, serait rendue à la mémoire
print(value)
value = next(gen) 
value = next(gen) 
#next(gen)  # exception car il n'y a que 3 valeurs rendues par yield

#%%

# yield mis dans une boucle

def myGenerator():
    i = 0
    print("Première exécution effective de myGenerator")
    while True :        # permet de demander un nombre de fois quelconque next()
        i +=1
        #print("Execution d'une itération")
        yield i        # yield remplace le return et fait que myGenerator devient un Generator


gen = myGenerator() 
for j in range(20):
    print(next(gen),end=" ") 
    
    #%%
def calculCarre(x):
    for i in range(x):
        yield i*i

calc = calculCarre(5) # armé pour 5 calculs
print(next(calc), end=" ")
print(next(calc), end=" ")
print(next(calc), end=" ")
print(next(calc), end=" ")
print(next(calc))
#print(next(calc))  # en trop provoque une exception

# comment lire l'ensemble des valeurs ?
calc = calculCarre(5) # armé pour 5 nouveaux calculs
while True:
    try:
        print ("Résultat du next(): ", next(calc))
    except StopIteration:
        break #on s'arrête ici automatiquement

# une boucle for rend l'écriture plus facile
# en effet, en interne du for : un next() est appelé à chaque itération, le StopItération est surveillé
calc = calculCarre(5) # armé pour 5 nouveaux calculs
for unCalcul in calc:
    print(unCalcul, end=" ")