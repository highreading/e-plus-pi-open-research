> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The full arctangent error in Toeplitz second-kind coordinates

Date: 2026-09-13. Original continuation by audit_computations.
Independent review passed in `raw_dual_second_kind_independent_review.md`.
This note proves a signed full-circle
second-kind identity and an exact partial-circle representation of the
actual arctangent error. It isolates their remaining connection problem.
No new canonical degree or root scan is used.

## 1. Normalization and the existing whole error

Assume n=2m>=2. Retain the actual primitive-cofactor polynomials V,U,
the reversal q(z)=z^nU(1/z), and the normalized Toeplitz solution

    v(z)=q(z)/(n!V(1)),       v=A^(-1)e_0,
    w(theta)=|1+e^(2i theta)|^(2m),
    f(theta)=e^(e^(i theta))w(theta),
    c_m=((2m)!)^2/[m!(3m)!].                                 (1)

All circle integrals below use dtheta/(2pi). The previously reviewed
formulas give V(1)!=0, v(0)>0, and

    U(t)=n!V(1)t^n v(1/t),
    Ra(1)=L[(1+t^2)^nU(t)/(1-t)^(n+1)],
    L(g)=(1/(2i)) integral_(-i)^i g(t)dt.                    (2)

The second equality is the full error Qhat(1)pi/4-Pa(1), not a
first omitted coefficient. Its sign (-1)^n is +1 on this even
subsequence. The earlier positive-kernel circular-arc formula and
the factorial absolute-mass obstruction were read before the present
derivation. No bound on ||U|| is substituted for a signed estimate.

## 2. A full-circle second-kind identity

Extend the finite functional
mu_n(p)=[z^(2n)]e^z(1+z^2)^np(z) to functions analytic near the
closed unit disk by the same contour integral. For |s|>1 define

    C_q(s)=mu_n(q(z)/(s-z)).

The exact moments of q give a rational expression:

    C_q(s)=sum_(r=0)^n (n+r)! V^(r)(1)/(r! s^(n+r+1))
           =n!V(1)s^(-n-1) B(1/s),
    B(x)=sum_(r=0)^n b_r x^r.                               (3)

Here b_r are the negative-row prediction coefficients already used
in V(1+t)/V(1)=sum n!b_r t^r/(n+r)!, and b_0=1. Equation (3)
is rational in s; its only possible pole is at zero. It must not
be confused with the arctangent error, which has different contour
data below.

Orthogonality supplies a useful exact product identity. The divided
difference (U(s)-U(z))/(s-z) is a polynomial in z of degree at most
n-1. Hence

    U(s) C_q(s)=mu_n(q(z)U(z)/(s-z)).

On the unit circle U(z)=z^n conjugate(q(z)), because q has real
coefficients. The contour weight of mu_n is f(z)z^(-n). Thus

    U(s) C_q(s)
      = integral_circle f(theta)|q(e^(i theta))|^2/(s-e^(i theta)).
                                                               (4)

In particular the same argument without the Cauchy kernel gives

    integral_circle f|q|^2
       =mu_n(qU)=n!u_n V(1)>0.                              (5)

This is a real positive quantity, although f is complex. It uses
u_n=U's leading coefficient, not U(0). The latter coefficient
appears in the different and possibly negative identity mu_n(q^2).

## 3. A signed half-line theorem and a prediction-product lower bound

For real a>1, put z=e^(i theta), c=cos theta, t=sin theta. Then

    Re[e^z/(a+z)]
       =e^c[(a+c)cos(t)+t sin(t)]/(a^2+2ac+1)>0.            (6)

Indeed a+c>0, cos(t)>=cos(1)>0, and t sin(t)>=0. Pairing
conjugate points shows the integral in (4) is real when s=-a.
Since q is not zero, equations (4) and (6) prove

    U(-a) C_q(-a)<0,             a>1.                       (7)

Neither factor can vanish on this half-line. From (3), C_q(-a)
has sign -sign(V(1)) for sufficiently large a. Continuity and
(7) therefore establish

    U(s)/V(1)>0 for s<-1,
    v(x)>0 and B(x)>0 for -1<x<0.                           (8)

These signs extend to the endpoints, as the following quantitative
bound makes explicit. Divide the integrand in (6) by
e^c cos(t), the positive Hermitian-part density. The ratio is

    [(a+c)+t tan(t)]/(a^2+2ac+1) >=1/(a+1),

because t tan(t)>=0 and
(a+c)/(a^2+2ac+1)>=1/(a+1); the last inequality is equivalent
to (a-1)(1-c)>=0. Equations (4)-(5) then give

    -U(-a)C_q(-a) >= n!u_n V(1)/(a+1).                    (9)

Both sides have finite limits as a decreases to one: the left
side is the product of a polynomial and the rational function in
(3), evaluated away from its only pole. One need not assign a
principal value to the singular boundary integrand to take this
limit. In particular U(-1)C_q(-1) remains strictly negative.

Substituting U(-a)=n!V(1)a^n v(-1/a) and (3) into (9) yields
the normalized product inequality

    v(x)B(x)>=v(0)/(1-x),            -1<=x<=0.               (10)

For -1<x<0 this is the preceding computation with x=-1/a.
At x=-1 it follows by the finite limit, and at x=0 it is equality
because B(0)=1. All three functions have real coefficients.
Thus both v and B are strictly positive on [-1,0]. Equivalently,
U has no real zero in (-infinity,-1], and q has no real zero in
[-1,0]. This is new signed information about the actual polynomials.

It does not give the sign of v at nonreal points on a semicircle,
or of U on the original complex arc. In fact the saved n=2 example
already shows that the latter real part changes sign.

## 4. Exact partial-circle Cauchy transform for the arctangent error

In (2), deform the t path to the previously reviewed LEFT arc
t=1-sqrt(2)e^(i phi), oriented from -i to i. Invert t=1/z.
Its image runs from i to -i on the left arc of the circle centered
at -1 with radius sqrt(2). Reversing this image gives an oriented
path gamma_L from -i to i. The transformed differential is

    [(1+t^2)^n t^n v(1/t)/(1-t)^(n+1)]dt
       =-[(1+z^2)^n v(z)/(z^(2n+1)(z-1)^(n+1))]dz.

The minus sign cancels the reversal of the path. Consequently

    Ra(1)/(n!V(1))
      =(1/(2i)) integral_(gamma_L)
             (1+z^2)^n v(z)/[z^(2n+1)(z-1)^(n+1)] dz.       (11)

All finite poles of this integrand are at 0 and 1. The region
between gamma_L and the left unit semicircle excludes both poles.
Thus gamma_L can be replaced by that semicircle, oriented from
-i through -1 to i, which is CLOCKWISE. This orientation is essential.

For a outside this left contour define the partial Cauchy transform

    J_n(a)=(1/(2i)) integral_(gamma_L)
                (1+z^2)^n v(z)/[z^(2n+1)(z-a)] dz.           (12)

It is holomorphic in a near 1. Since the nth a derivative of
1/(z-a) is n!/(z-a)^(n+1), (11) is exactly

    Ra(1)/(n!V(1))=J_n^(n)(1)/n!.                          (13)

Equivalently the clockwise unit-semicircle parametrization gives

    J_n(a)=-(1/2) integral_(pi/2)^(3pi/2)
           f(theta)v(z)e^(-z)z^(-n)/(z-a) dtheta,
    z=e^(i theta).                                         (14)

Equations (11)-(14) retain the path, its orientation, the exponential
multiplier removed from the Toeplitz weight, and every factorial.
They describe an incomplete-circle transform, not the full-circle
function C_q from (3)-(4).

## 5. Which Toeplitz data the partial contour still probes

The exact Toeplitz equation determines a finite Laurent block:

    f(z)v(z)=1+sum_(r=1)^n b_r z^(-r)+z^(n+1)G_n(z),        (15)

where G_n is entire. This follows because the Laurent coefficients
at powers 1,...,n vanish, the constant coefficient is one, and
the lowest possible power is -n. Equivalently

    e^z(1+z^2)^n v(z)
      =z^n+sum_(r=1)^n b_r z^(n-r)+z^(2n+1)G_n(z).

Substitution into (14) is an exact separation into a known finite
Laurent contribution and a positive-power tail. In the latter the
factor z^(-n) cancels z^(n+1), leaving

    -(1/2) integral_left G_n(z)e^(-z)z/(z-a) dtheta.          (16)

The previous negative-row predictions control the b_r, not this
partial-contour contribution and its nth derivative at a=1.
Of course G_n is fixed by v; no quantitative signed estimate for
this particular partial-contour functional of G_n has been proved.
The complete exterior Cauchy transform is already determined by
(3), but a complete-circle identity cannot be substituted for a
half-circle integral. Closing the contour on the right would
encounter the evaluation pole at a=1 after differentiation.

The signed theorem in Section 3 controls the negative real values
v(-a^(-1)) and B(-a^(-1)), including v(-1)>0. It does not control
the complex partial-contour scalar in (13). The exact obstruction
is this missing signed connection, not an unproved small absolute
norm of the original factorial polynomial U.

## 6. A single dimensionless connection scalar and the primitive ledger

Define

    a_n=(2n+1)! J_n^(n)(1)/n!
       =(2n+1)! Ra(1)/(n!V(1)).                             (17)

This is real; it is defined by the actual rational Toeplitz solution
and the explicit partial contour in (12). The reviewed exponential
estimate then gives

    Ra(1)/Re(1)=a_n/[exp(1/2)(1+theta_n)],
    theta_n=O(1/n),

    Re(1)+4Ra(1)
      =n!V(1)/(2n+1)!
          [exp(1/2)(1+theta_n)+4a_n].                       (18)

Thus a signed estimate on a_n, or control of its distance from
-exp(1/2)/4 at the needed scale, is a precise remaining analytic
target. Positivity on the negative real interval does not yet imply
a_n>=0. No such implication is asserted.

The actual primitive form is sign(Z)[Re(1)+4Ra(1)]/g, where
g=gcd(|Z|,|Pe(1)+4Pa(1)|). That factor remains even if a_n were
controlled. No new rational approximant is being constructed here.

## 7. Frozen degree-two normalization check

The already saved n=2 data give

    q(s)=1176-972s-118s^2,
    U(s)=1176s^2-972s-118,
    V(1)=925,
    C_q(s)=1850/s^3+204/s^4+1176/s^5,
    B(x)=1+(102/925)x+(588/925)x^2.

These obey (3), with n!V(1)=1850. The full-circle quadratic
quantity in (5) is 1850*1176>0, distinct from the previously
computed negative value mu_2(q^2). The existing whole error is
Ra(1)=4108pi-12852. Its connection scalar is exactly
120(4108pi-12852)/1850 by (17). This is only a normalization
check at the frozen degree, not evidence for an all-index sign of a_n.

The exact checks are recorded in `check_raw_dual_second_kind_existing.py`
and `raw_dual_second_kind_existing_checks.json`. They also verify the
divided-difference orthogonality, reciprocal product identity, and
the minus sign in the inverted contour differential. All assertions
pass after rational simplification; no new degree was constructed.
