from unicodedata import decimal
import numpy as np

def qr(A: np.ndarray):
    if len(A.shape) != 2:
        raise ValueError(f"expects 2D-array but got size: {A.shape}")
    r = np.zeros((A.shape[1],)*2)
    q = np.zeros(A.shape)
    for j in range(0, A.shape[1]):
        y = A[:,j]
        for i in range(0, j):
            r[i][j] = q[:,i] @ A[:,j]
            y = y - r[i][j] * q[:,i]
        r[j][j] = np.linalg.norm(y)
        q[:,j] = y / r[j][j]
    
    return q, r


# 1a
one_a = np.array([[4,0],[3,1]])
print(f"one_a:\n{one_a}")

q, r = qr(one_a)
print(f"r:\n{r}")
print(f"q:\n{q}")

one_a_result = q @ r
print(f"result:\n{one_a_result}")
print(f"Rounded result:\n{np.around(one_a_result, decimals=0)}")

# 2a
two_a = np.array([[2,3],[-2,-6],[1,0]])
print(f"two_a:\n{two_a}")

q, r = qr(two_a)
print(f"r:\n{r}")
print(f"q:\n{q}")

two_a_result = q @ r
print(f"result:\n{two_a_result}")
print(f"Rounded result:\n{np.around(two_a_result, decimals=0)}")
