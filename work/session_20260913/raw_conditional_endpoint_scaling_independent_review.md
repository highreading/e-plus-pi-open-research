> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: conditional endpoint scaling

Date: 2026-09-13. Reviewer: audit_computations.

Reviewed `raw_conditional_endpoint_scaling.md`, Sections 1–4, against the definitions of the reflected polynomial and the proved broad-band concentration theorem. **The argument passes.** Its hypothesis remains the unproved lower bound on the actual endpoint ratio; this review does not remove that hypothesis.

## 1. Derivatives and the endpoint weights

For the reflected polynomial



$$
P_n(t)=\sum_{j=0}^n B_{n,j}\frac{t^{n-j}}{(n-j)!},
$$



the identity is exactly $P_n^{(r)}(0)=B_{n,n-r}$. There is no extra factorial. For the orthonormal shifted Legendre polynomial,



$$
\phi_l^{(r)}(0)=(-1)^{l+r}\sqrt{2l+1}
\frac{(l+r)!}{(l-r)!r!},\qquad l\ge r.
$$



Write $w_l=(-1)^l\sqrt{2l+1}a_l$, so $P_n(0)=\sum_lw_l$. The normalized derivative is



$$
\frac{B_{n,n-r}}{P_n(0)n^{2r}}
=\frac{(-1)^r}{r!}\frac{\sum_lw_l h_{l,r}}{\sum_lw_l},
\quad h_{l,r}=\frac{(l+r)!}{(l-r)!n^{2r}},
$$



with $h=0$ for $l<r$. On the top band, for fixed $r$, $h=1+O_r(w/n)$. On the entire range $|h|\le4^r$. The endpoint absolute mass of the low block is bounded by



$$
\sum_{l\le d}\sqrt{2l+1}|a_l|
\le(d+1)\|\operatorname{Proj}_{\le d}P_n\|_2.
$$



The total absolute endpoint mass dominates $\|P_n\|_2$. Therefore the ratio of the low mass to $|P_n(0)|$ is at most $(d+1)\epsilon_n/\kappa_0$, exactly as claimed. This proves the fixed-r limit and its stated $O_r(1/\log n)$ error. The uniform bound $4^r/(\kappa_0r!)$ follows directly from the same endpoint mass inequality.

## 2. Both entire limits

The reciprocal polynomial uses the derivative coefficient without a Taylor factorial and consequently tends to $e^{-w}$. The scaled reflected polynomial uses an additional factor $1/r!$ and consequently tends to $\sum_r(-1)^rt^r/(r!)^2$. On any fixed disk the two majorants are, respectively,



$$
\frac{(4R)^r}{\kappa_0r!},\qquad
\frac{(4R)^r}{\kappa_0(r!)^2}.
$$



They are summable independently of $n$. Extending the finite coefficient arrays by zeros proves compact uniform convergence by dominated series convergence. Cauchy's formula then supplies convergence of all derivatives on smaller compact disks. No growing-radius claim is used.

## 3. Roots and power sums

On each fixed reciprocal disk, $e^{-w}$ has positive minimum modulus. The reciprocal polynomial is therefore eventually zero-free there, including its boundary. Every nonzero root $\rho$ of $B_n$ corresponds to $w=n^2/\rho$, so the bound $\max|\rho|=o(n^2)$ follows with the correct quantifiers: choose an arbitrary fixed $R$, then pass to sufficiently large $n$, then let $R$ increase. Zero roots cause no problem.

The factorization is



$$
E_n(w)=\prod_{j=1}^n(1-\rho_{n,j}w/n^2).
$$



On a fixed zero-free disk its analytic logarithm normalized at zero converges to $-w$. Comparing coefficients of



$$
\log E_n(w)=-\sum_{k\ge1}\frac{s_{n,k}}{k n^{2k}}w^k
$$



proves the two power-sum assertions with their stated signs. These are complex signed sums. The bound $\max|\rho|\ge |s_{n,1}|/n=n(1+o(1))$ is compatible with, and does not improve, the conditional upper bound.

The simple-zero transport for the entire Bessel-series limit is a direct application of Rouché on an isolated-zero disk. In a conjugation-invariant disk, uniqueness forces the approximating zero to be real when the limiting zero is real.

## 4. Scope

No substantive correction is required. The condition $\kappa_n\ge\kappa_0>0$ is still unproved. Compact convergence cannot be evaluated at the growing arguments corresponding to the actual endpoint. The note proves neither the $O(n)$ polynomial-root bound required by accessory compactness nor a mixed-remainder bound.
