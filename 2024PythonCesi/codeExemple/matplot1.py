# coding: utf-8

# site https://python.doctor/page-creer-graphiques-scientifiques-python-apprendre
# pip install matplotlib  pour installer le module

import matplotlib.pyplot as plt
import numpy as np

#essai très simple
plt.plot([1,2,3,4,2,3,1])
plt.ylabel('Label 1')
plt.show()

#input("enter pour continuer")

# agir sur les x, y et les labels
plt.title("Fourniture de valeurs x et y")
plt.plot([50,100,80,200], [1,2,3,4]) # liste en X puis liste en Y
plt.xlabel('mon label en X')
plt.ylabel('mon label en Y')
plt.show()

# plusieurs courbes dans la meme zone
plt.plot([50,100,150,200], [1,2,3,4])
plt.plot([50,100,150,200], [2,3,7,10])
plt.plot([50,100,150,200], [2,7,9,10])
plt.show()

# 2 graphes dans la même zone et emploi de scipy
plt.subplot(211)    # emplacement 2x1 ie 2 lignes 1 colonne
plt.plot([50,100,150,200], [1,2,3,4], "r--", linewidth=5)
plt.plot([50,100,150,200], [2,3,7,10], "b", linewidth=3)
plt.plot([50,100,150,200], [2,7,9,10], "g", linewidth=10)
plt.xlabel('Vitesse')
plt.ylabel('Temps')
plt.axis([80, 180, 1, 10])

plt.subplot(212)
plt.plot([50,100,150,200], [1,2,3,15], "r--", linewidth=5)
plt.plot([50,100,150,200], [2,3,7,10], "b", linewidth=3)
plt.plot([50,100,150,200], [2,7,9,10], "g", linewidth=10)
plt.xlabel('Vitesse')
plt.ylabel('Temps')
plt.axis([80, 180, 1, 10])

plt.show()


# mise en place d'une fonction sensible à l'événement clic dans la zone de tracé
toggle = True

def onclick(event):
    global toggle

    toggle = not toggle
    event.canvas.figure.clear()

    if toggle:
        plt.title("Graphe 1 Cliquer pour changer de graphe")
        event.canvas.figure.gca().plot([50,100,80,200], [1,2,3,4])
    else:
        plt.title("Graphe 2 Cliquer pour changer de graphe")
        event.canvas.figure.gca().plot([50,100,120,200,250], [1,2,1,4,3])

    event.canvas.draw()

fig = plt.figure()
fig.canvas.mpl_connect('button_press_event', onclick) # on associe ici le traitement du clic à ce graphe

plt.title("Graphe 1 Cliquer pour changer de graphe")
plt.plot([50,100,80,200], [1,2,3,4])
plt.show()

#histogramme
a = np.random.randn(10000)
hh = plt.hist(a, 40)
plt.show()


# pie
name = ['-18', '18-25', '25-50', '50+']
data = [5000, 26000, 21400, 12000]

explode=(0, 0.15, 0, 0)
plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
plt.axis('equal')
plt.show()

# en provenance de https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html
import pandas as pd
df2 = pd.DataFrame(np.random.rand(10, 4)*2, columns=['a', 'b', 'c', 'd'])
df2.plot.bar()

df2.plot.bar(stacked=True); #barres cumulatives

df2.plot.area(stacked=False)
