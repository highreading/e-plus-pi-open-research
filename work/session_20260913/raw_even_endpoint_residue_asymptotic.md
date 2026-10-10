> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The actual even endpoint residue asymptotic and the primitive-denominator threshold

Date: 2026-09-13. Original bounded continuation by audit_sources.
Independent review: PASS by audit_results; see raw_even_endpoint_residue_independent_review.md for the complete algebraic, contour, normalization and primitive-denominator audit.

This proves the asymptotic of the original integer endpoint scalar $Z_n=\widehat Q_n(1)$ relative to the leading coefficient $u_n=[t^n]U_n$, on even $n=2m$. The global circle maximum is proved algebraically. The subsequent approximation and gcd corollaries combine this theorem with the separately proved exterior saddle assembly; each source retains its independent verification record.

Put


$$
\rho=\frac{\sqrt5-1}{2},\quad \phi=1/\rho,\quad
\xi=\sqrt{\frac{27}{4\rho^5}},\quad
\tau=\sqrt{\frac{27\rho^5}{4}},\quad
\kappa=\frac52+\sqrt5.
$$


The actual interior multiplier theorem gives $R_n(\rho)\to B_s>0$, with $0.604<B_s<0.605$, and local uniform convergence of the whole family. Its independent review is raw_even_interior_multiplier_independent_review.md.

The endpoint theorem is


$$
\boxed{\displaystyle
\frac{Z_n}{u_n}
=C_Z\,\frac{\xi^n}{\sqrt n}\,[1+o(1)],\qquad
C_Z=\frac{e^{H(-\rho^2)}B_s}
 {(1-\rho)\sqrt{2\pi\kappa}}>0.}                        \tag{1}
$$


Here $H$ is the analytic base transport term from raw_base_polynomial_uniform_asymptotic.md. No estimate for a primitive denominator is included in (1).

## 1. The original residue and an admissible circle

Retain the actual Toeplitz solution $v(z)$, $v_0=v(0)>0$, and the original integer leading coefficient


$$
u_n=(2n)![t^n]V_n=n!V_n(1)v_0\ne0.
$$


The reviewed residue identity gives


$$
\frac{Z_n}{u_n}
=-\operatorname{Res}_{z=0}
 \frac{(1+z^2)^n[v(z)/v_0]}
 {z^{2n+1}(z-1)^{n+1}}.
$$


For even $n$, $n+1$ is odd. Therefore


$$
\frac{Z_n}{u_n}
=\frac1{2\pi i}\int_{|z|=\rho}
 \frac{(1+z^2)^n[v(z)/v_0]}
 {z^{2n+1}(1-z)^{n+1}}\,dz,                            \tag{2}
$$


where the circle is counterclockwise. Its only enclosed pole is zero; $z=1$ lies outside. This contour computes the residue itself and does not discard the residue from an arctangent path deformation.

The compact base expansion is


$$
v(z)/v_0=e^{(n/2)L(-z^2)+H(-z^2)}R_n(z)[1+O(1/n)]
$$


uniformly on this circle and in its neighborhood. The relative error belongs to the explicit base factor. The actual multiplier is retained.

## 2. An algebraic strict maximum on every interior circle

For $|x|<1$, define


$$
h(x)=\log(1+x)+\tfrac12L(-x),\qquad
b(x)=\frac1{1+x+\sqrt{1+x+x^2}},
$$


with branches equal to their real values at zero. The discriminant has no zero in the open disk. Direct algebra gives


$$
x=\frac{1-2b}{b(2-b)},\qquad
xh'(x)=\frac{1-2b}{2(1-b)}
      =1-\frac1{2(1-b)}.                               \tag{3}
$$


The denominators are nonzero in this disk. For instance $b=1$ would imply $x=-1$; $b=0,2$ contradict the defining quadratic.

Writing $b=u+iv$, the inverse relation in (3) gives the exact sign identity


$$
\Im x
=-\frac{2v(|b|^2-\Re b+1)}{|b(2-b)|^2}.                \tag{4}
$$


Its real factor $|b|^2-\Re b+1=(u-\tfrac12)^2+v^2+\tfrac34$ is strictly positive. On the other hand


$$
\Im[xh'(x)]=-\frac{v}{2|1-b|^2}.
$$


Thus $\Im[xh'(x)]$ has the same sign as $\Im x$.

On $x=se^{i\theta}$, $0<s<1$,


$$
\frac{d}{d\theta}\Re h(se^{i\theta})
=-\Im[xh'(x)].
$$


It is strictly negative for $0<\theta<\pi$ and strictly positive for $\pi<\theta<2\pi$. Consequently


$$
\Re h(x)\le h(s)\quad(|x|=s),
$$


with equality only at $x=s$.

The interior phase is


$$
\mathcal H_{\rm in}(z)
=h(z^2)-2\log z-\log(1-z).                              \tag{5}
$$


On $|z|=r<1$, the even part is maximal only at $z=\pm r$. Also
$|1-z|\ge1-r$, with equality only at $z=r$. Therefore the real part of (5) has its unique strict global maximum on every such circle at $z=r$. On any closed portion bounded away from that point, compactness gives a strictly positive phase gap.

No interval computation or numerical sample is used for this maximum.

## 3. The stationary radius, exact height, and curvature

Differentiating (5) and using (3) simplifies the derivative to


$$
\mathcal H_{\rm in}'(z)
=-\frac1{z(1-b(z^2))}+\frac1{1-z}.                      \tag{6}
$$


At $z=\rho$, one has $b(\rho^2)=\rho^2$ and $1-\rho=\rho^2$. Hence (6) vanishes.

The inverse derivative in (3) is


$$
b'(x)=-\frac{b^2(2-b)^2}{2(b^2-b+1)}.
$$


Substitution gives


$$
\mathcal H_{\rm in}''(\rho)
=\frac{25+11\sqrt5}{4}>0,\qquad
\rho^2\mathcal H_{\rm in}''(\rho)=\kappa.                \tag{7}
$$


The closed primitive for $L$, with $b=\rho^2$, gives


$$
e^{2\mathcal H_{\rm in}(\rho)}
=\frac{27}{4\rho^5}=\xi^2.                             \tag{8}
$$


These identities may also be checked by reduction modulo $\rho^2+\rho-1=0$. In particular, $\xi>1$ and $\tau/\xi=\rho^5$.

## 4. A complete varying-amplitude saddle proof

Parameterize the circle by $z=\rho e^{i\theta}$, $-\pi\le\theta\le\pi$. To avoid a global logarithm ambiguity, use the continuous phase


$$
P(\theta)=h(\rho^2e^{2i\theta})
          -2\log\rho-2i\theta-\log(1-\rho e^{i\theta}).
$$


Its exponential to the integer power $n$ is the exact nth-power factor in (2). Near zero,


$$
P(0)=\log\xi,\qquad P'(0)=0,\qquad
P''(0)=-\kappa.
$$


The amplitude in (2), after $dz=iz\,d\theta$, is


$$
a_n(\theta)=
\frac{e^{H(-z^2)}R_n(z)}{1-z}[1+O(1/n)].
$$


It is uniformly bounded on the whole circle and converges uniformly there, by the actual local uniform multiplier theorem and the compact base expansion. At zero its limit is


$$
a_0=\frac{e^{H(-\rho^2)}B_s}{1-\rho}>0.
$$



Choose a fixed small $\delta>0$. Taylor's theorem and (7) give
$\Re[P(\theta)-P(0)]\le-\kappa\theta^2/4$ for $|\theta|\le\delta$.
The strict global maximum proved in Section 2 gives a positive gap on the rest of the circle. Its contribution is therefore exponentially smaller than $\xi^n/\sqrt n$.

In the remaining integral, set $\theta=t/\sqrt n$. For fixed $t$,


$$
n[P(t/\sqrt n)-P(0)]\to-\kappa t^2/2,\qquad
a_n(t/\sqrt n)\to a_0.
$$


The Gaussian majorant just obtained and the uniform amplitude bound permit dominated convergence on the expanding interval. Therefore


$$
\frac1{2\pi}\int_{-\pi}^{\pi}e^{nP(\theta)}a_n(\theta)d\theta
=\frac{a_0\xi^n}{\sqrt{2\pi\kappa n}}\,[1+o(1)].
$$


This proves (1), including its sign. No unproved convergence rate of $R_n$ is used.

## 5. Combining the two saddles: actual endpoint approximation

Use the exterior assembly raw_even_dual_saddle_assembly.md, whose complete end-to-end review is raw_even_saddle_assembly_independent_review.md. Its proof uses its separate phase certificate and exterior multiplier theorem and does not depend on the interior residue theorem here. In the notation of that assembly,


$$
\frac{R_{a,n}(1)}{u_n}
=(-1)^m C_a\,\frac{\tau^n}{\sqrt n}[1+o(1)],
\quad
C_a=\frac{\rho^3 e^{H(-\rho^2)}}2
       \sqrt{\frac{2\pi}{h_{\rm out}}}\,A_s>0,
$$


where $h_{\rm out}=(25-11\sqrt5)/4$ and $0.049<A_s<0.050$.
The exact curvature relation is


$$
\frac{\mathcal H_{\rm in}''(\rho)}{h_{\rm out}}=\rho^{-10}.
$$


It cancels the common base transport and simplifies the quotient to


$$
\boxed{\displaystyle \frac{C_a}{C_Z}=\pi\rho\,\frac{A_s}{B_s}.} \tag{9}
$$


Thus


$$
\frac{R_{a,n}(1)}{Z_n}
=(-1)^m\pi\rho\frac{A_s}{B_s}\rho^{5n}[1+o(1)].          \tag{10}
$$



The even exponential-error theorem gives


$$
R_{e,n}(1)/[t^n]V_n=O(\beta^n/n),\qquad \beta=3\sqrt3/4.
$$


Since $u_n=(2n)![t^n]V_n$, its ratio to the nonzero arctangent error tends to zero at least at the rate
$O((\beta/\tau)^n/((2n)!\sqrt n))$.

Retain the original integers


$$
N_n=\widehat P_{e,n}(1)+4\widehat P_{a,n}(1),\qquad
Z_n=\widehat Q_n(1).
$$


Their exact errors satisfy $Z_n(e+\pi)-N_n=R_{e,n}(1)+4R_{a,n}(1)$. Consequently


$$
\boxed{\displaystyle
(e+\pi)-\frac{N_n}{Z_n}
=(-1)^m C_{\rm app}\rho^{5n}[1+o(1)],
\qquad
C_{\rm app}=4\pi\rho\,\frac{A_s}{B_s}>0.}                \tag{11}
$$


This is the actual unreduced endpoint approximation, with all original scalar factors canceled by proved identities. It is eventually nonzero. Formula (11) is not a primitive integer-form estimate.

## 6. The exact remaining arithmetic threshold

Set


$$
g_n=\gcd(|Z_n|,|N_n|),\qquad
q_n=|Z_n|/g_n,\qquad p_n=\operatorname{sign}(Z_n)N_n/g_n.
$$


Then $p_n,q_n$ are the actual reduced numerator and positive denominator, and


$$
\ell_n=q_n(e+\pi)-p_n
=q_n\left[(e+\pi)-N_n/Z_n\right].
$$


Equation (11) gives the exact asymptotic criterion


$$
|\ell_n|\sim C_{\rm app}\,q_n\rho^{5n}.                 \tag{12}
$$


On any even subsequence tending to infinity, primitive shrinking is therefore equivalent to


$$
q_n\rho^{5n}\to0.                                     \tag{13}
$$


Equivalently, using (1),


$$
\frac{g_n}{|u_n|\tau^n/\sqrt n}\to\infty.                \tag{14}
$$


A sufficient exponential condition is


$$
\limsup_{n\to\infty,\ n\ {\rm even}}\frac{\log q_n}{n}
<5\log\phi.
$$


More generally, $\liminf_{n\ {\rm even}}q_n\rho^{5n}=0$ would supply a shrinking subsequence.

If that arithmetic condition were proved, eventual nonvanishing in (11) would prove irrationality: for a rational value $a/b$, every nonzero $q_na/b-p_n$ has absolute value at least $1/b$. The required arithmetic condition is NOT proved here.

In particular, $u_n=(2n)![t^n]V_n$, with its nonzero integer final factor, can be very large. The relative exponential error alone does not remove this factorial scale from the primitive form. The known exact dyadic lower bound for $q_n$ and the existing gcd carriers remain compatible with an unresolved global cancellation problem. No rationality or irrationality conclusion follows without that additional result.
