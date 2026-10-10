> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 237 — algebraicity and an exact recurrence for the common $j=1$ phase residual

Date: 2026-08-31

## 1. Scope and verdict

Items 229, 231, and 236 leave one common phase residual



$$
c_h^*=c_h\!\left(-{4h+3\over6}\right),\qquad h\geq1.
$$



This item determines that sequence exactly.

**PROVED — fixed algebraic coefficient.**  There is a single algebraic
series $C(x)$, independent of $h$, such that



$$
\boxed{c_h^*=[x^{2h}]C(x)}.             \tag{1.1}
$$



It has a rational parametrization $C=N/D^3$ on an explicit degree-six
curve, and therefore an explicit primitive resultant equation of bidegree
$(9,6)$.

**PROVED — all-$h$ recurrence.**  The sequence obeys an exact order-three,
step-three recurrence



$$
\boxed{\sum_{k=0}^3p_k(h)c_{h+3k}^*=0},           \tag{1.2}
$$



where every $p_k\in\mathbb Q[h]$ has degree 16 and is recorded below.
This is certified by substituting the rational parametrization into the
corresponding differential operator and obtaining the zero polynomial.
It is not a guessed recurrence justified by a long table.

**EXACT FINITE / OPEN — comparison with Item 222.**  Exact rational
evaluation gives



$$
c_h^*=\mathcal R_hE_h^*               \tag{1.3}
$$



for all 54 admissible $h\leq80$, and the recurrence that (1.3) predicts
for $E_h^*$ holds through $h\leq220$ modulo two independent primes.
No symbolic telescoping certificate for that recurrence is obtained.
Thus (1.3) remains **OPEN** for unbounded $h$.

**PROVED — a scoped endpoint-ratio no-go.**  In each class
$h\equiv1,2\pmod3$, the ratio $K_h/E_h^*$ does not obey a first-order
rational recurrence whose two polynomial coefficients have degree at most
5.  This rules out that ansatz only.

No all-prime nonvanishing theorem, radical bound, or prime log-mass saving
follows.  The new unconditional Route-1 rate and divisibility exponent are
both zero.

## 2. The phase coefficient before normalization

Put



$$
Q(y)=1+y+{y^2\over2},                                      \tag{2.1}
$$



and



$$
A(y)={20+14y+4y^2\over3},\qquad
 B(y)=2-5y-3y^2.                                            \tag{2.2}
$$



The coefficient formula proved in Item 229 becomes



$$
c_h^*=[y^{2h}](1+y)^{-2h-1}Q(y)^{(4h+3)/3}
                         \bigl(hA(y)+B(y)\bigr).              \tag{2.3}
$$



This formula is valid over formal power series.  Rational powers always
mean the branch with constant term 1, so there is no analytic convergence
assumption.

## 3. Removing $h$ from the coefficient kernel

Make the formal change of variable



$$
x={y(1+y)\over Q(y)^{2/3}}=y+O(y^2).         \tag{3.1}
$$



Residue substitution in (2.3) gives



$$
c_h^*=[x^{2h}]Q(y)^{1/3}\bigl(hA(y)+B(y)\bigr){dy\over dx}. \tag{3.2}
$$



If



$$
U_A=Q^{1/3}A{dy\over dx},\qquad
 U_B=Q^{1/3}B{dy\over dx},                                  \tag{3.3}
$$



then $h[x^{2h}]U_A={1\over2}[x^{2h}]xU_A'$.  Hence (3.2)
is exactly (1.1) with



$$
C(x)=U_B+{x\over2}{dU_A\over dx}.      \tag{3.4}
$$



Now define



$$
D(y)=6+14y+7y^2+2y^3.                                     \tag{3.5}
$$



Direct differentiation of (3.1) gives



$$
{dx\over dy}=Q(y)^{-5/3}{D(y)\over6}.                      \tag{3.6}
$$



Thus $U_A=6Q^2A/D$, $U_B=6Q^2B/D$, and the right side of
(3.4) is rational in $y$.  Exact simplification yields



$$
\boxed{C(x(y))={N(y)\over D(y)^3}},                         \tag{3.7}
$$



where



$$
\begin{aligned}
N(y)={}&432+2064y+4440y^2+5376y^3+4044y^4\\
     &\quad+1860y^5+486y^6+48y^7.                           \tag{3.8}
\end{aligned}
$$



The checker verifies (3.7) as a polynomial identity: after putting (3.4)
over $D^3$, its numerator is exactly the eight-term polynomial (3.8).
It also independently applies Lagrange inversion and matches (2.3)
through $h=40$; that finite replay is not the logical basis for the
all-$h$ derivation.

## 4. A compact algebraic equation

Let $u=x^3$ and $v=C(x)$.  Cubing (3.1) gives the polynomial curve



$$
u(y^2+2y+2)^2-4y^3(1+y)^3=0.                              \tag{4.1}
$$



Eliminate $y$ from (4.1) and $vD(y)^3-N(y)=0$.  The primitive
resultant is



$$
\boxed{
 \mathscr P(u,v)=2^{-27}\operatorname {Res}_y\!\left(
 u(y^2+2y+2)^2-4y^3(1+y)^3,\ vD(y)^3-N(y)\right).
}                                                            \tag{4.2}
$$



The raw resultant has content $2^{27}$.  The primitive polynomial has
38 nonzero terms and



$$
\deg_u\mathscr P=9,\qquad\deg_v\mathscr P=6. \tag{4.3}
$$



Consequently



$$
\mathscr P(x^3,C(x))=0.              \tag{4.4}
$$



The canonical JSON contains all 38 integer coefficients, indexed by the
powers of (u) and (v).  The checker recomputes the resultant with an
exact fraction-free Sylvester determinant, reconstructs it from a
two-dimensional interpolation grid, and performs an off-grid evaluation
at $(u,v)=(13,11)$.

## 5. The exact step-three recurrence

Write $b_n=[x^n]C(x)$, so $c_h^*=b_{2h}$.  The four recurrence
polynomials are most compactly recorded as



$$
p_k(h)=\lambda_kL_k(h)q_k(h),         \tag{5.1}
$$



where the coefficient lists for $q_k$ are low-to-high:



$$
\begin{array}{c|c|l}
k&\lambda_k&[q_{k,0},q_{k,1},\ldots]\\ \hline
0&-1/76742461255680&
[6414233265,5112300033,1603835736,247582992,18819760,564080]\\
1&-1/710578344960&
[402660529612416,1002494068911927,1039962332216826,
596405304955566,209971952382012,47325249956016,
6857541598288,618060903584,31525303040,694946560]\\
2&-1/105270865920&
[1090010738003273316,2470146696629963712,2354075629101513405,
1243406090403290781,403775302745693160,84106392952710132,
11294493697293648,946720367971824,45093571774720,932385882560]\\
3&1/18050560&
[214443126,369944721,239554248,72513072,10358560,564080].
\end{array}                                                   \tag{5.2}
$$



The linear-factor products are



$$
\begin{aligned}
L_0={}&(h+3)(2h+3)(h+5)(h+6)(2h+9)(4h+9)(4h+15)\\
 &\quad\cdot(4h+21)(4h+27)(4h+33)(4h+39),\\
L_1={}&(h+2)(h+6)(2h+9)(4h+21)(4h+27)(4h+33)(4h+39),\\
L_2={}&(h+2)(h+4)(h+5)(2h+7)(2h+11)(4h+33)(4h+39),\\
L_3={}&(h+2)(h+4)(h+5)(h+7)(h+8)(2h+7)(h+9)\\
 &\quad\cdot(2h+11)(2h+13)(2h+15)(2h+17).
                                                               \tag{5.3}
\end{aligned}
$$



All four $p_k$ have degree 16.  In particular, $p_3(h)>0$ for every
integer $h\geq1$, so (1.2) determines each residue-class subsequence
from three initial values.

Here is the symbolic certificate.  With



$$
\theta=x{d\over dx},\qquad
 \mathcal D=\sum_{k=0}^3x^{18-6k}p_k\!\left({\theta-6k\over2}\right), \tag{5.4}
$$



the coefficient of $x^{n+18}$ in $\mathcal DC$ is



$$
\sum_{k=0}^3p_k(n/2)b_{n+6k}.         \tag{5.5}
$$



Under (3.1),



$$
\theta={3y(1+y)(y^2+2y+2)\over D(y)}{d\over dy}.             \tag{5.6}
$$



Substitute $C=N/D^3$, use (4.1) for the powers of $x^3$, and clear



$$
D(y)^{35}(y^2+2y+2)^{12}.               \tag{5.7}
$$



The resulting numerator is identically zero in $\mathbb Q[y]$.  The
checker performs this calculation coefficient by coefficient.  Therefore
$\mathcal DC=0$, and setting $n=2h$ in (5.5) proves (1.2) for every
$h\geq1$.

## 6. The exact target for the Item 222 comparison

At the phase $s_*=-(4h+3)/6$, Item 222 defines



$$
E_h^*={h\over4h+3}x_hv_h
       +{9(4h+1)\over2(4h+3)}u_hy_h.                         \tag{6.1}
$$



The observed ratio in (1.3) starts with



$$
\mathcal R_1=-{49\over18},\qquad
 \mathcal R_2={4235\over1944},                              \tag{6.2}
$$



and has step quotient



$$
\rho(h)={\mathcal R_{h+3}\over\mathcal R_h}
={h(4h+1)(4h+5)(4h+7)(4h+9)(4h+11)(4h+15)^2
 \over
864(h+1)(h+2)(2h+1)^2(2h+3)(2h+5)^2(4h+3)}.                 \tag{6.3}
$$



Combining (1.2) with the proposed gauge gives one precise target:



$$
\boxed{
 \sum_{k=0}^3p_k(h)
 \left(\prod_{j=0}^{k-1}\rho(h+3j)\right)E_{h+3k}^*=0.
 }                                                            \tag{6.4}
$$



If (6.4) is proved, the six already verified initial identities — three
in each of $h\equiv1,2\pmod3$ — and $p_3(h)\ne0$ prove (1.3) for all
admissible $h$.

The sums in (6.1) have a rigorous proper-hypergeometric formulation.  For
a polynomial $K$, let



$$
O_K(t)=\sum_j(-1)^jK_{2j+1}t^j,\qquad
 V_K(t)=\sum_j(-1)^jK_{2j}t^j,                              \tag{6.5}
$$



and define the normalized beta functional



$$
\mathfrak B_{\alpha,\beta}(t^j)={ (\alpha)_j\over
                                      (\alpha+\beta)_j}.      \tag{6.6}
$$



For $K_0=(1-z)^{2h}(1+z)$ and
$K_1=(1-z)^{2h}(1+z)^4$, the four factors in (6.1) are exactly



$$
\begin{aligned}
x_h&=\mathfrak B_{s_*+1,\,2s_*+1}(O_{K_0}),&
y_h&=\mathfrak B_{h+1,\,2s_*+1}(O_{K_0}),\\
u_h&=\mathfrak B_{s_*,\,2s_*}(V_{K_1}),&
v_h&=\mathfrak B_{h+1,\,2s_*}(O_{K_1}).                      \tag{6.7}
\end{aligned}
$$



Moreover, for $e=1,4$,



$$
[z^m](1-z)^{2h}(1+z)^e=(-1)^m{2h\choose m}
 \sum_{a=0}^e(-1)^a{e\choose a}
 {m^{\underline a}\over(2h-m+1)_a}.                         \tag{6.8}
$$



Thus the left side of (6.4) is a definite double sum of proper
hypergeometric terms.  A rational bivariate WZ/Hermite divergence
certificate would prove it, but no such certificate is present in this
package.  Exact modular checks of (6.4) cover all admissible
$h\leq220$ modulo both 1000000007 and 1009999999, with no failures.
Those 294 congruence rows are **EXACT FINITE ONLY**.

This is the precise current barrier: the recurrence for $c_h^*$ is
proved; its proposed gauge-conjugate recurrence for $E_h^*$ is not.

## 7. Comparison with the remaining endpoint scalar

Let $K_h$ denote Item 231's natural endpoint eliminant.  A simple
first-order hypergeometric quotient $K_h/E_h^*$ could have supplied a
second localization.  Fix a residue $r\in\{1,2\}$, write $h=3n+r$,
and consider



$$
A(n){K_{h+3}\over E_{h+3}^*}
 +B(n){K_h\over E_h^*}=0,\qquad \deg A,\deg B\leq5.          \tag{7.1}
$$



After clearing the two $E$-denominators, evaluate exact rational rows
modulo 1000000007.  The columns are



$$
n^dK_{h+3}E_h^*,\qquad n^dK_hE_{h+3}^*,\qquad0\leq d\leq5.  \tag{7.2}
$$



The resulting ranks are



$$
\begin{array}{c|c|c|c}
r&\text{rows}&\text{columns}&\text{rank}\\ \hline
1&13&12&12\\
2&12&12&12.
\end{array}                                                   \tag{7.3}
$$



Every sampled denominator is nonzero modulo the prime.  If a rational
identity (7.1) existed, clearing coefficient denominators and dividing by
their gcd would give a primitive integer null vector.  Its reduction
modulo the displayed prime would be nonzero, contradicting (7.3).  Hence
(7.1) is rigorously excluded in the stated degree bound.

This says nothing about higher degree, higher order, non-rational gauges,
or a direct gcd theorem.  Separately, through the 27 admissible values
$h\leq40$, every prime factor remaining in the numerator of $E_h^*$
after removing its gcd with the numerator of $K_h$ is at most $4h+3$.
That attractive observation is **EXACT FINITE ONLY** and is not promoted
to an all-$h$ unit theorem.

## 8. Arithmetic and rate ledger

Algebraicity and P-recursiveness control the common residual as a sequence,
but do not prove that it is nonzero modulo the moving row prime
$p=6s+4h+3$.  Because (1.3) is still open, even replacing the Item 222
condition by $c_h^*\equiv0\pmod p$ is not yet justified uniformly.
And even after that replacement, the simultaneous endpoint condition
involving $K_h$ would remain.

Accordingly,



$$
\boxed{\text{new unconditional linear log rate}=0,\qquad
        \text{new divisibility exponent}=0.}                 \tag{8.1}
$$



No sparsity, density-zero, radical, or prime-avoidance conclusion is
inferred from the finite checks.

## 9. Reproducibility and labels

The companion checker uses only the Python standard library and the pinned
Item 222, 229, 231, and 236 certificates.  It verifies the rational
closed form, recomputes the resultant, proves the differential-operator
identity exactly, replays the finite (c/E) and gauged-recurrence checks,
and verifies the full-rank endpoint-ratio obstruction.  Canonical and
replay JSON are intended to be byte-identical.

Classification:

* **PROVED:** (1.1), (3.7), (4.2)--(4.4), the all-$h$ recurrence
  (1.2), and the bounded first-order $K/E$ no-go (7.1)--(7.3).
* **EXACT FINITE ONLY:** $c_h^*=\mathcal R_hE_h^*$ through $h\leq80$,
  (6.4) modulo two primes through $h\leq220$, and the $K/E$ gcd pattern
  through $h\leq40$.
* **OPEN:** an all-$h$ proof of (1.3) or (6.4), a unit-localized
  all-$h$ $K/E$ theorem, all-prime exclusion, and any positive Route-1
  rate or radical saving.
