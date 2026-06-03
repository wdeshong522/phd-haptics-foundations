# Week 3 Notes
## Week 3 Monday Notes
### Casella Berger 2.1-2.3

Given a random variable $X$ with a known distribution, and a function $Y = g(X)$, find the distribution of $Y$.

---

#### Key Intuition: Compression and Stretching

When a transformation $g$ maps X-values to Y-values, the density of Y in any region depends on how much of the X-domain maps into it:

- **Compression** $\rightarrow$ many X-values crowd into a small Y-region $\rightarrow$ **high density**
- **Stretching** $\rightarrow$ few X-values spread across a large Y-region $\rightarrow$ **low density**

**Example:** $Y = X^2$, $X \sim \text{Uniform}(0,1)$

- Small X-values (near 0) get compressed into an even smaller Y-region near 0 $\rightarrow$ high density near $y = 0$
- Large X-values (near 1) spread across more Y-space $\rightarrow$ lower density near $y = 1$

This is confirmed by the resulting pdf: $f_Y(y) = \frac{1}{2\sqrt{y}}$, which is large near 0 and equals $\frac{1}{2}$ at $y = 1$.

---

#### The CDF Method

The standard technique for deriving the distribution of $Y = g(X)$.

#### General Recipe

1. Write $F_Y(y) = P(Y \leq y) = P(g(X) \leq y)$
2. Solve the inequality to express it in terms of $X$
   - If $g$ is **non-monotone**, split the domain into monotone pieces
3. Recognize and evaluate $F_X(\cdot)$
4. Differentiate to obtain $f_Y(y) = \frac{d}{dy} F_Y(y)$

---

#### Worked Examples

#### Example 1: Monotone transformation

$X \sim \text{Uniform}(0,1)$, $Y = X^2$

$$F_Y(y) = P(X^2 \leq y) = P(X \leq \sqrt{y}) = F_X(\sqrt{y}) = \sqrt{y}$$

$$f_Y(y) = \frac{d}{dy}\sqrt{y} = \frac{1}{2\sqrt{y}}, \quad y \in (0,1)$$

#### Example 2: Non-monotone transformation

$X \sim \text{Uniform}(-1,1)$, $Y = X^2$

The inequality $X^2 \leq y$ gives $-\sqrt{y} \leq X \leq \sqrt{y}$, so:

$$F_Y(y) = P(-\sqrt{y} \leq X \leq \sqrt{y}) = F_X(\sqrt{y}) - F_X(-\sqrt{y})$$

Since $f_X(x) = \frac{1}{2}$ on $(-1,1)$, we have $F_X(x) = \frac{x+1}{2}$:

$$F_Y(y) = \frac{\sqrt{y}+1}{2} - \frac{-\sqrt{y}+1}{2} = \sqrt{y}$$

$$f_Y(y) = \frac{1}{2\sqrt{y}}, \quad y \in (0,1)$$

> **Note:** Same pdf as Example 1 — by symmetry of Uniform(-1,1) around 0, squaring folds the negative side onto the positive side, recovering the same distribution.

---

#### Key Principle for Non-Monotone Functions

When $g(X)$ is not monotone, **partition the support of X into intervals on which $g$ is monotone**, then sum contributions:

$$F_Y(y) = \sum_i P(X \in A_i(y))$$

where each $A_i(y)$ is the subset of the $i$-th monotone piece satisfying $g(X) \leq y$.

---

## Research Bridge

**White Cane Project:** If vibration envelope amplitude $X \sim \mathcal{N}(\mu, \sigma^2)$, the CDF method gives the distribution of $Y = |X|$ (absolute amplitude) — relevant when computing power or RMS from raw accelerometer data.

The CDF method also underlies **inverse transform sampling**, used to generate random variates from any distribution in simulation — directly applicable to the stochastic surface texture model in MSIM 510.

$e^{\frac{-x^2+2(\mu + t\sigma^2)x-\mu^2}{2\sigma^2}}$



### Casella & Berger §2.2 — Expected Values and LOTUS

#### Core Result
For a random variable X with pdf $f_X$, the expected value of any function $g(X)$ is:
$$E[g(X)] = \int_{-\infty}^{\infty} g(x) f_X(x) \, dx$$

This is the **Law of the Unconscious Statistician (LOTUS)** — use $f_X$ directly without first deriving the distribution of $g(X)$.

**Verification:** For X ~ Uniform(0,1), Y = X², both routes give E[Y] = 1/3:
$$E[Y] = \int_0^1 y \cdot \frac{1}{2\sqrt{y}} dy = \int_0^1 x^2 \cdot 1 \, dx = \frac{1}{3}$$

#### Linearity of Expectation

$$E[aX + b] = aE[X] + b$$
$$E\left[\sum_i a_i g_i(X)\right] = \sum_i a_i E[g_i(X)]$$

**Why it works:** Linearity of the integral directly gives linearity of expectation. No independence assumptions required — holds universally.

#### Research Bridge
**White Cane Project:** RMS amplitude is grounded in the second moment $E[X^2]$, computable via LOTUS directly from $f_X$. Linearity of expectation justifies combining moment-based features across accelerometer axes additively.

---

### Casella & Berger §2.3 — Moment Generating Functions

#### Definition
$$M_X(t) = E[e^{tX}] = \int_{-\infty}^{\infty} e^{tx} f_X(x) \, dx$$

#### Why $e^{tX}$? — The Taylor Series Motivation
$$M_X(t) = 1 + tE[X] + \frac{t^2}{2!}E[X^2] + \frac{t^3}{3!}E[X^3] + \cdots$$

Every moment of X is encoded in M_X(t). To extract the n-th moment:
$$E[X^n] = \left.\frac{d^n}{dt^n} M_X(t)\right|_{t=0}$$

#### Uniqueness Theorem
> If $M_X(t) = M_Y(t)$ for all t in some open interval around 0, then X and Y have the same distribution.

#### Key MGFs

**Bernoulli(p):**
$$M_X(t) = 1 - p + pe^t$$

**Binomial(n,p):** MGFs multiply under independence:
$$M_X(t) = (1-p+pe^t)^n$$

**Normal($\mu$, $\sigma^2$):** Derived by completing the square — remaining integral is a Normal pdf integrating to 1:
$$M_X(t) = e^{t\mu + \frac{t^2\sigma^2}{2}}$$

#### MGF of a Sum of Independent RVs
$$M_{X+Y}(t) = M_X(t) \cdot M_Y(t)$$

#### Research Bridge
**White Cane — Surface Transition Detection:**

The white cane system is a **transition detection** problem, not surface identification. A user needs to know *when* the surface changes, not *what* it is — and some surfaces may be perceptually indistinguishable even when statistically distinct.

If surface class k has amplitudes $\sim N(\mu_k, \sigma_k^2)$, its MGF is:
$$M_k(t) = e^{t\mu_k + \frac{t^2\sigma^2_k}{2}}$$

By the uniqueness theorem, two surfaces are statistically distinguishable iff their MGFs differ. The magnitude of difference between consecutive MGFs determines perceptual salience. This reframes the goal: detect when the moment structure of the signal has shifted — a distributional change detection problem. KL divergence (Week 16, Bishop) is the natural measure of that shift.