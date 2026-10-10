> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The actual even exterior saddle multiplier: limit, phase and certificate

Date: 2026-09-13. Original bounded continuation by audit_results.
Independent review: PASS by audit_sources after an identical interval postprocessing rerun; see raw_even_saddle_multiplier_independent_review.md. The fixed-operator interval postprocessor is PASS;
the coordinate interface and its phase are explicitly retained below.

Let phi=(1+sqrt(5))/2. For the actual even family n=2m, this proves

    (-1)^m Rtilde_(2m)(-1/phi) -> A_s,
    0.049 < A_s < 0.050.                                  (1)

The same phase-adjusted analytic multipliers converge locally uniformly on
the open unit disk. In particular, their fixed-order derivatives converge
near -1/phi, and the limiting multiplier is nonzero there.

The proof uses the already established even compression limit and the
unchanged two solved vectors from the independently certified odd limiting
operator. No new inverse solve, quadrature, or canonical degree is used.
It does not itself estimate the whole signed arctangent contour.

## 1. The original polynomial and the monic comparison

Use the actual even Toeplitz matrix and its endpoint solution

    A_ij=[z^(2m+i-j)] exp(z)(1+z^2)^(2m),   0<=i,j<=2m,
    u(z)=sum_(j=0)^(2m)(A^(-1))_(j0) z^j,
    u_0=u(0)>0,
    c_m=((2m)!)^2/[m!(3m)!].

The positive base circle weight is |1+z^2|^(2m). Retain the exact
comparison polynomial from raw_actual_dual_hardy_factor_allocation.md:

    F_m(z)=Phi_m^*(-z^2),
    Psi_(2m)(z)=z^(2m) F_m(1/z)=(-1)^m Phi_m(-z^2).        (2)

Psi is MONIC of degree 2m, and its squared base norm is 1/c_m.
It has every root strictly inside the unit disk. The actual reversal is

    Rtilde_(2m)(w)=u^*(w)/(u_0 F_m(w)).

All coefficients are real, so the exact exterior identity is

    Rtilde_(2m)(1/z)=u(z)/(u_0 Psi_(2m)(z)),  |z|>1.        (3)

Replacing Psi in (3) by F_m(z), or suppressing the sign in (2),
would change the normalization.

## 2. The exact finite Cayley ratio

Write

    u(z)=u_1(t)+z u_2(t),   t=z^2,
    deg u_1<=m,   deg u_2<=m-1.

Use t=(1+iy)/(1-iy), and multiply BOTH components by (1-iy)^m.
The common positive scalar measure is a constant times
(1+y^2)^(-2m-1)dy. The transformed actual space is the full
two-component degree-m space with the constraint

    P_2(-i)=0.                                           (4)

Let v_m^o be the unit Riesz vector for evaluation at +i in component 1;
let w_m^o be the one for evaluation at -i in component 2.
The superscript o denotes the original phases before the reversal
phases introduced below. Put Pi_m=I-w_m^o(w_m^o)* and

    B_m=Pi_m E_m Pi_m+w_m^o(w_m^o)*,
    x_m^o=B_m^(-1)v_m^o,
    g_m=(v_m^o)*x_m^o=(A^(-1))_00/c_m.                    (5)

Here E_m is the common-space compression of

    F(t)=exp[0 t;1 0].

The exact coordinate identities are

    u <-> sqrt(c_m) x_m^o,
    sqrt(c_m) Psi_(2m) <-> k_m^o,                         (6)

where k_m^o is the unit Riesz vector for evaluation at -i in
component 1. To see the normalization, the original constant coefficient
is P_1(i)/2^m and its functional norm is sqrt(c_m). The original top
coefficient is P_1(-i)/2^m; its unit Riesz polynomial is
sqrt(c_m) Psi_(2m), since Psi is monic with norm squared 1/c_m.
Both Cayley coefficient factors 2^(-m) are POSITIVE.

For real z<-1, set

    d=(z^2-1)/(z^2+1),  0<d<1,   y=-id.

Let ell_m^o(d) be the scalar unit Riesz vector for evaluation at -id.
The original evaluation combines components as P_1(y)+z P_2(y).
The positive evaluation-kernel magnitude, common Cayley denominator,
and the factors in (6) all cancel in the ratio (3). Therefore

    Rtilde_(2m)(1/z)
      =(ell_m^o)*[(x_m^o)_1+z(x_m^o)_2]
        /[g_m (ell_m^o)*(k_m^o)_1].                      (7)

Equation (7) retains both the missing second-channel constraint and
the actual component coefficient z.

## 3. The three phases and the fixed operator

Reverse the common scalar orthonormal basis, whose polynomial q_j
has positive leading coefficient, by writing r=m-j. Use the phases

    v_m=i^m v_m^o,          x_m=i^m x_m^o,
    w_m=(-i)^m w_m^o,       k_m=(-i)^m k_m^o,
    ell_m(d)=(-i)^m ell_m^o(d).

Multiplication of w_m by a phase does not change its projection.
The already proved even inverse-corner theorem gives norm limits

    v_r=sqrt(2/3)(i/sqrt(3))^r [1;0],
    w_r=sqrt(2/3)(-i/sqrt(3))^r [0;1],
    k_r=sqrt(2/3)(-i/sqrt(3))^r [1;0],                   (8)

and

    x_m -> x=B_+^(-1)v,       g_m->g_+=v*x>0,
    B_+=Pi E_+ Pi+ww*,        Pi=I-ww*,
    E_+=P_+ F(J) P_+.                                    (9)

Here J is the bilateral zero-diagonal Jacobi operator with constant
off-diagonal sqrt(3)/2. All strong/inverse convergence and coercivity
in (9) were proved in raw_even_endpoint_inverse_corner_limit.md.
In particular x belongs to w-perpendicular.

In (7), the numerator contains the relative phase between x_m^o
and ell_m^o, whereas the denominator pairs two -i phase vectors.
Substituting the displayed phases gives the exact finite formula

    (-1)^m Rtilde_(2m)(1/z)
       =ell_m(d)*[(x_m)_1+z(x_m)_2]
           /[g_m ell_m(d)*(k_m)_1].                      (10)

For example, x_m^o=i^(-m)x_m and
k_m^o=(-i)^(-m)k_m, whose relative scalar is (-1)^m.
Thus the phase in (1) is intrinsic to the actual monic normalization.

## 4. Imaginary-node kernels, including a fixed real interval

The specific saddle kernel has a separate independently checked proof
in raw_even_imaginary_saddle_kernel_tail.md. It establishes the full
norm convergence, with a summable bound on every reversed coefficient,

    ell_m(1/sqrt(5)) -> ell_s,
    (ell_s)_r=sqrt(2/5)(-i sqrt(3/5))^r.                  (11)

The Riesz COLUMN has the -i phase in (11); the evaluation ROW has
the conjugate +i phase.

For the local-uniform analytic conclusion below, we also give the
fixed-d version, not only the one saddle value. The exact recurrence is

    a_(j,m)^2=alpha_(j,m)
       =j(2beta-j)/[(2beta-2j)^2-1],    beta=2m+1.

For 1<=j<=m, 0<alpha_j<3/4 and alpha_j increases with j.
For the monic polynomials, put Q_j(-id)=(-i)^j D_j. Then

    D_0=1, D_1=d, D_j=d D_(j-1)+alpha_(j-1) D_(j-2),
    T_j=D_j/D_(j-1)=d+alpha_(j-1)/T_(j-1).

Thus d<=T_j<=d+3/(4d). Every fixed final window of alpha_j
converges to 3/4. The limiting two-step map, for f(T)=d+3/(4T),
satisfies

    (f^2)'(T)=(3/4)^2/[dT+3/4]^2
        <=[(3/4)/(d^2+3/4)]^2<1.

Comparison of a fixed number of final maps, followed by taking that
number to infinity, proves

    T_(m-r)->T_*=(d+sqrt(d^2+3))/2

for every fixed r. This argument is uniform over the compact interval
of allowed starting T values, so it does not assume a convergent
state at the lower end of the window.

Here is the full tail control needed in addition to those fixed ratios.
Extending alpha to a real variable j gives

    alpha(j)=(beta^2-1/4)/[4(beta-j)^2-1]-1/4,
    0<alpha'(j)<4/(m+1),       0<=j<=m.

Indeed its derivative is
8(beta^2-1/4)(beta-j)/[4(beta-j)^2-1]^2, maximized at j=m;
with u=m+1, beta<2u and 4u^2-1>=3u^2 bound it by
32/(9u)<4/u.

Write the orthonormal evaluations as q_j(-id)=(-i)^j C_j, C_j>0.
Their positive recurrence implies, for j>=2,

    C_j/C_(j-2)
       >=[d^2+alpha_(j-1)]/sqrt(alpha_j alpha_(j-1)).

Arithmetic-geometric mean and the derivative bound give
sqrt(alpha_j alpha_(j-1))<=alpha_(j-1)+2/(m+1).
For m+1>=4/d^2, it follows that

    C_j/C_(j-2)>=1+2d^2/3.

A remaining single backward step is bounded by
C_(m-1)/C_m<=sqrt(3)/(2d). Thus, for each fixed d>0, all
reversed ratios have a summable geometric majorant independent of
sufficiently large m. Dominated normalization proves the norm limit

    ell_m(d)->ell_d,
    (ell_d)_r=sqrt(1-rho(d)^2)(-i rho(d))^r,
    rho(d)=(sqrt(d^2+3)-d)/sqrt(3).                       (12)

For 0<d<1, 1/sqrt(3)<rho(d)<1. No estimate uniform as d
approaches zero is claimed.

## 5. The exact limiting exterior amplitude

Combining (8)-(12), for every fixed real z<-1,

    (-1)^m Rtilde_(2m)(1/z)->A(z),
    A(z)=ell_d*(x_1+z x_2)/(g_+ ell_d*k_1),
    d=(z^2-1)/(z^2+1).                                  (13)

The base denominator is explicitly positive:

    ell_d*k_1
       =sqrt(1-rho(d)^2)sqrt(2/3)/(1-rho(d)/sqrt(3))>0.   (14)

The finite ratios in (10) are defined: Psi has no exterior roots.
At z=-phi, d=1/sqrt(5), rho=sqrt(3/5), so

    d_s=ell_s*k_1=2/[sqrt(15)(1-1/sqrt(5))],
    A_s=ell_s*(x_1-phi x_2)/(g_+ d_s).                   (15)

This is a fixed-operator expression for the ACTUAL amplitude.

## 6. Certification using the unchanged solved columns

Let f_0,f_1 be the first two exact solutions already certified in
raw_odd_limiting_determinant_interval_certificate.md. The even
inverse-corner proof establishes exactly

    f_0=E_+^(-1)w/sqrt(2),   f_1=E_+^(-1)v/sqrt(2).

Consequently

    alpha=(w*f_1)/(w*f_0),
    x=sqrt(2)(f_1-alpha f_0),
    g_+=sqrt(2)[v*f_1-alpha v*f_0].                       (16)

The denominator in alpha has positive real part, since
sqrt(2) w*f_0=w*E_+^(-1)w.

The unchanged exact rational approximate vectors in
raw_odd_limit_certificate_vectors.json have full Hilbert-space errors
below 3.508e-13 and 2.827e-12. The present outward-interval checker

    check_raw_even_saddle_multiplier.py

uses the larger rational bounds 4e-13 and 3e-12. The v,w tests are
unit norm. The saddle test f->ell_s*(f_1-phi f_2) has norm
sqrt(1+phi^2)<2, so its complete pairing error is at most twice
the corresponding solved-vector bound. The exact approximants have
finite support; the stated full-space error already contains their
entire infinite tails.

The checker performs just those finite geometric pairings and interval
arithmetic in (15)-(16). Its output

    raw_even_saddle_multiplier_certificate.json

is PASS and encloses the real amplitude in

    0.0493603201444840 < A_s < 0.0493603201863010.

The asserted rational bounds are (1). The amplitude is real because
it is the limit of real finite ratios (10); its positivity is certified,
not inferred from entrywise positivity of an operator.

For reproducibility, a suitable explicit invocation is

    /opt/homebrew/bin/python3.12 check_raw_even_saddle_multiplier.py

from this directory. The checker inserts the local math_packages path
and uses outward interval arithmetic at 100 decimal digits. It does not
solve a new linear system or recompute a canonical degree.

## 7. Local uniform convergence and derivative control

The independently proved exact positive-measure identity gives

    ||Rtilde_(2m)||_(H^2)<=e sec(1),

uniformly in m. Therefore (-1)^m Rtilde_(2m) is a locally bounded
analytic family on |w|<1. Every subsequence has a further subsequence
converging uniformly on compact subsets to an analytic function.

Equation (13) gives the same pointwise limit at EVERY w=1/z
in the interval (-1,0). The identity theorem forces any two such
analytic subsequential limits to agree. Hence the entire sequence
converges locally uniformly:

    (-1)^m Rtilde_(2m)(w)->mathcal A(w),   |w|<1,          (17)
    mathcal A(1/z)=A(z) for real z<-1.

The standard compact-disk Cauchy formula also proves convergence of
every fixed-order derivative locally uniformly. By (1),

    mathcal A(-1/phi)=A_s>0.

An explicit fixed neighborhood is also available from the same Hardy
bound. On |w|<=4/5 the limiting function has modulus less than 9:
use e<11/4 and cos(1)>27/50 in the Hardy evaluation bound.
Since |1/phi|<5/8, the disk centered at -1/phi of radius 1/6
lies inside |w|<4/5. Its Cauchy coefficient bound gives, for
|w+1/phi|<=1/10000,

    |mathcal A(w)-A_s|
       <=9(1/10000)/(1/6-1/10000)=54/9994<0.006.

Thus Re mathcal A(w)>0.043 on this disk. Local uniform convergence
then makes the actual phase-adjusted multipliers have real part
greater than 0.04 there for every sufficiently large m. There is
no claimed convergence rate or effective first index.

## 8. Scope

This supplies the nonzero actual even multiplier and its sign at the
exterior arctangent saddle, with a rigorous interval and local derivative
convergence. The alternating factor (-1)^m must be retained when it is
combined with other phase factors in the contour representation.

The theorem does not by itself construct a steepest-descent contour,
bound the remaining contour portions or endpoints, or estimate the
primitive endpoint gcd. Those are separate requirements for any full
arctangent-error or irrationality conclusion.
