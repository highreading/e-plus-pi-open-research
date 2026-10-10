> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 276 — primitive growing Casoratians transport singleton depth instead of bounding it

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain the beta denominator



$$
q_0=q_1=1,\qquad
q_{n+2}=(4n+6)q_{n+1}+q_n.                              \tag{1.1}
$$



Item 265 localized the unresolved excess-valuation mass to high
prime-power levels, and Item 274 proved that every fixed-window
reverse-Bessel determinant is either blind to a deep singleton or
contains a formal power of $q_n$.  This item tests the smallest
genuinely growing continuation: keep determinant size two but let its
index gap $h=h(n)$ grow.

The admissible class is defined narrowly and exactly in Section 2.  It is
one primitive $2\times2$ minor of the two-state transition-row matrix,
equivalently one gap continuant $P_h(n)$, together with the associated
scalar Casoratian



$$
\mathcal C_h(n)
 :=q_nq_{n+h+1}-q_{n+1}q_{n+h}.                         \tag{1.2}
$$



> **PROVED — exact depth-transport theorem.**  If $p^s\mid q_n$, then
> for every $h\ge1$,
> 

$$
> \boxed{
> p^s\mid\mathcal C_h(n)
> \quad\Longleftrightarrow\quad
> p^s\mid P_h(n)
> \quad\Longleftrightarrow\quad
> p^s\mid q_{n+h}.}                                     \tag{1.3}
>
$$


> More sharply, if $a=v_p(q_n)$ and
> $b=v_p(P_h(n))<a$, then
> 

$$
> \boxed{v_p(\mathcal C_h(n))=b.}                       \tag{1.4}
>
$$



Thus a primitive growing Casoratian reaches a singleton level only by
transporting that same level to a second sequence index.  It cannot reach
a level which is genuinely supported only at $n$ inside a window
containing both $n$ and $n+h$.

> **PROVED — exact residual-height scale.**  For every $n\ge0$ and
> $h\ge1$,
> 

$$
> \boxed{
> (4n+6)^{h-1}\le P_h(n)
> \le\{4(n+h)\}^{h-1}.}                                 \tag{1.5}
>
$$


> Consequently, within this primitive class,
> 

$$
> \log P_{h(n)}(n)=O(n)
> \quad\Longleftrightarrow\quad
> h(n)=O\!\left({n\over\log n}\right)                   \tag{1.6}
>
$$


> for $n\to\infty$, with the harmless convention $h\ge1$.

The exact odd-modulus anti-period gives an unconditional way to reach a
divisor $M\mid q_n$: take $h=M$.  Its residual coefficient already
has



$$
\log P_M(n)\ge(M-1)\log(4n+6).                          \tag{1.7}
$$



In particular, for an Item-265 high level $p^a>N$ at an index
$N\le n<2N$, the universal choice $h=p^a$ costs at least



$$
N\log(4N+6),                                           \tag{1.8}
$$



the full $N\log N$ scale rather than $O(N)$.

This proves a sharply scoped no-go: the primitive two-state
Casoratian/continuant construction either uses a short *second zero* as
new arithmetic input or pays main-scale height in the universal
seed-only construction.  It does **not** prove that a short second zero
outside the chosen block cannot occur, and it does not cover products or
sums of a growing number of minors.

The Item-265 clearing overlap is preserved exactly.  For



$$
\overline q_{m,n}={q_n\over\gcd(q_n,D_m)},
$$



one has



$$
\boxed{
\overline q_{m,n}\mid\mathcal C_h(n)
\Longleftrightarrow
\overline q_{m,n}\mid P_h(n)
\Longleftrightarrow
\overline q_{m,n}\mid q_{n+h}.}                         \tag{1.9}
$$



No little-oh squarefull theorem, uniform
$v_p(q_n)\log p=O(n)$ estimate, or capacity reduction follows.
Booking remains zero.

## 2. Exact admissible growing-window class

Define the continuants



$$
P_0(X)=0,\qquad P_1(X)=1,
$$





$$
P_{d+2}(X)=(4X+4d+6)P_{d+1}(X)+P_d(X).                 \tag{2.1}
$$



The recurrence (1.1) gives the exact transfer identity



$$
\boxed{
q_{n+d}=P_d(n)q_{n+1}+P_{d-1}(n+1)q_n
\qquad(d\ge1).}                                        \tag{2.2}
$$



For $d\ge1$, put



$$
r_d(n)=\bigl(P_d(n),P_{d-1}(n+1)\bigr),\qquad
r_0(n)=(0,1).                                          \tag{2.3}
$$



Then $q_{n+d}=r_d(n)(q_{n+1},q_n)^t$.  The continuant
addition formula gives, for $e>d$,



$$
\boxed{
\det\bigl(r_e(n),r_d(n)\bigr)
=(-1)^dP_{e-d}(n+d).}                                  \tag{2.4}
$$



Every primitive $2\times2$ transition-row minor is therefore, up to
sign and a base-index shift, one gap continuant.  Adjacent minors are
units.  Since the transition-row matrix has two columns, its larger raw
minors vanish identically.

This item calls the following the **primitive growing-Casoratian class**:

1. one minor (2.4), with $e-d$ allowed to grow with the base index;
2. its primitive gap coefficient $P_{e-d}(n+d)$; or
3. the scalar two-output Casoratian (1.2), whose residual modulo $q_n$
   is governed by the same $P_h(n)$.

This definition deliberately excludes:

* a product or sum of a growing number of distinct minors, where
  $p$-adic depth may split among many factors;
* arbitrary growing Hankel, block, or interpolation determinants not
  equal to a single two-state transition minor; and
* coefficients depending on a new global relation among many gaps.

Those larger classes are not ruled out by the theorem below.

## 3. Singleton valuation is exactly a second-zero condition

Adjacent beta denominators are coprime.  Indeed, (1.1) gives



$$
\gcd(q_n,q_{n+1})=\gcd(q_n,q_{n-1})=1                 \tag{3.1}
$$



by induction from $q_0=q_1=1$.  Reducing (2.2) modulo $q_n$ gives



$$
q_{n+h}\equiv P_h(n)q_{n+1}\pmod {q_n}.                \tag{3.2}
$$



Since $q_{n+1}$ is a unit modulo every divisor of $q_n$,



$$
\boxed{
\gcd(q_n,q_{n+h})=\gcd(q_n,P_h(n)).}                   \tag{3.3}
$$



For the scalar Casoratian, (3.2) gives



$$
\boxed{
\mathcal C_h(n)
\equiv-P_h(n)q_{n+1}^{\,2}\pmod {q_n}.}                \tag{3.4}
$$



Now let $p^s\mid q_n$.  The boundary value $q_{n+1}$ is a
$p$-unit.  Equations (3.2) and (3.4) immediately prove all three
equivalences in (1.3).

For the sharper valuation statement, put



$$
a=v_p(q_n),\qquad b=v_p(P_h(n)).
$$



Equation (3.4) is an integer equality of the form



$$
\mathcal C_h(n)=-P_h(n)q_{n+1}^{\,2}+q_nT_{n,h},
\qquad T_{n,h}\in\mathbb Z.                            \tag{3.5}
$$



If $b<a$, the two terms on the right have distinct valuations $b$
and at least $a$.  No cancellation is possible, so (1.4) follows.

Suppose now that a level $p^s$ is supported only at $n$ in an
interval $I$.  If $n+h\in I$, equation (1.3) gives



$$
p^s\nmid P_h(n),\qquad p^s\nmid\mathcal C_h(n).         \tag{3.6}
$$



This remains true even when $h$ grows with $n$.  The determinant has
not bounded the singleton valuation; it has merely tested whether the
same level occurs at another index.

## 4. Exact coefficient height and the $O(n)$ threshold

The polynomials $P_h$ have positive values at $n\ge0$.  Moreover,
$P_1(n)=1$, $P_2(n)=4n+6$, and



$$
P_{d+2}(n)\ge(4n+6)P_{d+1}(n).                         \tag{4.1}
$$



Iteration proves the lower bound in (1.5).

For the upper bound, positivity gives $P_d(n)\le P_{d+1}(n)$.  At
every step $0\le d\le h-2$,



$$
\begin{aligned}
P_{d+2}(n)
&\le(4n+4d+7)P_{d+1}(n)\\
&\le4(n+h)P_{d+1}(n).
\end{aligned}                                          \tag{4.2}
$$



Iteration proves the upper bound in (1.5).

If $\log P_{h(n)}(n)\le Cn$, the lower bound gives



$$
h(n)\le1+{Cn\over\log(4n+6)}.                          \tag{4.3}
$$



Conversely, if $h(n)=O(n/\log n)$, then $n+h(n)=O(n)$, and the
upper bound gives $\log P_{h(n)}(n)=O(n)$.  This proves (1.6).

Here $\log P_h(n)$ is the most optimistic primitive residual
coefficient height: (3.4) has also the boundary unit
$q_{n+1}^{\,2}$, whose ordinary size is much larger.  Thus failure at
the $P_h$ level cannot be repaired by retaining the full
Casoratian.

## 5. The universal global construction pays the full scale

The archived exact beta anti-period states that, for every odd
$M\ge1$,



$$
\boxed{q_{n+M}\equiv-q_n\pmod M.}                      \tag{5.1}
$$



If $M\mid q_n$, then $M\mid q_{n+M}$.  Since
$\gcd(M,q_{n+1})=1$, the transfer identity also gives



$$
\boxed{M\mid P_M(n).}                                  \tag{5.2}
$$



Thus $h=M$ is an unconditional, seed-compatible growing continuant
which reaches the full modulus $M$.  But (1.5) gives exactly



$$
\log P_M(n)\ge(M-1)\log(4n+6).                         \tag{5.3}
$$



For a high singleton prime-power level $p^a>N$ at
$N\le n<2N$, take $M=p^a$.  Then $p^a-1\ge N$, and



$$
\log P_{p^a}(n)
\ge N\log(4N+6).                                       \tag{5.4}
$$



This is already the main $N\log N$ height scale which Item 265 could
not admit.

Equations (1.3) and (1.6) isolate the only possible escape within the
primitive class: prove that every relevant high level has a second zero
at some short gap



$$
h=O(N/\log N),                                         \tag{5.5}
$$



or obtain an equivalent global relation.  A short second zero outside
the original block is not excluded here.  Its existence would be new
arithmetic input; it does not follow from the local two-state
Casoratian algebra.  Conversely, excluding all such short returns
would prove only that this primitive auxiliary cannot reach the depth,
not an upper bound for the depth itself.

No minimal-period claim is made for the universal gap $M$.

## 6. Exact de-overlap with the Item-265 reservoir

Retain the actual clearing divisor and normalized beta denominator



$$
D_m={K_m^{(0)}\over\gcd(K_m^{(0)},c_m)},\qquad
\overline q_{m,n}={q_n\over\gcd(q_n,D_m)}.              \tag{6.1}
$$



Item 265 proved



$$
J_{m,n}\mid\overline q_{m,n}^{\,2}.                    \tag{6.2}
$$



Because $\overline q_{m,n}\mid q_n$, equation (3.1) gives



$$
\gcd(\overline q_{m,n},q_{n+1})=1.
$$



Reducing (2.2) and (3.4) modulo $\overline q_{m,n}$
proves the exact equivalence (1.9).

Prime by prime, put



$$
t=v_p(q_n),\qquad r=v_p(D_m),\qquad
\overline a=(t-r)_+.
$$



If $\overline a>0$, then



$$
\boxed{
v_p(\mathcal C_h(n))\ge\overline a
\Longleftrightarrow
v_p(P_h(n))\ge\overline a
\Longleftrightarrow
v_p(q_{n+h})\ge\overline a.}                           \tag{6.3}
$$



Thus even after the clearing overlap is removed, a primitive
Casoratian reaches the surviving depth only by reproducing that same
surviving level at another sequence index.  It does not create a fresh
factor which can be added to the already optimistic two-copy reservoir.

Since every $q_n$ is odd, (5.1) may also be applied with
$M=\overline q_{m,n}$.  This gives the simultaneous universal gap



$$
\overline q_{m,n}\mid P_{\overline q_{m,n}}(n),         \tag{6.4}
$$



but its primitive coefficient height is at least



$$
\bigl(\overline q_{m,n}-1\bigr)\log(4n+6).              \tag{6.5}
$$



Assuming that (6.5) is $O(n)$ would already force
$\overline q_{m,n}=O(n/\log n)$, hence
$\log\overline q_{m,n}=O(\log n)$.  It is therefore circular as a
proof of the missing prime-power-height estimate.

## 7. What is and is not closed

### PROVED

* The exact transfer, transition-minor, and gap-gcd identities
  (2.2), (2.4), and (3.3).
* The Casoratian residual identity (3.4).
* The level-by-level equivalence (1.3) and exact shallow-order formula
  (1.4).
* The height bounds (1.5) and $O(n)$-height threshold (1.6).
* The universal anti-period construction and its main-scale lower
  height (5.3)–(5.4).
* The overlap-normalized equivalences (1.9) and (6.3).

### PROVED SCOPED NO-GO

* A single primitive growing two-state minor cannot reach an in-window
  singleton level.
* The unconditional gap $h=M$ which reaches every divisor
  $M\mid q_n$ is not an $O(n)$-height residual for Item-265 high
  levels $M=p^a>N$.
* Therefore this primitive method does not by itself prove a uniform
  singleton-height or little-oh squarefull theorem.

### EXACT FINITE ONLY

* The portable checker replays bounded polynomial, transfer, minor,
  Casoratian, valuation, height, anti-period, and de-overlap identities.
* It performs no exceptional-singleton census and makes no asymptotic
  extrapolation.

### OPEN

* Products or sums of a growing number of minors, where the required
  $p$-adic order can split among many gaps.
* Arbitrary growing Hankel or block determinants outside the primitive
  two-state class.
* A uniform theorem producing or excluding a short second zero at each
  relevant high level.
* The uniform estimate $v_p(q_n)\log p=O(n)$, any sufficient
  little-oh aggregate, and the actual correlation with the clearing
  divisor and transverse matching factor.
* Route 1 and every conclusion about $e+\pi$.

### BOOKING



$$
\boxed{
\text{new Route-1 rate}=0,\qquad
\text{new beta capacity reduction}=0.}                 \tag{7.1}
$$



The Item-265 high-singleton ceiling and its two-copy overlap
normalization remain unchanged.

## 8. Deterministic replay

From the archive root:

~~~text
python scripts/item276_beta_growing_casoratian_certificate.py ^
  --output results/item276_beta_growing_casoratian_certificate_replay.json
~~~

The canonical result and replay must be byte-identical.  The checker is
Python-standard-library only, uses exact integer arithmetic, has no
randomness or timestamps, and records digests of every bounded row set.
