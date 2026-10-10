> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact dual error integrals, an integral Rodrigues polynomial, and the primitive ledger

Date: 2026-09-13. Original continuation by audit_computations; independent review passed in `raw_dual_endpoint_error_integrals_independent_review.md`.

This note derives both full simultaneous errors from the primitive dual
polynomial. The exponential error has a real beta-weight integral. The
arctangent error has an integral Rodrigues polynomial and, after an exact
contour deformation, a real positive kernel multiplying the real part of
that polynomial on a specified circular arc. The latter absolute mass
has an all-index factorial lower bound. No sign assumption on the
primitive residual polynomial or its transformed polynomial is made.

The resulting integer form is exactly a multiple of the existing type-I
endpoint form. This does not create a different approximation sequence or
remove the endpoint gcd.

## 1. Earlier representations and the precise new object

The following existing notes were inspected before this derivation:

* `sources/raw_arctan_endpoint_remainder.md`: the type-I endpoint has
  two real tail integrals, a Peano kernel, and a contour identity; its
  polynomial and endpoint primitive normalizations are different.
* `raw_arctan_positive_kernel_attempt.md`: the whole normalized type-I
  error is one positive-kernel integral against a necessarily signed
  polynomial P_B.
* `raw_arctan_dual_factorial_mass.md`: that type-I polynomial has at
  least factorial absolute mass, and some strong cancellation is
  already forced by its high orthogonality.
* `raw_extremal_dual_polynomial_and_content_identity.md`: the primitive
  cofactor polynomial W, the simultaneous denominator Qhat, its endpoint
  scalar Z, and the exact type-I cross-product identity.
* `raw_actual_endpoint_integral_dual_numerators.md`: both simultaneous
  numerator polynomials are globally integral and their endpoint
  combination gives the selected actual rational approximant.

The new integrals below are for the two simultaneous type-II errors,
in that primitive-cofactor normalization. They are not the previous
type-I tail integrals with a renamed free polynomial.

Fix n>=1. Use the integer primitive cofactor vector w_k, n<=k<=3n,
and the exact polynomials

    W(t)=sum_(k=n)^(3n) w_k t^k=t^n(t-1)^n V(t),
    V in Z[t], deg V<=n, content(V)=1,
    T(t)=sum_(r=0)^(2n) (n+r)! w_(n+r) t^r,
    Qhat(z)=z^(2n)T(1/z)/n!,       Z=Qhat(1)!=0.               (1)

The raw moment functional is

    L(f)=(1/(2i)) integral_(-i)^i f(t)dt.

The exact conditions are

    L(t^s T)=0, 0<=s<n,
    Borel(T)=D^n W.                                         (2)

Let Pe and Pa be the Taylor polynomials of degrees at most 2n of
Qhat(z)e^z and Qhat(z)atan(z), respectively. Both belong to Z[z].
Write

    Re(z)=Qhat(z)e^z-Pe(z),
    Ra(z)=Qhat(z)atan(z)-Pa(z).                               (3)

## 2. The full exponential error has a positive beta kernel

Taylor's integral formula, applied separately to each reciprocal
coefficient in (1), gives

    Re(z)=z^(2n+1)/n! * integral_0^1
                                e^{z(1-t)} Borel(T)(t)dt.

Every derivative W^(j) with j<n vanishes at both zero and one.
Integrating by parts n times therefore has no boundary terms and yields

    Re(z)=z^(3n+1)/n! * integral_0^1 e^{z(1-t)} W(t)dt.         (4)

This is an entire-function identity, not just the first free Taylor
coefficient. In particular

    Re(1)=(-1)^n/n! * integral_0^1
                           e^{1-t}[t(1-t)]^n V(t)dt.         (5)

Its kernel is positive. Thus a fixed sign of V on (0,1), if proved,
would determine the sign of Re(1). No such sign is assumed here.
The immediate bound is

    |Re(1)|<= e n!/(2n+1)! * ||V||_[0,1].                    (6)

It retains the norm of the actual primitive polynomial V.

## 3. A second, globally integral Rodrigues polynomial

There is a unique polynomial S with D^n S=T and with zeros of order
at least n at both -i and i. To see existence, first choose the
n-fold antiderivative based at -i. Its j-th derivative at i, j<n,
is an integral of T against (i-t)^(n-1-j), which vanishes by (2).
Uniqueness follows because the difference of two such antiderivatives
has degree less than n and a zero of order n. Conjugation and the two
endpoint conditions show that S has real coefficients.

Therefore

    S(t)=(1+t^2)^n U(t),    deg U<=n,
    T=D^n[(1+t^2)^n U(t)].                                  (7)

This U is not the original primitive V. It is nonzero, because T is
nonzero. Its integrality and stronger factorial divisibility are exact.
Consider the integer polynomial

    S0(t)=sum_(r=0)^(2n) r! w_(n+r) t^(n+r).

One has D^n S0=T, so S-S0 has degree less than n. Divide S0 by the
monic integer polynomial (1+t^2)^n. The quotient is U: otherwise
the difference of the two quotients, multiplied by that degree-2n
polynomial, would have degree less than 2n. The remainder consequently
has degree less than n. In particular U and S are integral.

More explicitly, if U(t)=sum_(j=0)^n u_j t^j, monic division at
infinity gives

    u_j=sum_(h=0)^floor((n-j)/2)
       (-1)^h binom(n+h-1,h) (n+j+2h)! w_(2n+j+2h).           (8)

Every term contains (n+j)!, proving

    U in Z[t],   (n+j)! divides u_j,   0<=j<=n.              (9)

In particular U is divisible coefficientwise by n!, but it is not
asserted primitive after that division. All further content is retained.
No exact degree n or nonzero endpoint of U or V is needed.

## 4. The full arctangent error and a positive-kernel circular arc

The identity atan(z)=z L((1-zt)^(-1)) and the reciprocal coefficients
in (1) give the full Taylor error

    Ra(z)=z^(2n+1)/n! * L(T(t)/(1-zt)).                       (10)

It initially follows near z=0 and continues analytically along the
real segment 0<=z<=1. The orthogonality in (2) alternatively puts
an extra factor (zt)^n in its integral. Substitution of (7) and n
integrations by parts give, with both endpoint zeros retained,

    Ra(z)=(-1)^n z^(3n+1)
              L((1+t^2)^n U(t)/(1-zt)^(n+1)).               (11)

At z=1 the only pole in the integrand is t=1. Deform the path from
-i to i to the LEFT circular arc

    t(phi)=1-sqrt(2)e^{i phi},
    phi: pi/4 down to -pi/4.

The region between the old segment and this arc excludes t=1;
there are no other poles. The two exact identities on this arc are

    (1+t^2)/(1-t)=2sqrt(2)cos(phi)-2=:F(phi)>=0,
    dt/(1-t)=-i dphi.

Thus the orientation and normalization yield

    Ra(1)=(-1)^n/2 * integral_(-pi/4)^(pi/4)
                           F(phi)^n U(t(phi))dphi
         =(-1)^n/2 * integral_(-pi/4)^(pi/4)
                           F(phi)^n Re U(t(phi))dphi.         (12)

The second equality uses conjugation and the real coefficients of U.
The kernel is strictly positive in the open arc, but its multiplying
real part is not asserted positive. The arc lies in |t|<=1.

Put rho=2(sqrt(2)-1), the exact maximum of F. On |phi|<=pi/4,
1-cos(phi)>=sqrt(2)phi^2/4, so

    F(phi)<=rho-phi^2<=rho exp(-phi^2/rho).

Consequently, for n>=1,

    |Ra(1)|<= (1/2)rho^n sqrt(pi rho/n)
                                  ||U||_arc.                (13)

This is a true full-error bound. It retains the actual integer
polynomial norm, whose factorial scale cannot be ignored.

## 5. Bounds in primitive V coordinates and a factorial mass obstruction

Put H_V=sum_j |[t^j]V|. The factorization W=t^n(t-1)^n V gives
sum_k|w_k|<=2^n H_V. Summing (8), bounding its factorials by (2n)!,
and using the hockey-stick identity gives

    ||U||_arc<=sum_j|u_j|
      <=(2n)! 2^n H_V
          *sum_(h=0)^floor(n/2) binom(n+h-1,h)
      <=(2n)! 8^n H_V.                                      (14)

This deliberately loose norm estimate supplies an explicit primitive-
coordinate upper bound in (13). It does not decay.

There is also a lower bound for the actual WEIGHTED ABSOLUTE MASS,
requiring no upper bound on H_V and no assumption about U's roots.
Define

    A_n=integral_(-pi/4)^(pi/4) F(phi)^n |Re U(t(phi))|dphi.

Let d=deg U and u_d!=0. Equation (9) gives |u_d|>=(n+d)!.
The polynomial

    p(x)=Re U(1-sqrt(2)e^{i phi}),   x=cos(phi),

is of degree d in x. For d>=1 its leading coefficient has magnitude

    |u_d| 2^(3d/2-1),                                       (15)

because cos(d phi)=T_d(x) has leading coefficient 2^(d-1).
For d=0, p is the nonzero integer constant U.

Set

    c=cos(pi/8),   ell=1-c>0,
    rho0=2sqrt(2)c-2>0.

For any real degree-d polynomial p of leading coefficient a_d,
testing against the shifted ordinary Legendre polynomial on [c,1]
gives

    integral_c^1 |p(x)|dx
       >= |a_d| ell^(d+1)/[(2d+1)binom(2d,d)].               (16)

Indeed the test polynomial has supremum at most one; its leading
coefficient is binom(2d,d)/ell^d and its squared L2 norm is
ell/(2d+1). Orthogonality removes every lower term of p.
Combining (15)-(16), using binom(2d,d)<=4^d and d<=n, gives

    integral_c^1 |p(x)|dx
       >= n! ell/[2(2n+1)] * (ell/sqrt(2))^n.                (17)

The d=0 case satisfies the same looser inequality directly. On the
inner arc |phi|<=pi/8 one has F>=rho0, while
dphi=dx/sqrt(1-x^2) dominates dx. Therefore

    A_n>= n! ell/(2n+1) * (rho0 ell/sqrt(2))^n.              (18)

Thus log A_n>=n log n-O(n), in the specified primitive-cofactor
normalization. This is an absolute-mass theorem, not a lower bound
for |Ra(1)|. A signed-cancellation factor is indispensable for proving
a small UNREDUCED arctangent error from this representation. In
particular a proof of shrinking obtained by merely dropping signs
from (12) and claiming a small polynomial norm is impossible in
this normalization. This does not exclude a strategy that separately
proves a sufficiently large endpoint gcd; that factor is restored
explicitly below.

## 6. The combined integer form and the exact endpoint gcd

Let N=Pe(1)+4Pa(1), an integer. Then the actual integer form is

    Lambda_n=Z(e+pi)-N=Re(1)+4Ra(1)

    =(-1)^n [ (1/n!)integral_0^1
                         e^{1-t}[t(1-t)]^n V(t)dt
                +2 integral_(-pi/4)^(pi/4)
                         F(phi)^n Re U(t(phi))dphi ].        (19)

Both displayed kernels are positive. Positivity of V and Re U in
one common orientation would be a sufficient sign lemma, but no
such property has been proved. Individual nonvanishing of Re(1)
and Ra(1) follows from irrationality of e and pi and the nonzero
integer Z; it does not exclude their cancellation in (19).

The cross-product bridge in the earlier notes proves

    A_n^I(1)=-N/Z,
    g=gcd(|Z|,|N|),      q_n=|Z|/g,
    q_n[(e+pi)-N/Z]=sign(Z) Lambda_n/g.                      (20)

Here A_n^I is the canonical type-I solution with B(1)=1,C(1)=4.
Thus Lambda_n/Z is EXACTLY the same normalized analytic remainder
as in the old type-I positive-kernel note. After removing g, (20)
is exactly the same endpoint-primitive integer form, up to its
fixed sign convention. The cofactor primitivity of V does not
permit one to replace g by one.

For example, the norm-only upper bound for this primitive form is

    |Lambda_n|/g
      <= [ e n! H_V/(2n+1)!
          +2 rho^n sqrt(pi rho/n) ||U||_arc ]/g.             (21)

Neither the arctangent norm nor this endpoint gcd is controlled
well enough to make (21) tend to zero. The previously proved
distinctness of the canonical endpoint rationals implies that at
most one Lambda_n vanishes; this note does not need a new all-index
nonvanishing assertion to preserve that result.

## 7. What the dual representation adds and what remains

The new formulas retain both errors at full order 3n+1, make the
two prescribed endpoint factors explicit, and introduce a second
integer polynomial U with coefficientwise factorial divisibility.
The arctangent contour has an exact positive kernel of maximum
2(sqrt(2)-1), with a Gaussian-width upper bound and an independent
factorial absolute-mass lower bound. These are concrete properties
of the actual dual solution, not arbitrary numerical evidence.

The signed factors V on [0,1] and Re U on the arc are linked by
the exact transformation (8) and all original orthogonality conditions.
No root-location or sign theorem for them follows merely from the
two Rodrigues factors. A useful next target is such a joint sign
or signed-integral bound, or an estimate for the actual cancellation
factor in (12) combined with the gcd in (20). Since (20) identifies
the result with the original endpoint family, this is a different
representation of its analytic/arithmetic obstruction, not a way
around primitive normalization. No irrationality conclusion is claimed.

Exact normalization controls using only the already saved n=1,2
cofactor vectors are in `check_raw_dual_error_integrals_existing.py`
and `raw_dual_error_integrals_existing_checks.json`. They verify the
integer U polynomial and divisibility, both numerator polynomials,
the complete exponential error, and the oriented circular-arc
arctangent error. No new canonical system or index scan was used.
