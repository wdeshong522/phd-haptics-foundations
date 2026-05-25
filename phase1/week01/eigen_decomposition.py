import numpy as np
import matplotlib.pyplot as plt

# Generate 100 points for angles from 0 to 2*pi
angles = np.linspace(0,2*np.pi,100)

# Calculate X and Y coordinates (radius = 1)
x = np.cos(angles)
y = np.sin(angles)

# Create Matrix
uc_matrix = np.array([x,y])

# Diagonalization --------------------------------------------------------------
A = np.array([[3,1],[1,2]])
eigvals, P = np.linalg.eig(A)

D = np.diag(eigvals)

print(D)
print(P)
print(P @ D @ np.linalg.inv(P))
# Incorrect way of checking for matching matrices
print(A == P @ D @ np.linalg.inv(P))
# Correct way of checking for matching matrices. Allows for floating point errors too
print(np.allclose(A, P @ D @ np.linalg.inv(P)))

new_UC_1 = np.linalg.inv(P)  @ uc_matrix
new_UC_2 = D @ np.linalg.inv(P) @ uc_matrix
new_UC_3 = P @ D @ np.linalg.inv(P) @ uc_matrix

# Create the plots
fig, axs = plt.subplots(nrows=1, ncols=4, sharex=True, sharey=True,figsize=(24,6))
fig.suptitle(r'Unit Circle Transformation $A=PDP^{-1}$')
#fig.figure(figsize=(6,12))

# Regular Unit Circle Plot
axs[0].plot(uc_matrix[0,:],uc_matrix[1,:],label="Unit Circle")
origin = np.array([[0, 0], [0, 0]]) 
axs[0].quiver(*origin, np.identity(2)[0,:], np.identity(2)[1,:], color = ['r','b'], scale = 5, label = "Eigenvectors")
# Transformed Unit Circle with Eigenvectors
axs[1].plot(new_UC_1[0,:],new_UC_1[1,:],label = r'Transformed Unit Circle (Step 1$ P^{-1}$)')
axs[1].quiver(*origin, P[0,:], P[1,:], color = ['r','b'], scale = 5, label = "Eigenvectors")
plt.legend(['Vector 1', 'Vector 2'])
# Transformed Unit Circle with Eigenvectors
axs[2].plot(new_UC_2[0,:],new_UC_2[1,:],label = r'Transformed Unit Circle (Step 2 $DP^{-1}$)')
axs[2].quiver(*origin, P[0,:], P[1,:], color = ['r','b'], scale = 5, label = "Eigenvectors")
plt.legend(['Vector 1', 'Vector 2'])
axs[2].annotate(r'$|\lambda_1|$', 
            xy=(D[0,0], 0),          # point the arrow at
            xytext=(2, 0.5),      # where the text sits
            arrowprops=dict(arrowstyle='->'))
axs[2].annotate(r'$|\lambda_2|$', 
            xy=(0,D[1,1]),          # point the arrow at
            xytext=(-1, 2),      # where the text sits
            arrowprops=dict(arrowstyle='->'))
# Transformed Unit Circle with Eigenvectors
axs[3].plot(new_UC_3[0,:],new_UC_3[1,:],label = r'Transformed Unit Circle (Step 3$PDP^{-1}$)')
axs[3].quiver(*origin, P[0,:], P[1,:], color = ['r','b'], scale = 5, label = "Eigenvectors")
plt.legend(['Vector 1', 'Vector 2'])
# Plot Formatting to keep it circular
#ax1.gca().set_aspect('equal')
for i in range(4):
    ax = axs[i]
    ax.axhline(0, color = 'black', linewidth = 1) # x-axis
    ax.axvline(0, color = 'black', linewidth = 1) # y-axis
    ax.grid(True, linestyle='--', alpha=0.6)

axs[0].set_xlim(-4,4)
axs[0].set_ylim(-4,4)
axs[0].set_title(r'Unit Circle ($U$)')
axs[1].set_title(r'Transformed Unit Circle (Step 1 $P^{-1}U$)')
axs[2].set_title(r'Transformed Unit Circle (Step 2 $DP^{-1}U$)')
axs[3].set_title(r'Transformed Unit Circle (Step 3 $PDP^{-1}U$)')
#fig.tight_layout()
plt.show()
