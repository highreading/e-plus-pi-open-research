> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Handoff: fixed-circle saddle reduction for the mixed-cubic boundary ray

Date: 2026-08-27.

Status: **unfinished research handoff**.  The algebraic reductions below are
exact.  Numerical root locations and the proposed saddle conclusion are
diagnostics only.  This note does not assert a coefficient asymptotic,
irrationality result, or transcendence result.

## 1. Frozen arithmetic input

The independently audited and frozen package

* `sources/mixed_cubic_boundary_cartier_content_and_recurrence.md`,
* `scripts/mixed_cubic_boundary_cartier_content_and_recurrence_certificate.py`,
* `results/mixed_cubic_boundary_cartier_content_and_recurrence_certificate.json`

proves the sharp clearing/content and recurrence statements.  Its manifest is
`results/mixed_cubic_boundary_cartier_content_and_recurrence_hashes.sha256`.
In particular, the proved arithmetic gives the following **conditional**
ledger if the saddle asymptotic below is established:



$$
d=2.3370623743589729959\ldots,qquad
 h\leq2.3246783391437311\ldots,qquad
 d/h=1.005327203771255\ldots.                                      \tag{1}
$$



Thus the sole live gap in that branch is the analytic coefficient asymptotic.

## 2. Exact contour functions

The two exact contour integrals are



$$
I_j(m)=\frac1{2\pi i}\oint \Psi(v)^m b_j(v)\frac{dv}{v}quad(j=0,2), \tag{2}
$$



where



$$
\Psi(v)=\frac{(1+2v)^6(1+(1-i)v)^6}{v^4(1+v)^4},qquad
 b_0(v)=\frac{1+(1+i)v}{1+v},                                      \tag{3}
$$



and



$$
b_2(v)=\frac{(1-i)(4v^4+8v^3+2v^2-2v-1)}{32v(1+v)^2}.             \tag{4}
$$



The exact integration-by-parts identity in the frozen source is



$$
B_m=\frac{2|C_m|^2}{m}\operatorname {Im}
       \left(I_2(m)\overline{I_0(m)}\right).                         \tag{5}
$$



The relevant saddle is the root



$$
\tau=0.3933435869406637868
      +0.2348766139072831759i                                      \tag{6}
$$



of



$$
S(v)=4v^3+(6-i)v^2-iv-1-i.                                        \tag{7}
$$



Put $r=|\tau|=0.458133388\ldots<1$.  The fixed circle $|v|=r$
avoids all poles of the amplitudes and of $\Psi$.  This makes a direct
one-dimensional complex Laplace proof possible; no contour deformation is
needed if the unique-maximum statement below is certified.

## 3. Exact fixed-circle modulus reduction

Write $v=x+iy=re^{i\theta}$, so $x^2+y^2=r^2$, and set



$$
A=|1+2v|^2=1+4x+4r^2,quad
 B=|1+(1-i)v|^2=1+2x+2y+2r^2,quad
 C=|1+v|^2=1+2x+r^2.                                                 \tag{8}
$$



Then, exactly,



$$
|\Psi(v)|^2=\frac{A^6B^6}{r^8C^4}.                                \tag{9}
$$



The angular logarithmic derivative has the same sign as



$$
N(x,y)=-6yBC+3(x-y)AC+2yAB.                                       \tag{10}
$$



Use the rational parametrization



$$
x=r\frac{1-t^2}{1+t^2},qquad
 y=r\frac{2t}{1+t^2},qquad t=\tan(\theta/2).                        \tag{11}
$$



After removing the nonzero factor $-r/(1+t^2)^3$, equation $N=0$
is the degree-six polynomial



$$
\begin{aligned}
 P_r(t)={}&12r^4t^6+16r^4t^5+12r^4t^4+32r^4t^3-12r^4t^2+16r^4t-12r^4\\
 &-36r^3t^6-80r^3t^5+20r^3t^4+20r^3t^2+80r^3t-36r^3\\
 &+39r^2t^6+106r^2t^5-89r^2t^4-44r^2t^3+89r^2t^2+106r^2t-39r^2\\
 &-18rt^6-60rt^5+50rt^4+50rt^2+60rt-18r\\
 &+3t^6+14t^5+3t^4+28t^3-3t^2+14t-3.                              \tag{12}
\end{aligned}
$$



This is the main exact reduction for the next agent.

## 4. Algebraic data for the radius

Let $R=r^2$.  Elimination of the real and imaginary parts of (7) gives
the exact polynomial factor containing the desired radius:



$$
128R^6-384R^5+280R^4-20R^3-55R^2+R+2=0.                           \tag{13}
$$



The desired root is the small positive root



$$
R=0.209886201147898\ldots,qquad r=\sqrt R.                         \tag{14}
$$



The other positive real root of (13) is
$1.99657337502923\ldots$, corresponding to the external
equal-critical-value saddle.  It is not on the fixed circle $|v|=r<1$.
The third saddle-radius square is the positive root
$0.298291481134921\ldots$ of



$$
16R^3+11R^2+2R-2.                                                   \tag{15}
$$



## 5. Diagnostics, not yet a theorem

At the radius (14), numerical root isolation of (12) gives exactly two real
roots and two nonreal conjugate pairs:



$$
\begin{aligned}
 t_{\max}&=0.2758461130970533\ldots,\\
 t_{\min}&=-281.441986935192\ldots,\\
 t&=-3.05030404770449\ldots\pm0.89674172229482\ldots i,\\
 t&=0.148728007814276\ldots\pm2.19328747874792\ldots i.             \tag{16}
\end{aligned}
$$



The first real root is exactly the parameter
$\operatorname {Im}\tau/(r+\operatorname {Re}\tau)$.  Numerical
evaluation shows it is the unique global maximum of (9); the second real
root is the unique minimum, near angle $-3.13449$.  These statements
have **not** yet been converted into an exact Sturm certificate.

The exact amplitude quotient is nonreal at the candidate saddle;
numerically,



$$
\operatorname {Im}\frac{b_2(\tau)}{b_0(\tau)}
 =0.0642986930247985444593\ldots>0.                                 \tag{17}
$$



This sign also still needs an exact algebraic interval certificate in the
new saddle package, although its formula is exact in the frozen source.

## 6. Next rigorous proof steps

1. Isolate the small positive root $R$ of (13) by rational endpoints,
   then isolate $r=\sqrt R$.
2. Run a Sturm sequence for $P_r(t)$ over the real algebraic field
   $\mathbb Q(r)$.  Prove that it has exactly two real roots, one in a
   short rational interval around each value in (16).
3. Evaluate the sign of the angular derivative on the three complementary
   arcs.  This proves that $t_{\max}$ is the unique global maximum and
   $t_{\min}$ the unique minimum.  Compare their exact algebraic modulus
   values, or use the sign pattern plus periodicity.
4. Prove $\Psi''(\tau)\ne0$ and obtain the standard fixed-circle
   complex-Laplace expansion, uniformly for both amplitudes:

   

$$
I_j(m)=\Psi(\tau)^m m^{-1/2}
       \left(K b_j(\tau)+O(m^{-1})\right),\qquad j=0,2,              \tag{18}
$$



   with the same nonzero Gaussian factor $K$.
5. Certify (17) by exact algebraic interval arithmetic.  Equations (5) and
   (18) then give a nonzero leading determinant and the rate
   $n^{-1}\log|B_m|\to2\ell$.
6. Combine this with the positive-integral Laplace upper bound and the
   frozen clearing/content theorem.  The conditional constants in (1) then
   become rigorous and cross the exponent-one threshold by
   $0.0123840352\ldots$ per $n$.

No step after item 2 should use the external saddle: its modulus is greater
than one and it is outside the fixed integration circle.

