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

A = np.array([ 1.0,  2,-1,0,3,1,2,-1,1 ])
A=A.reshape((3,3))
try:
   L,U = LUfactorize(A)
   print(L); print(U)
except np.linalg.LinAlgError as e:
   print(f"LinAlgError: {e}")
