> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the odd five-mode boundary reduction

Date: 2026-09-13. Reviewer: audit_sources.
Target: raw_odd_toeplitz_five_mode_boundary_reduction.md.
Result: **FULL PASS. No correction required.**

The proof establishes fixed-rank exceptional boundary spaces for the actual normalized odd matrix and its actual high compression. It does not estimate the remaining exceptional singular values. This review uses exact identities and finite-dimensional arguments only; no singular-value or degree scan was performed.

## 1. Two-parity symbol and normalization

For p(z)=u(z^2)+zv(z^2), the positive metric becomes two copies of the weight |1+t|^(2m+2), with t=z^2 and degree bounds <=m. Haar measure pushes forward without an extra factor. Pairing z with -z removes the opposite parity terms.

Relative to the positive weight, the original signed scalar symbol is e^z/(z+z^-1). Its two-by-two paired entries are


$$
\frac{\sinh z}{z+z^{-1}},\quad
 \frac{z\cosh z}{z+z^{-1}},\quad
 \frac{z^{-1}\cosh z}{z+z^{-1}},\quad
 \frac{\sinh z}{z+z^{-1}}.
$$


Replacing z^2 by t gives exactly


$$
a(t)=\frac1{1+t}\begin{pmatrix}ts(t)&tc(t)\\c(t)&ts(t)\end{pmatrix}.
$$


In particular the asymmetric factors t in the upper-right and absence of t in the lower-left are correct.

The compression in the weighted Hilbert space has the actual sesquilinear matrix A_n in monomial coordinates. Passage to an orthonormal coordinate system gives G^(-1/2)A_nG^(-1/2), not a transposed or differently normalized matrix. The inherited norm bound C_0=e sqrt(5/4) therefore applies exactly.

The multiplier a is allowed to be unbounded on the full Hilbert space. Every Laurent polynomial used later is bounded near t=-1, and multiplication by a produces at most a simple pole. Its squared norm is locally bounded by a multiple of |1+t|^(2m), which is integrable even for m=0. This checks the crucial domain endpoint.

## 2. Inverse symbol, truncation and operator error

The identity c^2-ts^2=1 gives det a=-t/(1+t)^2. Direct inversion yields


$$
r=(1+t)\begin{pmatrix}-s&c\\c/t&-s\end{pmatrix}.
$$


Thus a r=I almost everywhere; no square-root branch is involved because c and s are entire power series.

The truncated r_1 has the stated row and column absolute-sum bound 16/3 on |t|=1. This bounds its Euclidean matrix norm and its multiplication operator on any of the weighted spaces. Orthogonal compression consequently preserves that same upper bound.

I independently multiplied a r_1. The diagonal is d=c c_1-ts s_1, and the off-diagonal entries are th and h, where h=s c_1-c s_1. Writing delta c=c_1-c and delta s=s_1-s,


$$
|d-1|+|h|\le(|c|+|s|)(|\delta c|+|\delta s|).
$$


The series tails sum to e-8/3, and |c|+|s|<=e. Since the two off-diagonal entries have the same modulus on the circle, both the row-sum and column-sum bounds give


$$
\|a r_1-I\|\le e(e-8/3).
$$


The numerical value is approximately 0.1403; the proof only needs the rigorous source bound <1/4. The elementary e<11/4 estimate gives <11/48, which is sufficient. This error multiplier is bounded on the whole Hilbert space, unlike a itself.

## 3. The five-dimensional quotient and legitimate compression identity

The entries of r_1 have powers between -1 and 2. Only its lower-left entry contains t^-1. For inputs in P_m:

- powers m+1 and m+2 can occur in either output component;
- power -1 can occur only in the second component.

Its coefficient there depends only on the constant coefficient of the first input. Therefore the image modulo the polynomial space is contained in the span of exactly the five displayed Laurent boundary directions.

Orthogonal projection need not preserve monomial coefficients, but it annihilates the original polynomial space. Thus applying I-P to the algebraic extension has rank at most five. The proof correctly uses this quotient dimension instead of assuming that weighted projection is ordinary truncation.

For every input in the finite polynomial space,


$$
AR=P M_aP M_{r_1}P
   =P M_{a r_1}P-P M_a(I-P)M_{r_1}P.
$$


All separate vectors lie in the Laurent-polynomial domain checked above. Hence


$$
AR=I+E-F,\quad \|E\|\le\delta,\quad \operatorname{rank}F\le5
$$


is a valid finite-dimensional identity. It does not require extending M_a to a bounded operator on the full space.

The auxiliary bound ||F||<=1+delta+C_0R_0 follows directly from this identity. It introduces no unproved weighted projection bound.

## 4. Singular values of the full matrix and high compression

On ker F, of dimension at least N-5, the identity implies


$$
\|ARx\|\ge(1-\delta)\|x\|.
$$


The singular-value min-max principle gives s_(N-5)(AR)>=1-delta, and the product inequality
s_j(AR)<=||R||s_j(A)
gives s_(N-5)(A)>=(1-delta)/R_0. With delta<1/4 and R_0=16/3, the stated sigma_*=9/64 is valid. For N<=5 the assertion is only a count, as the source explicitly states.

For the actual unit vector v and Pi=I-vv*, on v-perpendicular,


$$
BR_B=\Pi A\Pi R\Pi
 =I+\Pi E\Pi-\Pi F\Pi-\Pi A v v^*R\Pi.
$$


The extra term has rank at most one, so the total correction has rank at most six. The space has dimension N-1, giving s_(N-7)(B)>=sigma_* when N>7. This checks the off-by-one index and retains the actual normalized high compression.

No inverse bound for the exceptional five or six singular values follows from this step. The source does not assert one.

## 5. Exact tail-product comparison

For a codimension-one orthogonal compression, extending B by zero on span(v) gives Pi A Pi. The difference


$$
A-\Pi A\Pi=vv^*A+\Pi A vv^*
$$


has rank at most two. Rank interlacing therefore gives


$$
b_i\ge a_{i+2}\quad(1\le i\le N-2).
$$


The upper inequality b_i<=a_i follows from restriction and projection contractions. Both are valid for arbitrary non-Hermitian matrices; no eigenvalue interlacing has been substituted.

Set k=N-7. For N>=8, all factors exist and


$$
1\le\prod_{i=1}^{k}\frac{a_i}{b_i}
 \le\frac{a_1a_2}{a_{k+1}a_{k+2}}
 \le(C_0/\sigma_*)^2.
$$


Here k+2=N-5, exactly the last full-matrix singular value with a proved uniform lower bound. The cancellation in the middle quotient also holds when k=1.

After these k factors are removed, seven A singular values and six B singular values remain. The first two of those A values, a_(N-6) and a_(N-5), lie in [sigma_*,C_0]. The remaining five/six ratio is precisely


$$
T_m=\frac{\prod_{i=N-4}^{N}a_i}
           {\prod_{j=N-6}^{N-1}b_j}.
$$


The determinant Schur identity det A=det B s_m then gives


$$
\sigma_*^2T_m\le|s_m|
 \le(C_0^4/\sigma_*^2)T_m.
$$


Every comparison factor is independent of N. The fixed finite degrees N<8 are irrelevant to the asymptotic equivalence and are not assigned invalid product indices.

Thus log T_m=o(m) is equivalent to the remaining odd scalar target log|s_m|=o(m). There is no product of N uncontrolled comparison constants.

## 6. Scope and useful next target

The result is stronger than the previously proved indefinite Hermitian gap: it gives an explicit approximate inverse whose failure after compression has uniformly bounded rank. It confines possible small singular values to five modes in the full matrix and six in the actual high compression.

The proof does not exclude exponentially small singular values in those modes. All-index dyadic nonvanishing ensures that the tail product is positive, but supplies no real lower bound. A stable determinant or quantitative inverse estimate on the finite boundary correction remains necessary. The fixed-combination endpoint gcd and the irrationality problem remain separate.

