> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 314 — the fully cleared ordinary-$j=2$ two-branch gate

Checked: 2026-08-31 (Beijing time)

## 1. Scope and strict verdict

Retain the actual ordinary-$j=2$ rows



$$
r=6n+e,\qquad e\in\{1,5\},\qquad
 p=2r+6s+3\ {\rm prime},\qquad s\geq1,
$$



and put



$$
c=2^{2s},\qquad D_{r,s}=cL_r+M_r.
$$



Items 306 and 309 proved the two separate algebraic-branch bridges.
This item combines them and performs the modular clearing that Item 309
left open.

> **PROVED — universal $18:11$ gate.**  There are rational
> coefficients $a_r$ on the $y=-1$ branch and
> $b_r=[x^r]C_+(x)$ on the $y=0$ branch such that, on both rays and
> for every $n\geq0$,
> 

$$
> D_{r,s}=\frac{g_n\kappa_e}{16^n}
>          \bigl(18c\,a_r+11b_r\bigr).
> \tag{1.1}
>
$$


> The factor outside the parentheses is a $p$-unit on **every**
> actual row.

> **PROVED — global integer clearing and all six modular layers.**  If
> 

$$
> G_{r,s}=18c\,a_r+11b_r,\qquad
> H_r=6^{r+3}r!,
> \tag{1.2}
>
$$


> then $H_ra_r,H_rb_r,H_rG_{r,s}\in\mathbb Z$, while $p\nmid H_r$.
> Consequently
> 

$$
> \boxed{
> D_{r,s}\equiv0\pmod p
> \iff G_{r,s}\equiv0\pmod p
> \iff H_rG_{r,s}\equiv0\pmod p}
> \tag{1.3}
>
$$


> for all actual rows, including the six forward-recurrence singular
> layers $s=1,\ldots,6$.

> **PROVED — the endpoint norm is not new.**  The cubic endpoint norm
> forced by (1.3) is exactly Item 250's old resultant, up to the
> $p$-unit cube in (1.1).  Norming the algebraic generating functions
> themselves does not yield a same-index coefficient divisor.

The new theorem removes the modular-gauge ambiguity in the full
two-branch gate.  It does **not** prove weighted zero density:



$$
\boxed{\text{new booking}=0},\qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling remains }1/105\text{ per }6M}.
$$



## 2. The two bridges collapse to one universal ratio

Write Item 309's second-branch coefficient as



$$
\mathcal A(X)=\sum_{r\geq0}a_rX^r,
$$



and Item 237's original branch as



$$
C_+(x)=\sum_{r\geq0}b_rx^r.
$$



Items 309 and 306 respectively give



$$
\frac{16^nL_r}{g_n}=\mu_ea_r,\qquad
 \frac{16^nM_r}{g_n}=\lambda_eb_r,
\tag{2.1}
$$



with



$$
\begin{array}{c|c|c}
e&\mu_e&\lambda_e\\ \hline
1&-729/50&-891/100\\
5&6377292/41405&3897234/41405.
\end{array}
$$



The four constants have the exact common factorization



$$
\mu_e=18\kappa_e,\qquad \lambda_e=11\kappa_e,
\tag{2.2}
$$



where



$$
\kappa_1=-\frac{81}{100},\qquad
 \kappa_5=\frac{354294}{41405}
          =\frac{2\cdot3^{11}}{5\cdot7^2\cdot13^2}.
\tag{2.3}
$$



Substitution into $D=cL+M$ proves (1.1).  The $18:11$ ratio is
therefore symbolic and residue-independent; it is not a fitted pattern.

## 3. Explicit coefficient extraction and integer clearing

For the $y=0$ branch, retain



$$
Q(y)=1+y+\frac{y^2}{2},\qquad
 x=\frac{y(1+y)}{Q(y)^{2/3}},
$$



and Item 237's rational parametrization



$$
C_+(x(y))=\frac{N(y)}{E_+(y)^3},\qquad
 E_+(y)=2y^3+7y^2+14y+6.
$$



For the $y=-1$ branch, Item 309 gives



$$
X=\frac{z(1-z)}{(1+z^2)^{2/3}},
\qquad
 \mathcal A(X(z))=
 \frac{6(1+z^2)^2(8z^3+25z^2-24z+9)}
 {(2z^3+z^2+6z-3)^3}.
\tag{3.1}
$$



Put



$$
\begin{aligned}
E_-(z)&=2z^3+z^2+6z-3,\\
P_-(z)&=16z^6+55z^5-199z^4+278z^3-42z^2-33z+45,\\
P_+(y)&=16y^6+151y^5+316y^4+352y^3
        +388y^2+292y+120.
\end{aligned}
$$



Direct differentiation gives the two exact factorizations



$$
\begin{aligned}
\mathcal A'(z)
 &=-12\,\frac{(z+1)(z^2+1)P_-(z)}{E_-(z)^4},\\
C_+'(y)
 &=-12\,\frac{(y+2)(y^2+2y+2)P_+(y)}{E_+(y)^4}.
\end{aligned}
\tag{3.2}
$$



Lagrange inversion now gives



$$
\begin{aligned}
a_r&=\frac1r[z^{r-1}]\mathcal A'(z)
 \left(\frac{(1+z^2)^{2/3}}{1-z}\right)^r,\\
b_r&=\frac1r[y^{r-1}]C_+'(y)
 \left(\frac{Q(y)^{2/3}}{1+y}\right)^r.
\end{aligned}
\tag{3.3}
$$



Thus the full gate has the single explicit, locally integral extraction



$$
\boxed{
\begin{aligned}
rG_{r,s}=-12\Bigg\{&
18c[z^{r-1}]
\frac{(z+1)(z^2+1)P_-(z)}{E_-(z)^4}
\frac{(1+z^2)^{2r/3}}{(1-z)^r}\\
&+11[y^{r-1}]
\frac{(y+2)(y^2+2y+2)P_+(y)}{E_+(y)^4}
\frac{Q(y)^{2r/3}}{(1+y)^r}
\Bigg\}.
\end{aligned}}
\tag{3.4}
$$



There is also a uniform global integer clearer.  Through degree $d$,
the coefficients of either inverse fourth power in (3.4) have
denominator dividing $6^{d+4}$.  The degree-$d$ coefficients of
either generalized $2r/3$-power have denominator dividing
$6^d d!$.  The two negative integral powers in (3.4) have integral
coefficients.  Therefore the coefficient at degree $r-1$, followed by
Lagrange's factor $1/r$, has denominator dividing



$$
H_r=6^{r+3}r!.
\tag{3.5}
$$



This proves $H_ra_r,H_rb_r\in\mathbb Z$, hence
$H_rG_{r,s}\in\mathbb Z$.  Formula (3.5) is deliberately a safe
uniform clearer, not a claim of minimal denominator.

## 4. The all-row $p$-unit theorem

Item 294's gauge is normalized by $g_0=1$ and



$$
\frac{g_n}{g_{n+1}}=\mathcal R(r),\qquad
 \mathcal R(t)=
 \frac{t(t+6)(2t+9)^2(2t+15)^2}
 {78732(t+1)^2(t+2)(t+4)(t+5)^2}.
\tag{4.1}
$$



The value $g_n$ uses only the past steps:



$$
g_n=\prod_{j=0}^{n-1}\frac1{\mathcal R(e+6j)}.
\tag{4.2}
$$



For every factor in (4.2), $t=e+6j\leq r-6$.  Hence the largest
positive linear factor is



$$
2t+15\leq2r+3<p.
\tag{4.3}
$$



All other displayed positive factors are smaller, and
$78732=2^2 3^9$.  Thus $g_n$ is a $p$-unit; for $n=0$ this is
the identity $g_0=1$.

The constants $\kappa_e$ are also $p$-units.  On the $e=1$ ray,
the smallest actual prime is at least $11$; on the $e=5$ ray it is
at least $19$.  Formula (2.3) therefore has no actual prime in its
numerator or denominator.

Finally $p>2r+3>r$ and $p>3$.  Consequently $p\nmid H_r$, and
(3.5) proves that both branch coefficients are $p$-integral.
The scale $g_n\kappa_e/16^n$ in (1.1) is a unit, proving (1.3).

### The six apparent singular layers

The forward coefficient of the order-three recurrence has the six
structural possibilities



$$
\begin{array}{c|c}
s&\text{factor equal to }p\\ \hline
1&2r+9\\
2&2r+15\\
3&2r+21\\
4&2r+27\\
5&2r+33\\
6&2r+39.
\end{array}
\tag{4.4}
$$



These factors occur at the **current forward step**.  They do not occur
in the past-step product (4.2), whose largest corresponding numerator
factor is only $2r+3$.  The proof of (1.3) evaluates the already-proved
characteristic-zero bridge directly and never divides by the current
forward coefficient.  This resolves all six layers at once, including
Item 294's first-two-layer gauge warning.

## 5. The endpoint cubic gives exactly the old resultant

The actual row relation is



$$
2^{2r+2}c^3
 =2^{2r+6s+2}=2^{p-1}\equiv1\pmod p.
\tag{5.1}
$$



If $G_{r,s}\equiv0\pmod p$, cubing
$18ca_r=-11b_r$ and using (5.1) yields



$$
N_r:=18^3a_r^3+11^3\,2^{2r+2}b_r^3
 \equiv0\pmod p.
\tag{5.2}
$$



This is the endpoint-conjugate norm, or equivalently the resultant up
to sign of



$$
18a_rT+11b_r,\qquad 2^{2r+2}T^3-1.
$$



However (2.1)--(2.2) give the exact rational identity



$$
\boxed{
L_r^3+2^{2r+2}M_r^3
=\left(\frac{g_n\kappa_e}{16^n}\right)^3N_r.}
\tag{5.3}
$$



The multiplier is a $p$-unit on every actual row.  Hence (5.2) is
precisely Item 250's old cubic resultant, not an additional
sequence-specific divisor.  No second gcd condition may be credited
from it.

The certificate checks (5.3) independently from the original Item 250
phase values.  This replay is finite; the theorem itself is the symbolic
substitution above.  Exact characteristic-zero nonvanishing of $N_r$
for all $r$ remains open, so a row with $N_r=0$ would make the
resultant condition vacuous.

## 6. Why further algebraic-branch norms do not yet help

The functions $C_+$ and $C_-$ are local branches of the same
algebraic curve, but a field norm of an algebraic **series** is a product
of series.  Its coefficient at index $r$ is a convolution,



$$
[x^r]\prod_jF_j(x)
 =\sum_{r_1+\cdots+r_k=r}\prod_j[x^{r_j}]F_j(x),
\tag{6.1}
$$



not the product of the same-index coefficients.  Therefore an algebraic
norm identity for the generating functions does not imply a divisor of
$18c\,a_r+11b_r$.  The only coefficientwise norm forced by the actual
row is the endpoint cubic (5.2), already identified with (5.3).

This is a scoped no-go: a new theorem relating the relevant convolutions
to same-index coefficients could change the conclusion, but no such
identity follows from algebraicity or branch conjugacy alone.

## 7. Height audit and capacity

Both branch series are algebraic over $\mathbb Q(x)$.  Eisenstein
global boundedness gives exponential denominator bounds, and their fixed
positive radii of convergence give exponential archimedean coefficient
bounds.  Thus



$$
h(a_r)=O(r),\qquad h(b_r)=O(r),\qquad h(N_r)=O(r)
\tag{7.1}
$$



whenever $N_r\neq0$.  This improves Item 250's earlier crude
individual $O(r\log r)$ estimate.

It still does not give the needed rate.  Summing the individual divisor
bounds over linearly many $r\leq M$ yields only



$$
\sum_{r\leq M}O(r)=O(M^2),
\tag{7.2}
$$



which is weaker than the already-known $O(M)$ raw cell ceiling.
Therefore the individual-height method and the conjugate-series norm
method cannot reduce the ordinary-$j=2$ capacity on their own.

The smallest remaining arithmetic target is



$$
\boxed{
\sum_{\substack{
r=6n+e,\ p=2r+6s+3\ {\rm prime}\\
18\,2^{2s}a_r+11b_r\equiv0\pmod p}}
\log p=o(M)}
\tag{7.3}
$$



over the actual parameter range, with duplicate primes and cell overlap
handled by the master ledger.  Proving (7.3) would control the necessary
rank-drop gate.  The actual period-incidence condition of Item 291 is
stronger, so a gate zero is not automatically an actual collision.

Item 314 books zero, and the raw ordinary-$j=2$ ceiling remains
$1/105$ per $6M$.

## 8. Deterministic replay

The checker verifies dependency hashes, both derivative factorizations,
the universal constants, the integer clearer, the direct two-branch
identity, all six singular layers, and the old-resultant identity.

At the declared replay bound $r\leq101$:



$$
\begin{array}{lr}
\text{actual branch rows}&34\\
\text{prime rows among }s=1,\ldots,6&123\\
\text{two-branch or unit failures}&0\\
\text{old-resultant identity failures}&0\\
\text{observed exact zeros of }N_r&0.
\end{array}
$$



The six-layer row-stream SHA-256 is

~~~text
15a47bfc257c8367e3f38dd8842266ec97ef6b7f2029a0cacb21b6e52a804c72
~~~

and the norm row-stream SHA-256 is

~~~text
2da64f72d478ea9b8ff07472de93ebaa10ff9e0b87a7d0fff87c63803cb6d992
~~~

The row counts and absence of observed zeros are **EXACT FINITE ONLY**.
They are not used to prove any asymptotic or nonvanishing statement.

## 9. Reproduction and strict labels

From the portable archive root:

~~~text
python work/item314_j2_two_branch_gate_certificate.py
python work/item314_j2_two_branch_gate_certificate.py \
  --output work/item314_j2_two_branch_gate_certificate_replay.json
~~~

### PROVED

* The residue-independent $18:11$ normalization (2.2).
* The exact rational derivative and coefficient formulas (3.2)--(3.4).
* The global integer clearer $H_r=6^{r+3}r!$.
* The all-row $p$-unit equivalence (1.3).
* The separation of all six current forward singular layers from the
  past-step gauge value.
* The endpoint norm identity (5.3) and its exact coincidence with the
  old Item 250 resultant.
* The scoped coefficientwise-norm and individual-height no-go.

### EXACT FINITE ONLY

* The declared $r\leq101$ six-layer and norm replays.
* The finite census of exact zeros of $N_r$.

### OPEN

* Weighted zero density (7.3) for the actual cleared two-branch gate.
* Exact nonvanishing of $N_r$ for all $r$.
* Any new sequence-specific divisor beyond Item 250's old resultant.
* Actual-period incidence on the surviving gate-zero rows.
* Any ordinary-$j=2$ capacity reduction, Route-1 completion, or
  conclusion about $e+\pi$.
