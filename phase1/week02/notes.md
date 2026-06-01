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

## Week 2 Thursday 

### Pseudoinverse and Least Squares (Strang §6.3)

#### Pseudoinverse Definition

For any matrix $A = U\SigmaV^T, the pseudoinverse is:

$$
A^+ = V\Sigma^+ U^T
$$

where $\Sigma^+$ is formed by replacing each nonzero singular value with its reciprocal, then transposing:

$$
\Sigma = 
\begin{bmatrix} 
5 & 0 \\ 
0 & 2 \\ 
0 & 0 
\end{bmatrix} \implies 
\Sigma^+ = 
\begin{bmatrix} 
1/5 & 0 & 0 \\ 
0 & 1/2 & 0 
\end{bmatrix}
$$

If A is m×n then $A^+$ is n×m.

---

#### Least Squares — Two Equivalent Methods

For an overdetermined system Ax = b (m > n, no exact solution), minimize $‖Ax - b‖^2$:

**Method 1 — Normal Equations:**

$$
A^T A \hat{x} = A^T b \implies \hat{x} = (A^T A)^{-1} A^T b
$$

**Method 2 — Pseudoinverse:**

$$
\hat{x} = A^+ b
$$

Both give the same result when A has full column rank.

---

#### Numerical Warning — Small Singular Values

If a singular value is very small (e.g. 1e-10) but not exactly zero, taking its reciprocal inflates it to 1e10 — massively amplifying noise in that direction.

**Fix — Truncated SVD:** set a threshold ε and treat any $\sigma_i < \epsilon$ as zero. `np.linalg.pinv` does this automatically.

This is the same decision as rank-k approximation — choosing which singular values to keep vs discard.

---
#### White Cane Connection

The white cane data matrix is overdetermined — many more time samples than axes. Fitting a model to this data is implicitly a least-squares problem. The pseudoinverse makes this well-posed even when no exact solution exists.

---
### Density and Mass Functions (C&B §1.6)
#### Discrete Random Variables
1. $p(x) \ge 0$ for all x
2. $\sum_x p(x) = 1$ for PMF, $\int_{-\infty}^{\infty} p(x) = 1$  for pdf

#### Bernoulli:
Models a single trial with probability p of success:

$$p(x)= p^x (1-p)^{1-x},\ x \in \{0,1\}$$

#### Binomial:
Models k successes in n independent Bernoulli trials:
$$p(x)= {n\choose x} p^x (1-p)^{n-x},\ x \in \{0,1,...,n\}$$

**Derivation:** two components multiply together:
- **Probability of one specific sequence** with k successes: $p^k(1-p)^{n-k}$
- **Number of such sequences** — choosing which k of n positions get a success: $\binom{n}
{k} = \frac{n!}{k!(n-k)!}$

Divide by k! because success positions are interchangeable; divide by (n-k)! because failure positions are interchangeable.

---

#### PDF — Continuous Random Variables

Must satisfy:
1. f(x) ≥ 0 for all x
2. ∫f(x)dx = 1

#### Uniform PDF on [a, b]

Constant density over the interval — all values equally likely:

$$
f(x) = \frac{1}{b-a}, \quad x \in [a, b]
$$

#### Exponential PDF

Models time between events in a Poisson process. Parameter λ > 0:

$$
f(x) = \lambda e^{-\lambda x}, \quad x \geq 0
$$

**Verification:**
- Non-negative: λ > 0 and $e^{-λx} > 0$ for all x ≥ 0 
- Integrates to 1 

$$
F(x)=\int_{0}^{\infty} \lambda e^{-\lambda x} dx \\
u = -\lambda x, du=-\lambda dx \\
F(x) = -\int_{0}^{-\infty}  e^{u} du \\
F(x) = -e^{-\infty}+e^{0} = 1
$$

**Memoryless property:** P(X > s+t | X > s) = P(X > t) — the probability of leaving a state does not depend on how long you've already been there.

---

### White Cane Connection

The white cane Markov chain makes a transition decision at every frame update independently of past dwell time — this is precisely the memoryless property. If extended to a continuous-time Markov chain, the Exponential would be the natural dwell time distribution with λ = 1/mean_dwell_time estimated from empirical data.

---
### Bridge
The white cane surface classifier can be defined by P(surface=k|x). If it is confident then P(surface=k|x) would have a dominant higher probability for one surface and lower probabilities for the other surfaces. For example, in trying to distinguish grass vs a rug, those probabilities might be something like P(Concrete|x) = 0.9, P(Rug|x)=0.01, P(Grass|x)=0.01, P(Tactile Pavement|x) = 0.08. If it were not confident, then it would have the most likely surfaces having similar probabilities. For example, in trying to distinguish grass vs a rug, those probabilities might be something like P(Grass|x) = 0.45, P(Rug|x)=0.46, P(Concrete|x)=0.05, P(Tactile Pavement|x) = 0.04.

In a scenario where the classifier is uncertain, it must decide what surface if should classify. 


---

### Block 4B: Angel Ch.1 Synthesis — Graphics Pipeline

#### Complete Rendering Pipeline

| Stage | Runs On | Input | Output |
|---|---|---|---|
| Application | CPU | Scene description, geometry, transformations | Vertex data sent to GPU |
| Geometry | GPU | Vertices | Projected, clipped primitives |
| Rasterization | GPU | Primitives | Pixels written to framebuffer |


#### Stage Details

**Application Stage (CPU)**
- Define vertices that make up 3D geometry
- Apply transformations (move, rotate, scale objects)
- Set up lighting, textures, materials
- Send processed data to GPU

**Geometry Stage (GPU)**
- Process vertices through transformation pipeline
- Apply projection — map 3D world to 2D projection plane
- **Clipping** — remove primitives that fall outside the view volume (no point rasterizing what the viewer cannot see)

**Rasterization Stage (GPU)**
- Convert projected geometric primitives to discrete pixels
- Write pixel values to the **framebuffer**
- Framebuffer output sent to display


#### Synthetic Camera Model

- Virtual objects exist in world space independently of the viewer
- The camera defines what gets seen — moving the camera does not touch the geometry
- The clipping rectangle is the digital equivalent of a physical camera's film frame
- Only geometry within the view volume reaches rasterization

#### Key Facts
- The entire pipeline can now run on the GPU (programmable shader pipeline)
- CPU/GPU boundary: application stage on CPU, everything after on GPU
- Framebuffer sits at the end of rasterization — stores final pixel values before display

## Week 2 Friday Notes 
### Rayleigh Quotient and Minimum Principles (Strang §6.4)

#### Rayleigh Quotient Definition

For a symmetric matrix A and nonzero vector x:

$$
R(x) = \frac{x^T A x}{x^T x}
$$

The denominator $x^Tx$ normalizes the quadratic form so R(x) is scale-invariant.

---

#### Key Result — Eigenvalue Bounds

$$
\lambda_{min} \leq R(x) \leq \lambda_{max}
$$

- **Minimum** achieved when x = first eigenvector (corresponding to $\lambda_{min}$)
- **Maximum** achieved when x = last eigenvector (corresponding to $\lambda_{max}$)

**Practical value:** find extreme eigenvalues by optimizing R(x) rather than solving the characteristic polynomial — far more efficient for large matrices.

---

#### Generalized Rayleigh Quotient

For the generalized eigenvalue problem $Ax = B \lambda x$:

$$
R(x) = \frac{x^T A x}{x^T B x}
$$

In structural mechanics and haptics: A = K (stiffness), B = M (mass):

$$
R(x) = \frac{x^T K x}{x^T M x}
$$

Minimum gives $\omega_{min}^2$ — the lowest resonant frequency of the system. The direction that minimizes R(x) is the mode easiest to excite.

---

#### Haptic Applications

**Spring wall stiffness:**
- Potential energy of displacement x: $U = \frac{1}{2} x^TKx$
- Minimum stiffness in any direction = $\lambda_{min}$ of K, achieved along first eigenvector
- If $\lambda_{min} \rightarrow 0$: wall becomes transparent in that direction — no force feedback

**Positive definiteness guarantee:**
- K positive definite $\rightarrow$ all eigenvalues positive $\rightarrow$ $\lambda_{min} > 0$
- Guarantees nonzero stiffness in every direction
- Mathematical guarantee that the haptic wall always pushes back

**Dental sim implication:**
- If $\lambda_{min}$ of K is too small, students can push through the wall without feeling appropriate resistance
- Positive definite K is a safety requirement, not just a mathematical convenience

**Haptic rendering loop:**
- The direction minimizing the generalized Rayleigh quotient resonates at the lowest frequency
- This direction requires the most careful stability management in the rendering loop

### Complex Matrices and Similarity Transformations (Strang §5.5–5.6)

#### Hermitian Matrices — $A =A^H$ 

The conjugate transpose $A^H$ replaces every entry $a_{ij}$ with its complex conjugate $\bar{a}_{ji}$. Hermitian is the complex generalization of symmetric.

**Key result: all eigenvalues are real.**

**Why $x^TAx$ matters:** for any input direction x, $x^TAx$ measures the "response" of the system A in that direction. For a stiffness matrix K, $U = \frac{1}{2}x^TKx$ is the potential energy stored when pushing in direction x. $x^TAx$ captures all possible input directions at once — not just eigenvectors.

For Hermitian A, %v^HAv$ equals its own complex conjugate $\rightarrow$ must be real $\rightarrow$ eigenvalues are real. Hermitian matrices represent physical observables that must produce real measurements.

**Practical rule:** Hermitian matrices behave like symmetric matrices — real eigenvalues, orthogonal eigenvectors — just extended to complex entries.

---

#### Unitary Matrices — $Q^H = Q^{-1}$

The complex generalization of orthogonal matrices. Columns are orthonormal in the complex sense.

**Key result: all eigenvalues lie on the unit circle.**

$$
|\lambda| = 1 \implies \lambda = e^{j\theta}
$$

**Why this matters:**
- Unitary transformations are pure rotations — magnitude of any vector is preserved
- $│\lambda│< 1$ $\rightarrow$ system decays. $│\lambda│> 1$ $\rightarrow$ system grows. $│\lambda│= 1$ $\rightarrow$ energy preserved
- The **DFT matrix is unitary** $\rightarrow$ FFT preserves signal energy (Parseval's theorem)
- Applying a unitary matrix repeatedly never causes growth or decay

---

#### Similarity Transformations

Two matrices A and B are **similar** if:

$$
B = M^{-1}AM
$$

**Key result: similar matrices have the same eigenvalues.**

All decompositions studied this week are similarity transformations in disguise:

| Decomposition | Similarity Transform M | Result |
|---|---|---|
| Diagonalization $A = PDP^{-1}$ | P (eigenvectors) | D diagonal |
| SVD $A = U\Sigma V^T$ | U, V orthogonal | $\Sigma$ diagonal |
| Cholesky $A = LL^T$ | L lower triangular | triangular form |

**For Hermitian matrices:** the similarity transform is always unitary ($Q^{-1} = Q^H$) — orthonormal eigenvectors, best numerical stability.

**Motivation:** finding a similarity transform that diagonalizes or triangularizes A makes eigenvalue computation trivial. The quality of the transform determines numerical stability.

---

#### DSP Connection

The complex exponential eʲωn has magnitude 1 — it sits exactly on the unit circle. This is precisely why it is the natural input for LTI systems (Block 3 today) and why the DFT — built from unitary transformations — is energy-preserving.

---
### Block 4A: Continuous Distribution Reference Card (Law §6.2.2)

### Distribution Families

| Distribution | Parameters | Support | When to Use |
|---|---|---|---|
| Uniform | a (min), b (max) | [a, b] | Equal likelihood across range; baseline/default |
| Exponential | $\beta$ (scale) | $[0, \infty)$ | Time between events; memoryless dwell times |
| Erlang | m (integer shape), $\beta$ (scale) | $[0, \infty)$ | Sum of m Exponentials; sequential waiting stages |
| Gamma | $\alpha$ (shape), $\beta$ (scale) | $[0, \infty)$ | Generalization of Exponential; flexible positive RV |
| Weibull | $\alpha$ (scale), $\beta$ (shape) | $[0, \infty)$ | Reliability and lifetime modeling; variable hazard rate |
| Normal | $\mu$ (location), $\sigma^2$ (scale) | $(-\infty, \infty)$ | Central limit theorem; symmetric measurement error |
| Lognormal | $\mu$, $\sigma^2$ (of ln(X)) | $(0, \infty)$ | Positive, right-skewed quantities (amplitudes, lifetimes) |
| Beta |  $\alpha,\beta$ (both shape) | [0, 1] | Probabilities, proportions, bounded quantities |
| Triangular | a (min), b (max), c (mode) | [a, b] | No data available; expert provides min/max/most likely |

---

### Key Relationships

- **Erlang** = Gamma(m, $\beta$) where m is a positive integer
- **Exponential** = Gamma(1, $\beta$) = Erlang(1, $\beta$)
- **Lognormal**: if X ~ Lognormal then ln(X) ~ Normal
- **Weibull shape $\beta$:** $\beta$ < 1 $\rightarrow$ decreasing failure rate; $\beta$ = 1 $\rightarrow$ Exponential; $\beta$ > 1 $\rightarrow$ increasing failure rate

---

### White Cane Connections

- **Micro-state vibration amplitudes** → Gaussian (Normal) — confirmed by MSIM 510 paper
- **Macro-state amplitudes** → GMM (mixture of Normals) — single Normal insufficient
- **Vibration envelope** → Lognormal candidate — always positive, right-skewed
- **Markov chain dwell times** → Exponential — memoryless property matches frame-by-frame transition decisions