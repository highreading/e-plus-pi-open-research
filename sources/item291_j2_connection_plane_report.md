> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 291 — the ordinary-$j=2$ connection plane and exact row-rank drop

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain the Item-250 ordinary cell



$$
p=2r+6s+3,\qquad r=2h+1\geq1,\qquad Q=2s,
 \tag{1.1}
$$



and write its affine $A$-tail coordinates as



$$
X_\nu=a_\nu e+b_\nu c+d_\nu,\qquad c=2^Q.
 \tag{1.2}
$$



Let $Y_\nu$ denote Item 250's **lower $B$-tail**.  Thus



$$
P_\nu^\flat=9b_\nu,\qquad
 H_\nu^\flat=9d_\nu-10Y_\nu.             \tag{1.3}
$$



The distinction between $Y_\nu$ and $b_\nu$ is essential.

> **PROVED — exact lower-tail collapse.**  For both $\nu=0,1$,
> term by term on every admissible $r$,
> 

$$
>                         \boxed{Y_\nu=2d_\nu},\qquad
>                         \boxed{H_\nu^\flat=-11d_\nu}.
> \tag{1.4}
>
$$



Put $f=(f_0,f_1)^{\mathsf T}$,
$b=(b_0,b_1)^{\mathsf T}$, and
$d=(d_0,d_1)^{\mathsf T}$.  Then the Item-250 determinant is



$$
\begin{aligned}
 D&=f_0U_1-f_1U_0,\qquad U_\nu=9cb_\nu-11d_\nu,\\
  &=9c\,\det(f,b)-11\,\det(f,d).
\end{aligned}                                                   \tag{1.5}
$$



> **PROVED — complete actual-row rank stratification.**  In Item 272's
> row matrix $R$, the coordinate $z_1$ is a $p$-unit on every
> actual row.  Consequently
> 

$$
>       \operatorname{rank}_{\mathbb F_p}R=2
>       \quad\Longleftrightarrow\quad D\ne0\pmod p.       \tag{1.6}
>
$$


> On $D=0$, the rank is one unless $f_0=f_1=U_0=U_1=0$,
> when it is zero.

Every common collision implies $D=0$.  The converse is false in
general: $D=0$ is row-rank drop, not the remaining incidence with
$x_p=(1,H_q,h_q)^{\mathsf T}$.

An order-three, degree-seventeen operator shared by
$L_n=9\det(f,b)$ and $16^nM_n$,
$M_n=-11\det(f,d)$, has been reconstructed exactly and passes the
bounded modular replays in Section 6.  It has **no all-$n$ symbolic
certificate**.  It is therefore labelled **EXACT FINITE ONLY / EXPERIMENTAL**,
not a proved translation module.

No new divisor, Frobenius realization, zero-density theorem, or capacity
reduction follows.  The retained ordinary-$j=2$ ceiling remains



$$
\boxed{\frac{2}{35}\text{ per }M
 =\frac1{105}\text{ per }6M},\qquad
 \boxed{\text{new Route-1 booking}=0}.                    \tag{1.7}
$$



## 2. The odd homogeneous chain

At the phase



$$
\bar Q=-\frac{2r+3}{3},\qquad
 n_a=r+\bar Q+1=\frac r3,                              \tag{2.1}
$$



let $w_t$ be the constant coordinate of $J_{2t+1}$.  The
Item-250 affine recurrence gives



$$
\frac{w_{t+1}}{w_t}
 =-\frac{\bar Q+1+2t}{3\bar Q+1+2t}
 =\frac{r/3-t}{t-r-1}=:A_t.                              \tag{2.2}
$$



All denominators in the ranges below were already audited in Item 250.
The present proof never crosses their first zero.

For $\nu=1$, the lower-tail hypergeometric weight has the same
successive ratio:



$$
\frac{W_{1,t+1}}{W_{1,t}}
 =\frac{n_a-t}{t-r-1}=A_t.                              \tag{2.3}
$$



For $\nu=0$, put $S_t=w_t+w_{t+1}$.  Since



$$
1+A_t=-\frac{2r+3}{3(t-r-1)},                           \tag{2.4}
$$



one obtains



$$
\frac{S_{t+1}}{S_t}
 =A_t\frac{1+A_{t+1}}{1+A_t}
 =\frac{r/3-t}{t-r}
 =\frac{W_{0,t+1}}{W_{0,t}}.                            \tag{2.5}
$$



These are rational identities in $\mathbb Q(r,t)$, not fitted
equalities.

## 3. The two base constants

Use Item 250's notation



$$
\begin{aligned}
 C_{a,0}&=-\frac{r!}{(\bar Q+1)_{r+1}},\\
 C_{a,1}&=\frac{(r+1)!}{(\bar Q)_{r+2}},
\end{aligned}                                                   \tag{3.1}
$$



and let $\beta=w_0$.  Backward propagation from the sole
Frobenius terminal gives a product over the odd pivots.  After inserting
$\bar Q$, its comparison with $C_{a,1}$ reduces to



$$
\prod_{j=0}^{r+1}(3j-2r-3)
 =-\prod_{i=0}^{r+1}(3i-r).                              \tag{3.2}
$$



Indeed $j=r+1-i$ sends each factor on the left to the negative of
the corresponding factor on the right, and $r+2$ is odd.  Thus



$$
C_{a,1}=2\beta.                  \tag{3.3}
$$



Also



$$
\frac{C_{a,0}}{C_{a,1}}
 =-\frac{\bar Q}{r+1}
 =\frac{2r+3}{3(r+1)}=1+A_0.                            \tag{3.4}
$$



Equations (2.3) and (3.3) prove, term by term,



$$
C_{a,1}W_{1,t}=2w_t.                                      \tag{3.5}
$$



Equations (2.5) and (3.3)--(3.4) similarly prove



$$
C_{a,0}W_{0,t}=2(w_t+w_{t+1}).                            \tag{3.6}
$$



Multiplying by the respective coefficients of
$(1-z)^r(1+z)^4$ and $(1-z)^r(1+z)$, then summing, gives
$Y_1=2d_1$ and $Y_0=2d_0$.  This proves (1.4), including
the endpoint $r=1$.

## 4. Connection-plane determinant

Item 250 proved $a_\nu=\kappa_rf_\nu$.  With (1.4), the two
localized rows are



$$
G_\nu=f_\nu Z+9cb_\nu-11d_\nu.                  \tag{4.1}
$$



Eliminating $Z$ without division gives



$$
f_0G_1-f_1G_0
 =9c(f_0b_1-f_1b_0)-11(f_0d_1-f_1d_0)=D.                 \tag{4.2}
$$



Thus the old Item-250 compatibility determinant is the displayed linear
combination of two connection-plane minors.  This is a structural
simplification of the existing necessary condition, not a new necessary
divisor.

## 5. Exact row rank and every chart

Retain Item 272's row vector $z=(z_0,z_1,z_2)$ and set
$U=(U_0,U_1)^{\mathsf T}$.  The three columns of $R$ are



$$
z_0f+U,\qquad z_1f,\qquad z_2f.                    \tag{5.1}
$$



Hence its minors are exactly



$$
\Delta_{01}=-z_1D,\qquad
 \Delta_{02}=-z_2D,\qquad
 \Delta_{12}=0.                                      \tag{5.2}
$$



Now



$$
z_1=B_s\frac{9\kappa_r}{2}\sigma_m\epsilon.           \tag{5.3}
$$



The factorials in $B_s$ are below $p$.  In the numerator of
$\kappa_r$, the raw rising factors are



$$
6-r+6i,\qquad 0\leq i<h.                           \tag{5.4}
$$



They are nonzero because $r$ is odd, and they lie between
$6-r$ and $2r-3$, while $p>2r+3$.  The remaining
numerator $2r+3$, all denominator factors, and the constants
$2,3$ are $p$-units by the Item-250 range audit.  Therefore
$z_1$ is a unit.

It follows from (5.2) that $D\ne0$ is equivalent to rank two.  If
$D=0$ and $f\ne0$, the rows are proportional but nonzero because
their $z_1f$ column is nonzero, so the rank is one.  If $f=0$,
then $R=(U,0,0)$, giving rank one for $U\ne0$ and rank zero
for $U=0$.

For the collision itself:

* if $f\ne0$, then $D=0$ plus one residual
  $f_\nu Z+U_\nu=0$ with $f_\nu\ne0$ is necessary and sufficient;
* if $f=0$, the condition is $U_0=U_1=0$.

Thus rank drop alone never replaces the actual period incidence.

## 6. Experimental order-three reconstruction

For phase $e=5$, put $r=1+6n$; for phase $e=1$, put
$r=5+6n$.  Define



$$
L_n=9\,\det(f,b),\qquad M_n=-11\,\det(f,d).          \tag{6.1}
$$



The certificate stores four explicit degree-seventeen polynomials
$P_0,\ldots,P_3$ for each phase.  On each recorded finite prefix it
checks



$$
\sum_{j=0}^3P_j(n)L_{n+j}=0,\qquad
 \sum_{j=0}^3P_j(n)16^{n+j}M_{n+j}=0                 \tag{6.2}
$$



modulo both $1000000007$ and $1000000009$.  Equivalently, the
candidate operator for $M$ has coefficients
$P_j/16^{3-j}$, up to a common scalar.

The recorded finite experiment uses exactly 82 terms in each phase and
checks the 79 recurrence rows $0\leq n\leq78$ for each sequence and
each certificate prime.

The same matrices have full rank in the two smaller rectangles:

* order at most two, coefficient degree at most seventeen;
* order at most three, coefficient degree at most sixteen.

Those two bounded-class exclusions are proved: after clearing a putative
rational relation to a primitive integer vector, its reduction cannot
vanish at either certificate prime, contradicting full column rank.

The positive order-three relation is different.  Finite agreement does
not prove it for all $n$.  No WZ numerator, Hermite reduction, de-Rham
certificate, or annihilating-operator identity is present.  Therefore
(6.2), including the attractive consequence



$$
16^nD_n=c_0L_n+16^nM_n\qquad(c_n=c_0/16^n),             \tag{6.3}
$$



remains **EXACT FINITE ONLY / EXPERIMENTAL** as a rank-three closure.

## 7. Admission and capacity

The proved output is an exact simplification and rank stratification of
the already known Item-250 compatibility condition.  It supplies no new
integer divisor.  Even a future all-$n$ proof of (6.2) would be only a
translation-difference recurrence; by itself it would not provide:

* a Frobenius or compatible lisse/crystalline realization;
* nontrivial monodromy and auxiliary-prime independence;
* all-prime nonvanishing of $D$; or
* a weighted zero-density theorem for the actual tied prime family.

Accordingly the master admission test fails at the density step, and no
part of the raw $2/35$-per-$M$ cell is removed.

## 8. Reproduction and strict labels

From the portable archive root:

~~~
python scripts/item291_j2_connection_plane_certificate.py \
  --output results/item291_j2_connection_plane_certificate.json
python scripts/item291_j2_connection_plane_certificate.py \
  --output results/item291_j2_connection_plane_certificate_replay.json
~~~

### PROVED

* The termwise identities $Y_\nu=2d_\nu$ and
  $H_\nu^\flat=-11d_\nu$, including $r=1$.
* The connection-minor formula (1.5).
* The all-row $z_1$-unit audit and complete rank stratification.
* Collision implies $D=0$, with the rank-one and rank-zero charts
  retained separately.
* The two explicitly bounded recurrence-class exclusions in Section 6.

### EXACT FINITE ONLY / EXPERIMENTAL

* The order-three, degree-seventeen candidate and the
  $L_n$/$16^nM_n$ conjugacy.
* The bounded phase, termwise, rank, and modular replays at the recorded
  bounds.

### OPEN

* An all-$n$ symbolic certificate for the reconstructed operator.
* A complete bounded-rank update for $W=(f_0,f_1,U_0,U_1)$.
* Any all-prime or weighted-density theorem for $D=0$.
* Any capacity reduction, Route-1 completion, or conclusion about
  $e+\pi$.

