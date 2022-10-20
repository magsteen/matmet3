import numpy as np

def LUfactorize(A):
    n,m = np.shape(A)
    L = np.eye(n)
    U = A.copy()
    for row in range(n-1):
        for row_2 in range(row+1,n):
            if ( U[row, row] == 0 ): #0 i pivot element
                raise np.linalg.LinAlgError("Zero pivot encountered")
                return 
            mult = U[row_2,row]/U[row,row]
            U[row_2,row]=0.0
            L[row_2, row] = mult
            for col in range(row+1, n):
                U[row_2,col] -= U[row,col] * mult
    return L,U

def LUsolve(L,U,b):
    # Løs Lc = b
    c = np.zeros_like(b)
    n = len(c)
    for row in range(n):
        c[row] = b[row]
        for col in range(0, row):
            c[row] -= L[row, col] * c[col]

    # Løs Ux = c
    x = c.copy()
    for row in range(n-1, -1, -1):
        for col in range(n-1, row, -1):
            x[row] -= U[row,col] * x[col]
        x[row] /= U[row,row]

    return x

A = np.array([3.0, 1,2,6,3,4,3,1,5])
A=A.reshape((3,3))
b = np.array([0,1.0,3])

try:
    L,U = LUfactorize(A)
    x = LUsolve(L,U,b)
except np.linalg.LinAlgError as e:
    print(f"LinAlgError: {e}")
