import numpy as np

def halvering_solve(f, a, b, tol):
   e = 1
   pe = None
   while e > tol and e != pe:
        c = (b-a)/2 + a
        f_c = f(c)
        
        if f(a)*f_c < 0:
            b = c
        elif f_c*f(b) < 0:
            a = c
            
        pe = e
        
        e = c - 2.080083823
        if (e < 0):
            e *= -1
   
   return c

f = lambda x : x**3 - 9
maks_feil = 0.000001
a = 2
b = 3
x_sol = halvering_solve(f,a,b, maks_feil)
print(x_sol)
