> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Top-two Legendre concentration: exact angles and the remaining graph estimate

Date: 2026-09-13. Bounded investigation by audit_results. The closed
diagnostic set is n=4,8,16, using only the actual F-moment formulas.
No canonical endpoint-matched triple or additional degree was solved.

**Outcome:** the uniform top-two O(1/n) concentration bound is not proved
or disproved. The exact diagnostics support testing it. This note
isolates its precise weighted graph/cofactor criterion and proves why
the natural leading-parity-minor perturbation does not justify it.

## 1. The two-dimensional space and its exact graph

Use the actual moment matrix



$$
M_{k,l}=\int_0^1F_k(x)L_l(x)\,dx,\quad
n+1\le k\le2n-1,\quad0\le l\le n,
$$



where L_l=P_l(2x-1). Its entries are computed from the exact factorial
sum in raw_projected_moment_positivity_attempt.md. Let



$$
A_n=M[:,0,\ldots,n-2],\qquad
B_n^{\rm mom}=M[:,n-1,n].
\tag{1}
$$



The symbol B_n^mom here is a two-column moment block, not the
exponential approximation polynomial. The high-orthogonal space W_n
is the kernel of M in the degree-at-most-n polynomial space and has
dimension2 by the existing rank theorem.

When det A_n is nonzero, put



$$
Z_n=-A_n^{-1}B_n^{\rm mom}.
$$



In orthonormal Legendre coordinates phi_l=sqrt(2l+1)L_l, the low
coefficients are related to the two high coefficients by



$$
\boxed{
G_n=
\operatorname{diag}_{0\le j\le n-2}(2j+1)^{-1/2}\,
Z_n\,
\operatorname{diag}(\sqrt{2n-1},\sqrt{2n+1}).}
\tag{2}
$$



Thus W_n is exactly the graph of G_n over
span(phi_(n-1),phi_n).

If lambda_1<=lambda_2 are the eigenvalues of G_n^*G_n, the two principal
angle sines are



$$
s_i=\sqrt{\frac{\lambda_i}{1+\lambda_i}}.
\tag{3}
$$



In particular, the desired estimate



$$
\|\Pi_{\le n-2}P\|_2\le\frac Cn\|P\|_2
\quad(P\in W_n)
\tag{4}
$$



is equivalent, up to fixed constants for sufficiently large n, to
||G_n||=O(1/n).

If A_n is singular, W_n contains a nonzero polynomial of degree at
most n-2 and the worst principal-angle sine is1. Therefore eventual
nonvanishing of this particular unbordered minor is also necessary.
The dimension2 rank theorem alone does not assert that transversality.

## 2. The predeclared exact diagnostics

The checker forms all entries with exact rational arithmetic and
inverts only A_n. After applying the orthonormal weights, the trace
and determinant of the two-by-two graph Gram matrix are rational.
The reported angle values are rounded evaluations of the resulting
exact quadratic algebraic numbers.

| n | smaller graph singular value | larger graph singular value | worst angle sine | n times worst angle sine |
|---:|---:|---:|---:|---:|
| 4 | 0.02246576417 | 0.36244979094 | 0.34075760166 | 1.36303040664 |
| 8 | 0.00543796382 | 0.03428195462 | 0.03426182738 | 0.27409461906 |
| 16 | 0.00145599362 | 0.01773006494 | 0.01772727883 | 0.28363646125 |

All three A_n determinants are nonzero and negative in the stated
normalization. Every resulting graph basis is checked exactly against
the original moment matrix.

These values are compatible with an eventual C/n theorem, but do
not establish one. The less favorable n=4 angle is not a counterexample
to a big-O assertion with an unspecified constant or threshold.
No curve or asymptotic law is fitted to these three degrees.

The complete rational graph columns and exact two-by-two Gram data
are saved in raw_top_two_angles.json.

## 3. An exact sufficient weighted cofactor estimate

Let D_n=det A_n and let D_(n;j,s) be the determinant of A_n with its
j-th column replaced by the moment column indexed s, for
0<=j<=n-2 and s in{n-1,n}. Cramer's rule and (2) give



$$
\boxed{
\|G_n\|_{\rm F}^2=
\frac1{|D_n|^2}
\sum_{j=0}^{n-2}\sum_{s=n-1}^{n}
\frac{2s+1}{2j+1}|D_{n;j,s}|^2.}
\tag{5}
$$



Since G has two columns, its Frobenius norm and operator norm differ
by at most sqrt2. Therefore the concrete missing theorem is



$$
\boxed{
D_n\ne0,\qquad
\sum_{j=0}^{n-2}\sum_{s=n-1}^{n}
\frac{2s+1}{2j+1}|D_{n;j,s}|^2
\le\frac{C^2}{n^2}|D_n|^2
\quad(n\ge n_0).}
\tag{6}
$$



This is a coherent determinant comparison, with all normalization
factors explicit. Bounding D_n away from zero without comparing its
cofactors does not prove(6). Nor may the numerator and denominator
be replaced independently by isolated positive Cauchy–Binet terms.

The same criterion can be phrased as a graph Schur-complement bound,
but (5) avoids introducing arbitrary row scalings or a large
monomial norm-equivalence factor.

## 4. Why the existing uniform interpolation estimate is insufficient at fixed width

The proved sublinear-band theorem bounds the low spectral projection
at degree d by a polynomial factor times



$$
8^d(2e^3)^n\,\frac{d!}{n!}.
$$



At d=n-2 the factorial ratio is only1/[n(n-1)], while the exponential
factor remains of order (16e^3)^n. Thus that estimate is vacuous for
the top-two target. Merely substituting a fixed width into the proved
bound is not an improvement.

The inverse-Borel expansion and parity interpolation are exact, so a
sharper proof could retain cancellation among their terms. Their
current absolute-value bounds discard precisely that information.
The following calculation shows another concrete loss if one tries
to approximate the projected moment determinant by the first
separated-parity coefficient minor.

## 5. An exact amplification in the leading-minor expansion

This subsection supplies an all-index obstruction to one proposed
method, not a counterexample to the top-two concentration conjecture.

Let C be the coefficient matrix of F_(n+1),...,F_(2n-1), in increasing
row degree and monomial degree. Let I0 contain the first m0 even and
first m1 odd powers, where m_sigma is the number of high rows of that
parity. Let I1 increase only the largest selected even power by2.

The previous separated-parity Vandermonde calculation gives



$$
\frac{\det C_{I_1}}{\det C_{I_0}}
=-\frac{S_n}{[(d+1)(d+2)]^2},
\tag{7}
$$



where d is that largest old even power and



$$
S_n=\sum_{\text{high even }k}k(k+1)
       -\sum_{j=0}^{m_0-1}(2j)(2j+1)>0.
$$



The minus sign is the single crossing of an odd column. This is the
specific pair already established in
raw_inverse_norm_independent_extension.md.

For the low determinant A_n, changing its test basis from shifted
Legendre to monomials multiplies its determinant by one common
positive constant. The relevant Cauchy–Binet terms therefore have
the same ratios as



$$
T_I=\det C_I\,
\det\left[\frac1{i+j+1}\right]_
       {i\in I,\ 0\le j\le n-2}.
\tag{8}
$$



The second determinant is positive and has the exact Cauchy product.
Its ratio can consequently be evaluated without any asymptotics.

### Even degrees

For even n>=4, m0=(n-2)/2 and d=n-4. Direct summation gives



$$
S_n=\frac{(n^2-4)(2n-1)}2.
$$



Replacing d by d+2 changes the Vandermonde factor of the Cauchy
determinant by (n-2)(n-3)/6. Its denominator factor changes by
(n-3)(n-2)/[(2n-4)(2n-3)]. Therefore



$$
\frac{\det H_{I_1}}{\det H_{I_0}}
=\frac{[(n-2)(n-3)]^2}{6(2n-4)(2n-3)}.
$$



Combining with(7) yields the exact identity



$$
\boxed{
\frac{T_{I_1}}{T_{I_0}}
=-\frac{(n+2)(2n-1)}{24(2n-3)}
\sim-\frac n{24}.}
\tag{9}
$$



### Odd degrees

For odd n>=3, m0=(n-1)/2 and d=n-3. Now



$$
S_n=\frac{(n^2-1)(2n-1)}2,
$$



and the Cauchy determinant ratio is



$$
\frac{\det H_{I_1}}{\det H_{I_0}}
=\frac{[(n-1)(n-2)]^2}{2(2n-3)(2n-2)}.
$$



Hence



$$
\boxed{
\frac{T_{I_1}}{T_{I_0}}
=-\frac{(n+1)(2n-1)}{8(2n-3)}
\sim-\frac n8.}
\tag{10}
$$



The individual coefficient-minor ratio in(7) is O(1/n). Integration
against the growing low polynomial block amplifies it into an
unbounded opposite-sign multiple. Thus a Neumann argument that
retains only the first coefficient minor as the reference and
treats all other terms as a small perturbation cannot be justified
by that coefficient-level O(1/n) estimate.

The full determinant may still have cancellations that are favorable
in the quotient(5). Equations(9)–(10) do not evaluate that quotient
or prohibit a proof that retains its common determinant structure.

## 6. What a successful refinement must still prove

The plausible target remains(6), or an equivalent bound for the
two-column weighted graph. A useful proof would control the low
determinant and its top-column replacements together, for example
through a uniform Schur-complement estimate or a parity interpolation
formula in which the cancellations are preserved before taking norms.

The known failures of coefficient total positivity, collocation
Chebyshev structure, and actual projected-moment total positivity
cannot be bypassed by treating all relevant determinant terms as
nonnegative. The present graph diagnostics also do not establish
eventual transversality of A_n.

If the top-two O(1/n) theorem were proved uniformly on W_n, it would
sharpen the already established sublinear spectral concentration.
It would still leave the selected endpoint cancellation ratio to
control: W_n is two-dimensional and contains a nonzero polynomial
vanishing at either chosen endpoint. Endpoint matching must remain
part of any inference about the actual beta_B quotient.

## 7. Files and verification scope

check_raw_top_two_angles.py constructs only the moment blocks n=4,8,16,
checks their exact graph kernels, and saves rational Gram invariants
before displaying angles. The arithmetic diagnostic is fully
reproducible from raw_top_two_angles.json.

Equations(7)–(10) are all-index algebraic calculations from the
separated-parity Vandermonde and Cauchy determinant products. They
are not inferred from the three angle measurements.
