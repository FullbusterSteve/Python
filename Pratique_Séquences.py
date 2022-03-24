# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 22:15:35 2022

@author: Steve
"""
# The Programm displays the vowels contained in the first names 

prenom=['Steve',"Yannick",'Lionel']
villes=["Yaoundé","Douala","Garoua"]
prenom.insert(2,'François')
prenom.extend(["Murielle",'Georges','Natacha'])
print(prenom)
for i,n in enumerate(prenom):
    print('le prénom numéro',i+1," est ", n)

print(" La liste prénom est de longueur : ",len(prenom))
moi='Steve'
voyelle="aeiouyAEIOUY"

for p in prenom:
    print("Le prénom ",p, "contient les voyelles : ")
    for l in p:
        if l in voyelle:
            print( "\n",l)
            