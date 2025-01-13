# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 15:39:46 2022

@author: droch
"""
class TestContextManager:
    def __enter__(self):
        print ( 'Entrer dans le gestionnaire de contexte!' )
        return "ressource factice ici"

    def __exit__(self, *args):
        print ( 'Quitter le gestionnaire de contexte!' )

with TestContextManager() as x:
    print ( "À l'intérieur du gestionnaire de contexte!" )
    print(x)

print(x) #x ne doit plus être utilisé