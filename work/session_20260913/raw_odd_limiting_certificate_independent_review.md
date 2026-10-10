> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the odd limiting determinant certificate

Date: 2026-09-13. Reviewer: audit_sources.
Status: PASS after a fresh run of the identical certificate. No mathematical correction required.

Reviewed in full:
- raw_odd_limiting_determinant_interval_certificate.md;
- check_raw_odd_limit_interval_certificate.py;
- raw_odd_limit_certificate_vectors.json;
- the regenerated raw_odd_limit_interval_certificate.json;
- the operator and endpoint normalization in raw_odd_boundary_operator_limit.md.

This is a rigorous interval certificate for one fixed limiting operator, with explicit bounds for every infinite tail. It is not a numerical inference from a finite sample of canonical degrees.

## 1. Reproduction, input exactness, and rounding

The successful independent invocation was


$$
\texttt{/opt/homebrew/bin/python3.12 work/session\_20260913/check\_raw\_odd\_limit\_interval\_certificate.py}.
$$


The bundled mpmath version is 1.4.1. The default system Python is too old to import this version; that failed import was resolved by using the displayed interpreter, without changing the certificate, vectors, or precision.

All three inputs contain 128 scalar complex coordinates. Their 768 real/imaginary entries are specified as ratios of integers, with positive power-of-two denominators of exponents 47 through 117. The verifier converts these directly to interval rationals. It does not read the exploratory floating-point inverse or the saved NPZ file.

The exact input hashes at review were:

    verifier SHA256:
    4b4a7230b19a9fbf0911afb16c06e9c45ba25c69382e25b58b62a2f8330cc80f

    vector JSON SHA256:
    196c620cad7043be1932aaae4fc07f8192351053a2e0f9a1ce50d01e75ecc83f

I inspected the interval arithmetic paths used here. Basic real operations take lower endpoints with floor rounding and upper endpoints with ceiling rounding. Complex operations are composed of these real interval operations. The interval constants, square roots, and cosine use enclosing endpoints; the cosine implementation includes quadrant extrema. Integer complex powers use interval repeated squaring. Strict interval comparisons only return true when the whole first interval lies on the indicated side of the second. The code does not convert a working enclosure back to an ordinary float.

The use of an upper endpoint through $\texttt{x.b}$ is safe: it returns a degenerate interval at the enclosing upper bound. The componentwise absolute-sum function is an upper bound for the complex modulus, and each widening contains the full complex error disk claimed in the proof.

The only clarification requested from the author was to record the explicit Python interpreter for reproducibility.

## 2. Symbol, annulus, quadrature, and all Fourier coefficients

The exact exponential of $J(y)=\left(\begin{smallmatrix}0&t\\1&0\end{smallmatrix}\right)$, with $J(y)^2=tI$, is


$$
F(y)=\begin{pmatrix}c(t)&t\,s(t)\\s(t)&c(t)\end{pmatrix}.
$$


This matches the verifier, including the upper-right $t$ factor.

For $R=4/3$, the annulus has


$$
|\Im y|\le(\sqrt3/2)(R-R^{-1})=7\sqrt3/24<17/33.
$$


Thus the denominator $1-iy$ is nonzero there and $|t|<25/8$. The row and column absolute sums are bounded by
$\cosh(9/5)+(9/5)\sinh(9/5)<16$. The induced matrix norm is therefore below 16, yielding


$$
\|F_k\|\le16R^{-|k|}.
$$


The annular holomorphy justifies the matrix Cauchy estimate. The symmetry $\zeta\mapsto\zeta^{-1}$ gives $F_{-k}=F_k$, without transpose or adjoint.

For every $0\le k\le128$, summing all aliases $k+\ell M$, $\ell\ne0$, gives exactly the conservative bound


$$
32R^{-(M-128)}/(1-R^{-M}).
$$


The paired cosine quadrature is the exact periodic trapezoidal sum for this even Fourier symbol. The cosine recurrence in the verifier has the correct initial values and index update.

At each true real quadrature node, $|t|=1$. After terms $j=0,\ldots,23$, the remainder of either entire series is less than $2/48!$. The code widens both real and imaginary components before multiplying by $t$, so the construction of the upper-right entry also retains its series error. It then adds the analytic alias bound to every coefficient. No quadrature or Fourier tail is omitted.

## 3. Full residuals and inverse estimates

The finite-support vectors use positions $0,\ldots,63$. The code computes $Ef$ through position 128, enough to evaluate $A_0Ef$ through position 127. The negative neighbor in row zero is explicitly zero. Both off-diagonal signs of $A_0$ agree with the independently reviewed limiting operator.

For the omitted output from row 128 onward, only $Ef$ from row 127 onward can contribute. Since


$$
\|Y\|=\sqrt3,\qquad \|A_0\|=1,
$$


the norm of this output tail is at most the norm of that input tail. Its first Fourier exponent is $127-64+1=64$, exactly the exponent $128-L$ used in the bound. Summing the squared geometric tail gives the denominator $\sqrt{1-R^{-2}}$. The finite weighted input sum is also enlarged by a componentwise absolute sum, so its use is conservative.

The endpoint right-hand side is


$$
v_r=\sqrt{2/3}(i/\sqrt3)^r(1,0)^{\mathsf T},
$$


with the same phase as in the operator-limit theorem. Its tail from row 128 has norm $3^{-64}$, as used. The other two right-hand sides have no tail.

The inverse estimate $\|(A_0E)^{-1}\|<12$ follows from the already proved base accretivity and does not use the approximate finite inverse. The full residual is the sum of a certified prefix bound and these tail bounds. Multiplication by 12 is therefore a valid Hilbert-space solution error estimate.

The independent run obtained solution errors below

    3.507717e-13,  2.826125e-12,  1.681508e-11.

These errors certify the saved vectors regardless of how they were discovered.

## 4. Boundary testing and determinant propagation

The outside row is $Wf=\sum_{s\ge0}F_{s+1}f_s$, since the row index is $-1$. The code uses this orientation and then multiplies by $J_b$ with the correct signs. The saved vectors have finite support, so their boundary tests are computed entirely from certified coefficients.

An actual solution error $\delta$ enlarges each upper boundary component by $3\delta$, using $\|V\|<3$. The lower row is paired with the exact geometric vector on the finite support; its missing solution error is at most $\delta$, because $\|v\|=1$. There is no unbounded truncation of the test functional.

The resulting intervals are inserted into the exact determinant formulas, with the two $U$ columns first and the $v$ column last. The same row/column order is used by the operator theorem.

The independent output again gives the strict rational enclosures


$$
\frac{62}{100}<\det D_{2,+}<\frac{63}{100},\qquad
-\frac{136}{100}<\det D_{3,+}<-\frac{135}{100},
$$


and


$$
-\frac{47}{100}<\frac{\det D_{2,+}}{\det D_{3,+}}
<-\frac{45}{100}.
$$


For reference, the narrower real enclosures from the fresh run are contained in

    det D2: (0.6237783705708, 0.6237783705940),
    det D3: (-1.3537731100203, -1.3537731098479).

Reality is proved independently of the small interval imaginary widths. Since
$\overline{F_k}=(-1)^kF_k$, conjugation by the coordinate phases $i^r$ makes $E,A_0,v,U$ real. The row $W$ is purely imaginary in this gauge and its phase is canceled by the imaginary matrix $J_b$. Thus the boundary matrices and their determinants are real.

## 5. Consequences and limits of the result

The independently reviewed convergence of the finite boundary matrices and these nonzero limiting determinants prove


$$
s_m\longrightarrow s_\infty\in(-0.47,-0.45).
$$


The exact positive factorial prefactor in the odd endpoint identity then gives the claimed odd absolute root-product limit $3\sqrt3/e$. The previously proved even limit combines with it to give the all-degree absolute limit. The odd endpoint ratio is eventually negative.

The large-$m$ inverse bounds also follow correctly. Woodbury applies to the finite rank-two correction because $D_{2,m}^{-1}$ is eventually uniformly bounded. The high-compression inverse formula divides by $v^*A_m^{-1}v=1/s_m$, which tends to a nonzero value. All exterior factors already have uniform bounds.

No effective first degree follows from the qualitative operator-limit theorem. No signed dual remainder estimate, global primitive-denominator estimate, or proof about the rationality of $e+\pi$ follows merely from this certificate.

The interval calculation and its operator link pass in full.

