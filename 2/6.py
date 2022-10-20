import numpy as np

h = 10
v = 60

actual = lambda h, v : np.sqrt((3*v)/(np.pi*h))

f = lambda r: np.pi*(r**2)*(h/3+(2*r)/3)-v
f_der = lambda r: 2*np.pi*r*(r+h/3)

initial_guess = 2

def estimated(x_0):
    x_r = x_0
    
    for i in range(10):
        x_r = x_r - f(x_r)/f_der(x_r)
        
    return x_r

radius = estimated(initial_guess)
print(radius)
