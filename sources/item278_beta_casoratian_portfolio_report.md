> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 278 — bounded Casoratian portfolios reduce to short-return depth

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain



$$
q_0=q_1=1,\qquad q_{n+2}=(4n+6)q_{n+1}+q_n,            \tag{1.1}
$$



and the gap continuants



$$
P_0(X)=0,\quad P_1(X)=1,\quad
P_{h+2}(X)=(4X+4h+6)P_{h+1}(X)+P_h(X).                 \tag{1.2}
$$



Item 276 treated one primitive growing two-state Casoratian.  This item
closes the immediate product loophole: several primitive residuals may
pool smaller $p$-adic orders even when no one residual reaches the full
singleton depth.

The admissible product class is exact.  Choose gaps $h_i\ge2$ and
multiplicities $w_i\ge1$, and put



$$
\mathcal A_{\mathcal H}(n)
 :=\prod_iP_{h_i}(n)^{w_i},                             \tag{1.3}
$$





$$
\mathcal D_{\mathcal H}(n)
 :=\prod_i\mathcal C_{h_i}(n)^{w_i},\qquad
\mathcal C_h(n)=q_nq_{n+h+1}-q_{n+1}q_{n+h}.            \tag{1.4}
$$



Here $\mathcal A_{\mathcal H}$ is the primitive residual coefficient
of the scalar-Casoratian product.  Define



$$
K=\sum_iw_i,\qquad
L=\sum_iw_i(h_i-1),\qquad
H=\log\mathcal A_{\mathcal H}(n).                       \tag{1.5}
$$



The number $K$ is total factor multiplicity and $L$ is the total gap
budget.

> **PROVED — exact height-versus-gap theorem.**
> 

$$
> \boxed{
> L\log(4n+6)\le H
> \le L\log\{4(n+L+1)\}.}                               \tag{1.6}
>
$$


> Hence a moving portfolio has $H=O(n)$ exactly when
> 

$$
> \boxed{L=O(n/\log n).}                                \tag{1.7}
>
$$



> **PROVED — exact accumulated-depth theorem.**  If $p^s\mid q_n$,
> then
> 

$$
> \boxed{
> \begin{aligned}
> \min\{s,v_p(\mathcal A_{\mathcal H}(n))\}
> &=\min\{s,v_p(\mathcal D_{\mathcal H}(n))\}\\
> &=\min\!\left\{
> s,\sum_iw_i\min\{s,v_p(q_{n+h_i})\}
> \right\}.
> \end{aligned}}                                       \tag{1.8}
>
$$



Thus a product reaches depth $s$ exactly by pooling same-prime return
depths at its selected gaps.  For fixed $K$, reaching $s$ with
$H=O(n)$ forces at least one short partial return:



$$
\boxed{
h_i=O(n/\log n),\qquad
p^{\lceil s/K\rceil}\mid q_{n+h_i}.}                   \tag{1.9}
$$



This is the smallest remaining arithmetic input.  It is not presently
proved or excluded uniformly for the actual high levels.

There is an unconditional portfolio generated only by the exact
anti-period.  Assign nonnegative depths $b_1,\ldots,b_K$ with
$\sum b_j\ge s$, and use gap $p^{b_j}$ when $b_j>0$.
For $s=Kq+r$, $0\le r<K$, the exact minimum certified gap cost is



$$
\boxed{
S_K(p,s)
=(K-r)(p^q-1)+r(p^{q+1}-1).}                           \tag{1.10}
$$



The balanced choice has $r$ depths $q+1$ and $K-r$ depths $q$.
Its residual height $H_{\rm can}$ satisfies



$$
S_K(p,s)\log(4n+6)
\le H_{\rm can}
\le S_K(p,s)\log\{4(n+p^{\lceil s/K\rceil})\}.          \tag{1.11}
$$



For fixed $K$, $H_{\rm can}=O(n)$ therefore forces



$$
\boxed{s\log p=O_K(\log n).}                            \tag{1.12}
$$



So bounded canonical anti-period accumulation reaches only
polynomial-size prime powers, whose logarithmic depth is already
negligible on the missing $n\log n$ scale.  It does not control the
dangerous high-singleton range.

All statements carry the Item-265 clearing overlap by taking



$$
s=\bigl(v_p(q_n)-v_p(D_m)\bigr)_+.                      \tag{1.13}
$$



No general beta no-go is claimed: actual short returns can beat the
canonical gap $p^b$, sums can cancel, and unbounded collections may
have different behavior.  No little-oh squarefull theorem or capacity
reduction follows.  Booking remains zero.

## 2. One-factor identities inherited by every portfolio

The transfer identity is



$$
q_{n+h}=P_h(n)q_{n+1}+P_{h-1}(n+1)q_n.                 \tag{2.1}
$$



Adjacent beta denominators are coprime, so reducing modulo any divisor
of $q_n$ gives



$$
\gcd(q_n,q_{n+h})=\gcd(q_n,P_h(n)).                    \tag{2.2}
$$



The scalar Casoratian satisfies



$$
\mathcal C_h(n)
\equiv-P_h(n)q_{n+1}^{\,2}\pmod {q_n}.                 \tag{2.3}
$$



Consequently, for every $p^s\mid q_n$,



$$
\boxed{
\min\{s,v_p(P_h(n))\}
=\min\{s,v_p(\mathcal C_h(n))\}
=\min\{s,v_p(q_{n+h})\}.}                              \tag{2.4}
$$



Taking weighted sums of valuations in (2.4), then truncating at $s$,
proves (1.8).  There is no assumption that the gaps are distinct.
Repeated gaps are formal powers of the same return factor; their
ordinary height is repeated by the same multiplicity.

For distinct gaps, the right side of (1.8) is exactly accumulated
pairwise recurrence overlap with $q_n$.  For repeated gaps, it is the
corresponding formal power of that overlap.  In neither case does the
product manufacture a new independent prime source.

## 3. Optimal residual height is a total-gap problem

Item 276 proved, for $h\ge1$,



$$
(4n+6)^{h-1}\le P_h(n)
\le\{4(n+h)\}^{h-1}.                                   \tag{3.1}
$$



Raise (3.1) to $w_i$ and multiply over the portfolio.  The lower
bound immediately gives



$$
\mathcal A_{\mathcal H}(n)\ge(4n+6)^L.                 \tag{3.2}
$$



Since each nontrivial gap satisfies $h_i\le L+1$, the upper bound
gives



$$
\mathcal A_{\mathcal H}(n)
\le\{4(n+L+1)\}^L.                                     \tag{3.3}
$$



Taking logarithms proves (1.6).

If $H\le Cn$, then (3.2) gives



$$
L\le{Cn\over\log(4n+6)}.                               \tag{3.4}
$$



Conversely, $L=O(n/\log n)$ implies $n+L+1=O(n)$, and
(3.3) gives $H=O(n)$.  This proves the equivalence (1.7), even if the
number of factors grows.  It is an exact reduction of the height
question to a gap-budget question, not a bound for the number of actual
returns.

One may package the remaining arithmetic in an optimal return cost.
For $p^s\mid q_n$ and an integer $K\ge1$, define



$$
\mathscr L_K(n,p,s)
:=\min\left\{
\sum_{j=1}^K(h_j-1):
h_j\ge1,\ 
\sum_{j=1}^K\min\{s,v_p(q_{n+h_j})\}\ge s
\right\}.                                              \tag{3.5}
$$



The harmless gap $h_j=1$ represents an unused slot.  Repetitions are
allowed.  Equations (1.6) and (1.8) show:



$$
\boxed{
\begin{gathered}
\text{a }K\text{-slot product reaches depth }s
\text{ with residual height }O(n)\\
\Longleftrightarrow\quad
\mathscr L_K(n,p,s)=O(n/\log n).
\end{gathered}}                                        \tag{3.6}
$$



The constants in (3.6) are uniform only if the constants in the two
big-oh statements are uniform.  Formula (3.5), rather than a finite
prime scan, is the exact missing global datum.

## 4. A bounded portfolio forces a short partial return

Expand each multiplicity $w_i$ into repeated slots.  If total
multiplicity is at most $K$ and the product reaches depth $s$,
(1.8) gives a sum of at most $K$ nonnegative integers at least $s$.
At least one is at least $\lceil s/K\rceil$.  Therefore



$$
p^{\lceil s/K\rceil}\mid q_{n+h_i}.                    \tag{4.1}
$$



If the residual height is $O(n)$, (1.7) also gives



$$
h_i-1\le L=O(n/\log n).                                \tag{4.2}
$$



Together, (4.1)–(4.2) prove (1.9).

This statement is sharp at the level of information retained:
repeating one gap whose return depth is
$\lceil s/K\rceil$ can make its $K$-th power reach depth at least
$s$.  Therefore top-level singleton support alone does not rule out a
bounded product; one must control partial-depth returns too.

The conclusion is also deliberately one-way.  A short return at the
partial level supplies a candidate portfolio, but its uniform existence
for every dangerous actual prime power is not known.  Nor is there a
proved uniform lower bound forcing every such return to be long.

## 5. Exact canonical anti-period optimizer

The exact odd-modulus anti-period says



$$
q_{n+M}\equiv-q_n\pmod M\qquad(M\ {\rm odd}).           \tag{5.1}
$$



If $p^b\mid q_n$, then



$$
p^b\mid q_{n+p^b},\qquad p^b\mid P_{p^b}(n).           \tag{5.2}
$$



A **canonical anti-period portfolio** assigns a certified depth
$b_j\ge0$ to slot $j$: for $b_j>0$ it uses
$P_{p^{b_j}}(n)$, and for $b_j=0$ it uses the unit
$P_1(n)=1$.  No credit is taken for accidental valuation beyond
$b_j$.  To guarantee depth $s$, it is enough and in this certified
accounting necessary that



$$
\sum_{j=1}^K b_j\ge s.                                 \tag{5.3}
$$



The associated gap cost is



$$
\sum_{j=1}^K(p^{b_j}-1).                               \tag{5.4}
$$



At a minimum, equality holds in (5.3).  If two depths differ by at
least two, say $u\ge v+2$, then



$$
p^u+p^v>p^{u-1}+p^{v+1}.                               \tag{5.5}
$$



Balancing such pairs strictly lowers (5.4).  Hence the unique multiset
of minimizing depths consists of $r$ copies of $q+1$ and $K-r$
copies of $q$, where $s=Kq+r$, $0\le r<K$.  This proves the exact
formula (1.10).

Applying (3.1) to the balanced portfolio proves (1.11).  In addition,
the arithmetic-geometric mean inequality gives



$$
S_K(p,s)+K
=\sum_{j=1}^Kp^{b_j}
\ge Kp^{s/K}.                                          \tag{5.6}
$$



If $K$ is fixed and $H_{\rm can}=O(n)$, the lower half of (1.11)
and (5.6) give



$$
p^{s/K}
\le1+O_K\!\left({n\over\log n}\right).                 \tag{5.7}
$$



Taking logarithms proves (1.12).  Conversely, if



$$
p^{\lceil s/K\rceil}=O_K(n/\log n),                    \tag{5.8}
$$



then the upper half of (1.11) gives $H_{\rm can}=O_K(n)$.
Thus the logarithmic threshold is exact up to fixed-$K$ constants.

This optimizer answers the canonical accumulation question completely:
splitting a level among finitely many anti-period factors helps
exponentially in the gap, but an $O(n)$ residual then occurs only
when the total prime-power logarithm is $O_K(\log n)$.  Such levels
are already far below the missing $O(n)$, let alone $n\log n$,
valuation scale.

This conclusion is not transferred to arbitrary actual returns.  A
return gap much shorter than $p^b$ would beat the canonical cost and
belongs to the open quantity (3.5).

## 6. Item-265 clearing overlap and capacity

Retain



$$
D_m={K_m^{(0)}\over\gcd(K_m^{(0)},c_m)},\qquad
\overline q_{m,n}={q_n\over\gcd(q_n,D_m)},              \tag{6.1}
$$



and Item 265's exact divisor



$$
J_{m,n}\mid\overline q_{m,n}^{\,2}.                    \tag{6.2}
$$



For a prime $p$, put



$$
a=v_p(q_n),\qquad r=v_p(D_m),\qquad s=(a-r)_+.          \tag{6.3}
$$



If $s>0$, then $p^s\mid q_n$, so (1.8) applies without change:



$$
\boxed{
\begin{aligned}
\min\{s,v_p(\mathcal A_{\mathcal H}(n))\}
&=\min\{s,v_p(\mathcal D_{\mathcal H}(n))\}\\
&=\min\!\left\{
s,\sum_iw_i\min\{s,v_p(q_{n+h_i})\}
\right\}.
\end{aligned}}                                         \tag{6.4}
$$



For distinct gaps, (6.4) is precisely accumulated recurrence overlap
at the surviving normalized level.  Repeating a gap raises both its
formal divisibility and its ordinary height by the same multiplicity.
Neither operation creates an independent copy which can be booked on
top of the optimistic two-copy clearing reservoir.

The canonical optimizer may be run with the surviving depth $s$, but
(1.12) shows that a fixed number of $O(n)$-height canonical factors
reaches only $s\log p=O_K(\log n)$.  No estimate is obtained for
actual short-return portfolios in (3.5).

Therefore the positive-linear-capacity admission test fails.  The
Item-265 high-singleton ceiling and overlap normalization remain
unchanged.

## 7. Strict labels and open boundary

### PROVED

* The exact product depth formula (1.8).
* The exact residual-height bounds (1.6) and gap-budget equivalence
  (1.7).
* The fixed-$K$ short partial-return consequence (1.9).
* The return-cost recognition (3.5)–(3.6).
* The balanced canonical optimizer (1.10), its height comparison
  (1.11), and fixed-$K$ logarithmic ceiling (1.12).
* The overlap-normalized formula (6.4).

### PROVED SCOPED NO-GO

* A bounded number of canonical anti-period factors with total residual
  height $O(n)$ cannot reach a dangerous super-polynomial singleton
  depth.
* An arbitrary bounded product can do so only if a short partial-depth
  return as in (1.9) exists.
* Products in the admitted class repackage return overlaps or their
  formal powers; they do not independently reduce the Item-265
  reservoir ceiling.

### EXACT FINITE ONLY

* The deterministic checker replays bounded product valuations,
  de-overlap, height inequalities, the balanced integer optimizer, and
  canonical anti-period portfolios.
* It performs no exceptional-singleton census and makes no
  distributional extrapolation.

### OPEN

* A uniform construction or lower bound for the actual short-return
  cost $\mathscr L_K(n,p,s)$.
* Sums with cancellation, arbitrary growing Hankel/block determinants,
  and unbounded portfolios using genuinely independent arithmetic
  input.
* The uniform estimate $v_p(q_n)\log p=O(n)$, a sufficient little-oh
  squarefull aggregate, and the actual correlation with the clearing
  divisor and transverse matching factor.
* Route 1 and every conclusion about $e+\pi$.

### BOOKING



$$
\boxed{
\text{new Route-1 rate}=0,\qquad
\text{new beta capacity reduction}=0.}                 \tag{7.1}
$$



## 8. Deterministic replay

From the archive root:

~~~text
python scripts/item278_beta_casoratian_portfolio_certificate.py ^
  --output results/item278_beta_casoratian_portfolio_certificate_replay.json
~~~

The checker is Python-standard-library only, deterministic, and uses
exact integer arithmetic.  The canonical result and replay must be
byte-identical.
