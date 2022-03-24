# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 14:59:22 2022

@author: Steve
"""
# The program sorts positive and negative numbers in an array
classeur={
    'positif':[],
    'négatif':[],
      }


while True:
        n=input('Entrez un nombre\n')
        n=int(n)
        if n>=0 :
           classeur['positif'].append(n)
        else:
           classeur['négatif'].append(n)
    
        for k,v in classeur.items():
            print(k,v)
        print('\n')




    

