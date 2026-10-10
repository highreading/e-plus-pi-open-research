> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the unconditional finite-state update

Date: 2026-09-13. Reviewer: audit_sources. The files reviewed are
`raw_hp_unconditional_finite_state_update.md` and
`raw_hp_all_degree_infinity_jets.md`, together with the previously audited
mixed-Wronskian transfer and homogeneous scalar equation. This review
records exact structural mathematics, not an endpoint asymptotic estimate
or a proof about the rationality of e+pi.

## 1. Result of review

The unconditional construction passes this independent review. In
particular, the rational descent, canonical Wronskian normalization,
and propagation of six endpoint jets are valid even at the stated
exceptional accessory configurations. No additional generic-locus
hypothesis is needed for existence or uniqueness of the bounded-size
rational update.

The operation-count assertion concerns arithmetic in rational numbers
and fixed-degree polynomial quotient algebras; it gives no uniform bit
complexity and no asymptotic estimate for the orbit. The refinements in
Sections 3 and 5 below make two implementation-free mathematical points
explicit: algebraic root extraction is unnecessary, and formal endpoint
coefficient columns do not assume independence of 1,e,pi.

## 2. All-degree infinity reconstruction

For the equation L=sum A_j partial^j, let q=deg Q and lambda be the
leading coefficient of Q. Direct differentiation gives

    partial_z^j(z^n F(1/z))
       = z^(n-j) (n-theta)_[j] F(x),  x=1/z.

Therefore the matrix entry in equation (7) of the infinity note is

    sum_j A_(j,q+1+j-(r-s)) (n-s)_[j].

The exponent of x is r-s, and the theta polynomial acts on the input
coefficient indexed by s. Thus there is no reversed operator-order or
index-shift error. Its diagonal is

    -lambda (s-(n-c))(s-(n-d)).

The two zero indices are distinct and lie in {0,...,4}. A triangular
recursion has at most one new free coefficient at each such index. The
actual two convergent Laurent germs have distinct leading orders in
this range and give independent five-jets. Consequently the truncated
kernel has dimension exactly two and is precisely the actual Laurent
plane. This proves compatibility at resonance; it does not presume it.

After exponential conjugation, the leading coefficient of tilde A_1
is lambda and that of tilde A_0 at degree q+2 is -b lambda. The entry
in equation (12) consequently has diagonal

    lambda (n-b-s).

Its unique zero is in {0,...,3}. The actual exponential-polynomial germ
supplies the nonzero kernel vector, so that kernel has dimension one.

Finally, a transfer numerator of degree at most six has the form
z^(n+6) times an analytic power series. Division by Q gives growth at
most z^(n+1) if and only if that series has order at least 5-q. Hence
exactly the coefficients indexed 0,...,4-q must vanish. At most the
first five input coefficients are needed, for both ordinary and
exponentially conjugated numerators. All infinity degree tests in the
unconditional synthesis are therefore both necessary and sufficient.

## 3. Rational descent without algebraic root extraction

The local conditions may be described over algebraic closures without
making algebraic root extraction part of the rational operation count.
Here is a fully rational implementation of the descent argument.

Squarefree-decompose Q over Q. Remove the known factors z and z^2+1
from the ordinary-point factors. For each remaining squarefree
multiplicity block f, use the finite etale algebra

    K = Q[t]/(f(t)).

Its degree is at most three. Local expansion at every root in this
block is represented simultaneously by z=t+x in K[[x]]. All matrices
in the finite Taylor-kernel and principal-part tests have coefficients
in K. Divisions by units use extended polynomial gcd, of bounded
degree. If a proposed Gaussian pivot is a nonzero nonunit, split f
using gcd(f,pivot) and work on the two factors. Each proper split
decreases the degree; there can be at most three resulting components.
Thus finite-dimensional linear algebra can be carried out without
assuming that a nonzero element of a product algebra is invertible.

After these fixed-size kernel calculations, write each resulting
linear condition in a rational coordinate basis of K. Equating those
coordinates gives exactly the rational conditions valid at all roots
of the block. The known logarithmic points are treated in Q[i], also
of fixed degree. Root multiplicities and the finite truncation orders
are bounded. Polynomial gcd, finite Taylor expansion, Gaussian
elimination, and these coordinate comparisons use a bounded number of
rational arithmetic operations independent of n.

This argument also shows why no arbitrary choice of local complex
solution normalization can affect the result: the condition is that
the entire intrinsic local jet kernel is mapped to the required germ
class, and is invariant under a change of basis of that kernel.

## 4. Canonical normalization of the next equation

Let Psi_n have columns (R_n,B_n exp(z),C_n) and derivative rows 0,1,2.
The proved exact Wronskian identity is

    det Psi_n = exp(z) z^(3n-1) Q_n/(1+z^2)^2.

The finite local conditions, infinity bounds, origin order, and two
endpoint normalizations identify the transformed triple with the
canonical next triple. Hence the completed transfer matrix is exactly

    T_n = Psi_(n+1) Psi_n^(-1).

It follows, with no unspecified scalar factor, that

    Q_(n+1) = det(T_n) Q_n/z^3.

The endpoint conditions are important here: a freely rescaled triple
would scale its Wronskian cubically, whereas the actual normalized
triple has already been selected uniquely.

Writing C_n for the monic companion matrix, differentiation gives

    C_(n+1) = (T_n' + T_n C_n) T_n^(-1).

The new polynomial scalar coefficients are recovered by putting
A_(3,n+1)=z(1+z^2)Q_(n+1) and multiplying the negatives of the last
companion row by A_(3,n+1). They are the actual polynomial coefficients
because the transformed fundamental matrix is the actual next one.
The previously proved degree bounds therefore apply anew, irrespective
of cancellations, repeated roots, or a drop in deg Q_(n+1).

## 5. Endpoint jets and the rational endpoint coefficient

At z=1 all three solutions are analytic. If h=ord_1 Q, their distinct
echelon orders sum to h+3<=6, and the largest is at most five. The
Euler recurrence has no resonant index k>=6. Thus six compatible jets
determine the jets through order ten using five further scalar
recurrence steps. Passing between derivative jets and Taylor
coefficients only multiplies by fixed factorials up to 10!.

To obtain the six output jets of S y with S of order two and a
denominator zero of order h<=3, one needs the numerator through
degree h+5, hence input jets through h+7<=10. The finite local tests
already ensure the required numerator cancellations. Endpoint value
normalization and six-jet propagation therefore remain rational and
bounded when Q(1)=0.

The rational constant coefficient of the remainder can be retained
with only one additional six-jet column. Define the actual local
solution

    K_n(z) = R_n(z) - B_n(z)exp(z) - (pi/4) C_n(z)
           = A_n(z)+C_n(z)(arctan z-pi/4).

It is a constant linear combination of solutions of the same scalar
equation. Its Taylor coefficients at z=1 are rational, because

    arctan(1+t)-pi/4 = arctan(t/(2+t))

as analytic germs near t=0, and the last germ has rational Taylor
coefficients. In particular K_n(1)=A_n(1).

The other two rational jet columns are U_n/e and C_n/4. Thus the
remainder jet is represented symbolically by

    K_n + e (U_n/e) + pi (C_n/4).

All three columns individually satisfy the rational scalar recurrence.
Their propagation by S is exact, and

    S K_n = K_(n+1),

because S maps each of R_n,U_n,C_n to its corresponding canonical
next function. Carrying six K_n jets in addition to the twelve U_n/e
and C_n jets retains A_n(1), including its actual reduced rational
denominator. No claim that a numerical real number has a unique
representation in the span of 1,e,pi is made or needed.

## 6. Local and global consistency cross-check

At the origin, the required principal parts use only jets through
h+1<=4. The high solution either vanishes in that truncation or, for
M=4, appears in the finite kernel itself. Its separate order-raising
test needs at most eight relative coefficients, since the maximal
required input exponent is 3n+5+h and M>=3n+1.

At a logarithmic point, the independently proved bounded-exponent
lemma supplies the full analytic-plus-logarithmic jet space. Applying
S coefficientwise preserves the logarithmic coefficient as S C.
After removing the prescribed non-logarithmic principal parts,
subtracting the new C times arctan leaves an analytic germ. Therefore
the rational functions Ahat,Bhat,Chat have no finite poles. The full
Laurent-plane infinity test then bounds all three polynomial degrees;
it does not require selecting C from that plane by a connection
constant.

The genuine mixed-Wronskian operator proves consistency. Canonical
next-triple uniqueness and the invertible three-solution jet matrix
prove injectivity for an operator of order at most two. The rational
linear system consequently has rank 21. This is valid on the actual
normalized orbit; it is not a claim that arbitrary proposed accessory
coefficients satisfy the same finite-kernel dimension identities.

## 7. Limits of this result

The proof establishes an exact bounded-state evolution and preserves
the actual normalized endpoint coefficient. It gives no bound on
intermediate rational heights, primitive denominator growth, endpoint
cancellation, or the asymptotic location of accessory roots. Those
remain separate arithmetic and analytic questions. In particular,
finite-dimensional rational dynamics alone does not provide the
nonzero shrinking integer forms required to settle e+pi.
