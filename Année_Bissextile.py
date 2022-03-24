# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 11:46:12 2022

@author: Steve
"""

while True:
    def bissextile():
      monAnne=int(input("Bonjour cher utilisateur.\n Entrez l'année dans laquelle nous sommes\n"))
      if monAnne%4!=0:
        print("L'année n'est pas bissextile")
      elif monAnne%100==0:
        if monAnne%400==0:
          print("L'année est bissextile")
        else: print("L'année n'est pas bissextile")
      else: print("L'année est bissextile")
   
    bissextile()
    print("\n")
