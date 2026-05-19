import numpy as np
import matplotlib.pyplot as plt

# Generate 100 points for angles from 0 to 2*pi
angles = np.linspace(0,2*np.pi,100)

# Calculate X and Y coordinates (radius = 1)
x = np.cos(angles)
y = np.sin(angles)

# Create Matrix
uc_matrix = np.array([x,y])

# Transform Unit Circle
A = np.array([[3,2],[2,3]])

new_UC = A @ uc_matrix

eigvalA, eigvecA = np.linalg.eig(A)
print(eigvalA[0])
print(eigvecA[:,0])
print(eigvalA[1])
print(eigvecA[:,1])

# Create the plots
fig, axs = plt.subplots(nrows=1, ncols=2, sharex=True, sharey=True,figsize=(12,6))
fig.suptitle("Unit Circle Transformation")
#fig.figure(figsize=(6,12))

# Regular Unit Circle Plot
axs[0].plot(uc_matrix[0,:],uc_matrix[1,:],label="Unit Circle")

# Transformed Unit Circle with Eigenvectors
axs[1].plot(new_UC[0,:],new_UC[1,:],label = "Transformed Unit Circle")
origin = np.array([[0, 0], [0, 0]]) 
axs[1].quiver(*origin, eigvecA[0,:], eigvecA[1,:], color = ['r','b'], scale = 5, label = "Eigenvectors")
plt.legend(['Vector 1', 'Vector 2'])
# Plot Formatting to keep it circular
#ax1.gca().set_aspect('equal')
for i in range(2):
    ax = axs[i]
    ax.axhline(0, color = 'black', linewidth = 1) # x-axis
    ax.axvline(0, color = 'black', linewidth = 1) # y-axis
    ax.grid(True, linestyle='--', alpha=0.6)

axs[0].set_xlim(-4,4)
axs[0].set_ylim(-4,4)
axs[0].set_title("Unit Circle (r=1)")
axs[1].set_title("Transformed Unit Circle")
#fig.tight_layout()
plt.show()



# # 1. Define a square matrix
# A = np.array([[3, 1], [0, 2]])

# # 2. Compute eigenvalues and eigenvectors
# # Note: eigenvectors are returned as columns in the second array
# evals, evecs = np.linalg.eig(A)
# print(evals)
# print(evecs)
# # 3. Setup the plot
# origin = np.array([[0, 0], [0, 0]]) # origin point for both vectors
# plt.figure(figsize=(6, 6))

# # 4. Plot eigenvectors using quiver
# # evecs[:, 0] is the first eigenvector, evecs[:, 1] is the second
# plt.quiver(*origin, evecs[0, :], evecs[1, :], color=['r', 'b'], 
#            scale=5, label='Eigenvectors')

# # Formatting the plot
# plt.grid()
# plt.axhline(0, color='black', lw=1)
# plt.axvline(0, color='black', lw=1)
# plt.xlim(-1, 1)
# plt.ylim(-1, 1)
# plt.legend(['Vector 1', 'Vector 2'])
# plt.title("Eigenvectors Visualization")
# plt.show()