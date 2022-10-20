import numpy as np

def naive_gauss(A,b):
    n,m = np.shape(A)
    S = np.zeros((n,n+1))
    S[:,0:n] = A
    S[:,-1] = b
    print(S)
    for row in range(n-1):
        for row_2 in range(row+1,n):
            mult = S[row_2,row]/S[row,row]
            print("L_%s%s: %s" % (row+1, row_2+1, mult))
            S[row_2,row]=0.0
            for col in range(row+1, n+1):
                S[row_2,col] -= S[row,col] * mult
                
    xs = np.zeros(n)
    for row in range(n-1, -1, -1):
        b = S[row,n]
        for col in range(n-1, row-1, -1):
            b -= S[row,col] * xs[col]
        
        x = b / S[row,col]
        xs[row] = x

    return xs

A = np.array([[1, 2,-1], 
              [0, 3, 1], 
              [2,-1, 1]])

b = np.array([2, 4, 2])

x = naive_gauss(A,b)
