> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Adjacent high-matrix contents: exact condensation and the missing multipliers

Date: 2026-09-13. Bounded arithmetic continuation by audit_results.

**Subsequent verified advance:**
`raw_shared_core_large_prime_saturation.md`, independently checked in
`raw_shared_core_module_independent_review.md`, proves
v_p(zeta_n)=0 for every p>3n. The original condensation identities
below are unchanged. Statements below describing zeta_n as an
open target record the state when the reduction was derived;
that large-prime support target is now closed. The original
high content and the two-new-column pivot remain unresolved.
The condensation itself passes
`raw_adjacent_content_condensation_root_review.md`.

This note gives actual determinant identities for adjacent high
matrices, including a common-content divisibility and fixed-size
local carriers. It does not prove that their large-prime contents
vanish, or derive an upper recurrence for their valuations. It
identifies the precise minors that would have to be controlled
before the finite-difference entry recurrences can be promoted
to such a content statement.

No degree or prime scan is used. Every high row imposing the
degree bound on A is retained in its appropriate matrix.

## 1. The common adjacent core

Let H_n have its original integer rows k=n+1,...,3n and columns
B_0,...,B_n,C_0,...,C_n. Let H_(n+1) have rows k=n+2,...,3n+3
and columns B_0,...,B_(n+1),C_0,...,C_(n+1). All entries are
the actual integer functionals

    H_(k,B_j)=(k)_j,
    H_(k,C_j)=k! tau_(k-j).

Negative Taylor subscripts, when needed in the universal ambient
matrix, are zero. The relevant retained rows here have positive
subscripts except for possible zero entries.

Their common old-column core C_n has rows

    n+2,...,3n                                      (2n-1 rows)

and the 2n+2 old columns. Let C_n^+ have the same rows and
also the two new columns B_(n+1),C_(n+1). Define

    D_n = gcd of all 2n-by-2n minors of H_n >0,
    zeta_n = gcd of all (2n-1)-by-(2n-1) minors of C_n^+ >0.

Both are nonzero: characteristic-zero full row rank of H_n
implies that deleting one of its rows leaves full row rank.
Thus C_n already has full row rank over Q, as does C_n^+.

The Smith reduction from raw_high_smith_finite_difference_reduction.md
gives v_p(D_n)=v_p(eta_n) for p>3n, where eta_n is the content
of its smaller G_n matrix.

## 2. A proved adjacent prime-power divisibility

There is the following exact integer relation, before localization:



$$
\boxed{\zeta_n\mid\gcd(D_n,D_{n+1}).}
\tag{1}
$$



For H_n, expand any maximal minor along its row k=n+1. Each
complementary determinant is a (2n-1)-minor of the old-column
core, hence a minor among those defining zeta_n. For H_(n+1),
expand any maximal minor along its three new rows
k=3n+1,3n+2,3n+3. Each complementary determinant is again a
(2n-1)-minor of C_n^+. This proves (1) with every multiplicity.

In terms of the smaller finite-difference contents,



$$
(\zeta_n)_{>3n+3}\mid
\gcd\bigl((\eta_n)_{>3n+3},(\eta_{n+1})_{>3n+3}\bigr).
\tag{2}
$$



This relation supplies a shared lower divisor, not the upper bound
needed to control the primitive arithmetic. In particular a
large prime in this common-core content cannot be removed by
looking at either adjacent degree alone. No bound for zeta_n
has been established here.

## 3. Uniform unit-pivot charts exist at every allowed prime

Fix p>3n+3 and put R=Z_p. The reviewed rank theorem gives
rank(H_n mod p)>=2n-1. Deleting one row implies



$$
\operatorname{rank}(C_n\bmod p)\ge2n-2.
\tag{3}
$$



Set t=2n-2. Choose t shared rows I and t old columns J with



$$
\Delta=\det H[I,J]\in R^\times.
\tag{4}
$$



For n=1, this is the empty minor Delta=1. There is exactly one
remaining shared row rho, four remaining old columns C, and
two new columns C^+. Let alpha=n+1 be the removed low row and
beta_1=3n+1,beta_2=3n+2,beta_3=3n+3 be the added high rows.

The existence assertion (3) does not identify a single pivot
minor that is a unit for every large prime. The gcd of all these
t-minors has no prime divisor above 3n, so the charts cover
every prime under consideration; switching charts may be necessary.

For r among alpha,rho,beta_1,beta_2,beta_3 and a free column c,
define the INTEGER bordered minor



$$
E_{r,c}=\det H[I\text{ followed by }r,\ J\text{ followed by }c].
\tag{5}
$$



This ordering fixes all signs. The ambient H in (5) has the union
of the specified rows and columns, with the same original entry
formula. No endpoint row is introduced.

## 4. Sylvester condensation gives fixed-size content carriers

The exact Sylvester identity is



$$
\det[E_{r,c}]_{r\in R_0,c\in C_0}
=\Delta^{k-1}\det H[I\text{ followed by }R_0,
J\text{ followed by }C_0],
\quad |R_0|=|C_0|=k.
\tag{6}
$$



It follows by a Schur complement: E_(r,c)=Delta times the
corresponding residual entry. The identity is also polynomial
and does not require division for its statement. In the present
unit chart all such divisions preserve R-integrality.

Define the two small matrices



$$
U=\begin{pmatrix}E_{\alpha,C}\\E_{\rho,C}\end{pmatrix}
\quad(2\text{ by }4),
\tag{7}
$$




$$
V=\begin{pmatrix}
E_{\rho,C}&E_{\rho,C^+}\\
E_{\beta_1,C}&E_{\beta_1,C^+}\\
E_{\beta_2,C}&E_{\beta_2,C^+}\\
E_{\beta_3,C}&E_{\beta_3,C^+}
\end{pmatrix}
\quad(4\text{ by }6).
\tag{8}
$$



Invertible operations over R put H_n and H_(n+1) respectively
into diag(I_t,U/Delta) and diag(I_t,V/Delta). Consequently,
writing v_p(I_k(M)) for the minimum valuation of the k-minors,



$$
\boxed{v_p(D_n)=v_p(I_2(U)),\qquad
v_p(D_{n+1})=v_p(I_4(V)).}
\tag{9}
$$



The first carrier consists of six explicit minors and the second
of fifteen. Moreover the previous rank bounds imply

    I_1(U)=R,  I_3(V)=R.

Thus each carrier still has at most one nonunit Smith invariant.
No additional rank assumption has entered this local comparison.

The common-core valuation has the especially simple form



$$
v_p(\zeta_n)=\min_c v_p(E_{\rho,c}),
\quad c\in C\cup C^+.
\tag{10}
$$



Expanding the small determinants along their rho row independently
recovers (1). The lost alpha row is present only in U; the two
new columns contribute to V's rho row and cannot be suppressed.

If the old common core has the stronger rank 2n-1 modulo p,
one can instead use a unit pivot of that size. The same argument
then reduces the contents to a 1-by-3 row and a 3-by-5 matrix.
If its rank is only 2n-2, every entry E_(rho,c) for old c is
divisible by p. The entries in the two new columns need not
be divisible by p; it is precisely these additional entries
that can restore the common row rank in the next matrix.

## 5. A further two-form comparison, and its exceptional multiplier

Use the actual residual matrices U/Delta and V/Delta, and write
the first as rows a,r. Write the second as rows

    [r | s], [w_1 | d_1], [w_2 | d_2], [b | d_3],

where old-column rows have length four and new-column rows
have length two. Suppose, as an ADDITIONAL local hypothesis,
that the two-by-two matrix D with rows d_1,d_2 has unit determinant.
Let W have rows w_1,w_2. Eliminating the new columns by those
two rows leaves the two-by-four matrix with rows



$$
\widetilde r=r-sD^{-1}W,\qquad
\widetilde b=b-d_3D^{-1}W.
\tag{11}
$$



Its maximal-minor content equals that of V over R. Equivalently,
in the common free module R^4,



$$
\boxed{
v_p(D_n)=\operatorname{contentval}(a\wedge r),\qquad
v_p(D_{n+1})=\operatorname{contentval}
(\widetilde r\wedge\widetilde b).
}
\tag{12}
$$



Here contentval is the minimum valuation of the six exterior
coordinates. Equation (12) is a precise adjacent determinant
identity, not an assertion that its two exterior vectors agree.

The exceptional multiplier is det D. It is itself a ratio of
bordered minors from the actual adjacent matrix. The known rank
theorems do not make it a unit: the two new columns may have
rank below two while the total residual V still has rank three
or four. At primes dividing det D, this second elimination is
not available in that chart. Even on a unit chart, the terms
sD^(-1)W and d_3D^(-1)W are actual new contributions. The
finite-difference entry recurrences alone do not bound them or
relate the two exterior vectors by a unit transformation.

## 6. What has and has not propagated

The proved relation (1) links actual adjacent contents, including
prime-power exponents. The condensation (9) makes every other
part of an adjacent comparison a fixed-size determinant problem
on unit charts. The sharper formula (12) identifies a possible
two-form propagation target and the exact additional multiplier
that would have to be controlled.

This does not prove a numerical recurrence, an upper divisibility
for D_n, or the absence of large primes. In particular, deleting
the alpha row and treating its cofactor data as redundant would
drop the degree-n condition on A in H_n. Treating the new two
columns as automatically invertible would likewise assume an
unproved modular minor condition. These are obstructions to this
specific propagation argument, not an impossibility theorem for
other approaches to the actual family.

The subsequent shared-core theorem resolves the large-prime
content zeta_n and forces a unit in at least one new-column rho
entry whenever the old core is deficient. The remaining exact
targets are the unit status of the two-new-column pivot det D
on suitable charts and the exterior-coordinate comparison in
(12). A successful bound for those actual minors could propagate
the full high Smith valuation. No upper recurrence or restricted
infinite family for that valuation has yet been established.
