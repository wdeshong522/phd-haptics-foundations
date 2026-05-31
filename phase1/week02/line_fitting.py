import numpy as np

A = np.array([[1, 1],
              [1, 2],
              [1, 3],
              [1, 4]], dtype=float)

b = np.array([1, 2, 2, 3], dtype=float)

U, s, Vt = np.linalg.svd(A)
sigma_p = np.zeros(A.T.shape)
sigma_p[:,:len(s)]=np.diag(1/s)
print(sigma_p)

A_p = Vt.T @ sigma_p @ U.T

x_1 = A_p @ b
x_2 = np.linalg.inv(A.T @ A) @ A.T @ b

print(x_1)
print(x_2)

print(A_p)
print(np.linalg.pinv(A))