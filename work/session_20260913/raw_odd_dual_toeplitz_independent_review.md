> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the odd signed Toeplitz reduction

Date: 2026-09-13. Reviewer: audit_sources.
Target: raw_odd_dual_toeplitz_scalar_obstruction.md.
Result: **PASS**, with one corrected frozen-example transcription noted below.

This review checks the positive-weight comparison, actual parity dimensions, indefinite Hermitian structure, compressed matrix, and scalar normalization. The subsequently reviewed added-column theorem proves the scalar is nonzero in every degree; the unsolved quantitative condition remains log|s_m|=o(m). No numerical scan or positivity assumption for the odd symbol is used.

## 1. Actual dimension and comparison Gram matrix

For n=2m+1, the actual coefficient space has dimension n+1=2m+2. Splitting


$$
p(z)=u(z^2)+zv(z^2),\quad \deg u,\deg v\le m,
$$


gives two spaces of the same dimension L=m+1. The weight


$$
G:\quad |1+z^2|^{2m+2}
$$


is invariant under z -> -z, so its cross-parity blocks vanish exactly. Each diagonal block is the L-square binomial Toeplitz matrix with parameter m+1. This checks both the dimension and the index in formula (5).

The actual complex symbol remains e^(e^(i theta))(2cos theta)^(2m+1). It has not been replaced by the positive comparison weight.

## 2. Positive-weight comparison and Cauchy recurrence

The Cayley substitution t=(1+iy)/(1-iy), with u(t)=P(y)/(1-iy)^m, gives exactly


$$
I_a(u)=\frac{4^a}{\pi}\int_{\mathbb R}
 |P(y)|^2(1+y^2)^{-a-m-1}\,dy.
$$


Consequently I_a/I_(a+1) is one quarter of the mean of 1+y^2 in the measure with exponent beta=a+m+2.

I independently checked the Rodrigues normalization for the weight (1+y^2)^(-beta). The polynomial obtained by multiplying the jth derivative of (1+y^2)^(j-beta) by (1+y^2)^beta has leading coefficient


$$
(-1)^j(2\beta-2j)_j.
$$


After division by this coefficient and integration by parts j times, its squared norm is


$$
h_j=\frac{j!}{(2\beta-2j)_j}
       \int_{\mathbb R}(1+y^2)^{j-\beta}\,dy.
$$


All relevant norms and integrations by parts are valid through j=m+1 for beta=2m+2 or 2m+3. In particular the endpoint case m=0,beta=2,j=1 has integrable quadratic norm and vanishing boundary terms; it is not silently excluded.

Taking the norm ratio, including the beta-integral ratio, gives


$$
\alpha_j=\frac{j(2\beta-j)}{(2\beta-2j)^2-1}.
$$


For the stated j range, the numerator increases and the positive denominator decreases as j increases. At j=m+1,beta=2m+2 the value is


$$
\frac{3(m+1)^2}{4(m+1)^2-1}\le1.
$$


The value decreases as beta increases. Thus all needed orthonormal recurrence coefficients sqrt(alpha_j) are at most one. The rectangular multiplication map by y, from degrees <=m to <=m+1, has norm at most two. It uses no coefficient beyond alpha_(m+1). This remains true for complex coefficient vectors.

Therefore the mean of 1+y^2 is at most five, giving exactly


$$
I_m\le(5/4)I_{m+1},\qquad I_{m+1}\le(5/4)I_{m+2}.
$$


The fixed 5/4 is uniform in m; no fixed-degree constant is reused at a growing degree.

## 3. Full normalized operator norm

Cauchy–Schwarz with weights |2cos theta|^(2m) and |2cos theta|^(2m+2) gives the correct split for the odd power 2m+1. Applying the first comparison separately to the two parity components yields


$$
\|G^{-1/2}AG^{-1/2}\|\le e\sqrt{5/4}.
$$


Both arguments of the bilinear form are retained; no unjustified contraction of a projection or comparison of non-Hermitian quadratic forms is involved.

## 4. Signed subspaces and the Hermitian gap

The spaces


$$
P_+=(1+z)u(z^2),\qquad P_-=(1-z)u(z^2)
$$


each have dimension L and are orthogonal in the G metric. Their cross product contains bar(z)-z, whose integral against the pi-periodic remaining factor vanishes. Each squared G norm is 2I_(m+1)(u).

Pairing theta and theta+pi gives exactly


$$
2(2x)^{2m+1}\cos y[\sinh x+x\cosh x],
$$


and


$$
2(2x)^{2m+1}\cos y[\sinh x-x\cosh x]
$$


for the plus and minus quadratic forms, with x=cos theta,y=sin theta. In particular the plus form is at least 2cos(1)I_(m+1), and the negative of the minus form is at least cos(1)I_(m+2)/12. The latter factor 1/12 follows from converting (2/3)x^3(2x)^(2m+1) to a multiple of (2x)^(2m+4).

After division by the G norm and use of the second weight comparison, the constants are exactly


$$
a=\cos1,\qquad b=\cos1/30.
$$


In the orthogonal decomposition, the Hermitian part has blocks A_+>=aI and A_-<=-bI. Its Schur complement is negative definite with inverse norm at most 1/b. The congruence factorization gives


$$
\|H^{-1}\|\le(1+C_0/a)^2/b
$$


and exactly L positive and L negative eigenvalues. This statement is about H, not the original non-Hermitian A. The source correctly refrains from using this indefinite gap as an accretivity estimate for A.

## 5. Actual compressed matrix and scalar identity

The inverse corner of G is the ratio of consecutive binomial determinants with parameter m+1 and sizes m,m+1:


$$
c_m=\frac{((2m+1)!)^2}{m!(3m+2)!}.
$$


This is distinct from the even-degree comparison factor.

For v=G^(-1/2)e_0/sqrt(c_m), the kernel of Pi Atilde corresponds exactly to coefficient vectors q for which Aq lies in span(e_0). The already proved rank of the n high rows gives a one-dimensional kernel. Its generator x=G^(1/2)q satisfies


$$
v^*x=q(0)/\sqrt{c_m}\ne0.
$$


Hence the kernel has trivial intersection with v-perpendicular, proving the square compression B invertible. This uses the actual high-row system and the actual q(0) theorem. It does not follow merely from a generic principal-minor assertion.

The Schur vector k=v-B^(-1)Pi Atilde v obeys v^*k=1 and Pi Atilde k=0. Comparing x with k and applying the normalized equation yields


$$
n!V_n(1)=q(0)s_m/c_m.
$$


Using q(0)=(2n)![t^n]V_n gives precisely the factor


$$
B_m^{\rm odd}
 =\frac{(4m+2)!\,m!\,(3m+2)!}{((2m+1)!)^3}.
$$


The scalar is real. The inverse identity v^*Atilde^(-1)v=1/s_m and the upper bound C_0+C_0^2||B^(-1)|| have their correct normalizations.

## 6. Incorporating the newly proved nonvanishing

The independently reviewed raw_dual_endpoint_added_column_dyadic.md now proves V_n(1)!=0 for all n and


$$
V_n(1)/[t^n]V_n\in1+2^{v_2(2n)}\mathbb Z_2.
$$


Thus s_m is nonzero for every m>=0. Also


$$
(A^{-1})_{00}=c_m/s_m,\quad
 v_2((A^{-1})_{00})=n,
$$


so


$$
v_2(s_m)=v_2(c_m)-n=-v_2(B_m^{\rm odd}).
$$


These are dyadic statements. They do not supply a real lower bound or a sign for s_m. The old zero obstruction is resolved; the subexponential real-size condition remains open.

Stirling's formula applied to B_m^odd gives the displayed n log n+[(3/2)log3-1]n+O(log n). Therefore log|s_m|=o(n) is exactly the remaining condition for the stated odd root-product limit. The optional upper estimate through ||B^(-1)|| and a separate lower estimate for |s_m| remain distinct requirements.

## 7. Corrected frozen example

The frozen n=1 data have U_1(t)=3-2t and therefore


$$
q_1(z)=-2+3z,
$$


not 3-2z. The author caught and corrected this reversal transcription during the audit. The matrices in the original note were already correct:


$$
A=\begin{pmatrix}1&1\\3/2&1\end{pmatrix},\quad G=2I.
$$


Indeed A(-2,3)^T=(1,0)^T, s_0=-1/4, and B_0^odd=4. Thus V_1(1)/[t]V_1=-1, as asserted. No general equation or matrix normalization was affected by the transcription.

## 8. Final scope

The entire reduction passes. It establishes a uniform positive comparison metric, bounded full normalized operator, uniformly invertible indefinite Hermitian part, and an always-defined actual scalar Schur complement. Together with the added-column theorem that scalar is nonzero.

It does not estimate the small singular value of the non-Hermitian compression B or the real magnitude of s_m. It does not produce an odd-degree shrinking integer form, control fixed endpoint gcd cancellation, or prove irrationality of e+pi.

