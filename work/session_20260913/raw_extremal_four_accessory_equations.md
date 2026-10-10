> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Four scalar accessory equations at the full extremal-content depth

Date: 2026-09-13. Original bounded arithmetic continuation by audit_results.
Independent audit: raw_extremal_four_equations_independent_review.md
passes the complete field and prime-power equivalences.

This note removes the unknown polynomials A and C, and the two low
initial conditions, from the previously reviewed extremal compatibility
system. The remaining condition consists of **four explicit polynomials
of degree at most d+1 in just two scalar parameters**. No nonvanishing
condition or saturation by an unspecified cofactor is needed. The
equivalence holds modulo every p-power for p>3d+3, so it retains the
entire valuation of the actual extremal content.

The main new fact is that the existence of the polynomial exponential
branch forces the polynomial part of the differential operator to be
surjective. Its proof uses the two arctangent singularities through the
factor (1+z^2)^2 in Abel's Wronskian identity. It does not use positivity
or characteristic-zero analytic solutions in a residue field.

The result is an exact smaller arithmetic system, not a proof that its
four equations have no common zero. Isolated large-prime extremal
defects remain possible until that arithmetic system is controlled.

## 1. Actual extremal matrix and the operator

Put n=d+1, M=3d+4, s=M-2=3d+2, and D=1+z^2. We may take
d>=2; the already settled d=0,1 exclusions are not repeated here.
Let X_n be the actual integer matrix with rows k=n,...,3n and
columns B_j,C_j for 0<=j<n, with entries

    (k)_j,  k! tau_(k-j),     tau_j=[z^j] arctan(z).

Let F_n be its positive maximal-minor content. All rows, in particular
the row k=n imposing the final allowed A coefficient, are retained.
Fix a prime p>3n=3d+3. Work either over a field K of this characteristic
or over R_h=Z/p^h Z, h>=1. The exponential and arctangent jets through
degree M-1 have unit denominators. The boundary p=M is allowed.

The reviewed no-accessory operator is



$$
\begin{aligned}
L={}&zD\partial^3
-[(z+s)D-4z^2]\partial^2\\
&+[(2d-2)z^2+\beta z+\gamma]\partial
-d(d-1)z+2d^2(d-1)-d\beta .
\end{aligned}                                      \tag{1}
$$



Write L^[1]=sum_j L_j(partial+1)^j. The old full system was



$$
LC=0,\quad L^{[1]}B=0,\quad LA+\mathcal T_L(C)=0,       \tag{2}
$$



together with the two initial zero coefficients of A+B E_T+C F_T.
Its forcing is



$$
\mathcal T_L(C)=3zC''-2(z+3d+1)C'+2dC
+\frac{-2C'+[(\beta+6d+2)z+\gamma-2d]C}{D}.            \tag{3}
$$



The prior finite-jet proof of sufficiency uses only the units
k(k-1)(k-M), 2<=k<=M-1. We will retain that proof; no division
by M or M! is introduced.

## 2. A polynomial exponential branch forces a one-dimensional polynomial kernel

**Lemma 1.** Over K, suppose L^[1] has a nonzero polynomial solution
B of degree at most d. Then B has degree exactly d, the space of
such B is one-dimensional, and



$$
\dim_K\ker(L:\mathcal P_d\longrightarrow\mathcal P_{d-1})=1.
                                                               \tag{4}
$$



Consequently the displayed map L is surjective.

**Proof.** The coefficient of z^(m+2) in L^[1](z^m) is m-d.
Thus a nonzero solution of degree m<d is impossible, since d<p.
Subtracting the suitable multiple of one degree-d solution from
another proves uniqueness up to scale.

The operator L maps P_d into P_(d-1), by the previously proved
two leading cancellations. Its polynomial kernel therefore has
dimension at least one. Suppose it contained independent C_1,C_2.
Define the exponential-gauged determinant



$$
W=\det\begin{pmatrix}
B&C_1&C_2\\
B+B'&C_1'&C_2'\\
B+2B'+B''&C_1''&C_2''
\end{pmatrix}.                                                \tag{5}
$$



It is a polynomial of degree at most 3d-2. For example, the last
row's exponential entry multiplies C_1 C_2'-C_1' C_2, whose degree
is at most 2d-2: if both polynomials have degree d their leading
terms cancel, and otherwise their degree sum is at most 2d-1.
The other two terms have at least as much degree reduction.

The determinant is nonzero. Here is a characteristic-independent
algebraic check that does not invoke a full exponential series.
After division by C_1, put

    K=(C_2/C_1)',       J=(B/C_1)'+B/C_1.

The first rational function is nonzero. Indeed a rational function
with numerator and denominator of degree less than p and derivative
zero is constant: reduce it to coprime numerator/denominator and
use divisibility into their derivatives. This would contradict the
independence of C_1,C_2. The second function is nonzero because a
nonzero rational logarithmic derivative cannot equal -1: it is
O(1/z) at infinity. The determinant vanishing would, by the direct
two-column determinant simplification, give

    K(J+J')-K'J=0,

up to an irrelevant fixed determinant sign. This says
(K/J)'/(K/J)=1, the same impossible rational logarithmic-derivative
identity. Therefore W is nonzero.

Differentiate (5) and use LC_1=LC_2=0 and L^[1]B=0. The algebraic
Abel identity is



$$
W'=\left(\frac{s}{z}-2\frac{D'}D\right)W.
                                                               \tag{6}
$$



The extra exponential factor contributes the subtracted 1: the
coefficient of partial^2 divided by zD in (1) is
-1-s/z+2D'/D. This derivation is a rational determinant identity.

Thus P=D^2 W is a nonzero polynomial of degree at most s satisfying
zP'=sP. Since s<p, coefficient comparison forces



$$
D^2W=\kappa z^s,\qquad \kappa\ne0.                       \tag{7}
$$



But D(0)=1, and D is nonconstant. The left side is divisible by
D^2 and the right side is not. This contradiction proves (4).
Surjectivity follows by dimension. Squarefreeness of D is not needed
for this last contradiction, though p is odd throughout. QED.

The conclusion is specific to the existence of the exponential
polynomial B. Without it, the old dimension-count observation only
gave a nonzero C for every beta,gamma, with no rank assertion.

## 3. Explicit cofactor C and its two scalar residues

Let U_d(beta,gamma) be the d-by-(d+1) coefficient matrix of
L:P_d -> P_(d-1), with row index k=0,...,d-1 and column index j.
It has only four possible nonzero entries in row k:



$$
\begin{array}{c|l}
j& (U_d)_{k,j}\\ \hline
k+2&(k+2)(k+1)(k-3d-2)=:a_k\\
k+1&(k+1)(\gamma-k)=:b_k\\
k&k(k-1)(k-3d)+(k-d)\beta+2d^2(d-1)=:c_k\\
k-1&-(k-d-1)(k-d)=:e_k.
\end{array}                                                    \tag{8}
$$



Out-of-range columns are omitted. Define the signed cofactor vector
and its polynomial by



$$
v_j=(-1)^j\det U_d[\text{all columns except }j],\qquad
C^*(z)=\sum_{j=0}^d v_j z^j.                                  \tag{9}
$$



These lie in Z[beta,gamma], have total parameter degree at most d,
and satisfy LC^*=0 identically. Lemma 1 proves that **on the locus
where B exists, this whole vector never vanishes modulo p**.
It therefore spans the kernel there. No particular v_j must be
nonzero, and no condition v_0!=0 has been imposed.

Define two integer polynomials R_0,R_1 by the ordinary monic division



$$
2(C^*)'-[(\beta+6d+2)z+\gamma-2d]C^*
\equiv R_0+R_1z\pmod{1+z^2}.                                \tag{10}
$$



Both have total degree at most d+1. Equation R_0=R_1=0 is precisely
the actual two-pole compatibility for this distinguished polynomial
kernel, including the case where D is irreducible over the field.

There is a short scalar determinant recurrence for one of these
cofactor coordinates. If D_m is the determinant of the leading
m-by-m block of U_d with columns 1,...,d, then



$$
\begin{aligned}
D_0&=1,\quad D_1=b_0,\quad D_2=b_1b_0-c_1a_0,\\
D_m&=b_{m-1}D_{m-1}-c_{m-1}a_{m-2}D_{m-2}
+e_{m-1}a_{m-2}a_{m-3}D_{m-3},\qquad m\ge3.
\end{aligned}                                                 \tag{11}
$$



In particular v_0=D_d. Expand the last row of this matrix, which
has one upper diagonal and two lower diagonals, to obtain (11).
It is a recurrence at fixed d for an actual cofactor polynomial;
it is not a recurrence in n for F_n and is not used to infer one.

## 4. The A equation and its two initial constraints become automatic

**Lemma 2.** Over K, suppose B is the monic degree-d solution of
L^[1]B=0 and R_0=R_1=0. Then there exists a unique triple with this
B, degrees at most d, satisfying the original extremal Taylor
conditions. Its C is a nonzero scalar multiple of C^*.

**Proof.** Take C_0=C^*. The pole condition makes T_L(C_0) a
polynomial of degree at most d-1. To check the degree, the only
possible degree-d term in the first line of (3) is
-2z C_0'+2d C_0, and it cancels when deg C_0=d; if the degree
is smaller, it is already at most d-1. The divided numerator
has degree at most d-1 as well.

Lemma 1 supplies A_0 in P_d with LA_0=-T_L(C_0), unique modulo
C_0. Let H_0=A_0+C_0 F_T, using the allowed arctangent jet.
The two initial columns



$$
\begin{pmatrix}C_0(0)&H_0(0)\\ C_0'(0)&H_0'(0)\end{pmatrix}
                                                               \tag{12}
$$



are independent. If not, a nonzero combination A+C F_T of them
would have its first two coefficients zero and would satisfy
L(A+C F_T)=O(z^(M-2)). The already reviewed triangular indicial
argument would give order at least M. A combination with C=0 is
a polynomial of degree at most d and hence cannot have that order
unless zero; otherwise the following exact two-function estimate
excludes it.

For polynomials A,C of degrees at most d with C nonzero, define



$$
S=D(A'C-AC')+C^2.                                           \tag{13}
$$



This nonzero polynomial has degree at most 2d: the leading terms
of A'C-AC' cancel when both degrees equal d. Nonvanishing follows
because (A/C)'+1/D cannot vanish; the rational derivative has zero
residue, while 1/D has nonzero simple-pole residues in a splitting
field. If A+C F_T has order at least M, differentiating its finite
jet gives z^(M-1)|S. The derivative error of F_T begins at degree
M-1, including when p=M. Since M-1=3d+3>2d, this is impossible.
Thus (12) is invertible.

We may consequently solve uniquely for mu,lambda so that



$$
A=\lambda A_0+\mu C_0,\qquad C=\lambda C_0                 \tag{14}
$$



makes the two initial coefficients of A+B E_T+C F_T zero.
The resulting lambda is nonzero. Otherwise a nonzero combination
mu C_0+B E_T would have order M, and the analogous exponential
polynomial

    C_0(B'+B)-C_0'B

would be a nonzero polynomial of degree at most 2d with origin
order at least M-1. Its nonvanishing follows from the impossibility
of a rational logarithmic derivative equal to -1. This is again
a contradiction. The finite-jet sufficiency proof of the old full
system now gives the desired order M. Uniqueness also follows
from (12), or from the previous injectivity of the top B coefficient
on the extremal Taylor space. QED.

For completeness, the residues also imply C_0(+/-i)!=0 here.
If a zero of C_0 at either root of D were simple, (10) would fail.
If its multiplicity m were at least two, the lowest local term of
LC_0 would have coefficient -2m^2(m-1), which is a unit for
2<=m<=d<p. Thus such a zero cannot occur. This local observation
is consistent with the original monomial Wronskian evaluation;
it supplies no separate exclusion once (10) is imposed.

## 5. Four parameter equations are equivalent to the full defect

Construct B^*(z;beta,gamma) from b_d=1 by solving the coefficients
of L^[1]B at degrees d+1,d,...,2, in that order. The coefficient
used to solve for b_(d-r) is -r, for r=1,...,d. Thus each coefficient
belongs to (1/d!)Z[beta,gamma], with total degree at most d, and
the construction is defined in every ring under consideration.
Put



$$
E_1=d![z^1]L^{[1]}B^*,\qquad E_0=d![z^0]L^{[1]}B^*.
                                                               \tag{15}
$$



These are integer polynomials of total degree at most d+1. The
factor d! is harmless at the allowed primes. The full coefficient
identity L^[1]B^*=0 is equivalent to E_0=E_1=0.

**Theorem 3 (field version).** For any field K of characteristic
p>3d+3, the actual extremal degree-d Taylor space is nonzero if
and only if there exist beta,gamma in K with



$$
\boxed{E_0=E_1=R_0=R_1=0.}                                  \tag{16}
$$



Necessity follows from the old no-accessory classification and
Lemma 1: normalize its unit top B coefficient, and its polynomial
C must be a nonzero multiple of (9). Sufficiency is Lemma 2.

The polynomial C^* being nonzero and the low initial matrix being
invertible are consequences of E_0=E_1=0 and, for the latter,
R_0=R_1=0. They are not omitted saturation hypotheses. In particular
(16) is a genuine four-equation description in two scalar variables,
not a system with hidden polynomial unknowns A,B,C.

The same equivalence over field extensions causes no descent issue:
nontriviality of the kernel of the original matrix with F_p entries
over an extension is equivalent to rank loss over F_p itself.

## 6. Prime-power version and exact extremal-content valuation

The previous theorem extends to R_h with "nonzero extremal triple"
replaced by "primitive coefficient vector in the kernel modulo p^h."
Here primitive means that at least one coefficient is a unit.

We record the lifting details so that a field-level rank test is not
silently promoted to a valuation bound.

* Starting from a primitive approximate extremal triple, its reduction
  modulo p is nonzero. The reviewed leading-numerator identity makes
  its b_d and Xi_d units. The finite-jet determinant order and degree
  bound therefore give N=kappa z^s with kappa a unit over R_h.
  The original cofactor construction of (1)--(3) works over R_h:
  its scalar divisions are by this kappa and by integers below p;
  its two leading Laurent coordinates have determinant Xi_d, a unit.
  Hence it gives beta,gamma and the full system (2), including residues.
  No division by a nonunit cofactor is needed.
  Lemma 1 applied after reduction modulo p then gives a unit maximal
  minor of U_d over R_h. Its kernel is R_h C^*, so the actual C is
  lambda C^* with lambda a unit, because its reduction is nonzero.
  The residue equations for the actual C therefore imply exactly
  R_0=R_1=0 for C^*, also at the full p-power depth.
* Conversely a solution of (16) in R_h gives B^* with unit leading
  coefficient. Its reduction satisfies the hypotheses of Lemma 1.
  Thus U_d has a unit maximal minor, is surjective over R_h, and
  has a free rank-one kernel generated by C^*. The construction
  of A_0, then (14), goes through using the initial determinant
  (12), which is a unit by Lemma 2 over the residue field. The
  scalar lambda is likewise a unit. Finally the same indicial
  units k(k-1)(k-M) give all required jets modulo p^h.

The statement about cofactor divisions in the first bullet can also
be checked directly: all divisions by z remove already known origin
factors in polynomial identities, the only constant Wronskian divisor
is kappa, and the infinity elimination uses the invertible two-by-two
leading Laurent matrix. These are exact algebraic operations in R_h.

The reviewed extremal nullity bound says X_n has at most one nonunit
Smith invariant at p>3n. Its valuation is f=v_p(F_n). Therefore a
primitive approximate kernel modulo p^h exists exactly for h<=f.
Combining this fact with the ring equivalence proves



$$
\boxed{
v_p(F_{d+1})=
\max\left(\{0\}\cup
\{h\ge1:\exists\beta,\gamma\in\mathbb Z/p^h\mathbb Z,
\ E_0=E_1=R_0=R_1=0\}\right).
}                                                            \tag{17}
$$



The maximum is finite because X_n has full column rank over Q.
The polynomial system in (17) is fixed for the given degree d;
no p-dependent truncation or change of parameter normalization
has been introduced. Compatible or incompatible choices of roots
at different h cause no issue in this equality.

## 7. What arithmetic remains

The exact isolated-defect question is now whether the ideal

    (E_0,E_1,R_0,R_1) in Z[1/(3d+3)!][beta,gamma]

is the whole ring, or, more weakly, whether the depths of its local
solutions in (17) admit a useful bound. A concrete sufficient
local identity would be

    P_0 E_0 + P_1 E_1 + Q_0 R_0 + Q_1 R_1 = c_d,

with all coefficients integral at p; then v_p(F_(d+1))<=v_p(c_d).
If c_d were supported only on primes at most 3d+3, it would exclude
all isolated large-prime defects. Such an identity has not been
proved. The existing full characteristic-zero rank ensures that
some nonzero rational constant lies in the ideal over Q, but it
does not control its integral prime factors or their exponents.

There is no inference from the order-d recurrence (11) alone to
the content F_n. It computes a particular accessory cofactor,
while the four simultaneous scalar equations and their lifting
depths carry the arithmetic. The new result removes the earlier
unknown A solvability, endpoint initial matrix, and C selection
from that smaller problem without dropping any actual Taylor row.

This does not bound the reduced endpoint denominator or prove a
shrinking integer form in e+pi. It is an arithmetic continuation of
the exact extremal-content and adjacent-content results.

## 8. Bounded algebra controls

An independent symbolic expansion of L(z^m)/z^m with arbitrary
symbolic d,m,beta,gamma verified every coefficient in (8), and an
arbitrary-monomial expansion of L^[1] verified its raising coefficient
m-d. The continuant (11) was also checked against direct determinants
of abstract banded matrices through size five, with all band entries
independent symbols. These are algebraic normalization controls, not
new actual HP degree constructions, modular scans, or evidence for
the unsolved saturation statement. The proofs above do not depend
on extrapolating those finite controls.
