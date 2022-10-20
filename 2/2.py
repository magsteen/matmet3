from re import X
import numpy as np

def fikspunkt_solve(f, x0, tol):
    x_i = x0
    feil = 1
    while feil > tol:
        x_i1 = f(x_i)
        print(x_i1)
        feil = (x_i1 - x_i) / x_i1
        if (feil < 0):
            feil *= -1
        
        x_i = x_i1

    return x_i

# f1 = lambda x: (x**3)/2 - 1             #Hvilken funksjon skal inn i fikspunkt_solve? (lign. 1)
f2 = lambda x: 7 - np.e**x              #Hvilken funksjon skal inn i fikspunkt_solve? (lign. 2)
f3 = lambda x: np.arcsin(4 - np.e**x)   #Hvilken funksjon skal inn i fikspunkt_solve? (lign. 3)

funcs = [f2,f3]
maks_feil = 0.00000001
sols = []

for f in funcs:
   x_sol = fikspunkt_solve(f, 1.0, maks_feil)
   sols.append(x_sol)

print(f"Løsning til første ligning x = {sols[0]}")
print(f"Løsning til andre ligning x = {sols[1]}")
print(f"Løsning til tredje ligning x = {sols[2]}")
