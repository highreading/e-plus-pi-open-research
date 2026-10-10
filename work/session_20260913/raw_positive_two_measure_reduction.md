> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An exact finite polynomial reduction to two positive spectral measures

Date: 2026-09-13. Root continuation of the reviewed boundary-free
operator. The reduction below is unconditional. It does not prove a
cofactor estimate, positivity of mixed minors, or irrationality.

Use T, its simple eigenvalues xi_l and real orthonormal eigenfunctions
psi_l from raw_boundary_free_moment_intertwiner.md. Put

    v_0=1,                 v_1=sqrt3(x−1/2).

The seed norms are ||v_0||²=1, ||v_1||²=1/4. The operator T commutes
with reflection x->1−x. Define g_l=<v_(l mod2),psi_l>; these are exactly
the nonzero amplitudes in that note, including its odd normalization.

Convention: the actual polynomial in the plus moment equations below
is U_n(x)=sum B_(n,j)(1-x)^(n-j)/(n-j)!, as in the original raw
moment construction. The generic symbol P in(1)-(5) denotes any
polynomial. If it denotes the reflected endpoint polynomial
P_n(t)=U_n(1-t), its odd branch changes sign in the high equations.
See raw_reflection_convention_bridge.md for the exact unitary map;
all spectral projection norms and measure norms are unchanged.

## 1. Exact finite degree constraints

For any nonzero polynomial f of degree d, Tf has degree exactly d+2
and the same leading coefficient: the derivative part preserves its
degree, while the leading x² in the potential adds two degrees.
Consequently the following vectors have distinct leading degrees
0,1,...,n:

    T^j v_0,  0<=j<=floor(n/2),
    T^j v_1,  0<=j<=floor((n−1)/2).

They form a basis of the polynomials of degree at most n. Every such
P therefore has a unique representation

    P=f_0(T)v_0+f_1(T)v_1,
    deg f_0<=floor(n/2), deg f_1<=floor((n−1)/2).       (1)

The seed factors make f_1's coefficients potentially contain1/sqrt3
when P has rational coefficients; this is a harmless fixed algebraic
factor, not an unproved rationality assertion.

For every j, T^j v_sigma is a polynomial, so each seed lies in the
domain of all powers of T. The spectral theorem hence gives the exact
coefficient formula, with no truncation,

    <P,psi_l>=g_l f_(l mod2)(xi_l).                    (2)

## 2. Two positive measures with explicit polynomial moments

Define discrete positive measures on the real line by

    mu_sigma=sum_(l= sigma mod2) g_l² delta_(xi_l).
                                                               (3)

Their masses are respectively1 and1/4 by Parseval. Every atom has
positive weight, and their supports lie in the disjoint, interlacing
intervals [l(l+1)+3/4,l(l+1)+1]. Each measure has infinite support.
All polynomial moments exist, because the seeds lie in every power
domain, and

    integral xi^j dmu_sigma=<v_sigma,T^j v_sigma>.     (4)

These moments are rational. The operator has rational polynomial
coefficients; for sigma0 this is direct polynomial integration, and
for sigma1 the two factors sqrt3 multiply to3.

Equations(1)-(3) give the exact isometry

    ||P||²=integral |f_0|² dmu_0
                          +integral |f_1|² dmu_1.     (5)

This positive two-measure representation is a finite-dimensional
polynomial parametrization. It is different from dropping spectral
indices l>n, which would be incorrect.

## 3. The actual high rows in this representation

Let E_k be the scaled actual Borel-Legendre polynomials. Their exact
spectral recurrence already defines real polynomial branches
p_k^(0),p_k^(1), with initial values

    (p_0^(0),p_1^(0))=(1,sqrt3/2),
    (p_0^(1),p_1^(1))=(0,1).

Since E_0=v_0 and E_1=(sqrt3/2)v_0+v_1, the finite polynomial identity
behind that recurrence is

    E_k=p_k^(0)(T)v_0+p_k^(1)(T)v_1.                  (6)

It also follows from uniqueness in(1) and the nonzero infinitely many
spectral amplitudes in(2). Its degree caps are

    deg p_k^(0)<=floor(k/2),
    deg p_k^(1)<=floor((k−1)/2),

with degree−infinity for the zero polynomial. The leading parity
component has its full indicated degree, because E_k has degree k.

Therefore the actual high orthogonalities are exactly the finite
polynomial constraints

    integral f_0 p_k^(0) dmu_0
       +integral f_1 p_k^(1) dmu_1=0,
                       n+1<=k<=2n−1.                (7)

All integrals in(7) are finite combinations of the rational moments(4).
The symmetric row normalization carries the explicit factor

    s_k=2^(-k) binom(2k,k) sqrt(2k+1), E_k=s_k F_k.

Consequently p_k also carries a varying row radical, not only the
fixed seed factor sqrt3. Dividing the kth equation by s_k gives the
branches of the rational polynomial F_k: their even coefficients are
rational and their odd coefficients are rational multiples of1/sqrt3.
For a rational P these pair with its corresponding rational and
rational/sqrt3 coefficients, so the divided constraints are rational.
The common nonzero row factor does not affect the kernel. Both
branches remain present. Discarding one branch or treating the high
p_k as consecutive scalar orthogonal polynomials has no justification.

## 4. The scalar orthogonal polynomials of the two measures

Write

    d_l=l(l+1)+3/4+t_(l−1)²+t_l²,
    b_l=t_l t_(l+1)>0,
    t_l=(l+1)/(2sqrt((2l+1)(2l+3))), t_(-1)=0.

For sigma in{0,1}, let pi_0^sigma=1 and pi_1^sigma(xi)=xi−d_sigma.
The monic orthogonal polynomials of mu_sigma satisfy exactly

    pi_(j+1)^sigma(xi)
      =(xi−d_(sigma+2j))pi_j^sigma(xi)
         −b_(sigma+2j−2)² pi_(j−1)^sigma(xi), j>=1.   (8)

To prove this without invoking a formal moment problem, put h_0=1,
h_1=1/2, so v_sigma=h_sigma phi_sigma. Induction in the actual
Legendre tridiagonal parity block gives

    pi_j^sigma(T)v_sigma
       =h_sigma product_(r=0)^(j−1)b_(sigma+2r)
                          phi_(sigma+2j).             (9)

The spectral isometry proves orthogonality and the exact squared norm

    integral (pi_j^sigma)² dmu_sigma
       =h_sigma² product_(r=0)^(j−1)b_(sigma+2r)².     (10)

Thus no uniqueness assumption for an abstract moment problem is
needed. Equations(8)-(10) are exact explicit scalar recurrences for
the two positive measures. In particular, their positivity does not
make the different mixed branch sequence p_k orthogonal.

## 5. What has changed and what remains

The actual unknown P now has the exact finite pair(f_0,f_1), its norm
is a positive two-measure norm, and its high equations use known
polynomial branches with a fixed recurrence. The scalar measures have
explicit Jacobi coefficients and prolate spectral weights. This is a
concrete route for structured interpolation and cofactor estimates.

The original difficulty remains visible in(7): the high-row branches
mix two interlacing spectral supports, and their constraints are not
the low-degree orthogonality defining the pi_j. Known positivity for
mu_sigma or their Hankel determinants does not imply positivity or
conditioning of this mixed matrix. No Nikishin, Angelesco, or scalar
Favard hypothesis for p_k is asserted. The endpoints B(1)=1 and C(1)=4
still select the actual member of the two-dimensional high kernel;
(7) alone does not replace those normalization equations.
