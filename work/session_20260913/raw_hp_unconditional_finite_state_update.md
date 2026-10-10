> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An unconditional bounded-state degree update

Date: 2026-09-13. Root synthesis and continuation. This note removes the
generic-locus assumptions from the bounded-state construction. It is
an exact algebraic reduction for the actual family, not an estimate for
its orbit or its endpoint error. The component arguments and the full
local-to-global construction have passed independent review; see
`raw_hp_unconditional_update_independent_review.md` and the separate
origin, infinity, and logarithmic-pole reviews.

## 1. Statement and input

For the canonical raw family n>=1, write



$$
R_n=A_n+B_ne^z+C_n\arctan z=O(z^{3n+1}),
 \quad B_n(1)=1,\quad C_n(1)=4,
$$



with polynomial degrees at most n. Retain its nonzero Wronskian factor
Q_n of degree q<=3, its scalar homogeneous equation
L_n=\sum_{j=0}^3 A_{j,n}(z)\partial_z^j, and six rational endpoint jets
of each of B_n e^z/e and C_n. Here division by e in the first jet list
means the constant value e at the endpoint:



$$
u_r=e^{-1}(B_ne^z)^{(r)}(1),\quad
 v_r=C_n^{(r)}(1),\qquad 0\le r\le5.
$$



There is an exact next-degree construction using a bounded number of
rational operations and fixed-size linear systems in these data and n.
The number of scalar entries and equations is bounded independently of
n. This assertion concerns arithmetic operation counts and dimensions;
it does not bound the bit sizes of rational entries.

No condition of cubic degree, squarefreeness, or avoidance of 0,1,+/-i
is imposed on Q_n. Polynomial factorization of degree at most three,
or equivalent exact quotient-algebra operations, is permitted in the
local description below. Conjugate algebraic conditions descend to
rational linear conditions of bounded size.

The unknown is



$$
S=\frac{N_0+N_1\partial_z+N_2\partial_z^2}{Q_n},
 \qquad \deg N_j\le6.
\tag{1}
$$



There are 21 rational unknowns. Existence of the actual operator with
these degree bounds was proved by mixed Wronskians in
`raw_hp_rational_degree_transfer.md`. The task here is to form all its
selecting conditions without carrying the length-n polynomial arrays.

## 2. Ordinary accessory points, including multiple roots

Let a be a Q-root away from 0,+/-i, and h its multiplicity. Every
solution of L_n is analytic there. If r0<r1<r2 are the echelon orders,
the Wronskian gives r0+r1+r2=h+3, so r2<=h+2<=5. Cofactor valuation
bounds make the equation regular singular at a, with indicial roots
exactly these three nonnegative integers.

In x=z-a, use the Euler form



$$
[\theta(\theta-1)(\theta-2)+b(x)\theta(\theta-1)
                         +c(x)\theta+d(x)]y=0,
\tag{2}
$$



where b,c,d are analytic rational germs. The six Taylor coefficients
y0,...,y5 of the local analytic solution space are the kernel of its
coefficient equations through degree five. This kernel has dimension
three: there are at most three free indices, the simple indicial
roots; the three actual analytic solutions inject into these jets.
All recurrences beyond five have nonzero diagonal coefficient.

For each vector of a basis of that kernel, require that the numerator
in (1) vanish modulo x^h. Only old jets through h+1<=4 are needed.
These are fixed-size linear conditions on the N coefficients. They
are equivalent to S mapping the entire actual local solution space
to analytic germs at a, including repeated apparent roots.

## 3. The origin and its possibly high indicial root

`raw_hp_origin_finite_jets.md` proves that the indicial roots at zero
are l0<l1<M, with



$$
l_0+l_1\le4,\qquad M\in\{3n+1,\ldots,3n+4\}.
$$



The coefficient equations of (2) through degree four give exactly the
truncated low analytic solution space, with the high root included if
M=4. Its dimension is at most three; actual low solutions ensure that
the resonant compatibility conditions do not introduce any additional
restriction at this truncation. Require the numerator in (1) to have
zero coefficients below h=ord_0 Q on this truncated space. These are
exactly the possible origin pole-removal conditions. A high solution
whose jets vanish through degree four contributes no missing principal
part, since such a part only uses old jets through h+1<=4.

In addition, reconstruct the normalized high solution
R_*=z^M(1+u1 z+...+u7 z^7+...) by the fixed recurrence in that note and
impose



$$
N_0R_*+N_1R_*'+N_2R_*''=O(z^{3n+4+h}).
\tag{3}
$$



This uses at most eight relative coefficients. It is unaffected by the
unknown nonzero scale of the actual high solution. Together the origin
conditions guarantee analyticity of every image and the required
next-degree order of the actual remainder.

## 4. Exceptional logarithmic points

At a=+i or -i, put x=z-a and h=ord_a Q<=3. All actual local solutions
have the form a(x)+b(x) log x with a,b analytic, and their logarithmic
coefficient space has dimension one. Their monodromy is nonzero and
has square-zero nilpotent part.

Here is an elementary bounded-exponent argument, including Q(a)=0.
Choose an echelon basis of the analytic plane span(B exp(z),C), with
orders l0<l1. The fixed monodromy image C has order c equal to one of
these two orders. Write the third solution as H+kappa C log x, where
H is analytic and kappa!=0. Subtract constant multiples of the two
analytic basis vectors until H has order d distinct from l0,l1, or
H=0 with d=infinity. This takes at most two eliminations.

The analytic and logarithmic parts of the Wronskian have nonzero
leading terms of orders d+l0+l1-3 and c+l0+l1-3 respectively. The latter
is the confluent Vandermonde for the repeated order c. Since d!=c,
these two terms cannot cancel. Thus, putting m=min(c,d),



$$
\boxed{m+l_0+l_1=h+1\le4.}
\tag{4}
$$



Subtracting the logarithmic column also gives the cofactor valuation
bounds needed for regular singularity. The indicial roots are
l0,l1,m. If d<c they are distinct. If c<d, the leading C log term
forces the root c to be double. Every root is a nonnegative integer
at most four.

Use the ten variables a0,...,a4,b0,...,b4 in the ansatz
`a(x)+b(x) log x` and impose both log and non-log equations from (2)
through degree four. This kernel is exactly the three-dimensional
jet image of the actual local solution space. For an index k with
I(k)!=0, the two new coefficients are uniquely determined. A simple
root allows at most one free coefficient; a double root allows at
most two. The actual solutions already provide three independent
jet vectors, so the finite kernel has dimension precisely three.
This dimension argument does not assume an unproved convergence of
newly constructed formal series.

For every basis vector of that kernel, apply (1) formally and require
all negative powers of x in both its log and non-log coefficients to
vanish. The most negative possible power is -h-2. All these principal
parts depend only on a,b through degree h+1<=4, so this is again a
bounded rational linear test. It is equivalent to preserving the
allowed analytic-plus-logarithmic behavior at the point.

## 5. Infinity data from two fixed five-coefficient systems

Write qlead=[z^q]Q. The actual infinity powers satisfy



$$
b+c+d=3n+q-4,\qquad b,c,d\le n,\qquad c\ne d.
$$



The two Laurent powers have defects n-c,n-d between zero and four;
the exponential-polynomial branch has defect n-b between zero and
three. None of these branches needs a chosen global normalization.

For x=1/z and y=z^n F(x), divide L_n y by z^(n+q+1). The resulting
polynomial-in-x Euler operator is



$$
\mathcal P_{\rm alg}(x,\theta)=
 \sum_{j=0}^3\sum_k [z^k]A_j\,
           x^{q+1+j-k}(n-\theta)_{\underline j}.
\tag{5}
$$



Every exponent of x is nonnegative by the proved coefficient degree
bounds. Its constant Euler polynomial is



$$
-qlead\,(s-(n-c))(s-(n-d)).
\tag{6}
$$



Therefore its equations through degree four on F0,...,F4 have kernel
exactly two. The two actual Laurent branches inject there, and the
recurrence has at most two free indices, both in this range.

For the exponential branch define
`tilde A_k=sum_{j>=k} binom(j,k) A_j`, the coefficients after the gauge
y=e^z g. Divide the equation for g=z^n G(x) by z^(n+q+2). The same
formula as (5), with tilde A and exponent q+2+j-k, gives nonnegative
powers. The degree bounds for tilde A0 and tilde A1 are q+2 and q+3;
their leading coefficients are -b qlead and qlead. The constant Euler
polynomial is thus



$$
qlead\,(n-b-s).
\tag{7}
$$



The coefficient equations through degree four have a one-dimensional
kernel containing exactly the truncated actual exponential branch.

For both vectors of the Laurent kernel, and for the exponential
kernel vector with derivatives interpreted after the exponential gauge,
require the numerator in (1) to have no powers greater than n+q+1.
Its maximum possible power is n+6. Only the first five coefficients
of the old branches can contribute to these forbidden terms. These
are bounded linear conditions on N0,N1,N2 for every q and every
infinity degree type.

## 6. Endpoint conditions and rational descent

The six carried endpoint jets determine all later jets needed in this
step, even when Q(1)=0. At the endpoint the three analytic echelon
orders have sum 3+ord_1Q<=6, so their maximum is at most five. The
Euler recurrence at that point has no resonant index at or above six.
Five further steps therefore give jets through ten.

Apply S to the endpoint u and v sequences, dividing out any zero of
Q by the ordinary derivative quotient. Impose



$$
(S(B e^z))(1)/e=1,\qquad (SC)(1)=4.
\tag{8}
$$



These are two rational linear equations. Pole removal already proved
that the required quotient limits exist. Computing six new endpoint
jets requires old jets only through 5+h+2<=10, so the new state again
has the same fixed size.

All local linear conditions at algebraic accessory roots are unchanged
by conjugation. Equivalently one may calculate them in quotient algebras
of the rational factors of Q, then equate rational coordinates. This
produces a rational linear system in the 21 N coefficients. The sum of
root multiplicities is at most three, and every local truncation and
degree bound above is fixed. Hence the total number of equations is
bounded independently of n; no root search of growing degree or
growing Taylor prefix is part of the construction.

One can avoid algebraic root extraction entirely. Squarefree-decompose
Q over Q and remove its known factors z and D. For each remaining
multiplicity block f, calculate in the etale quotient algebra
Q[t]/f(t), translating z=t+x. If a candidate Gaussian pivot is a
nonzero nonunit, split f with its gcd with that pivot. The degree is
at most three, so this process has uniformly bounded length. Once
the needed pivots are units, fixed-degree extended gcd supplies their
inverses. Equating quotient-algebra coordinates gives the rational
linear conditions asserted above.

## 7. Global sufficiency, uniqueness, and state propagation

For a solution N of all these equations, define the rational functions
\widehat A,\widehat B,\widehat C by the explicit formulas (11) of
`raw_hp_rational_degree_transfer.md`. Their only possible finite poles
are at Q-roots and +/-i. At an ordinary finite point, S maps all actual
solutions to analytic functions; hence \widehat B and \widehat C have
no poles, and then \widehat A has none. The same holds at the origin.

At a logarithmic point, S(B e^z) and SC have no negative powers and
no logarithm, so \widehat B,\widehat C are analytic. The log coefficient
of SR is exactly kappa SC by differentiation. Subtracting
\widehat C arctan z therefore leaves an analytic germ, by the imposed
non-log principal-part conditions. Thus \widehat A is analytic too.
All three rational functions are polynomials.

The infinity conditions show that \widehat B has degree at most n+1
and that the full Laurent plane maps to germs of growth at most n+1.
In particular \widehat C has that degree bound. Since
arctan z minus its local infinity constant is O(1/z), the corresponding
Laurent image also gives the bound for \widehat A. Condition (3) is
the next raw Taylor condition, and (8) is its canonical normalization.
The existing all-degree rank theorem identifies the resulting triple
with the actual next triple.

The system is consistent because the genuine mixed-Wronskian transfer
satisfies every local condition. It is unique: two solutions would
give the same next polynomial triple, so their difference would be a
rational operator of order at most two annihilating the three linearly
independent actual solutions. Their invertible meromorphic jet matrix
forces that operator to be zero. Thus the rational system has rank 21.

The next two rows of the full transfer follow by differentiation and
the current companion equation. Update the companion by
`C_next=(T'+T C) T^{-1}` and update the Wronskian scale by
`Q_next=det(T) Q/z^3`. The latter preserves the canonical normalization.
The previously proved degree bounds apply again, regardless of the
new Q configuration. Endpoint jets propagate as in Section 6.

The actual remainder jets may be carried as an additional fixed column,
or as three formal rational coefficient columns attached to 1,e,pi.
These columns are propagated from the known polynomial representation;
they are not recovered by assuming a unique representation of a real
number. No rational linear independence of 1,e,pi is assumed. The zeroth
remainder jet is A_n(1)+e+pi, so its specified constant rational
coefficient also retains the actual reduced endpoint denominator. This
reduction provides no bound for that denominator or for the rational
recurrence orbit.

There is an especially simple entirely rational choice of the extra
six-jet column. Set, as a germ near z=1,



$$
K_n^{\rm end}(z)=R_n(z)-U_n(z)-\frac\pi4 C_n(z)
                =A_n(z)+C_n(z)(\arctan z-\pi/4).
\tag{9}
$$



Its derivatives at 1 are rational, it is a constant linear combination
of old solutions, and S K_n^end=K_(n+1)^end. Its zeroth jet is exactly
A_n(1). Thus eighteen rational endpoint scalars, for U_n/e, C_n and
K_n^end, retain both the whole endpoint form and its reduced rational
denominator. This coefficientwise statement is independent of any
unknown arithmetic relation between e and pi.

## 8. Remaining mathematical task

This construction removes departure from the generic locus as an
obstruction to existence of a bounded-state rational update. It does
not prove orbit stability, scaled accessory limits, asymptotic modes,
control of cancellation in the endpoint products, or primitive
shrinking. Those are now concrete dynamical and arithmetic estimates
for the actual normalized orbit. No proof of rationality or irrationality
of e+pi is claimed.
