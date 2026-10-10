> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual odd interior and exterior saddle multipliers

Date: 2026-09-13. Original bounded analytic continuation by audit_results.
Independent proof review: FULL PASS by audit_sources, saved in
raw_odd_saddle_multipliers_independent_review.md. The interval postprocessor passes
using only the unchanged three independently certified witness vectors.
No new canonical degree, inverse solve, or quadrature is used.

Put n=2m+1, rho=(sqrt(5)-1)/2 and phi=1/rho. For the actual odd family
this note proves


$$
R_{2m+1}(\rho)\longrightarrow B_{\rm o},\qquad
 0.282<B_{\rm o}<0.283,
 \tag{1}
$$




$$
(-1)^m\widetilde R_{2m+1}(-\rho)\longrightarrow A_{\rm o},
 \qquad -1.193<A_{\rm o}<-1.192.                       \tag{2}
$$


Both limiting constants are nonzero. The exterior constant is negative.
The extra z in the odd monic reference is retained throughout and is
essential to that sign. Both phase-adjusted analytic multiplier families
converge locally uniformly on the open unit disk, with every fixed-order
derivative.

This is an amplitude theorem. The actual contour phase, scalar reference
transport, error factorials and signed relative-error assembly remain
separate arguments.

## 1. Actual odd reference and full two-channel space

Use the original matrix and solution


$$
A_{ij}=[z^{n+i-j}]e^z(1+z^2)^n,\qquad
 u(z)=\sum_{j=0}^n(A^{-1})_{j0}z^j,\qquad u_0=u(0).
 \tag{3}
$$


For the positive metric w_+=|1+z²|^(2m+2) on the unit circle, put


$$
c_m=\frac{((2m+1)!)^2}{m!(3m+2)!}.
 \tag{4}
$$


Let Phi_m be the monic scalar orthogonal polynomial for
|1-w|^(2m+2), and define


$$
F_m(z)=\Phi_m^*(-z^2),\qquad
 \Psi_n(z)=z^{2m+1}F_m(1/z)=(-1)^m z\Phi_m(-z^2).
 \tag{5}
$$


Then F_m(0)=1, deg F_m=2m=n-1, and Psi_n is MONIC of degree n.
The reference exponent is a=m+1. Equivalently,
Phi_m^*(w)={}_2F_1(-m,m+1;-2m-1;w).
This exponent and the leading factor z are not the even references.

The exact factors are


$$
R_n(z)=\frac{u(z)}{u_0F_m(z)},\qquad
 \widetilde R_n(w)=\frac{w^nu(1/w)}{u_0F_m(w)}.
 \tag{6}
$$


All coefficients are real. Hence, for real z outside the unit circle,


$$
\widetilde R_n(1/z)=\frac{u(z)}{u_0\Psi_n(z)}.         \tag{7}
$$


Positive scalar orthogonality puts all roots of Phi_m strictly inside
the circle. Thus F_m has no roots in the closed unit disk and the
factors (6) are analytic there.

Write p(z)=p_1(t)+zp_2(t), t=z². Both component degrees are at most m.
Under


$$
t=\frac{1+iy}{1-iy},\qquad P_j(y)=(1-iy)^m p_j(t),
 \tag{8}
$$


the scalar measure is a positive constant times
(1+y²)^(-beta)dy with beta=2m+2. The transformed space is the
FULL two-component degree-m space, with no missing-channel constraint.
The coefficient functionals are exactly


$$
p(0)=2^{-m}P_1(i),\qquad [z^n]p=2^{-m}P_2(-i).
 \tag{9}
$$


Both factors 2^(-m) are positive.

The constant-coefficient unit Riesz polynomial is sqrt(c_m)F_m;
the top-coefficient one is sqrt(c_m)Psi_n. Indeed both reference
norms are 1/c_m, and reversed/monic orthogonality reproduces the
corresponding coefficients. These identities, including the unequal
degrees n-1 and n in (5), are independently derived in
raw_odd_hardy_reference_and_reversal_framework.md.

## 2. The full odd inverse solution and its fixed limit

Use the finite and limiting operators in the independently reviewed
raw_odd_boundary_operator_limit.md:


$$
\widetilde A_m=A_{0,m}E_m+U_mV_m,\quad
 Q_m=(A_{0,m}E_m)^{-1},\quad
 D_{2,m}=I+V_mQ_mU_m.
 \tag{10}
$$


Let v_m^o be the unit Riesz column for +i in component one, with
the original positive-leading scalar polynomial basis, and set
x_m^o=tilde A_m^-1 v_m^o. The exact coordinate identities are


$$
u\longleftrightarrow\sqrt{c_m}\,x_m^o,\qquad
 u_0=c_m g_m,\qquad g_m=(v_m^o)^*x_m^o=1/s_m.
 \tag{11}
$$


The scalar s_m has the independently certified nonzero limit s_infty<0.
In particular u_0 is not presumed positive.

Reverse the scalar basis by r=m-j, and choose
v_m=i^m v_m^o, x_m=i^m x_m^o. The passed boundary limit gives


$$
v_m\to v,\qquad
 v_r=\sqrt{2/3}(i/\sqrt3)^r\binom10.
 \tag{12}
$$


Write J for the bilateral Jacobi operator with off-diagonal sqrt3/2,
P_+ for r>=0, Y=P_+JP_+, and


$$
E=P_+\exp\begin{pmatrix}0&t(J)\\1&0\end{pmatrix}P_+,
 \quad
 A_0=\frac12\begin{pmatrix}0&I+iY\\I-iY&0\end{pmatrix},
 \quad Q=(A_0E)^{-1}.
 \tag{13}
$$


Also U=(sqrt3/4)e_0, V=J_b iota_(-1)^*F(J)P_+,
J_b=[[0,i],[-i,0]], and D_2=I+VQU.
The independent fixed-operator certificate proves det D_2 nonzero.

Woodbury, the strong Q_m convergence, norm convergence of the finite
boundary maps, and D_(2,m)^-1->D_2^-1 therefore prove


$$
x_m\longrightarrow x
 =Qv-QU D_2^{-1}VQv,\qquad
 g_m\longrightarrow g=v^*x=1/s_\infty<0.               \tag{14}
$$


All convergence in (12),(14) is in Hilbert norm. In particular this
uses the full odd correction, not the even constrained compression.
The previously passed odd flatness note proves a uniform bound on
the full finite inverses, including the finite prefix.

## 3. Odd imaginary-node kernel convergence

The scalar positive-leading orthonormal polynomials for beta=2m+2
obey


$$
yq_j=a_{j+1,m}q_{j+1}+a_{j,m}q_{j-1},\qquad
 \alpha_{j,m}=a_{j,m}^2
 =\frac{j(2\beta-j)}{(2\beta-2j)^2-1}.                 \tag{15}
$$


For 1<=j<=m, alpha_j increases with j and lies in (0,3/4).
Every fixed final window converges to 3/4. For fixed d>0 write
the monic evaluations at -id as Q_j(-id)=(-i)^jD_j with D_j>0.
The exact recurrence is


$$
D_0=1,\quad D_1=d,\quad
 D_j=dD_{j-1}+\alpha_{j-1}D_{j-2}.
 \tag{16}
$$


For T_j=D_j/D_(j-1),
d<=T_j<=d+3/(4d). The limiting two-step map for
f(T)=d+3/(4T) has derivative


$$
(f^2)'(T)=\frac{(3/4)^2}{(dT+3/4)^2}
 \le\left(\frac{3/4}{d^2+3/4}\right)^2<1.
$$


Comparison on an arbitrary fixed final window, followed by sending
the window length to infinity, proves


$$
T_{m-r}\longrightarrow\frac{d+\sqrt{d^2+3}}2
 \quad\hbox{for each fixed }r.
 \tag{17}
$$


The contraction is uniform on the stated interval of possible starting
values; it assumes no convergence at the lower end of the window.

Here is the required summable tail, rather than only fixed-coordinate
convergence. The real-variable extension of alpha satisfies


$$
\alpha(j)=\frac{\beta^2-1/4}{4(\beta-j)^2-1}-\frac14,
 \quad
 0<\alpha'(j)<\frac4{m+1}\quad(0\le j\le m).           \tag{18}
$$


Indeed the derivative is
8(beta²-1/4)(beta-j)/[4(beta-j)²-1]², maximized at j=m.
With u=beta-m=m+2 and beta<2u, its value is below
32/(9u)<4/(m+1).

For orthonormal values q_j(-id)=(-i)^jC_j, C_j>0,
the positive recurrence gives, for j>=2,


$$
\frac{C_j}{C_{j-2}}\ge
 \frac{d^2+\alpha_{j-1}}{\sqrt{\alpha_j\alpha_{j-1}}}.
 \tag{19}
$$


Arithmetic-geometric mean and (18) bound the denominator by
alpha_(j-1)+2/(m+1); it is also strictly less than 3/4.
If m+1>=4/d², the numerator minus that denominator is at least d²/2,
so the ratio in (19) is at least 1+2d²/3.
The remaining single backward step is bounded by
C_(m-1)/C_m<=sqrt3/(2d). These give a summable geometric
majorant for every reversed tail, uniformly in sufficiently large m.

Let ell_(m,-)^o(d) and ell_(m,+)^o(d) be the scalar unit Riesz
columns for -id and +id. In reversed coordinates choose the phases


$$
\ell_{m,-}=(-i)^m\ell_{m,-}^o,\qquad
 \ell_{m,+}=i^m\ell_{m,+}^o.
 \tag{20}
$$


The norm convergence following from (17)-(19) is


$$
\ell_{m,\pm}(d)\longrightarrow\ell_{\pm,d},\qquad
 \ell_{\pm,d}(r)=\sqrt{1-q(d)^2}\,(\pm i q(d))^r,
 \quad q(d)=\frac{\sqrt{d^2+3}-d}{\sqrt3}.              \tag{21}
$$


The plus case follows also by complex conjugation, because the
measure and polynomials are real. This proof uses the actual odd
beta=2m+2 throughout; it does not assume a parity carryover.

The endpoint -i unit column in component two, given phase (-i)^m,
converges to


$$
k_r=\sqrt{2/3}(-i/\sqrt3)^r\binom01.
 \tag{22}
$$


This is (21) at d=1 or the exact endpoint ratio already proved in
the odd boundary-limit note.

## 4. Exact finite evaluation and the two different phases

For real 0<z<1 set d=(1-z²)/(1+z²), so the Cayley point is +id.
Evaluation combines P_1+zP_2, and the reference F_m lies in
component one. All common Cayley factors and scalar kernel norms
cancel, yielding exactly


$$
R_n(z)=
 \frac{\ell_{m,+}(d)^*((x_m)_1+z(x_m)_2)}
      {g_m\,\ell_{m,+}(d)^*(v_m)_1}.
 \tag{23}
$$


Both the endpoint solution and the evaluation column were given
phase i^m, so there is no remaining phase in (23).

For real z<-1, put d=(z²-1)/(z²+1), so the point is -id.
The reference Psi_n now lies in component TWO. Its evaluation is
z times the scalar pairing with the -i endpoint column. Thus, with
k_m=(-i)^m k_m^o,


$$
(-1)^m\widetilde R_n(1/z)=
 \frac{\ell_{m,-}(d)^*((x_m)_1+z(x_m)_2)}
      {g_m\,z\,\ell_{m,-}(d)^*(k_m)_2}.
 \tag{24}
$$


To see the exact phase, the original x_m^o=i^(-m)x_m whereas
k_m^o=(-i)^(-m)k_m and ell_(m,-)^o=(-i)^(-m)ell_(m,-).
The numerator has factor (-1)^m and the denominator has factor one.
The factor z in the denominator is separate from this phase; omitting
it would change both the amplitude and its sign.

## 5. Fixed-operator amplitude formulas

Taking the norm limits in (23)-(24), the base scalar pairings are
the same positive geometric sum:


$$
d(d)=\ell_{+,d}^*v_1=\ell_{-,d}^*k_2
 =\frac{\sqrt{1-q(d)^2}\sqrt{2/3}}{1-q(d)/\sqrt3}>0
 \quad(0<d<1).
 \tag{25}
$$


Hence for every fixed real z in (0,1),


$$
R_n(z)\longrightarrow
 \frac{\ell_{+,d}^*(x_1+zx_2)}{g\,d(d)}.
 \tag{26}
$$


For every fixed z<-1, the phase-adjusted exterior limit is


$$
(-1)^m\widetilde R_n(1/z)\longrightarrow
 \frac{\ell_{-,d}^*(x_1+zx_2)}{g\,z\,d(d)}.
 \tag{27}
$$



At the two saddles d=1/sqrt5 and q(d)=sqrt(3/5). Set


$$
\ell_\pm(r)=\sqrt{2/5}(\pm i\sqrt{3/5})^r,\qquad
 d_s=\frac2{\sqrt{15}(1-1/\sqrt5)}.
$$


The actual constants in (1)-(2) are therefore


$$
\boxed{B_{\rm o}=
 \frac{\ell_+^*(x_1+\rho x_2)}{g\,d_s},\qquad
 A_{\rm o}=
 \frac{\ell_-^*(x_1-\phi x_2)}{g\,(-\phi)\,d_s}.}     \tag{28}
$$


They are real as limits of exact real finite ratios.

## 6. Reuse of the three certified solved vectors

Let f_0,f_1,f_2 be the unchanged exact solutions approximated in
raw_odd_limit_certificate_vectors.json:


$$
[f_0\ f_1]=QU,\qquad f_2=Qv.
$$


The independently certified boundary matrix and vector are
D_2=I+V[f_0 f_1] and c=Vf_2. Thus


$$
\eta=D_2^{-1}c,\quad
 x=f_2-\eta_0f_0-\eta_1f_1,\quad
 g=v^*f_2-\eta_0v^*f_0-\eta_1v^*f_1.                 \tag{29}
$$


This is the full odd Woodbury solution. It is not the even projection
formula involving two solved columns.

The old full-space solution errors are bounded by
3.508e-13, 2.827e-12 and 1.682e-11, respectively.
The new postprocessor uses the larger rational bounds
4e-13, 3e-12 and 2e-11. The v test has norm one.
Each saddle test ell^*(f_1+zf_2) has norm sqrt(1+z²)<2 for
z=rho or -phi, so twice the corresponding solution error covers the
entire test error, including every infinite tail.

No new boundary convolution is performed. The already certified D_2
and c entries in raw_odd_limit_interval_certificate.json are enclosed
in explicitly given rational boxes. The postprocessor verifies that
these boxes contain the saved 100-digit intervals with a generous
10^(-90) serialization allowance. Their imaginary radii are 10^(-10).
The determinant is checked to have real part greater than 0.62 before
using the two-by-two inverse formula. All further arithmetic uses
100-decimal outward intervals.

Run:

    /opt/homebrew/bin/python3.12 check_raw_odd_saddle_multipliers.py

The output raw_odd_saddle_multiplier_certificate.json is PASS and gives


$$
-2.170279018834<g<-2.170279018372,
$$




$$
0.282159231929<B_{\rm o}<0.282159232248,
$$




$$
-1.192623911385<A_{\rm o}<-1.192623910411.             \tag{30}
$$


The broader rational bounds asserted in (1)-(2) are checked directly.
Small imaginary interval widths are error enclosures; reality follows
from the exact finite ratios, not from rounding them away.

## 7. Local uniformity and derivatives

The independently derived odd reference framework proves


$$
\sup_m\{\|R_{2m+1}\|_{H^2},
          \|\widetilde R_{2m+1}\|_{H^2}\}<\infty.
 \tag{31}
$$


Its precise sufficient bound is K_A sup_m|s_m|, using the full odd
inverse norm and the exact Bernstein--Szego moment identity for
w_+ and the references (5). No positive-sector assertion for the
odd signed matrix is used.

Equation (31) makes both analytic families locally bounded on the
open disk. Equations (26)-(27) give pointwise limits on the real
intervals (0,1) and (-1,0), respectively, with accumulation points
inside the disk. Any two analytic subsequential limits must therefore
agree by the identity theorem. Hence the whole families
R_(2m+1) and (-1)^m Rtilde_(2m+1) converge locally uniformly.
Cauchy's formula gives convergence of every fixed-order derivative.

The strict nonzero bounds (1)-(2) then supply neighborhoods of rho
and -rho on which the corresponding analytic limiting functions are
nonzero; the actual finite multipliers are bounded away from zero
there for all sufficiently large m. No effective first index or
convergence rate is claimed.

## 8. Scope

This supplies actual odd saddle amplitudes with their phases, the
negative exterior sign, and enough local uniformity for contour
analysis. The odd scalar reference transport and signed contour
orientation remain in computations' separate assembly. The reference
degree is n-1 in the denominator F and n in the monic Psi; these
must remain distinct when translating to the original errors.

No even-parity phase, positivity of u_0, or disappearance of the
second channel is assumed. No arithmetic conclusion is inferred
solely from these multiplier limits.
