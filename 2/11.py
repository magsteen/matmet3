import numpy as np

def naive_gauss(A,b):
    n,m = np.shape(A)
    S = np.zeros((n,n+1))
    S[:,0:n] = A
    S[:,-1] = b
    for row in range(n-1):
        for row_2 in range(row+1,n):
            mult = S[row_2,row]/S[row,row]
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

def create_data(rows, cols):
    b = np.ones(rows)
    H = np.zeros((rows, cols))
    for row in range(rows):
        for col in range(cols):
            a = 1 / (row+1 + col+1 - 1)
            H[row,col] = a
    return H, b
   
ns = [2,5,10]
xs = []
for n in ns:
    H,b = create_data(n,n)
    x = naive_gauss(H,b)
    xs.append(x)
