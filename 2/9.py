import numpy as np

def naive_gauss(A,b):
    n,m = np.shape(A)
    S = np.zeros((n,n+1))
    S[:,0:n] = A
    S[:,-1] = b
    for row_1 in range(n-1):
        for row_2 in range(row_1+1,n):
            mult = S[row_2,row_1]/S[row_1,row_1]
            S[row_2,row_1]=0.0
            for col in range(row_1+1, n+1):
                S[row_2,col] -= S[row_1,col] * mult

    return S[:,0:n],S[:,-1]

A = np.array([[1, 2,-1], 
              [0, 3, 1], 
              [2,-1, 1]])

b = np.array([2, 4, 2])

Ar, br = naive_gauss(A,b)
