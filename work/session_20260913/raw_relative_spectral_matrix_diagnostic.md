> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Closed diagnostic of the actual finite spectral matrix

Date: 2026-09-13. Bounded computation by audit_computations.

Only the requested degrees **n=4,8,16** were examined. No canonical HP polynomial was solved for, and no larger degree was sampled. The calculation uses the explicit parity Jacobi operator, its actual amplitudes, and the independently proved branch recurrence.

The singular values and principal angles below are **high-precision numerical estimates**, not interval-certified eigenvalue or singular-value enclosures. A separate analytic bound rigorously controls the Jacobi cutoff error for exact finite eigenpairs. Numerical stability was checked at 100 and 160 decimal digits.

## 1. Results and their limited interpretation

The row-normalized matrix is exactly the one specified in `raw_relative_spectral_truncation.md`:



$$
\widetilde M_{k,l}=\frac{u_k(l)}{
\sqrt{u_k(n-1)^2+u_k(n)^2}},\quad
n+1\le k\le2n-1,\quad0\le l\le n.
$$



The numerical matrices had full row rank. The two-dimensional right kernel was compared with the coordinate plane spanned by columns n−1 and n, using orthonormal right singular vectors.

| n | Smallest nonzero singular value | n² times that value | Nonzero condition number | Two principal angles, degrees |
|---:|---:|---:|---:|---:|
| 4 | 1.10949572640 | 17.7519316224 | 64.2529 | 1.54252515, 20.23911580 |
| 8 | 0.409510484866 | 26.2086710314 | 2.07478 × 10⁶ | 0.40807285, 2.06804391 |
| 16 | 0.00264963954647 | 0.678307723897 | 8.39400 × 10¹⁸ | 0.11772465, 1.05059325 |

The corresponding two principal sines are

| n | Smaller sine | Larger sine |
|---:|---:|---:|
| 4 | 0.0269188905865 | 0.345938827166 |
| 8 | 0.00712215465566 | 0.0360863386390 |
| 16 | 0.00205468135438 | 0.0183352837982 |

These cases do not contradict a polynomial lower bound of the proposed size c/n². They also do not establish one: n²σ_min drops substantially between n=8 and n=16. No rate or monotonicity is inferred from three points.

The global condition number and the absolute smallest singular value convey different information here. At n=16 the largest matrix entry has magnitude approximately 1.05277 × 10¹⁶, while each row's last two entries have squared sum one. Thus the matrix is severely scaled across its columns even though its estimated smallest nonzero singular value is about 2.65 × 10⁻³. Ordinary double precision would be unreliable for this diagnostic. The observed small kernel angles in the last two cases give a reason to study the finite-kernel theorem, but remain evidence only.

## 2. Exact operator and normalization conventions

The Jacobi cutoff is **Legendre degree 64**. Each reflection parity is diagonalized separately. The finite matrix is the principal compression of



$$
S=\Lambda+\tfrac34 I+X^2,
\quad t_l=\frac{l+1}{2\sqrt{(2l+1)(2l+3)}}.
$$



Its diagonal retains $t_{l-1}^2+t_l^2$, including the last $t_l^2$ at the cutoff. It is **not** obtained by squaring a truncated X and losing that returning path.

The finite eigenvector for index l is phased to have positive $\phi_l$ coefficient. Its amplitude is its first parity coefficient for even l and **one half** that coefficient for odd l. The physical row values are computed as



$$
u_k(l)=\begin{cases}
g_l\sqrt{2k+1}\,r_k^{(0)}(\xi_l),&l\text{ even},\\
g_l\sqrt{(2k+1)/3}\,r_k^{(1)}(\xi_l),&l\text{ odd}.
\end{cases}
$$



Thus both the odd amplitude factor and the row radical are retained. The common row radical cancels only in the final normalization. The shifted first-difference recurrence evaluates the branch polynomials.

As an independent normalization control, every computed row/node value was compared with the direct projection of the exact polynomial E_k onto the finite eigenvector. The rational moments used for that check are



$$
\int_0^1x^jP_l(2x-1)dx
=\frac{(j!)^2}{(j-l)!(j+l+1)!}\quad(j\ge l),
$$



and zero for j<l. The raw monic Q recurrence gives F_k by exact coefficientwise factorial division. This builds the known test polynomials only, through k=31; it is not a canonical HP solve.

The largest relative disagreement between the branch and direct-polynomial routes was below 7.76 × 10⁻⁹⁹ at 100 digits and 4.09 × 10⁻¹⁶⁰ at 160 digits. All displayed 55-digit singular-value and angle data agree between the two precision runs. The SVD reconstruction relative residuals were below 10⁻¹⁵⁹ at the higher precision; the largest absolute kernel residual was below 7.09 × 10⁻¹⁵⁷.

## 3. A rigorous bound for the Jacobi cutoff, separated from roundoff

This section concerns the **exact** finite Jacobi matrix and its exact eigenvectors. It does not convert the floating-point diagonalization or SVD into interval arithmetic.

Every parity off-diagonal satisfies



$$
0<t_jt_{j+1}\le\frac1{6\sqrt5}<B:=\frac3{40}.
$$



Let $\widetilde\xi_l$ be its exact finite eigenvalue with index l, and L the largest retained degree in that parity. Finite min-max gives
$\lambda_l+3/4\le\widetilde\xi_l\le\lambda_l+1$.
Above its central coordinate l, backward elimination of the tail tridiagonal system gives



$$
\left|\frac{v_{j+2}}{v_j}\right|
\le\frac{B}{\lambda_{j+2}-\lambda_l-13/40}.
\tag{1}
$$



For a direct proof, start from the last row. Its backward ratio is bounded by $B/(d_L-\widetilde\xi_l)$. Inductively, the next denominator loses at most B because the already bounded next ratio is less than one. Since $d_j-\widetilde\xi_l\ge\lambda_j-\lambda_l-1/4$, this gives (1); all these denominators are strictly positive.

Extending the normalized finite eigenvector by zero leaves only one nonzero residual coordinate outside its parity cutoff. Since its central coefficient has absolute value at most one,



$$
\varepsilon_l:=B
\prod_{j=l+2,l+4,\ldots,L}
\frac{B}{\lambda_j-\lambda_l-13/40}
\tag{2}
$$



is a rational upper bound for its residual norm under the infinite operator. The known disjoint eigenvalue intervals identify the nearby infinite eigenvalue with the same index. A conservative gap to every other eigenvalue is



$$
G_l=2l-1/4\quad(l\ge1),\qquad G_0=7/4.
$$



The spectral theorem bounds the off-eigenvector component by $\varepsilon_l/G_l$, and the normalized vector difference by



$$
e_l:=2\varepsilon_l/G_l.
\tag{3}
$$



Both finite and infinite vectors have positive, near-unit central coordinates, so the aligned sign in this bound agrees with the phase used in the computation. The evaluated residual bounds are far smaller than the spectral gaps.

## 4. Propagating that bound through the actual row normalization

The normalizers can be very small, so an eigenvector residual alone is insufficient. The following calculation controls their effect explicitly.

The finite-eigenvector version of the amplitude proof is unchanged: its lower principal determinant, min-max intervals, and central-coordinate perturbation bound are the same. For the anchor l=n−1, let m=⌊l/2⌋ and



$$
\eta_l=\frac{3H_m}{23(l+1)},\qquad
G_l^{\rm rat}=\frac{2^{l\bmod2}(l!)^4}
{((2l)!)^2(m!)^2(2l+1)}.
$$



The rational quantity



$$
g_l^{\rm low}=G_l^{\rm rat}
\left(1-\frac1{(16l-1)^2}\right)(1-\eta_l)>0
\tag{4}
$$



is a lower bound for both the exact finite and infinite amplitude. Here $\sqrt{2l+1}\le2l+1$, $\sqrt3\ge1$, $\sqrt{1-x}\ge1-x$, and $e^{-\eta}\ge1-\eta$ deliberately weaken the sharp formula to rational bounds.

Shifted positivity gives $r_k^{(\sigma)}(\xi_l)\ge r_k^{(\sigma)}(1)>0$. Combining (4) with $\sqrt{2k+1}\ge1$ and $1/\sqrt3\ge1/2$ gives the rational lower bound used for each row normalizer:



$$
d_k^{\rm low}=g_l^{\rm low}r_k^{(l\bmod2)}(1)
\begin{cases}1,&l\text{ even},\\1/2,&l\text{ odd}.\end{cases}
\tag{5}
$$



Let N_k be a rational upper bound for $\|E_k\|_2$, obtained by taking an integer ceiling of its exact rational squared-norm square root. Put $E_{\rm all}=\sum_{l=0}^ne_l$, $E_{\rm top}=e_{n-1}+e_n$. The difference of the exact finite and infinite normalized row vectors is at most



$$
\frac{N_k E_{\rm all}}{d_k^{\rm low}}
+\frac{N_k^2E_{\rm top}}{(d_k^{\rm low})^2}.
\tag{6}
$$



Indeed the unnormalized vector difference is at most $N_kE_{\rm all}$, the two-entry norm difference is at most $N_kE_{\rm top}$, each denominator is at least (5), and the retained finite vector has norm at most N_k by Bessel's inequality. Summing (6) over rows bounds the matrix Frobenius norm and hence its operator norm.

The resulting exact-rational bounds, rounded **upward** here for readability, are:

| n | Bound for exact finite-to-infinite normalized matrix difference |
|---:|---:|
| 4 | < 1.54 × 10⁻¹¹⁴ |
| 8 | < 4.26 × 10⁻⁹⁵ |
| 16 | < 7.29 × 10⁻⁴⁹ |

These are analytic cutoff bounds; they do not include floating-point errors. Their exact rational values are saved in the JSON. At n=16 the cutoff bound is approximately 2.75 × 10⁻⁴⁶ times the estimated smallest singular value, so cutoff error is negligible for the displayed diagnostic. The numerical SVD itself remains uncertified.

## 5. Files and next mathematical step

The complete data, including both precision runs, all singular values, both angles, normalizers, residuals, and exact rational cutoff bounds, are in `relative_spectral_matrix_probe.json`. The reproducible computation is `probe_relative_spectral_matrix.py`.

The sample remains closed at n=4,8,16. Its useful conclusion is methodological: the retained-column normalization does not make every matrix entry moderate, but high precision and controlled Jacobi truncation make the finite spectral target measurable. The proof task remains an all-index lower bound for the relevant singular value or a direct cofactor estimate, together with a finite-kernel angle bound. None is inferred from these three numerical cases.
