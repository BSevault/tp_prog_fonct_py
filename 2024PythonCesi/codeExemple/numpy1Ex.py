# coding: utf-8

# utilisation du module numpy
# pip install numpy  pour installer

#site https://courspython.com/tableaux-numpy.html 

import numpy as np
import matplotlib.pyplot as plt

v = np.array([1, 3, 2, 4]) # creation à partir de liste
print (v)
print (type(v))

v = np.arange(1,5) # vecteur de 1 compris à 5 non compris
print (v)
v = np.linspace(1,4,5) # vecteur de 1 à 4 et 5 valeurs souhaitées
print (v)

v = np.array([1, 3, 2, 4])
x = np.array([0, 1, 2, 3])
plt.figure()
plt.plot(x,v, 'rv--', label='v(x)')
plt.legend(loc='lower right')
plt.xlabel('x')
plt.ylabel('v')
plt.title("Premier graphe")
plt.xlim([-1, 4])
plt.ylim([0, 5])
plt.show()
plt.savefig('toto.png')

# une matrice: l'argument est une liste emboitée
M = np.array([[1, 2, 3], [4, 5, 6]])
print (M)
print(type(v), type(M))
print("shape ", v.shape, M.shape) # forme du array np.shape(v) équivalent
print("size ", v.size, np.size(M))   # nbre d'éléments
print("nb lignes ", np.size(M,0), " nb col " , np.size(M,1))   # nbre de lignes et de colonnes

# courbe sinus entre -10 et 10

xx = np.linspace(-10, 10, 100)
print(xx)
print(np.sin(xx))

plt.plot(xx, np.sin(xx))
plt.show()

x, y = np.mgrid[0:5, 0:5]
print("x :",x)
print("y :",y)

# une matrice diagonale
d = np.diag([1,2,3])
print(d)

# Pour résoudre le système d’équations linéaires 3*x0 + x1 = 9 et x0 + 2*x1 = 8 :
a = np.array([[3,1], [1,2]])
b = np.array([9,8])
x = np.linalg.solve(a, b)
print("resultat " , x)

