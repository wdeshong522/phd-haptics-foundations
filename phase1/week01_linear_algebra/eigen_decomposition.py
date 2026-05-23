import numpy as np

# Diagonalization --------------------------------------------------------------
A = np.array([[3,1],[0,2]])
eigvals, P = np.linalg.eig(A)

D = np.diag(eigvals)

print(D)
print(P)
print(P @ D @ np.linalg.inv(P))
# Incorrect way of checking for matching matrices
print(A == P @ D @ np.linalg.inv(P))
# Correct way of checking for matching matrices. Allows for floating point errors too
print(np.allclose(A, P @ D @ np.linalg.inv(P)))

