## Week 2 Monday Notes
### SVD Definitions and Examples
SVD definition: 

$$A=U \Sigma V^T$$

U is the eigenvectors of $AA^T$, V is the eigenvectors of $A^TA$, and $\Sigma$ is the square root of the eigenvalues of $AA^T$ and $A^TA$, which are the same numbers.

Geometric Interpretation: 

The first multiplication by $V^T$ rotates to the principal axes, the $\Sigma$ scales the axes, and the last $U$ rotates it again to the output coordinate system. $A^TA=V \Sigma^T \Sigma V^T$, which means that the $\Sigma$ diagonal matrix gets squared. The square root of the eigenvalues of $A^TA$ needs to be taken to get the singular values ($\sigma$)  

#### Example 1
$$
A=\begin{bmatrix}
3 & 0 \\
0 & 2
\end{bmatrix}
$$

$$
A^TA=\begin{bmatrix}
9 & 0 \\
0 & 4
\end{bmatrix}
$$

$$
V=\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
$$

$$
\Sigma=\begin{bmatrix}
\sqrt{9} & 0 \\
0 & \sqrt{4}
\end{bmatrix}=\begin{bmatrix}
3 & 0 \\
0 & 2
\end{bmatrix}
$$

$$
AA^T=\begin{bmatrix}
9 & 0 \\
0 & 4
\end{bmatrix}
$$

$$
U=\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
$$

$$
\Sigma=\begin{bmatrix}
\sqrt{9} & 0 \\
0 & \sqrt{4}
\end{bmatrix}=\begin{bmatrix}
3 & 0 \\
0 & 2
\end{bmatrix}
$$

$$
A=U \Sigma V^T=\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}\begin{bmatrix}
3 & 0 \\
0 & 2
\end{bmatrix}\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}=\begin{bmatrix}
3 & 0 \\
0 & 2
\end{bmatrix}
$$

#### Example 2
$$
A=\begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix}
$$

$$
A^TA=\begin{bmatrix}
1 & 1 \\
1 & 2
\end{bmatrix}
$$

$$
V=\begin{bmatrix}
\frac{-1+\sqrt{5}}{2} & \frac{-1-\sqrt{5}}{2} \\
1 & 1
\end{bmatrix} \approx \begin{bmatrix}
0.618 & -1.618 \\
1 & 1
\end{bmatrix} 
$$

$$
||V|| \approx \begin{bmatrix}
0.528 & -0.851 \\
0.851 & 0.528
\end{bmatrix} 
$$

$$
\Sigma= \begin{bmatrix}
\sqrt{\frac{3+\sqrt{5}}{2}} & 0 \\
0 & \sqrt{\frac{3-\sqrt{5}}{2}}
\end{bmatrix} \approx \begin{bmatrix}
1.618 & 0 \\
0 & 0.618
\end{bmatrix}
$$

$$
AA^T=\begin{bmatrix}
2 & 1 \\
1 & 1
\end{bmatrix}
$$

$$
U=\begin{bmatrix}
\frac{1+\sqrt{5}}{2} & \frac{1-\sqrt{5}}{2} \\
1 & 1
\end{bmatrix} \approx \begin{bmatrix}
1.618 & -0.618 \\
1 & 1
\end{bmatrix} 
$$

$$
||U|| \approx \begin{bmatrix}
0.851 & -0.528 \\
0.528 & 0.851 
\end{bmatrix}
$$

$$
\Sigma=\begin{bmatrix}
\sqrt{\frac{3+\sqrt{5}}{2}} & 0 \\
0 & \sqrt{\frac{3-\sqrt{5}}{2}}
\end{bmatrix} \approx \begin{bmatrix}
1.618 & 0 \\
0 & 0.618
\end{bmatrix}
$$

$$
A=||U|| \Sigma ||V^T||= \begin{bmatrix}
0.851 & -0.528 \\
0.528 & 0.851 
\end{bmatrix} \begin{bmatrix}
1.618 & 0 \\
0 & 0.618
\end{bmatrix} \begin{bmatrix}
0.528 & 0.851 \\
-0.851 & 0.528
\end{bmatrix} \\
A= \begin{bmatrix}
1.3177 & -0.3263 \\
0.8543 & 0.5259
\end{bmatrix} \begin{bmatrix}
0.528 & 0.851 \\
-0.851 & 0.528
\end{bmatrix} = \begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix} 
$$

### Discrete Time Signals and System Properties- Oppenheim 2.0-2.2.5

- Linearity- The signal needs to be linear. It needs to meet additivity and homogeneity. Physically, it means that you can add or scale signals.

- Time Invariance- a time shift in the input produces an identical time shift in the output

- Memoryless- The signal does not depend on information from previous signals.

- Causality- The signal does not depend on information from signals in the future.

- Stability- Bounded Input, Bounded Output

An important note: A memoryless system is always causal, but a causal system is not necessarily memoryless.

For the Unity implementation of the White Cane:
- Linearity- No, the vibration signal itself could be additive and scaled. However, the transition probabilities in the markov chain cannot be scaled.
- Time Invariance- No, the surface signal depends on the the state at the time before, so the signals produced are dependent on the internal state. 
- Memoryless- No, the state machine needs to know where it was previously
- Causality- Yes, the state machine only looks at where it was previously
- Stability- Yes, and needs to be for safety reasons.

This means the system is not Linear-Time Invariant (LTI). 

## Week 2 Tuesday Notes
### Python SVD Implementation
- Reconstructed $A=U \Sigma V^T$ in Python
  - Python SVD implementation gives a 1-D array of eigenvalues. Need to use np.diag() to create a diagonal matrix 
- Created a Rank-K Approximation via Slicing
  - Only need the top K eigenvalues and eigenvectors of $U,\Sigma,V^T$
  - Error is calculated using Frobenius Norm: 
   
   $$||A-A_{Approx}|| = \sqrt{\sum_{i=1}^{m}\sum_{j=1}^{n}|a_{ij}-b_{ij}|^2}$$

  - Percent Explained uses the singular values from the $\Sigma$ Eigenvalue matrix:
   
   $$PctExp = \frac{\sum_{i=1}^{k}\sigma_{i}^{2}}{\sum_{i=1}^{n}\sigma_{i}^{2}}$$

- Plotted Error and Percent Explained vs k
![SVD Visualization](figures/rank_k_approximation.png)
- Identified thresholds at which XX% of variance explained

### SVD Examples
#### Example 1

$$
A=\begin{bmatrix}
2 & 4 \\
1 & 2
\end{bmatrix}
$$

$$
AA^T=\begin{bmatrix}
20 & 10 \\
10 & 5
\end{bmatrix}
$$

$$\lambda_1 = 25, \lambda_2=0$$

$$
U=\begin{bmatrix}
\frac{2}{\sqrt{5}} & \frac{-1}{\sqrt{5}} \\
\frac{1}{\sqrt{5}} & \frac{2}{\sqrt{5}}
\end{bmatrix}
$$

$$
A^TA=\begin{bmatrix}
5 & 10 \\
10 & 20
\end{bmatrix}
$$

$$\lambda_1 = 25, \lambda_2=0$$

$$
V=\begin{bmatrix}
\frac{1}{\sqrt{5}} & \frac{-2}{\sqrt{5}} \\
\frac{2}{\sqrt{5}} & \frac{1}{\sqrt{5}}
\end{bmatrix}
$$

$$
\Sigma =\begin{bmatrix}
5 & 0 \\
0 & 0
\end{bmatrix}
$$

$$
A = U \Sigma V^T =\begin{bmatrix}
2 & 4 \\
1 & 2
\end{bmatrix}
$$

## Week 2 Wednesday 
### Block 1: Positive Definite Matrices (Strang §6.2)

### Definition

A symmetric matrix **A** is **positive definite** if for every nonzero vector **x**:

$$
x^T A x > 0
$$

Geometrically, this defines a bowl shape — the quadratic form is always positive regardless of direction. In haptics, the stiffness matrix **K** must be positive definite so that potential energy $U = \frac{1}{2} x^TKx$ is always positive (physically stable system).

---

### Three Equivalent Tests

All three tests are equivalent — a matrix passes all three or none.

#### Test 1: All Eigenvalues Positive

If **Av = λv**, substituting **x = v** into the definition gives:

$$
v^T A v = \lambda v^T v = \lambda \|v\|^2
$$

Since $‖v‖^2 > 0$ always, the sign depends entirely on λ. Therefore all eigenvalues must be positive.

#### Test 2: All Pivots Positive

Pivots are the leading diagonal entries produced during Gaussian elimination. All pivots must be positive.

#### Test 3: All Upper-Left Determinants Positive

For an n×n matrix, all k×k upper-left submatrix determinants (k = 1, 2, ..., n) must be positive.

**Key relationship:** det(A) = product of eigenvalues = product of pivots

---

### Examples

**Positive definite** — all three tests pass:

$$
A = 
\begin{bmatrix} 
4 & 2 \\
2 & 3 
\end{bmatrix}
$$

- Pivots: 4, 2 
- Eigenvalues: $\frac{7 \pm \sqrt{17}}{2} \approx 5.56, 1.44$ 
- Determinants: 4, 8 

**Not positive definite** — fails Test 3:

$$
A = 
\begin{bmatrix} 
1 & 2 \\
2 & 1 
\end{bmatrix}
$$

- det(A) = -3 < 0 $\rightarrow$ one positive, one negative eigenvalue $\rightarrow$ **indefinite** (saddle shape)

**3×3 positive definite** (tridiagonal spring stiffness matrix):

$$
A = 
\begin{bmatrix} 
2 & -1 & 0 \\
-1 & 2 & -1 \\ 
0 & -1 & 2 
\end{bmatrix}
$$

- Upper-left determinants: 2, 3, 4 — all positive
- This is the stiffness matrix for a chain of 3 springs — positive definite confirms stable energy storage.

### Cholesky Decomposition

### Key Idea

Cholesky is LU decomposition exploiting symmetry. For a symmetric positive definite matrix:

$$
A = LL^T
$$

where **L** is lower triangular with positive diagonal entries.

---

### Derivation from LU

Standard LU gives $A = LU$. For symmetric positive definite A, this can be written as:

$$
A = LDL^T
$$

where **D** is diagonal with the pivots on the diagonal. Since positive definiteness guarantees all pivots are positive, we can take their square roots:

$$
\tilde{L} = L\sqrt{D} \implies A = \tilde{L}\tilde{L}^T
$$

**Why positive definiteness is required:** if any pivot were negative, $\sqrt{D}$ would produce imaginary entries — Cholesky only exists for positive definite matrices.

---

### Manual Derivation (2×2 Example)

Solve for L entry by entry by expanding $A = LLᵀ$:

$$
\begin{bmatrix} 
4 & 2 \\ 
2 & 3 
\end{bmatrix} = 
\begin{bmatrix} 
l_{11} & 0 \\ 
l_{21} & l_{22} 
\end{bmatrix} 
\begin{bmatrix} 
l_{11} & l_{21} \\ 
0 & l_{22} 
\end{bmatrix}
$$

Matching entries:
- Top-left: $l_{11}^2 = 4 \rightarrow l_{11} = 2$
- Bottom-left: $l_{21} · l_{11} = 2` \rightarrow l_{21} = 2/2 = 1$
- Bottom-right: $l_{21}^2 + l_{22}^2 = 3 \rightarrow l_{22} = \sqrt{2} \approx 1.414$

Result:

$$
L = 
\begin{bmatrix} 
2 & 0 \\ 
1 & \sqrt{2} 
\end{bmatrix}
$$

Note: diagonal entries of L are $\sqrt{(pivots)}$ — confirming the $LDL^T$ connection.

### White cane Bridge
If we wanted to simulate synthetic data for the white cane vibration then the Cholesky decomposition would be needed to preserve the relationship between sensors. Additionally multi-point haptic actuators will need to know this information as well. The main limitation with using this approach is that we need to stick with actuators located at the same places as the sensor. On the haptic cane, that is unrealistic. A more flexible approach would need to use a spatial covariance model rather than a fixed empirical covariance model.


### LTI Systems and Convolution (Oppenheim §2.3–2.4)
#### Core Result — The Convolution Sum

If you know a system's impulse response h[n], the output for any input x[n] is:

$$
y[n] = \sum_{k=-\infty}^{\infty} x[k] \cdot h[n-k]
$$

**Why h[n] is sufficient:** any input can be written as a sum of scaled and shifted impulses:

$$
x[n] = \sum_{k=-\infty}^{\infty} x[k] \cdot \delta[n-k]
$$

By linearity, each impulse produces a scaled shifted version of h[n]. By time-invariance, a shifted input produces the same shifted output. Superposition gives the convolution sum.

---

#### Causality and BIBO Stability

**Causality:** h[n] = 0 for n < 0 — output depends only on present and past inputs.

**BIBO Stability:**

$$
\sum_{n=-\infty}^{\infty} |h[n]| < \infty
$$

Example: $h = [1, 0, -1] \rightarrow \sum{|h[n]|} = 1 + 0 + 1 = 2 < \infty \rightarrow$ stable and causal.

---

#### Convolution Properties and System Interconnections

| Property | Formula | System Interpretation |
|---|---|---|
| Commutativity | x[n] * h[n] = h[n] * x[n] | Input and impulse response are interchangeable |
| Associativity | (x * $h_1$) * $h_2$ = x * ($h_1$ * $h_2$) | Cascade systems $\rightarrow$ single system with $h_1[n]$ * $h_2[n]$ |
| Distributivity | x * ($h_1[n]$ + $h_2[n]$) = x*$h_1[n]$ + x*$h_2[n]$ | Parallel systems $\rightarrow$ single system with h₁[n] + h₂[n] |

**Key results:**
- Cascade: order does not matter (commutativity)
- Parallel: impulse responses add
- Both: can always be reduced to a single equivalent system
---

#### White Cane Connection

The MSIM 510 signal processing pipeline (Butterworth filter $\rightarrow$ RMS envelope) is a cascade of two LTI systems. By associativity:

$$
y[n] = x[n] * (h_1[n] * h_2[n]) = x[n] * h[n]
$$

where $h_1[n]$ is the Butterworth filter, $h_2[n]$ is the RMS envelope, and h[n] is the entire pipeline as a single equivalent system.

---

### Distribution Parameter Types (Law §6.2.1)

- **Location** — shifts the distribution along the x-axis without changing its shape or spread (e.g. μ in Gaussian)
- **Scale** — stretches or compresses the spread of the distribution (e.g. σ in Gaussian)
- **Shape** — controls the form of the distribution: skewness, tail heaviness, modality (e.g. k in Gamma, α in Beta)

**Note:** Not all distributions have all three parameter types. The Gaussian has only location and scale — its shape is fixed. Distributions requiring a GMM indicate that a single location-scale family has insufficient shape flexibility to capture multimodal behavior.

