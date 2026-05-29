import numpy as np
import matplotlib.pyplot as plt

A = np.array([[3,1],
             [2,4]])

U, s, Vt = np.linalg.svd(A)

print(U)
print(s)
print(np.diag(s))
print(Vt)

print (U @ np.diag(s) @ Vt)

B = np.array([[3,1],
             [2,4]])

U, s, Vt = np.linalg.svd(B)
k=1
print (U[:,:k] @ np.diag(s)[:k,:k] @ Vt[:k,:])


C = np.random.randn(20,10)
U, s, Vt = np.linalg.svd(C)
errors = []
pct_explained = []
for k in range(min(C.shape)):
    C_approx = U[:,:k+1] @ np.diag(s)[:k+1,:k+1] @ Vt[:k+1,:]
    errors.append(np.linalg.norm(C-C_approx))
    pct_explained.append(np.sum(np.power(s[:k+1],2)) / np.sum(np.power(s,2)))
print(np.array(errors))
pct_explained_arr = np.array(pct_explained)
print(pct_explained_arr)
print(np.argmax(pct_explained_arr[pct_explained_arr<=0.9])+1)
print(np.argmax(pct_explained_arr[pct_explained_arr<=0.95])+1)


# plt.plot(range(1,11),errors)
# plt.title("Rank-K Approximation Error")
# plt.ylabel('Error')
# plt.xlabel('k')
# plt.show()

# Create the plots
fig, axs = plt.subplots(nrows=1, ncols=2, sharex=True, sharey=False,figsize=(12,6))
fig.suptitle("Rank-K Approximation Error")
#fig.figure(figsize=(6,12))

# Error
axs[0].plot(range(1,11),errors,label="Error")

# Percent Explained
axs[1].plot(range(1,11),pct_explained,label="Percent Explained")

axs[0].set_title("Error")
axs[1].set_title("Percent Explained")
#fig.tight_layout()
plt.savefig('phase1/week02/figures/rank_k_approximation.png', dpi=150, bbox_inches='tight')
plt.show()