import numpy as np

def halvering_solve(f, a, b, tol):
   #Din kode her :) --->
   feil = 1
   while feil > tol:
        c = (b-a)/2 + a
        f_c = f(c)
        
        if (f_c < 0):
            a = c
        if (f_c > 0):
            b = c
        
        feil = c - 2.080083823
        if (feil < 0):
            feil *= -1
   
   return c#<---------

f = lambda x : x**3 - 9 #Hvilken funksjon f er det du skal finne roten av?
maks_feil = 0.000001 #Hva blir maks feil om x_sol skal være riktig med minst 6 desimaler?
a = 2
b = 3
x_sol = halvering_solve(f,a,b, maks_feil) #Hva må startintervallet være?
print(x_sol)
