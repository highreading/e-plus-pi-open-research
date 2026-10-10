> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Odd reference polynomials and the two actual endpoint contours

Date: 2026-09-13. Original bounded continuation by audit_computations.
Independent review: FULL PASS in
`raw_odd_reference_contour_independent_review.md`. The nonzero actual
multiplier inputs have also passed their separate full review in
`raw_odd_saddle_multipliers_independent_review.md`. Thus the signed odd
relative-error formula (24)-(25) is unconditional for the actual family.

Let n=2m+1. The actual odd Toeplitz geometry uses the positive comparison
weight $|1+z^2|^{2m+2}$, not the literal absolute value
$|1+z^2|^{2m+1}$ of its signed symbol. The distinction changes a finite
transport factor. Both weights have the same exponential phase. This
note derives the fixed-offset reference formula covering both, and then
uses the first weight for the actual operator and contour normalization.

Write


$$
\rho=(\sqrt5-1)/2,\quad\phi=1/\rho,\quad
 \tau=\sqrt{27\rho^5/4},\quad\xi=\sqrt{27/(4\rho^5)},
$$




$$
h_o=(25-11\sqrt5)/4,\qquad\kappa=5/2+\sqrt5.
$$


The phases, their strict contour maxima, and these curvatures have already
been independently proved in the even-family work. No phase certificate
or numerical degree scan is repeated here.

## 1. Exact circular-binomial reference, including the odd degree

For fixed lambda>=0 put a=m+lambda, with m>=1, and consider the positive
circular weight $|1-w|^{2a}$. Its monic degree-m orthogonal polynomial
and its reversal are


$$
\Phi_m^{[a]}(w)=\sum_{j=0}^m\binom mj
       \frac{(a)_{m-j}}{(a+j+1)_{m-j}}w^j,
$$




$$
f_m^{(\lambda)}(w)=\Phi_m^{[a]*}(w)
   =\sum_{j=0}^m\frac{(-m)_j(m+\lambda)_j}
                       {(-2m-\lambda)_j j!}w^j.       \tag{1}
$$


Here all rising factorials occur in finite sums. No lower hypergeometric
parameter is used after termination. In particular the denominator in
(1) is nonzero for every 0<=j<=m, including lambda=0.

For completeness, the circular moments are


$$
\mu_l=(-1)^l\frac{\Gamma(2a+1)}
                    {\Gamma(a+l+1)\Gamma(a-l+1)}.
$$


They follow from the beta integral at l=0 and the integration-by-parts
recurrence $(a+l)\mu_l=-(a-l+1)\mu_{l-1}$. Multiplying the coefficient
of w^j in Phi by $\mu_{j-l}$, for 0<=l<m, reduces its orthogonality
sum to a constant times


$$
\sum_{j=0}^m(-1)^j\binom mj
 (a+m-j-1)_{\underline{m-l-1}}(a+j)_{\underline l}=0.
$$


The summand after the binomial is a polynomial in j of degree m-1.
For integral a the same identity follows by continuity, including any
out-of-support moments. This proves the stated reference for both
lambda=1/2 and lambda=1 without importing a varying-weight asymptotic.

The monic extremal argument for a positive weight proves that all roots
of Phi lie strictly inside the unit disk. Thus f has no zero in the
closed disk. Its constant coefficient is one, and its leading
coefficient is exactly


$$
[w^m]f_m^{(\lambda)}=\frac{m+\lambda}{2m+\lambda}.     \tag{2}
$$



For the actual comparison weight use lambda=1 and define


$$
F_m(z)=f_m^{(1)}(-z^2),\quad
 \Psi_n(z)=z^nF_m(1/z)=(-1)^m z\Phi_m^{[m+1]}(-z^2).
                                                               \tag{3}
$$


F has degree n-1, while Psi is monic of degree n and has a zero at the
origin. The extra z in (3) is necessary. Its omission would change the
exterior evaluation functional by a nonconstant factor.

The finite norm normalization is


$$
\|F_m\|_{w_+}^2=\|\Psi_n\|_{w_+}^2
 =\frac{m!(3m+2)!}{((2m+1)!)^2}=\frac1{c_m},\qquad
 w_+=|1+z^2|^{2m+2}.                                  \tag{4}
$$


The circular-binomial norm formula follows from the beta moment
determinant, as in the previously reviewed prediction note. Pushing
Haar measure forward under w=-z^2 gives (4) without an extra factor two.
At m=0, (3)-(4) read F_0=1, Psi_1=z, and c_0=1/2.

## 2. Exact equation and uniform fixed-offset transport

Coefficient comparison in (1) gives


$$
A(w)f''-[2m+\lambda+(\lambda+1)w]f'
                 +m(m+\lambda)f=0,\quad A=w(1-w).     \tag{5}
$$


Let


$$
S=\sqrt{1-w+w^2},\quad S(0)=1,\qquad
 r=\frac1{1+S},\quad L(w)=\int_0^w r(t)dt.
$$


The square root is analytic and nonzero in the open unit disk. If
$r_m=f'/(mf)$, root exclusion gives
$|r_m(w)|\le(1-|w|)^{-1}$. Dividing (5) by m^2 f yields


$$
A(r_m^2+r_m'/m)
 -\left[2+\frac{\lambda+(\lambda+1)w}{m}\right]r_m
 +1+\lambda/m=0.                                     \tag{6}
$$


Every subsequential analytic limit solves Ar^2-2r+1=0 and has value
1/2 at zero, since r_m(0)=(m+lambda)/(2m+lambda); hence it is the
displayed r throughout the disk. Cauchy
bounds and subtraction of the limiting equation then give, successively,


$$
r_m=r+O(m^{-1}),\qquad
 r_m=r+\frac{h_\lambda}{m}+O(m^{-2}),
$$




$$
h_\lambda=\frac{Ar'-[\lambda+(\lambda+1)w]r+\lambda}{2S}.
                                                               \tag{7}
$$


All estimates and fixed derivatives are uniform on each compact subdisk.
The denominator after subtraction tends uniformly to -2S and is bounded
away from zero there; thus the two estimates do not assume a rate from
normal-family convergence alone. Integration of the logarithm normalized
at zero gives


$$
\boxed{f_m^{(\lambda)}(w)
 =e^{mL(w)+H_\lambda(w)}[1+O(m^{-1})],\quad
 H_\lambda(0)=0,\ H_\lambda'=h_\lambda.}              \tag{8}
$$


This includes local derivative estimates for the relative error.

The fixed-offset correction has an explicit primitive. With


$$
\chi=\frac1{1-w+S},\qquad Q(\chi)=\chi^2-\chi+1,
$$


put


$$
H_\lambda=H_0+\lambda J,\quad
 e^{H_0}=\sqrt{\frac{3/4}{Q(\chi)}},\quad
 e^J=\frac{9\chi}{2(1+\chi)^2}.                       \tag{9}
$$


All logarithms and square roots are continued from their value one or
zero at w=0. To verify the new expression, use


$$
w=\frac{2\chi-1}{\chi(2-\chi)},\quad
 S=\frac{Q(\chi)}{\chi(2-\chi)},\quad
 \frac{dw}{d\chi}=\frac{2Q(\chi)}{\chi^2(2-\chi)^2}.
$$


Equation (7) gives


$$
J'=\frac{1-(1+w)r}{2S},\qquad
 J'\,dw=\left(\frac1\chi-\frac2{1+\chi}\right)d\chi.
$$


Since chi(0)=1/2, integration proves (9).

For n=2m+1 define the actual odd transport


$$
K(w)=H_1(w)-\tfrac12L(w)=H_0(w)+J(w)-\tfrac12L(w).
                                                               \tag{10}
$$


Then f_m^(1)=exp(nL/2+K)(1+O(1/n)). At the common saddle argument
$w_s=-\rho^2$, the already known change of variable gives


$$
\chi(w_s)=\rho^2,\quad e^{L(w_s)}=\frac{27\rho}{20},\quad
 e^{J(w_s)}=\frac9{10},
$$




$$
\boxed{T_o:=e^{K(w_s)}
 =e^{H_0(w_s)}\sqrt{\frac3{5\rho}}
 =\frac{3\sqrt{10}}{20\rho^{3/2}}>0.}                \tag{11}
$$


The literal absolute-symbol reference lambda=1/2 instead has transport
H_(1/2)-L/2 and saddle ratio sqrt(2/(3rho)) relative to exp H_0. It is
not the reference used in the actual odd operator normalization.

## 3. Exact all-parity contour identities and the extra odd sign

Retain the original integer polynomials and normalizations


$$
S_n(t)=(1+t^2)^nU_n(t),\quad
 q(z)=z^nU_n(1/z),\quad v=q/(n!V_n(1))=A_n^{-1}e_0,
$$




$$
u_n=[t^n]U_n=(2n)![t^n]V_n=n!V_n(1)v_0\ne0.
                                                               \tag{12}
$$


Here v_0 need not be positive in the odd family. The proved all-degree
nonvanishing results ensure that every division in (12) is defined.

The full error identity is


$$
R_{a,n}(1)=\frac{(-1)^n}{2i}\int_{-i}^{i}
                 \frac{S_n(t)}{(1-t)^{n+1}}dt.
$$


Inverting t=1/z reverses the endpoint order; the minus sign from
dt=-z^(-2)dz cancels that reversal. Deforming in the left half-plane,
without crossing 0 or 1, gives exactly


$$
\boxed{\frac{R_{a,n}(1)}{u_n}
 =\frac{(-1)^n}{2i}\int_\Gamma
 \frac{(1+z^2)^n[v(z)/v_0]}{z^{2n+1}(z-1)^{n+1}}dz.}   \tag{13}
$$


Gamma is the left arc $|z+1/2|=\sqrt5/2$, from -i to i, with upward
tangent at -phi. For odd n, the explicit factor in front is negative.
It must not be copied from the even contour without change.

The residue of the integrand in (13), without its prefactor, is


$$
\operatorname{Res}_0 I_n=(-1)^{n+1}Z_n/u_n,
 \qquad Z_n=\widehat Q_n(1).                           \tag{14}
$$


Indeed D^n v=z^{3n}S_n(1/z)/(n!V_n(1)), and expanding (z-1)^(-n-1)
leaves $(-1)^{n+1}\sum_{d=n}^{3n}\binom dn S_{n,d}$.
Since this sum is S_n^(n)(1)/n!=Z_n, (14) follows after normalization.
Consequently the coefficient contour has the SAME positive sign in both
parities:


$$
\boxed{\frac{Z_n}{u_n}=\frac1{2\pi i}\int_{|z|=\rho}
 \frac{(1+z^2)^n[v(z)/v_0]}{z^{2n+1}(1-z)^{n+1}}dz.}    \tag{15}
$$


The circle is counterclockwise. It encloses 0 and excludes 1.

As a frozen normalization control, n=1 has V=2-t, U=3-2t,
Qhat=-2z^2+6z-6, Z=u_n=-2, and Pa(1)=0. Thus Ra/u_n=pi/4>0 and
Z/u_n=1. Equation (14) has positive sign at n=1, while (13) has its
explicit negative prefactor. These agree with the original error
Ra=Z pi/4-Pa(1); no new degree was constructed.

## 4. Actual factorization and unchanged global phases

Use the actual reference (3), and define


$$
R_n(z)=\frac{v(z)}{v_0F_m(z)},\qquad
 \widetilde R_n(w)=\frac{v^*(w)}{v_0F_m(w)},\quad
 v^*(w)=w^n v(1/w).                                    \tag{16}
$$


The odd Hardy/reference lemma in
`raw_odd_hardy_reference_and_reversal_framework.md` proves uniform H^2
bounds on both ratios (full independent PASS in
`raw_odd_hardy_framework_independent_review.md`);
its proof uses the accepted bounded odd inverse and scalar s_m, not
positive accretivity of the signed odd matrix. This lemma is a separate
input from audit_sources. The exact factorization is


$$
v(z)/v_0=F_m(z)R_n(z)
         =z^nF_m(1/z)\widetilde R_n(1/z).               \tag{17}
$$



The interior and exterior phases are therefore EXACTLY the previously
reviewed functions


$$
\mathcal H_i(z)=\log(1+z^2)-2\log z-\log(1-z)
                                      +\tfrac12 L(-z^2),
$$




$$
\mathcal H_o(z)=\log(1+z^2)-\log(-z)-\log(1-z)
                                      +\tfrac12 L(-1/z^2).
                                                               \tag{18}
$$


The only base-factor change is the bounded analytic amplitude exp K
instead of exp H_0. Since (-z)(1-z)=z(z-1), the exterior integer-power
factor in (18) is correct for every n; it supplies no additional odd
sign. The only such sign is the one already displayed in (13).

For the interior circle, the reviewed algebraic maximum proof in
`raw_even_endpoint_residue_asymptotic.md`, Sections 2-3, applies to
(18) without alteration. Its unique maximum is rho, with height xi and
angular curvature kappa. For the exterior middle arc, the independently
certified strict maximum from `raw_exterior_phase_strict_maximum.md`
likewise applies without alteration, with saddle -phi, height tau and
vertical curvature h_o. The compact saddle arguments lie in |w|<1,
where K and its derivatives are bounded.

The endpoint estimate also carries over with its proof intact. If
a=-Re z on Gamma, then |z|^2=1+a and root exclusion gives


$$
|f_m^{(1)}(-1/z^2)|\le(1+|z|^{-2})^m
                  \le(1+|z|^{-2})^{n/2}.
$$


Together with the odd Hardy bound, the old estimate is only improved.
For delta=1/8, the endpoint contribution is bounded by a constant times
$(\sqrt5\,\delta)^n/n$, whose base is strictly smaller than tau.
Thus no unproved extension of a compact asymptotic to the endpoints is
being made.

## 5. Uniform varying-multiplier asymptotics

Put


$$
A_n=(-1)^m\widetilde R_n(-\rho),\qquad B_n=R_n(\rho),
$$




$$
c_a=\frac{\rho^3 T_o}{2}\sqrt{\frac{2\pi}{h_o}},\qquad
 c_Z=\frac{T_o}{(1-\rho)\sqrt{2\pi\kappa}}.           \tag{19}
$$


The root-free reference expansion, uniform H^2 bounds and Cauchy
derivative estimates give the same uniformly bounded, locally Lipschitz
amplitudes used in the reviewed even varying-multiplier Gaussian lemma.
Its elementary proof therefore gives


$$
\boxed{\frac{R_{a,n}(1)}{u_n}
 =(-1)^{m+1}c_a A_n\frac{\tau^n}{\sqrt n}
                      +O(\tau^n/n),}                 \tag{20}
$$




$$
\boxed{\frac{Z_n}{u_n}
 =c_Z B_n\frac{\xi^n}{\sqrt n}+O(\xi^n/n).}         \tag{21}
$$


The error constants are uniform in the actual sequence. These estimates
do not divide by A_n or B_n or assume their lower bounds. At the exterior
saddle dz=i dy, so the prefactor dz/(2i) is positive dy/2; this verifies
the factor one-half and, together with (-1)^n, the sign in (20).
At the interior saddle dz=i z dtheta cancels the extra z in the
denominator of (15), leaving the factor 1/(1-rho) in (19).

The separately certified actual odd multiplier theorem,
`raw_odd_saddle_multiplier_limits.md`, with FULL PASS in
`raw_odd_saddle_multipliers_independent_review.md`, proves


$$
A_n\longrightarrow A_o\ne0,\qquad B_n\longrightarrow B_o\ne0.
                                                               \tag{22}
$$


Its rigorous bounds are -1.193<A_o<-1.192 and 0.282<B_o<0.283.
Then (20)-(21) are signed leading-term asymptotics with 1+o(1) relative
errors. Both constants retain the actual v_0 normalization in (16);
neither contains an arbitrary rescaling of the operator solution.

## 6. Relative error, sign, and the actual primitive form

The common transport T_o cancels exactly between the two saddles.
The previously proved curvature relation simplifies (19) to


$$
\frac{c_a}{c_Z}
 =\pi\rho^3(1-\rho)\sqrt{\kappa/h_o}=\pi\rho.        \tag{23}
$$


Using (22), and retaining the odd exponential-error theorem,


$$
\frac{R_{e,n}(1)}{[t^n]V_n}=O(\beta^n/n),
 \qquad\beta=3\sqrt3/4,
$$


one has Re/Ra=O((beta/tau)^n/((2n)!sqrt(n))) ->0. Hence


$$
\boxed{(e+\pi)-\frac{N_n}{Z_n}
 =(-1)^{m+1}4\pi\rho\frac{A_o}{B_o}
                  \rho^{5n}[1+o(1)],\quad n=2m+1,}    \tag{24}
$$


where the original integer numerator is
N_n=Pe_n(1)+4Pa_n(1). The factor four in (24) is the original arctangent
coefficient; the quotient Ra/Z itself has pi rho, not 4pi rho.

The independent multiplier certificate gives A_o<0 and B_o>0. Therefore
(24) reads (-1)^m C_o rho^(5n)(1+o(1)), with


$$
C_o=-4\pi\rho A_o/B_o>0.                              \tag{25}
$$


This sign statement uses the actual certified amplitudes and their full
independent review, not a numerical value substituted into a base
polynomial. No analytic input remains pending.

Finally retain


$$
g_n=\gcd(|Z_n|,|N_n|),\quad q_n=|Z_n|/g_n,\quad
 p_n=\operatorname{sign}(Z_n)N_n/g_n.
$$


With the proved nonzero limits (22), the odd primitive form has magnitude


$$
|q_n(e+\pi)-p_n|
 \sim4\pi\rho|A_o/B_o|\,q_n\rho^{5n}.                \tag{26}
$$


The contour derivation itself asserts no denominator estimate. Combining
(26) with a separately proved uniform arithmetic lower divisor is a
subsequent step, whose prime certificates and strict rate comparison
must remain independently verified.
