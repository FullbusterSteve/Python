

def fact(n):
   if n==0 | n==1: return 1
   else: return n*fact(n-1)
   
a=int(input("Entrez un nombre entier\n"))
r=fact(a)
print("Le factoriel de ",a,"est ",r)


