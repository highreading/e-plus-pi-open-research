> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 261 — exact punctured cohomology on the $p\equiv1\pmod6$ phase

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain an actual ordinary-$j=2$ row with



$$
p\equiv1\pmod6,\qquad p=6m+2r+9,\qquad r\equiv5\pmod6.          \tag{1.1}
$$



Put



$$
q={p-1\over6},\qquad
 \delta={r+4\over3},\qquad m=q-\delta,\qquad
 n={p-1\over2}=3q,\qquad
 \epsilon=\left({2\over p}\right).                              \tag{1.2}
$$



Thus $\delta\ge3$ is odd.  Let



$$
F(x)={(1-x/2)^3\over x},\qquad
 w_\delta(x)={x^\delta\over1-x},                                 \tag{1.3}
$$



and define the punctured sextic moment



$$
T_\delta=\sum_{x\in\mathbf F_p^*\setminus\{1\}}
                 w_\delta(x)F(x)^q.                              \tag{1.4}
$$



Item 254's exact character split is



$$
H_m=\epsilon(2q+\delta+1)-T_\delta.      \tag{1.5}
$$



> **PROVED — exact birational elliptic localization.**  On the Kummer
> curve
> 

$$
> y^6=F(x),
>
$$


> put
> 

$$
> X={y^2\over1-x/2},\qquad Z=yX.
>
$$


> Then
> 

$$
> \boxed{x=X^{-3},\qquad Z^2=X^3-\frac12,}                       \tag{1.6}
>
$$


> and
> 

$$
> {dx\over y}=-3x\,{dX\over Z}.                                  \tag{1.7}
>
$$


> The omitted point $x=1$ becomes the six geometric points above
> $X^3=1$; none is silently discarded.

Define



$$
\mathcal D(R)=F R'+{5\over6}F'R,
 \qquad \mathcal D(R){dx\over y}=d(Ry^5).                        \tag{1.8}
$$



Put



$$
c_0=1,\qquad
 c_{j+1}=c_j{6j+1\over3j+2},\qquad
 K_\delta=\sum_{j=0}^{\delta-1}c_j,\qquad
 \Gamma_\delta=\sum_{j=0}^{\delta-1}c_{j+1}.                     \tag{1.9}
$$



> **PROVED — exact Hermite reduction with every pole retained.**  There
> is an explicit rational $P_\delta(x)$ such that
> 

$$
> \boxed{
> w_\delta{dx\over y}
> =\left(w_0-\Gamma_\delta x^{-1}\right){dx\over y}
>   +d(P_\delta y^5).}                                           \tag{1.10}
>
$$


> Here $K_\delta=B_\delta^{(1)}$ is exactly Item 254's fixed-cutoff
> coefficient.  All reduction denominators are $p$-units.

> **PROVED — exact finite-field endpoint correction.**  For
> 

$$
> \Lambda_p(f)=\sum_{x\in\mathbf F_p^*\setminus\{1\}}f(x)F(x)^q
>
$$


> and $0\le j<q$, set
> 

$$
> R_j={x^{j+1}\over(1-x/2)^2}.
>
$$


> Then
> 

$$
> \boxed{
> \Lambda_p(\mathcal D(R_j))
> =-{3h_{q-j+1}\over2(3j-1)}
>   -\epsilon\,{3j-1\over6}.}                                   \tag{1.11}
>
$$


> Thus the exact differential in (1.10) does not vanish under the
> finite-field sum.  The first term is the Laurent/Frobenius resonance;
> the second is exactly the omitted $x=1$ endpoint.

> **PROVED — bounded two-class finite normal form.**  Put
> 

$$
> U_p=\Lambda_p(x^{-1}),\qquad V_p=\Lambda_p((1-x)^{-1}).
>
$$


> Then
> 

$$
> \boxed{
> U_p=-{h_q\over5}-\epsilon,\qquad
> V_p=-H_q+{2\epsilon\over3},}                                  \tag{1.12}
>
$$


> and
> 

$$
> \boxed{
> T_\delta=V_p-5K_\delta U_p
>                 +\epsilon(\delta-5K_\delta).}                  \tag{1.13}
>
$$


> Consequently
> 

$$
> \boxed{H_{q-\delta}=H_q-K_\delta h_q\pmod p.}                  \tag{1.14}
>
$$


> The cohomological reduction recovers, but does not improve, Item 254's
> fixed-cutoff collision $H_q/h_q=K_\delta$.

> **PROVED — the surviving Item-251 period uses the same two coordinates.**
> Define the fixed rational
> 

$$
> \Pi_r=\sum_{k=1}^{r+2}2^{-k}
>          {(1/3-\delta)_k\over(1/2)_k},\qquad
> D_r=K_\delta+c_\delta\Pi_r.                                   \tag{1.15}
>
$$


> Then Item 251's integer period is
> 

$$
> \boxed{
> A_s=(-1)^m\{\epsilon[H_q-D_rh_q]-1\}\pmod p.}                  \tag{1.16}
>
$$


> Substitution into Item 251's exact formula for $Z$, and then into
> $G_\nu=f_\nu Z+U_\nu$, expresses the full rank-aware affine gate in
> the same bounded pair $(H_q,h_q)$, together with already explicit
> fixed-$r$ coefficients.  It does not remove the separate
> $f_0=f_1=0$ branch.

> **PROVED, SHARPLY SCOPED NO-GO — compact elliptic trace data do not close
> the puncture.**  Under (1.6),
> 

$$
> w_0{dx\over y}=-{3\,dX\over(X^3-1)Z},\qquad
> x^{-1}{dx\over y}=-{3\,dX\over Z}.                             \tag{1.17}
>
$$


> At $(\alpha,\beta)$, where $\alpha^3=1$ and
> $\beta^2=1/2$,
> 

$$
> \boxed{\operatorname {Res}_{(\alpha,\beta)}
> \left(-{3\,dX\over(X^3-1)Z}\right)=-{\alpha\over\beta}\ne0.}   \tag{1.18}
>
$$


> Exact differentials and compact $H^1(E)$ classes have zero residues.
> Hence even the full unpunctured elliptic Frobenius data cannot replace
> the logarithmic coordinate $V_p$.

> **NO ALL-PRIME EXCLUSION / ZERO BOOKING.**  The actual
> $p\equiv1\pmod6$ row
> 

$$
> (p,r,s,m,\delta)=(43,11,3,2,5)                                \tag{1.19}
>
$$


> has $H_m=0\pmod p$.  No weighted zero theorem for the moving
> positive-mass cell follows.  Item 261 therefore books
> 

$$
> \boxed{\text{new unconditional Route-1 rate}=0,\qquad
>        \text{new \(j=2\) capacity reduction}=0.}               \tag{1.20}
>
$$



Every bounded scan in the checker is **EXACT FINITE ONLY**.

## 2. Birational transport and punctures

Let $A=1-x/2$.  From $X=y^2/A$,



$$
X^3={y^6\over A^3}={1\over x}.
$$



Also $y^2=XA$, so



$$
Z^2=y^2X^2=X^3A=X^3-\frac12.
$$



Since $y=Z/X$ and $x=X^{-3}$, differentiation gives (1.7).
Consequently



$$
w_\delta{dx\over y}
 =-3{x^{\delta+1}\over1-x}{dX\over Z}.                          \tag{2.1}
$$



The branch point $x=2$ maps to a regular point of the smooth curve.
Although the rational primitives below contain $A^{-2}$, the product
$y^5/A^2$ is regular there: with $y$ as local parameter, $A$ has
order two and $y^5/A^2$ has order one.  The excluded $x=0$ is retained
as the Laurent endpoint, while $x=1$ produces the logarithmic poles at
$X^3=1$.

## 3. Exact Hermite reduction

Differentiation of $y^6=F$ gives



$$
d(Ry^5)=\left(FR'+{5\over6}F'R\right){dx\over y}.               \tag{3.1}
$$



For



$$
R_j={x^{j+1}\over(1-x/2)^2},
$$



direct simplification yields



$$
\boxed{
 \mathcal D(R_j)
 ={6j+1\over6}x^{j-1}-{3j+2\over6}x^j.}                         \tag{3.2}
$$



Thus, with $a_j=(6j+1)/(3j+2)$,



$$
x^j=a_jx^{j-1}-{6\over3j+2}\mathcal D(R_j).                    \tag{3.3}
$$



Set $P_{-1}=0$ and define



$$
P_j=a_jP_{j-1}+{6\over3j+2}R_j.                                \tag{3.4}
$$



Induction gives



$$
\mathcal D(P_j)=c_{j+1}x^{-1}-x^j.                             \tag{3.5}
$$



The elementary punctured partial fraction is



$$
{x^\delta\over1-x}={1\over1-x}-\sum_{j=0}^{\delta-1}x^j.       \tag{3.6}
$$



Summing (3.5), and writing $P_\delta=\sum_{j<\delta}P_j$, proves
(1.10).  This is a coefficientwise identity over $\mathbf Q(x,y)$;
no finite-field sample enters.

For actual $0\le j<\delta$,



$$
3j+2\le r+3<p,\qquad
 6j+1\le2r+3<p,\qquad
 |3j-1|\le r<p.                                                  \tag{3.7}
$$



Thus every scalar denominator in the Hermite and endpoint reductions is
a $p$-unit.  The branch denominators are handled geometrically as above.

Under the elliptic transport,



$$
x^{-1}{dx\over y}=-3{dX\over Z},
$$



which is holomorphic, while $w_0dx/y$ is the logarithmic form in
(1.17).  Hence (1.10) is a two-class cohomological normal form for the
entire fixed-$r$ weight family.

## 4. Why the exact differential contributes

Because $q+1\equiv5/6\pmod p$,



$$
\mathcal D(R_j)F^q={d\over dx}\{R_jF^{q+1}\}.                   \tag{4.1}
$$



Moreover



$$
R_jF^{q+1}=x^{j-q}(1-x/2)^{n+1}.                               \tag{4.2}
$$



In its Laurent expansion, the only differentiated exponent whose sum on
$\mathbf F_p^*$ survives is the term before differentiation with
exponent one.  Its coefficient is



$$
C_j=\binom{n+1}{q-j+1}\left(-{1\over2}\right)^{q-j+1}
 ={3h_{q-j+1}\over2(3j-1)}.                                    \tag{4.3}
$$



Therefore the sum over all $x\in\mathbf F_p^*$ is $-C_j$.
At the omitted point $x=1$,



$$
F(1)^q=\epsilon,\qquad
 \mathcal D(R_j)(1)={3j-1\over6}.                               \tag{4.4}
$$



Subtracting (4.4) proves (1.11).  The point $x=2$ contributes zero
because $F(2)^q=0$; the excluded Laurent point $x=0$ is already
accounted for by the power-sum calculation.  Thus every boundary and
puncture has been retained.

Applying $\Lambda_p$ to (1.10) gives



$$
T_\delta=V_p-\Gamma_\delta U_p+E_\delta,                       \tag{4.5}
$$



where the summed exact-form defect is



$$
\boxed{
 E_\delta=(\Gamma_\delta-5K_\delta)U_p
                 +\epsilon(\delta-5K_\delta).}                  \tag{4.6}
$$



Equations (4.5)–(4.6) give (1.13).  Dropping $E_\delta$ would replace
the original finite-field sum by a different object.

## 5. Evaluation of the two residual coordinates

For $0\le j\le q$, multiplicative power orthogonality gives



$$
\sum_{x\in\mathbf F_p^*}x^jF(x)^q=-h_{q-j}.                     \tag{5.1}
$$



Indeed



$$
F(x)^q=x^{-q}(1-x/2)^{3q}
       =\sum_{\ell=0}^{3q}h_\ell x^{\ell-q},
$$



and $\ell=q-j$ is the unique exponent-zero term in the phase range.
At $x=1$, $F(1)^q=2^{-3q}=\epsilon$.  Therefore



$$
U_p=-h_{q+1}-\epsilon.                                         \tag{5.2}
$$



At $p=6q+1$,



$$
{h_{q+1}\over h_q}={2q+1\over4q+4}\equiv{1\over5}\pmod p,      \tag{5.3}
$$



proving the first formula in (1.12).

The $m=q$ instance of Item 254's exact Jacobi split gives



$$
H_q=-V_p+\epsilon(2q+1).
$$



Since $2q+1\equiv2/3\pmod p$, this proves the second formula in
(1.12).

Alternatively, the elementary identity



$$
{x^\delta\over1-x}={1\over1-x}-\sum_{j<\delta}x^j
$$



with (5.1) gives directly



$$
T_\delta=V_p+K_\delta h_q+\delta\epsilon.                       \tag{5.4}
$$



Equations (1.5), (1.12), and (5.4) prove (1.13)–(1.14).

## 6. The full Item-251 period and affine gate

Item 251 uses



$$
P_{r+2}(m)=\sum_{k=1}^{r+2}2^{-k}
 { (m+1/2)_k\over(1/2)_k}.                                      \tag{6.1}
$$



On the present phase,



$$
m=q-\delta\equiv-\frac16-\delta\pmod p,
$$



so



$$
P_{r+2}(m)\equiv\Pi_r
 =\sum_{k=1}^{r+2}2^{-k}
 { (1/3-\delta)_k\over(1/2)_k}\pmod p.                          \tag{6.2}
$$



Also



$$
h_m=c_\delta h_q.                                               \tag{6.3}
$$



Combining (1.14), (6.2), and (6.3) proves (1.16).
Every denominator is a unit: the odd factors in $(1/2)_k$ are at most
$2r+3<p$, and only powers of $2$ and $3$ are otherwise introduced.

For completeness, Item 251's remaining coordinate is



$$
Z=B_s\left({9\kappa_r\over2}A_s-\tau_{r,s}\right),              \tag{6.4}
$$



and the gate rows are $G_\nu=f_\nu Z+U_\nu$.  Substitution of (1.16)
therefore gives an exact two-period formula for each $G_\nu$.  On the
rank-one eliminant, one nonzero $f_\nu$ still gives the Item-251 affine
target; if $f_0=f_1=0$, the correct branch remains $U_0=U_1=0$.
No division by a possibly zero gate coefficient is introduced here.

## 7. The surviving logarithmic class

At $X=\alpha$, where $\alpha^3=1$,



$$
X^3-1=3\alpha^2(X-\alpha)+O((X-\alpha)^2).
$$



At either point $Z=\beta$, $\beta^2=1/2$, the residue is



$$
-{3\over3\alpha^2\beta}
 =-{1\over\alpha^2\beta}
 =-{\alpha\over\beta}\ne0.                                     \tag{7.1}
$$



Thus the logarithmic class cannot be exact or lie in compact
$H^1(E)$.  The ordinary $j=0$ elliptic trace, or even the full compact
Frobenius matrix, controls a different quotient.  The bounded reduction
is real, but it is a bounded **punctured** two-state reduction; it is not
an evaluation by the scalar CM trace.

## 8. Recurrences, zeros, and rate

Normalize the base puncture period by



$$
Z_q={H_q\over h_q}.
$$



The prefix recurrence gives



$$
\boxed{Z_{q+1}=1+{4q+4\over2q+1}Z_q,\qquad Z_0=1.}              \tag{8.1}
$$



The boundary coefficients obey



$$
c_{j+1}=c_j{6j+1\over3j+2},\qquad
 K_{\delta+1}=K_\delta+c_\delta.                                \tag{8.2}
$$



Thus the $r$-dependence and the punctured state are fixed-order.
However, successive $q$'s in (8.1) use different row primes
$p=6q+1$; the recurrence cannot propagate a modular nonzero value from
one prime to the next.

Every prefix zero is the fixed-rational collision



$$
Z_q=K_\delta\pmod p.                                            \tag{8.3}
$$



The exact row (1.19) disproves a uniform all-prime exclusion.  At global
Item-219 index $M$, a single fixed $r$ ray has only
$O(\log M)=o(M)$ raw prime weight, but this is the previously frozen
fixed-ray geometry.  The positive-mass cell has linearly many moving
$r$'s, so it cannot be summed as a new capacity saving.

No all-prime exclusion, uniform zero-density theorem, or positive-mass
weighted theorem follows from (8.1)–(8.3).  The booking is zero.

## 9. Exact replay and strict labels

The standard-library checker performs:

* $67$ coefficientwise rational Hermite reductions with explicit
  primitives and fixed Item-251 tail coefficients;
* all $p\equiv1\pmod6$ residual-coordinate identities through
  $p\le401$;
* $1{,}150$ exact endpoint summation-by-parts identities;
* $548$ actual rows, $2{,}740$ localized row equalities, and
  $1{,}644$ Item-251 period equalities;
* an **EXACT FINITE ONLY** zero census finding the three prefix-zero rows
  

$$
(43,11,3,2,5),\quad(193,29,22,21,11),\quad
  (241,89,10,9,31)
$$


  in $(p,r,s,m,\delta)$ order.

### PROVED

* the Kummer-to-elliptic transport and complete puncture set;
* the exact Hermite identity (1.10) and unit ranges;
* the endpoint lemma (1.11) and summed correction (4.6);
* the bounded residual coordinates (1.12)–(1.14);
* the full Item-251 period reduction (1.15)–(1.16);
* the nonzero-residue obstruction (1.18);
* the recurrence statements and zero booking.

### EXACT FINITE ONLY

* every bounded prime count, row count, zero count, and digest.

### OPEN

* all-prime or weighted control of $H_q/h_q$;
* a genuinely arithmetic theorem for the logarithmic puncture class;
* a uniform theorem when $r$ moves through the positive-mass cell;
* any new Route-1 capacity or conclusion about $e+\pi$.

Accordingly,



$$
\boxed{\text{new unconditional linear-log rate}=0,\qquad
        \text{capacity reduction}=0.}                            \tag{9.1}
$$


