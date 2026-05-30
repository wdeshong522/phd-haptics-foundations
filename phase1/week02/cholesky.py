import numpy as np

A = np.array([[4., 2.],
              [2., 3.]])

L = np.linalg.cholesky(A)
print(L)
print(L @ L.T)