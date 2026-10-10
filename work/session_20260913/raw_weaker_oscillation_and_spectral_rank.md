> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A weaker oscillation route: the singular-endpoint bridge, parity positivity, and two closed degrees

Date: 2026-09-13. Original continuation by audit_computations.
Root review in raw_weaker_oscillation_root_review.md passes the proof;
the arXiv Newton-collocation corollary number was clarified in review.

This note proves the sign-change bridge for the actual prolate problem,
an all-degree same-parity extended Chebyshev theorem, and the weaker
mixed zero bound at the two predeclared degrees n=4,5. It does not prove
the mixed bound for arbitrary n. The previous counterexamples to ordinary
Chebyshev behavior remain valid.

## 1. The exact spectral bridge survives the singular natural endpoints

On (0,1) the actual column operator is



$$
T=-D\,p(x)D+V(x),\qquad p=x(1-x),\quad V=x^2-x+1.
\tag{1}
$$



After u=2x-1, this is the order-zero prolate operator at c=1/2, plus
3/4. Let its real normalized eigenfunctions be psi_j and eigenvalues
xi_j, in increasing order starting at j=0. They are analytic across
[0,1], and psi_j has exactly j simple interior zeros. These facts are
stated for PSWFs in Osipov, *Certain inequalities involving prolate
spheroidal wave functions and associated quantities*, Theorem 1:
https://arxiv.org/pdf/1206.4056 . Analyticity of the bounded m=0 branch,
strict eigenvalue ordering, and the zero count are also recorded in
https://dlmf.nist.gov/30.3 and https://dlmf.nist.gov/30.4#ii .

The familiar regular-endpoint Sturm theorem must not simply be applied
to (1), since p vanishes at the endpoints. Here is a direct adaptation
of Liouville's proof, as revisited in Bérard--Helffer, Section 2:
https://arxiv.org/pdf/1807.03990 . Their stated model is regular
Dirichlet; the following endpoint argument is supplied for our operator.

Every nonzero analytic eigenfunction has nonzero values at both endpoints.
For example, if its first nonzero Taylor term at zero were a_m x^m with
m>=1, the lowest term of `-D(pD psi)` would be `-m^2 a_m x^(m-1)`,
which cannot cancel `(V-xi)psi`. The endpoint one is identical. Thus
psi_0 can be chosen strictly positive on all of [0,1].

For a finite sum U=sum_(j=0)^k a_j psi_j, put



$$
U_1=\sum_{j=0}^k (\xi_0-\xi_j)a_j\psi_j.
$$



Subtracting its eigenfunction equations gives the exact identity



$$
\big[p\psi_0^2(U/\psi_0)'\big]'=\psi_0U_1.          \tag{2}
$$



The quantity in square brackets vanishes at BOTH endpoints: p does,
while all the functions and their derivatives are bounded. If U has
q>=1 distinct interior zeros, Rolle's theorem first gives q-1 zeros
of that bracket in the interior. Including its two endpoint zeros and
applying Rolle again gives at least q interior zeros of U_1. The latter
is nonzero unless U is a multiple of the zero-free ground state.

Iterate (2). If k is the largest index with a_k!=0, then after division
by `a_k(xi_0-xi_k)^m` the m-th iterate converges in C^1[0,1] to psi_k.
The limit has nonzero endpoint values and only k simple interior zeros.
C^1 convergence therefore bounds the zeros of all sufficiently late
iterates by k: outside small disjoint neighborhoods of those zeros the
function is bounded away from zero, and inside each neighborhood its
derivative has one fixed sign. Since no iterate lost any of the
original q zeros, q<=k. This proves the required strict Chebyshev
property of the first k+1 ACTUAL prolate eigenfunctions.

Consequently any nonzero continuous function with finitely many sign
changes, orthogonal to psi_0,...,psi_n, has at least n+1 sign changes
in (0,1). To see this without an infinite-series zero argument, suppose
there are s<=n sign-change points. The determinant interpolant from
psi_0,...,psi_s vanishing at those s points is nonzero elsewhere by the
just-proved Chebyshev property. Its sign alternates across each of the
points, because the ordered collocation determinant has one fixed
nonzero sign. Its product with the original function then has one sign
and is nonzero on an open set, contradicting orthogonality.

In particular, if every nonzero function in



$$
\mathcal H_n=\operatorname{span}(F_{n+1},\ldots,F_{2n-1})
\tag{3}
$$



has at most n distinct interior zeros, the actual high spectral matrix
`(<F_k,psi_l>)_(n+1<=k<=2n-1,0<=l<=n)` has full row rank n-1.
A rank failure would give a nonzero polynomial in (3) orthogonal to all
those columns and hence at least n+1 sign changes. Reflection of the
physical polynomial only changes column parity signs, not this rank.

## 2. All same-parity Borel--Legendre families are extended Chebyshev

Write lambda_k=k(k+1), sigma in {0,1}, and
alpha_(sigma,m)=[x^sigma]F_(sigma+2m)>0. The exact coefficient
recurrence gives



$$
\frac{F_{\sigma+2m}(x)}{\alpha_{\sigma,m}x^\sigma}
=\sum_{j=0}^m
\frac{\prod_{r=0}^{j-1}(\lambda_{\sigma+2m}-\lambda_{\sigma+2r})}
 {((\sigma+2j)!/\sigma!)^2}x^{2j}.                  \tag{4}
$$



Indeed the ratio of consecutive coefficients is
`[lambda_k-d(d+1)]/[(d+1)^2(d+2)^2]`; the first coefficient fixes (4).
The numerator array in (4), with rows m and columns j, is exactly the
lower-triangular Newton collocation matrix at the increasing nodes
`lambda_sigma,lambda_(sigma+2),...`. This matrix is totally nonnegative.
An explicit positive bidiagonal factorization, including the case of
its own ordered interpolation nodes, is Theorem 2 and Corollary 2(a)
in the arXiv v1 version (printed pages 8–10) of
Khiar--Mainar--Royo-Amondarain--Rubio, *On the accurate computation of
the Newton form of the Lagrange interpolant* (2024):
https://arxiv.org/pdf/2312.14483 ; published version
https://doi.org/10.1007/s11075-024-01843-7 . Their terminology calls
nonnegative minors 'totally positive'; here the triangular matrix is
called totally nonnegative to distinguish strict positivity.

Dividing its columns by the positive factorials preserves all minor
signs. Its minor in any r increasing rows and the first r columns is
strictly positive: those columns are monic Newton polynomials of
degrees 0,...,r-1 evaluated at distinct increasing lambda nodes, so
its determinant is their ordinary positive Vandermonde, divided by
positive factorials.

Put y=x^2. Apply Cauchy--Binet to the Wronskian of any r selected
same-parity functions after removing `alpha x^sigma`. Every coefficient
minor is nonnegative. For increasing exponents j_1<...<j_r the
monomial derivative determinant is



$$
\det\big[(D_y^{i-1}y^{j_k})\big]_{i,k=1}^r
=y^{\sum j_k-r(r-1)/2}\prod_{a<b}(j_b-j_a)>0
\quad(y>0).                                        \tag{5}
$$



The term j_k=k-1 has a strictly positive coefficient minor. Thus every
such Wronskian is strictly positive. Multiplication by the common
positive x^sigma and the increasing change y=x^2 preserve its sign.
All initial Wronskians are therefore nonzero on (0,infinity), proving
by successive quotient differentiation that every nonzero combination
of r selected same-parity functions has at most r-1 zeros there,
counted with multiplicity. This is an all-degree statement, including
arbitrarily high starting indices. It does not combine the two parities.

## 3. The closed n=4 and n=5 checks give actual weaker bounds

The only degrees examined were the predeclared n=4 and n=5. Exact
rational certificates are saved in
`raw_weaker_zero_count_exact_certificates.json`, reproduced by
`check_raw_weaker_zero_count.py`. These certificates are finite proofs
of the Wronskian facts used below, not asymptotic evidence.

For functions f_1,f_2 with f_1 and W_2=W(f_1,f_2) nonzero, define



$$
\mathcal Df=\left(\frac{(f/f_1)'}{(f_2/f_1)'}\right)'.
\tag{6}
$$



Two applications of Rolle imply that a function with q distinct zeros
has at least q-2 zeros after (6), unless the transformed function is
zero; the latter case is the two-dimensional initial Chebyshev span.
Direct Wronskian identities give



$$
\mathcal Df_j=\frac{f_1W(f_1,f_2,f_j)}{W_2^2},\qquad
W(\mathcal Df_3,\mathcal Df_4)
=\frac{f_1^2W(f_1,f_2,f_3,f_4)}{W_2^3}.             \tag{7}
$$



For n=4 choose `(f_1,f_2,f_3)=(F_5,F_7,F_6)`.
The first two Wronskians are nonzero by Section 2. The third has exactly
one simple interior zero. Explicitly it is a nonzero constant times
x times P(x^2), where P(0)>0>P(1) and



$$
P(y)=1008000000-2923200000y-611280000y^2+340920000y^3
-40206000y^4-1920600y^5-26950y^6-2541y^7.
$$



Its derivative is strictly negative on [0,1]; this follows directly
by combining `1022760000y^2-1222560000y<=0` and the other negative
terms. Hence the one-dimensional transformed space in (7) has only
one zero. Every nonzero function of H_4 therefore has at most THREE
interior zeros, and the high spectral matrix at n=4 has full row rank.
This is consistent with the earlier example attaining three zeros.

For n=5 choose `(f_1,f_2,f_3,f_4)=(F_6,F_8,F_7,F_9)`.
Again W_2 is nonzero on the interior. Each of W_3 and W_4 has exactly
one simple interior zero, and the two zeros are distinct. Here is a
fully rational certification procedure, with the exact integers in the
saved JSON: remove the positive denominators and write each Wronskian
as a polynomial in y=x^2, choosing its sign positive at zero. For W_3,
its derivative has all nonpositive Bernstein coefficients on [0,1],
with at least one negative; its root is in (1/4,1/2) in the y coordinate.
For W_4, its derivative has all strictly negative Bernstein coefficients
on each of [0,1/2] and [1/2,1], and its root is in (3/4,1). All endpoint
and bracket signs are exact rational inequalities. The largest derivative
Bernstein coefficients on the two W_4 subintervals are respectively



$$
-19561686058058136930/11,\qquad
-3180838754705284938405/512.
$$



The standard identity
`p(y)=sum_(k=0)^d b_k binom(d,k)y^k(1-y)^(d-k)`, with
`b_k=sum_(j<=k)[y^j]p * binom(k,j)/binom(d,j)`, makes these
certificates elementary coefficient-sign proofs; no floating-point
root count is needed.

Let g_3=Df_3,g_4=Df_4. By (7), g_3 has one simple zero c, and
W(g_3,g_4) has one simple zero d!=c. In particular g_4(c)!=0.
For a combination ag_3+bg_4 with b!=0, zeros are solutions of
`g_4/g_3=-a/b`. This ratio has just one pole c and just one critical
point d, so it has at most three intersections with any horizontal
line on (0,1). A root at the critical point cannot add further roots
on either adjoining strictly monotone branch. The case b=0 has only
one zero. Therefore every nonzero transformed combination has at most
three distinct zeros. Equations (6)--(7) prove



$$
\boxed{Z_{(0,1)}(f)\le5\quad(0\ne f\in\mathcal H_5).} \tag{8}
$$



Thus the high spectral matrix at n=5 also has full row rank. This is
a finite oscillation theorem, not an extrapolation to larger n.

## 4. The all-index obstruction is now a precise mixed Wronskian problem

Separate H_n into one parity family of size r and the other of size
m=n-1-r. Section 2 supplies a globally nonsingular order-r generalized
Rolle operator annihilating the first family. Up to a nonvanishing
smooth factor it is



$$
\mathcal L_r f=\frac{W(f_1,\ldots,f_r,f)}{W(f_1,\ldots,f_r)}.
\tag{9}
$$



It loses at most r distinct zeros. A sufficient all-index intermediate
lemma is therefore that every nonzero function in the m-dimensional
remaining space



$$
\operatorname{span}\{\mathcal L_r F_k:k\text{ of the other high parity}\}
$$



has at most `n-r=m+1` interior zeros. This is only two zeros beyond
ordinary Chebyshev accuracy, but neither (4) nor separate parity
positivity establishes it. The mixed Wronskians in (9), with their
opposite-parity x factor, are the concrete missing objects.

Ordinary monomial Descartes counting does not supply the missing bound.
For every n>=3, `F_(2n-2)-c F_(2n-1)` with c>0 belongs to H_n and has
strictly alternating nonzero coefficients in every degree 0,...,2n-1.
Its Descartes variation count is therefore the maximal `2n-1`, larger
than n. This is an exact obstruction to that coefficient-sign shortcut,
not a claim that this particular polynomial has 2n-1 positive zeros.
The fourth-order Borel eigen-equation alone likewise lacks the shared
second-order boundary conditions used in Section 1.

No all-index mixed zero bound, full high spectral row rank theorem, or
endpoint quantitative estimate is proved here. The useful new inputs
are the valid singular-endpoint bridge, the all-degree same-parity
Wronskian positivity, and the exact residual problem (9).
