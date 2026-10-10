> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The actual even interior multiplier at the endpoint-residue saddle

Date: 2026-09-13. Original bounded continuation by audit_results.
Independent review: PASS by audit_sources after an identical interval postprocessing rerun; see raw_even_interior_multiplier_independent_review.md. The interval postprocessor is PASS.
No new canonical degree, quadrature or inverse solve is used.

Put rho=(sqrt(5)-1)/2. For the ACTUAL even family n=2m this proves

    R_(2m)(rho) -> B_s,
    0.604 < B_s < 0.605,                                 (1)

with NO alternating phase. In fact R_(2m) converges locally uniformly
on the open unit disk to an analytic function mathcal B with
mathcal B(0)=1, together with every fixed-order derivative.

This is the amplitude input for the endpoint-residue saddle. It does
not itself evaluate that contour, its factorial normalization, or
the primitive endpoint gcd.

## 1. Exact original polynomial and positive base reference

Retain the actual matrix, polynomial, and positive normalization

    A_ij=[z^(2m+i-j)] exp(z)(1+z^2)^(2m),
    u(z)=sum_(j=0)^(2m)(A^(-1))_(j0)z^j,
    u_0=u(0)>0,
    c_m=((2m)!)^2/[m!(3m)!],
    F_m(z)=Phi_m^*(-z^2),
    R_(2m)(z)=u(z)/(u_0 F_m(z)).                         (2)

The positive base circle weight is |1+z^2|^(2m). The reversed
orthogonal polynomial F_m has constant coefficient one and norm
squared 1/c_m. Its constant-coefficient Riesz polynomial is exactly

    c_m F_m,

so the unit endpoint Riesz polynomial is sqrt(c_m)F_m.

For an explicit check, reversal of the monic orthogonality says
F_m is orthogonal to z,z^2,...,z^(2m). Expanding F_m, whose constant
coefficient is one, gives <F_m,1>=||F_m||^2=1/c_m.
Thus multiplication by c_m reproduces the constant coefficient
on the entire degree-at-most-2m polynomial space.

This is the reference needed in (2). The exterior theorem instead
uses the monic Psi_(2m)=z^(2m)F_m(1/z); its different phase must
not be imported into the present interior normalization.

## 2. Exact finite two-channel evaluation

Write a polynomial as p(z)=p_1(t)+z p_2(t), with t=z^2 and
degrees at most m and m-1. Use the common Cayley transform

    t=(1+iy)/(1-iy),
    P_j(y)=(1-iy)^m p_j(t).

The common scalar measure is a positive constant times
(1+y^2)^(-2m-1)dy. The actual space is the full two-component
degree-m space with the exact condition P_2(-i)=0.

As in the independently passed even inverse-corner theorem, let
v_m^o be the unit Riesz vector for +i in component 1, w_m^o
the one for -i in component 2, and

    Pi_m=I-w_m^o(w_m^o)*,
    B_m=Pi_m E_m Pi_m+w_m^o(w_m^o)*,
    x_m^o=B_m^(-1)v_m^o,
    g_m=(v_m^o)*x_m^o=(A^(-1))_00/c_m.

The common compression E_m has symbol exp[0 t;1 0].
The original constant coefficient equals P_1(i)/2^m, with a
positive factor. The exact unitary coordinate identities are

    u <-> sqrt(c_m)x_m^o,
    sqrt(c_m)F_m <-> v_m^o,
    u_0=c_m g_m.                                         (3)

For a fixed real z in (0,1), put

    d=(1-z^2)/(1+z^2),   0<d<1,   y=+id.

Let ell_(m,+)^o(d) be the scalar unit Riesz vector for evaluation
at +id. Evaluation of the original polynomial combines the
transformed components as P_1(y)+zP_2(y). All common Cayley and
scalar-kernel factors cancel between the two polynomials in (2).
Equations (2)-(3) therefore give exactly

    R_(2m)(z)
       =ell_(m,+)^o(d)*[(x_m^o)_1+z(x_m^o)_2]
          /[g_m ell_(m,+)^o(d)*(v_m^o)_1].               (4)

In particular the second component is multiplied by +rho at
the desired saddle; it is not removed by the -i constraint.

## 3. Phase and norm limits

Reverse the positive-leading scalar orthonormal basis by r=m-j.
The endpoint solution is given the phase i^m:

    v_m=i^m v_m^o,   x_m=i^m x_m^o.

At +id, the scalar orthonormal evaluations have the form
q_j(+id)=i^j C_j, with C_j>0. Their Riesz coefficients are the
conjugates (-i)^j C_j. Consequently use the SAME phase

    ell_(m,+)(d)=i^m ell_(m,+)^o(d).

Its reversed coefficients are proportional to i^r C_(m-r).
In (4), the scalar from the conjugated evaluation vector cancels
the scalar of the solution in the numerator, and the identical
cancellation holds for the reference vector in the denominator.
Thus the exact finite formula is

    R_(2m)(z)
       =ell_(m,+)(d)*[(x_m)_1+z(x_m)_2]
          /[g_m ell_(m,+)(d)*(v_m)_1],                  (5)

without a factor (-1)^m.

All full-space limits of x_m,v_m and g_m are proved in
raw_even_endpoint_inverse_corner_limit.md:

    v_r=sqrt(2/3)(i/sqrt(3))^r [1;0],
    w_r=sqrt(2/3)(-i/sqrt(3))^r [0;1],
    x_m->x=B_+^(-1)v,   g_m->g_+=v*x>0,
    B_+=Pi E_+ Pi+ww*,   Pi=I-ww*,
    E_+=P_+exp[0 t(J);1 0]P_+,
    t(y)=(1+iy)/(1-iy).

Here J is the bilateral Jacobi operator with zero diagonal and
constant off-diagonal sqrt(3)/2. The constraint remains w*x=0.

The independently passed fixed-d kernel proof in
raw_even_saddle_multiplier_limit.md §4 applies at +id simply by
complex conjugation: the scalar measure and its orthonormal
polynomials are real. It includes a uniform summable reversed
tail for every fixed d>0, not just coefficientwise convergence.
Its full norm limit is

    ell_(m,+)(d)->ell_(+,d),
    ell_(+,d)(r)=sqrt(1-q(d)^2)(i q(d))^r,
    q(d)=(sqrt(d^2+3)-d)/sqrt(3).                         (6)

For 0<d<1 the number q(d) lies between 1/sqrt(3) and 1.

## 4. The fixed-operator interior amplitude

By (5)-(6), at every fixed real z in (0,1),

    R_(2m)(z)->B(z)
       =ell_(+,d)*(x_1+z x_2)/(g_+ ell_(+,d)*v_1),       (7)
    d=(1-z^2)/(1+z^2).

The limiting base denominator is a positive geometric sum:

    ell_(+,d)*v_1
       =sqrt(1-q(d)^2)sqrt(2/3)/(1-q(d)/sqrt(3))>0.       (8)

The finite ratios are defined because F_m is zero-free on the
closed unit disk.

At z=rho, one has t=rho^2 and d=1/sqrt(5). Therefore

    ell_+(r)=sqrt(2/5)(i sqrt(3/5))^r,
    d_s=ell_+*v_1=2/[sqrt(15)(1-1/sqrt(5))],
    B_s=ell_+*(x_1+rho x_2)/(g_+ d_s).                   (9)

This has the same positive base denominator as the exterior
saddle, but both the kernel phase and the component combination
have changed.

## 5. Exact interval reuse and positive certificate

Use the unchanged two exact solutions from the independently
certified odd limiting-operator computation:

    f_0=E_+^(-1)w/sqrt(2),   f_1=E_+^(-1)v/sqrt(2),
    alpha=(w*f_1)/(w*f_0),
    x=sqrt(2)(f_1-alpha f_0),
    g_+=sqrt(2)[v*f_1-alpha v*f_0].                       (10)

The denominator w*f_0 has positive real part. The exact rational
approximants in raw_odd_limit_certificate_vectors.json have
certified full-space errors smaller than 3.508e-13 and 2.827e-12.
The new postprocessor

    check_raw_even_interior_multiplier.py

uses the larger rational bounds 4e-13 and 3e-12. Pairing with
v,w costs their unit norm; the interior test
f->ell_+*(f_1+rho f_2) has norm sqrt(1+rho^2)<2.
The full error is therefore bounded by twice the appropriate
solved-vector error. This includes every infinite tail, since
the error estimates compare the finite approximants to the
whole exact solutions.

Outward interval arithmetic in (9)-(10), using the same finite
vectors without any new solve, gives PASS:

    0.6040688968602422 < B_s < 0.6040688969081851.           (11)

The asserted rational interval is (1). The output is saved in

    raw_even_interior_multiplier_certificate.json.

The amplitude is real by the exact real finite ratios (5).
Its positive sign follows from the certified interval, not from
a pointwise positive-matrix inference.

The explicit reproducible invocation is

    /opt/homebrew/bin/python3.12 check_raw_even_interior_multiplier.py

from this directory. The checker inserts math_packages and
uses 100-decimal outward interval arithmetic.

## 6. Locally uniform convergence and a nonzero neighborhood

The previously proved Hardy bound is

    ||R_(2m)||_(H^2)<=e sec(1).

Hence this analytic family is locally bounded on |z|<1. Its
pointwise limits at every real point of (0,1), proved in (7),
force any two analytic subsequential limits to coincide by
the identity theorem. It follows that the entire sequence
converges locally uniformly:

    R_(2m)(z)->mathcal B(z),   |z|<1,
    mathcal B(0)=1,
    mathcal B(z)=B(z) for real 0<z<1.                    (12)

Cauchy's formula gives local uniform convergence of all
fixed-order derivatives.

For a fixed quantitative neighborhood, the Hardy evaluation
bound gives |mathcal B(z)|<9 on |z|<=4/5. Since rho<5/8,
the radius-1/6 disk centered at rho lies inside this disk.
Cauchy's coefficient bound then gives, for |z-rho|<=1/10000,

    |mathcal B(z)-B_s|
       <=9(1/10000)/(1/6-1/10000)=54/9994<0.006.

Thus Re mathcal B(z)>0.598 on that disk, and local uniform
convergence implies Re R_(2m)(z)>0.59 there for all sufficiently
large m. No convergence rate or effective first index is claimed.

## 7. Scope and exact phase distinction

This proves the nonzero actual interior factor for the endpoint
residue saddle, including the base polynomial normalization and
both channels. The two separate proved saddle amplitudes are

    R_(2m)(rho)->B_s>0,
    (-1)^m Rtilde_(2m)(-rho)->A_s>0.

The absence of an alternating factor in the first line is an
exact consequence of the common +i endpoint/reference phases.
It does not follow by taking an absolute value of the exterior
theorem.

The endpoint residue representation, contour dominance, final
factorials, integer normalization and endpoint gcd remain in
their own arguments. No arithmetical inference is made solely
from this fixed-operator amplitude.

