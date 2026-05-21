\## Week 1 Monday Bridge

The Pacinian corpuscle detects deep pressure, touch, and high frequency vibrations around 250 Hz. At a 1 kHz sampling rate, we will get 4 samples per cycle, which is above the Nyquist frequency. An open question is if that sampling rate is enough for our purposes. Eigendecomposition of the accelerometer covariance matrix could identify redundant sensing axes before developing classification methods.



\## Week 1 Tuesday Bridge

One simplified measure of correct dental hygiene technique can be defined by amount of force applied during cleaning ($F\in[F_{min},F_{max}]$). The observed force ($F_{obs}$) can fall into one of three possible events $\{A:F_{obs} \lt F_{min};\ B:F_{min} <= F_{obs} \le F_{max};\ C:F_{max} \lt F_{obs}\}$, where the event for the correct technique is $Event\ B$. Each of these events are disjoint, so $P(A)+P(B)+P(C) = 1$.

\## Week 1 Wednesday Notes

Focus of todays Linear Algebra work is Diagonalization ($A = PDP^{-1}$) where P is the matrix of eigenvectors and D is a diagonal matrix where the diagonals are the eigenvalues. The eigenvectors and eigenvalues must be in the same order. Completed the proof diagonalization. Calculated examples that demonstrated diagonalization. Also proved that $A^n = PD^nP^{-1}$. A brute force hand calculation of $A^3$ and $PD^nP{-1}$ confirmed this relationship. 

$$
A=\begin{bmatrix}
3 & 1 \\
0 & 2
\end{bmatrix}
$$
$$
P=\begin{bmatrix}
1 & -1 \\
0 & 1
\end{bmatrix}
; 
D=\begin{bmatrix}
3 & 0 \\
0 & 2
\end{bmatrix}
;P^{-1}=
\begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix}
$$
$$
A^3 = \begin{bmatrix}
3 & 1 \\
0 & 2
\end{bmatrix}\begin{bmatrix}
3 & 1 \\
0 & 2
\end{bmatrix}\begin{bmatrix}
3 & 1 \\
0 & 2
\end{bmatrix}
$$
$$
A^3 = \begin{bmatrix}
9 & 5 \\
0 & 4
\end{bmatrix}\begin{bmatrix}
3 & 1 \\
0 & 2
\end{bmatrix} = \begin{bmatrix}
27 & 19 \\
0 & 8
\end{bmatrix}
$$
$$
A^3 = \begin{bmatrix}
27 & 19 \\
0 & 8
\end{bmatrix} 
=\begin{bmatrix}
1 & -1 \\
0 & 1
\end{bmatrix}
\begin{bmatrix}
3 & 0 \\
0 & 2
\end{bmatrix}^3
\begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix}
$$
$$
A^3 = \begin{bmatrix}
27 & 19 \\
0 & 8
\end{bmatrix} 
=\begin{bmatrix}
1 & -1 \\
0 & 1
\end{bmatrix}
\begin{bmatrix}
27 & 0 \\
0 & 8
\end{bmatrix}
\begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix}
$$
$$
A^3 = \begin{bmatrix}
27 & 19 \\
0 & 8
\end{bmatrix} 
=\begin{bmatrix}
27 & 19 \\
0 & 8
\end{bmatrix}
$$

I calculated the Fibonnaci eigenvalues as well. The Fibonacci Matrix is: 

$$
F = \begin{bmatrix}
1 & 1 \\
1 & 0
\end{bmatrix} 
$$

The eigenvalues and eigenvectors are:
$$
\lambda_1=\frac{1+\sqrt{5}}{2} \approx 1.618
$$
<!--
$$
v_1 = 
\begin{bmatrix}
\frac{1+\sqrt{5}}{2}\\\\\\\\ 1
\end{bmatrix} 
$$

\lambda_2=\frac{1-\sqrt{5}}{2}\approx-0.618;\ v_2 = \begin{bmatrix}\frac{1-\sqrt{5}}{2}\\ 1
\end{bmatrix} 
\\
$$
Notice that the eigenvalue of $\lambda_1$ is the golden ratio. -->
