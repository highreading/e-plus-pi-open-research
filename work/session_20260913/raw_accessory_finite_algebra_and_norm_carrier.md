> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A finite free accessory algebra and a controlled scalar norm carrier

Date: 2026-09-13. Original all-degree arithmetic continuation by
audit_results. Independent audit: raw_accessory_finite_algebra_independent_review.md
passes finite freeness, the full local quotient and both norm inequalities.

This note proves a previously unresolved finiteness statement for the
two actual exponential accessory equations. Their quotient algebra is
free of rank

    D_d=(d+1)(d+2)/2

over Z[1/d!], with an explicit monomial basis. In particular either
accessory parameter satisfies a monic degree-D_d equation with only
small-prime denominators. This holds in every allowed residue
characteristic, not just generically in characteristic zero.

Adding the two actual residue equations gives, locally at p>3d+3,
the exact algebra Z_p/(p^f), where f=v_p(F_(d+1)). A scalar norm
construction therefore gives an explicit nonzero integer c_d with

    f <= v_p(c_d) <= D_d f.

The integer has precisely the same large-prime support as the actual
extremal content, with a controlled multiplicity loss. Its size and
small-prime saturation are not established. Thus this is a finite
elimination and depth carrier, not an exclusion of isolated defects.

## 1. Actual equations and their highest weighted terms

Use the four integer polynomials E_0,E_1,R_0,R_1 of
raw_extremal_four_accessory_equations.md. Its complete equivalence,
including prime powers, has passed the independent review
raw_extremal_four_equations_independent_review.md.

Fix d>=2 and put A=Z[1/d!]. Assign weights

    wt(beta)=1,  wt(gamma)=2.

The monic polynomial B^*=sum_(r=0)^d b_(d-r) z^(d-r) is
constructed from the upper coefficients of L^[1]B^*=0, with b_d=1.
We retain exactly the normalization

    E_1=d! [z] L^[1]B^*,    E_0=d! [1] L^[1]B^*.

Define h_r and P_r by



$$
\sum_{r\ge0}h_r t^r=\exp(\beta t+\gamma t^2/2),
\qquad P_r=r!h_r.
                                                               \tag{1}
$$



Only the finite polynomials in (1) are used in positive characteristic;
no infinite exponential is being asserted over that field. They obey



$$
P_0=1,\quad P_1=\beta,\quad
P_r=\beta P_{r-1}+(r-1)\gamma P_{r-2}.                         \tag{2}
$$



The highest weighted part of b_(d-r) is h_r. To see this directly,
the coefficient solving for b_(d-r) is -r. At weight r, its only
other contributions are beta b_(d-r+1) and gamma b_(d-r+2).
Thus its leading recurrence is

    r h_r=beta h_(r-1)+gamma h_(r-2).

All remaining contributions have smaller weight. This can also be
checked from the complete conjugated operator:



$$
\begin{aligned}
L^{[1]}={}&zD\partial^3
 +[2z^3+(2-3d)z^2+2z-3d-2]\partial^2\\
&+[z^3+(2-4d)z^2+(\beta+1)z+\gamma-6d-4]\partial\\
&-dz^2+[\beta-d(d-1)]z
 +\gamma+2d^2(d-1)-d\beta-3d-2.
\end{aligned}                                                 \tag{3}
$$



The last two unsolved coefficients consequently have weighted parts



$$
\boxed{\operatorname{in}_w(E_1)=P_{d+1},\qquad
       \operatorname{in}_w(E_0)=\gamma P_d.}                    \tag{4}
$$



Their weighted degrees are respectively d+1 and d+2. In the first
equation the leading contribution is d!(beta h_d+gamma h_(d-1))
=(d+1)!h_(d+1). In the second it is d! gamma h_d. This tracks
the actual integer normalization, so no parameter-dependent factor
has been discarded.

## 2. A monic basis for the leading ideal

Put



$$
G_j=\gamma^jP_{d+1-j},\qquad 0\le j\le d+1.                    \tag{5}
$$



Order monomials first by weight and then by beta exponent. The leading
monomial of G_j is beta^(d+1-j) gamma^j, with coefficient one.
The recurrence (2) gives



$$
\gamma G_j-\beta G_{j+1}=(d-j)G_{j+2},\quad 0\le j<d,
\qquad \gamma G_d-\beta G_{d+1}=0.                            \tag{6}
$$



Every integer d-j inverted here is a unit in A. Thus the G_j generate
the same ideal as G_0,G_1. They form a monic Groebner basis. Indeed
their adjacent S-polynomials reduce by (6). For an explicit check
of all other pairs, when i<j,



$$
\gamma^{j-i}G_i-\beta^{j-i}G_j
=\sum_{r=i}^{j-1}\beta^{r-i}\gamma^{j-r-1}
       (\gamma G_r-\beta G_{r+1}).                             \tag{7}
$$



Replace each summand by (6), interpreting the r=d summand as zero.
The leading beta exponent on every resulting term is two smaller
than that of the original least-common-multiple monomial, and its
weight is no larger. This is a standard representation of each
S-polynomial by smaller leading monomials and proves the assertion.
Monic division works over A, without division by any nonunit integer.

The standard monomials are exactly



$$
\mathcal B_d=\{\beta^a\gamma^b:a,b\ge0,\ a+b\le d\}.
                                                               \tag{8}
$$



They number D_d and have weight at most 2d.

In particular G_0 and G_1 have no common weighted point at infinity
in characteristic greater than d. This also follows directly: if
gamma=0, P_(d+1)=beta^(d+1); if gamma is nonzero, simultaneous
vanishing of P_(d+1),P_d propagates backwards by (2) to P_0=0.
The latter argument inverts only 1,...,d.

## 3. The actual, nonhomogeneous quotient is finite free

Let



$$
\mathscr A_d=A[\beta,\gamma]/(E_1,E_0).                        \tag{9}
$$



**Theorem 1.** This is a free A-module with basis (8).

Here is the filtered argument, including why a lower-degree hidden
relation does not arise. The polynomials G_0,G_1 are coprime in
the UFD A[beta,gamma]. For example their common factors over Q would
propagate backwards using (2); neither gamma nor a constant prime
factor can divide the monic G_0. Gauss's lemma then gives the claim
over A. Consequently every polynomial syzygy between G_0,G_1 is
a multiple of (G_1,-G_0) with coefficients in A[beta,gamma].

Consider H=u E_1+v E_0. If its highest possible weighted terms
cancel, the highest parts of u,v obey precisely such a homogeneous
syzygy. Subtract the corresponding multiple of (E_0,-E_1) from
(u,v). This does not change H and strictly lowers the maximum
weighted degree of the two summands. Iterate. The nonnegative
integer weights ensure termination. It follows that the leading
part of every nonzero H belongs to (G_0,G_1). The reverse inclusion
for the associated graded ideal follows from (4). Thus



$$
\operatorname{in}_w(E_1,E_0)=(G_0,G_1).                       \tag{10}
$$



One can implement the reduction explicitly: start with F_0=E_1,
F_1=E_0 and set

    F_(j+2)=(gamma F_j-beta F_(j+1))/(d-j),   0<=j<d.

Then F_j belongs to the actual ideal and has highest part G_j.
Reduction by these monic leading monomials spans the actual quotient
by (8). If a nonzero A-linear combination of standard monomials
were in the actual ideal, its highest part would violate (10) and
the monic basis in Section 2. Hence these monomials are independent.
This proves freeness, not just a bound on the generic dimension.

Base change now shows that the same dimension D_d holds over every
field of characteristic greater than d. The scheme can be nonreduced;
no simple-root assertion for the two E equations is made. It has at
most D_d distinct geometric accessory points. This closes the
previously unproved all-characteristic finiteness of this parameter
locus.

Multiplication by beta and gamma in the basis (8) gives explicit
D_d-by-D_d matrices M_beta,M_gamma with entries in A. Cayley-Hamilton
gives monic degree-D_d univariate eliminants



$$
\det(TI-M_\beta)|_{T=\beta}=0,\qquad
\det(TI-M_\gamma)|_{T=\gamma}=0
\quad\text{in }\mathscr A_d.                                 \tag{11}
$$



All reductions defining these matrices divide only by integers
supported on primes at most d. The degree and denominator assertions
in (11) therefore hold uniformly at every allowed large prime.

## 4. The full four-equation algebra has one exact local scalar

Fix p>3d+3, let R=Z_p, n=d+1, and f=v_p(F_n). Put



$$
\mathscr S_d=(\mathscr A_d\otimes_A R)/(R_0,R_1).               \tag{12}
$$



**Theorem 2.** There is an R-algebra isomorphism



$$
\boxed{\mathscr S_d\simeq R/(p^f),}                           \tag{13}
$$



where f=0 means the zero ring. This proof uses the actual constant
matrix X_n and monic B normalization; it is stronger than merely
counting solutions modulo p^h.

First, S is finite over R by Theorem 1. It is torsion over R:
over an algebraic closure of Q_p a common four-equation zero would,
by the characteristic-zero version of the reviewed equivalence,
produce a nonzero actual extremal triple, contradicting full column
rank of X_n. Thus S tensor Q_p=0 and some p-power annihilates S.

Over an algebraic closure of F_p the extremal Taylor space has
dimension at most one, and its top B coefficient is injective.
Hence a nonzero triple with top B=1 is unique and is defined over F_p.
The associated beta,gamma are unique as well. Explicitly, comparison
of the coefficients at z^(d+1) and z^d in (3), for monic B, gives



$$
\beta=3d^2-d+b_{d-1},\qquad
\gamma=2d+2+2b_{d-2}-b_{d-1}^2-2b_{d-1}.                      \tag{14}
$$



For the second identity, the coefficient at degree d is
-2b_(d-2)+(b_(d-1)+2)b_(d-1)+gamma-2d-2. These formulas agree
with the independently derived local-transversality continuation
by audit_sources; they are also direct coefficient identities here.

If f=0, the field equivalence shows S/pS=0, and finite generation
implies S=0. If f>0, S has exactly one residue point, with residue
field F_p; since it is p-power torsion it is a local Artinian ring.

The universal beta,gamma in S satisfy the four equations. The unit
minor and initial determinant from the reviewed sufficiency proof
remain units over this local ring. Consequently that proof constructs
the universal actual triple over S with top B=1. All finite-jet
divisions are units; no field-only step is used here.

Take a Smith form of the constant matrix X_n over R. Its only
possible nonunit invariant is p^f times a unit. Absorb that unit.
After the fixed invertible coordinate change, the universal kernel
vector has all coordinates zero except its last coordinate y, with

    p^f y=0.

The top B functional on this vector is u y for a fixed u in R.
The nonzero extremal reduction makes u a unit. Monic normalization
therefore gives y=u^(-1), a fixed constant. In particular p^f=0
in S and all B,C coordinates of the universal triple are images of
constants in R. Formula (14) makes beta,gamma constants as well.
Since they generate S over R, the map R->S is surjective.

Conversely the Smith form gives an actual primitive approximate
kernel modulo p^f, with unit top B. The reviewed four-equation
necessity supplies an R-algebra map S->R/(p^f). Together with
p^f=0 and surjectivity, this proves exactly (13).

This argument preserves the full p-adic exponent. It also specifies
why arbitrary nonreduced structure of the two-equation E algebra
does not create extra parameter directions in the full quotient.

## 5. An explicit norm polynomial and a nonzero integer carrier

In the finite free algebra A_d form the multiplication matrices of
the actual residues R_0 and R_1 in basis (8), and define



$$
\mathcal N_d(t)=\det(M_{R_0}+tM_{R_1})\in A[t].                \tag{15}
$$



Its degree is at most D_d. Clear its denominators by an integer
q_d supported only on primes at most d, and let c_d be the positive
gcd of the coefficients of q_d N_d(t).

The norm polynomial is not identically zero. Over an algebraic
closure of Q, the finite E algebra is a product of local Artinian
algebras supported on finitely many points x. Multiplication by
R_0+tR_1 has determinant



$$
\mathcal N_d(t)=\prod_x[R_0(x)+tR_1(x)]^{m_x},
\qquad \sum_xm_x=D_d,                                       \tag{16}
$$



where m_x is the length of the local algebra. This factorization
follows, including nilpotents, by triangularizing multiplication
on its maximal-ideal filtration. The full characteristic-zero
rank says R_0(x),R_1(x) are never simultaneously zero. Every
factor in (16) is therefore a nonzero polynomial. Thus c_d is a
well-defined positive integer.

**Theorem 3 (controlled scalar carrier).** At every p>3d+3,



$$
\boxed{
v_p(F_{d+1})\le v_p(c_d)
\le D_d\,v_p(F_{d+1}).}
                                                               \tag{17}
$$



For the lower inequality when f>0, the actual solution modulo p^f defines
an evaluation functional on A_d tensor R with value 1 on its first
basis vector. It is therefore a primitive row. Both multiplication
matrices M_(R_j) have this row as a left annihilator modulo p^f.
Complete it to an invertible row transformation over R. Every
coefficient of their norm pencil's determinant is then divisible
by p^f. Clearing q_d changes no valuation at p.
When f=0, the lower inequality is simply the integrality of the
norm coefficients at p.

For the upper inequality, Theorem 2 says precisely

    p^f in (R_0,R_1) inside A_d tensor R.

Thus p^f=a R_0+b R_1 for some elements a,b of that integral
finite algebra. Evaluate at a geometric point x over an algebraic
closure of Q_p. Every such evaluation of an algebra element is
integral over R, because the algebra is finite. Hence



$$
0\le\min\{v_p(R_0(x)),v_p(R_1(x))\}\le f.                    \tag{18}
$$



Normalize v_p(p)=1 on the extension. The Gauss valuation of a
linear polynomial is the minimum valuation of its two coefficients,
and Gauss valuations add under multiplication. Applying this fact
to (16), now over an algebraic closure of Q_p, gives



$$
v_p(c_d)=\sum_x m_x
       \min\{v_p(R_0(x)),v_p(R_1(x))\}\le D_d f.
                                                               \tag{19}
$$



The value is an integer because the original norm has coefficients
in Q_p. Nilpotent multiplicities have been retained as m_x. This
proves the upper inequality, including f=0.

In particular the carrier has **exactly** the same prime support
as F_(d+1) above 3d+3. Equality of their exponents is not asserted.
The possible loss is real for abstract finite algebras: in
R[x]/(x^2), residues x and p^f have quotient R/(p^f), while the
norm of x+t p^f has coefficient content p^(2f). Thus the factor
D_d must not be silently discarded.

## 6. Consequence and remaining scope

The two actual exponential accessories now belong to an explicit
finite algebra of known rank in every large characteristic. Both
have controlled monic univariate eliminants, and the full residue
compatibility has one scalar local quotient. The norm (15) turns
that arithmetic into a concrete nonzero coefficient-gcd carrier
with the exact support and the exponent comparison (17).

No estimate for the Archimedean size or factorization of c_d is
proved here. In particular its large-prime part is not shown to
vanish, and the norm construction is not automatically more
efficient than the original minors. The useful next calculation
would simplify this specific norm pencil or produce a small-prime
Bezout identity for its residues inside the explicit algebra (9).
Generic determinant identities alone do not supply that identity.

This result does not prove irrationality or rationality of e+pi.
It supplies an all-degree elimination theorem and an exact arithmetic
carrier for one remaining part of the actual Hermite--Pade route.
