> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Top-two graph audit and exact Newton–Cauchy resummation

Date: 2026-09-13. Independent review of
`raw_top_two_concentration_attempt.md`, followed by a bounded symbolic
resummation. The graph and amplification formulas pass. The new
resummation is exact but supplies no uniform determinant lower bound
or top-two concentration estimate.

## 1. Graph, cofactor, and angle normalization

Writing a polynomial as sum p_l L_l, with
phi_l=sqrt(2l+1)L_l, gives p_l=sqrt(2l+1)a_l in orthonormal coordinates.
Therefore the low-to-high graph matrix is exactly
D_low^(-1/2)(-A^(-1)B)D_high^(1/2), as stated in the reviewed note.
For a graph vector (Gu,u), its squared low fraction is
||Gu||²/(||Gu||²+||u||²). The principal-angle sines are consequently
sqrt(lambda/(1+lambda)), where lambda runs over the eigenvalues of
G*G. This validates the equivalence of the uniform top-two estimate
with ||G||=O(1/n), once the graph exists.

If A is singular, a nonzero vector in ker A gives a polynomial entirely
in the low space and still in the full high-orthogonal kernel. The
worst angle sine is then one. Thus the particular unbordered minor's
eventual nonvanishing cannot be inferred from the known full row rank.

Cramer's rule gives a graph entry -D_(j,s)/D. Squaring and inserting
the orthonormal weights gives exactly the reviewed weighted cofactor
sum. The Frobenius/operator comparison has factor at most sqrt2
because there are two columns. No row scale or factorial is missing.
The diagnostic Gram trace and determinant can indeed be rational even
though its off-diagonal entry has a square-root weight.

## 2. Independent verification of the amplified adjacent terms

Put r=n-1. The first selected monomial set I0 is



$$
I_0=\begin{cases}
\{0,1,\ldots,n-3,n-1\},&n\text{ even},\\
\{0,1,\ldots,n-2\},&n\text{ odd}.
\end{cases}
$$



The largest selected even power is d=n-4 in the even case and d=n-3
in the odd case. Replacing d by d+2 crosses exactly one selected odd
column. In its even block, replacing the last Newton polynomial
p_(m-1) by p_m multiplies the Vandermonde by
sum lambda_high - sum mu_low. The Borel factorial quotient is
(d!)²/((d+2)!)². This proves the sign and factorial normalization in
the reviewed coefficient-minor ratio.

For the Cauchy moment determinant, changing the row index d to d+2
changes its Vandermonde by (d+1)(d+2)/6 in the even case and by
(d+1)(d+2)/2 in the odd case. The different denominator is caused by
the additional selected odd power d+3 in the even case. Its Cauchy
denominator ratio is, in both cases,



$$
\frac{(d+1)(d+2)}{(d+n)(d+n+1)}.
$$



The two high-minus-low spectral sums are respectively
(n²-4)(2n-1)/2 and (n²-1)(2n-1)/2. Combining these factors reproduces
exactly



$$
-\frac{(n+2)(2n-1)}{24(2n-3)},\qquad
-\frac{(n+1)(2n-1)}{8(2n-3)}.
$$



Thus the coefficient-level O(1/n) term becomes an unbounded
opposite-sign multiple after integration. This does not evaluate the
full determinant or its graph quotient. The scope of the reviewed
obstruction is correct.

## 3. Exact resummation of all coefficient columns

Let C be the coefficient matrix of the r high polynomials F_k,
k=n+1,...,2n-1, in monomial degrees0,...,2n-1. Let C0=C[:,I0], and
let E be the complementary degree set; it has r+2=n+1 elements.
The separated-parity Vandermonde proves C0 invertible for n>=3.
Define



$$
H_0=\left(\frac1{i+j+1}\right)_{
i\in I_0,\ 0\le j\le r-1},\quad
H_E=\left(\frac1{D+j+1}\right)_{
D\in E,\ 0\le j\le r-1},
$$





$$
R=C_0^{-1}C[:,E],\qquad W=H_EH_0^{-1},\qquad
\mathcal K=RW.
\tag{1}
$$



The Cauchy determinant makes H0 invertible. If A_mon is the actual
high moment matrix tested against1,x,...,x^(n-2), then



$$
\boxed{A_{\rm mon}=C_0(I+\mathcal K)H_0,\qquad
\det A_{\rm mon}=\det C_0\det H_0\det(I+\mathcal K).}
\tag{2}
$$



This sums all the Cauchy–Binet terms before taking absolute values.
Passing to shifted Legendre test columns adds one known positive
triangular determinant, so it does not change the relative-term
statements in Section 2.

Crucially, W has explicit entries with no numerical inversion. For
b in I0 and any D not in I0,



$$
\boxed{W_{D,b}=
\frac{(b+1)_{\overline r}}{(D+1)_{\overline r}}
\prod_{i\in I_0\setminus\{b\}}\frac{D-i}{b-i}.}
\tag{3}
$$



One proof forms the rational difference
1/(D+t)-sum_b W_(D,b)/(b+t), whose zeros are t=1,...,r.
Its numerator is a constant multiple of product_(j=1)^r(t-j).
Matching residues at -D and at -b gives (3), including its signs.
Equivalently (3) is the ratio of Cauchy determinants with the indicated
row replaced in its original position.

## 4. A single-column family sums as a rank-one determinant

Fix b in I0. Retain the base term and all terms obtained by replacing
only column b by one complementary degree D. In unsorted replacement
order their exact ratios are R_(b,D)W_(D,b). Sorting contributes the
same permutation to the coefficient and moment determinants, so the
product is unchanged. Hence this entire family has normalized sum



$$
\boxed{1+\sum_{D\in E}R_{b,D}W_{D,b}
=1+\mathcal K_{bb}
=\det(I+e_be_b^T\mathcal K).}
\tag{4}
$$



This is a coherent rank-one resummation, rather than a claim that its
individual tail terms are small or share a sign.

For the largest even selected power d=2(m-1), its coefficient row also
has an explicit divided-difference formula. Let lambda_i=k_i(k_i+1)
be the m high even spectral nodes, and write f_k=F_k/q_(k,0). The
polynomial



$$
\Phi_d(x)=(d!)^2\sum_{i=1}^m
\frac{f_{k_i}(x)}{\prod_{j\ne i}(\lambda_i-\lambda_j)}
\tag{5}
$$



has selected coefficients equal to one at d and zero at every other
degree in I0. Indeed the spectral expansion coefficient at degree2s
is the divided difference of the monic polynomial p_s, divided by
((2s)!)²; it vanishes for s<m-1 and equals1 after the factor(d!)²
when s=m-1. Thus



$$
\Phi_d(x)=x^d+\sum_{D\in E}R_{d,D}x^D.
$$



Only even D occur in that sum. Let psi_d be the unique polynomial of
degree at most r-1 satisfying integral x^i psi_d=delta_(i,d) for i in
I0. Formula (3) states exactly integral x^D psi_d=W_(D,d). Therefore
the resummed family is also the explicit scalar integral



$$
\boxed{1+\mathcal K_{dd}=\int_0^1\Phi_d(x)\psi_d(x)\,dx.}
\tag{6}
$$



For completeness, psi_d can be written without a matrix inverse:
its x^(j-1) coefficient is the residue at D=-j of the rational
function in (3), for j=1,...,r. This follows by partial fractions of
its moment function. Equations (3),(5),(6) retain all higher even
replacements coherently. They do not give their integral a controlled
sign or magnitude.

## 5. The full correction has necessarily growing rank

There is a useful exact limitation to a fixed-rank determinant-lemma
strategy based on this reference minor. The tail coefficient matrix
C[:,E] has rank r: its columns with degrees n+1,...,2n-1 form a
triangular square matrix, with nonzero entries1/k! on the diagonal.
These degrees all lie outside I0. Therefore R has rank r.

The rectangular Cauchy matrix H_E also has rank r, since any r distinct
rows have a nonzero Cauchy determinant. Thus W has rank r as well.
Their intermediate dimension is |E|=r+2. The rank inequality gives



$$
\boxed{\operatorname{rank}\mathcal K
\ge\operatorname{rank}R+\operatorname{rank}W-(r+2)
=r-2=n-3.}
\tag{7}
$$



Accordingly, although one replacement family is rank one, the entire
correction cannot be a perturbation of uniformly bounded rank in this
reference expansion. This does not prohibit a low-displacement-rank
description, a finite recurrence, or another structured determinant
identity. It specifically rules out treating the whole correction in
(2) as a fixed-rank update merely because the first adjacent family
has a compact formula.

## 6. What a uniform estimate must still control

Let H0_L denote the I0 moments against the low shifted Legendre test
polynomials, and let V have columns
V_(a,s)=integral Phi_a L_s for s=n-1,n, where the Phi_a are the full
coefficient-cardinal high polynomials C0^(-1)F. The actual graph
matrix before orthonormal weighting is exactly



$$
\boxed{Z=-H_{0,L}^{-1}(I+\mathcal K)^{-1}V.}
\tag{8}
$$



This is defined precisely when the low determinant is nonzero. It
shows what coherent resummation has preserved: the same middle
matrix governs the denominator and both replaced-column numerators.
The reviewed weighted graph estimate still requires control of this
whole product. Neither the scalar family (6), the determinant identity
(2), nor the full-rank statement (7) gives such a bound.

The resummation therefore replaces an invalid isolated-leading-term
approximation with an exact structured matrix and explicit weights.
The missing result remains eventual transversality together with a
uniform weighted inverse/observation estimate. No top-two concentration,
endpoint noncancellation, or primitive shrinking is asserted.

Verification: `check_raw_newton_cauchy_resummation.py` checks the two
adjacent ratios symbolically in n, then verifies the factorization,
all Cauchy cardinal weights, rank-one family identity, and scalar
integral on the already studied n=4 moment matrix. It constructs no
new HP degree. The exact certificate is
`raw_newton_cauchy_resummation_checks.json`. At n=4 the adjacent ratio
is -7/20, while its entire one-column family sums to2099/2880;
this illustrates why the family sum must be retained, without
establishing any asymptotic estimate.
