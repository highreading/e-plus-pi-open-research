> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 282 — unbounded Casoratian portfolios have an exact efficiency dichotomy

Checked: 2026-08-31 (Beijing time)

## 1. Scope, quantifiers, and verdict

Retain



$$
q_0=q_1=1,\qquad q_{n+2}=(4n+6)q_{n+1}+q_n,            \tag{1.1}
$$



the continuants



$$
P_0(X)=0,\quad P_1(X)=1,\quad
P_{h+2}(X)=(4X+4h+6)P_{h+1}(X)+P_h(X),                 \tag{1.2}
$$



and the scalar Casoratians



$$
\mathcal C_h(n)=q_nq_{n+h+1}-q_{n+1}q_{n+h}.            \tag{1.3}
$$



This item extends Item 278 from fixed total multiplicity to arbitrary
$K=K(n)$.  Every quantifier used below is explicit.

* $n\ge1$ is arbitrary.
* $Q$ is any positive divisor of $q_n$.  In the actual application,
  $Q$ may be any surviving target divisor of
  

$$
\overline q_{m,n}={q_n\over\gcd(q_n,D_m)}.            \tag{1.4}
$$


* A product portfolio is any finite family of gaps $h\ge2$ with
  nonnegative integer weights $w_h$, not all zero.  Both the support
  and the total multiplicity may depend on $n$.
* Asymptotic $O$-constants are required to be uniform along the
  actual family under discussion.

Put



$$
\mathcal A(n)=\prod_{h\ge2}P_h(n)^{w_h},\qquad
\mathcal D(n)=\prod_{h\ge2}\mathcal C_h(n)^{w_h},       \tag{1.5}
$$





$$
K=\sum_hw_h,\qquad
L=\sum_hw_h(h-1),\qquad H=\log\mathcal A(n).            \tag{1.6}
$$



Define the de-overlapped captured logarithmic capacity



$$
\operatorname{Cap}_Q(\mathcal A)
 :=\log\gcd(Q,\mathcal A).                              \tag{1.7}
$$



> **PROVED — unbounded product efficiency theorem.**  For every such
> $n,Q,\mathcal A$,
> 

$$
> \boxed{
> \gcd(Q,\mathcal A)
> \mid\prod_{h\ge2}\gcd(Q,P_h(n))^{w_h},}               \tag{1.8}
>
$$


> and
> 

$$
> \boxed{
> {\operatorname{Cap}_Q(\mathcal A)\over H}
> \le
> \max_{h:w_h>0}
> {\log\gcd(Q,P_h(n))\over\log P_h(n)}.}                \tag{1.9}
>
$$


> Moreover
> 

$$
> \boxed{\gcd(Q,\mathcal D)=\gcd(Q,\mathcal A).}        \tag{1.10}
>
$$



Thus unlimited powering cannot improve captured depth per unit residual
height over the best single primitive return.  It can only scale that
return until the exponents already present in $Q$ saturate.

Items 276–278 give



$$
L\log(4n+6)\le H\le L\log\{4(n+L+1)\}.                 \tag{1.11}
$$



Hence



$$
H=O(n)\quad\Longrightarrow\quad
K\le L=O(n/\log n).                                    \tag{1.12}
$$



The portfolio may be unbounded, but an $O(n)$-height portfolio has at
most $O(n/\log n)$ nontrivial factor copies.

The exact positive-linear dichotomy follows.  Suppose



$$
H\le Cn,\qquad
\operatorname{Cap}_Q(\mathcal A)\ge\delta n             \tag{1.13}
$$



for fixed $C,\delta>0$.  Then some selected gap satisfies



$$
\boxed{
h=O(n/\log n),\qquad
\log\gcd(Q,P_h(n))
\ge{\delta\over C}\log P_h(n)
\ge{\delta\over C}(h-1)\log(4n+6).}                    \tag{1.14}
$$



This is a genuine high-efficiency short return.  Conversely, if



$$
\max_{\substack{2\le h\le C'n/\log n}}
{\log\gcd(Q,P_h(n))\over\log P_h(n)}
=o(1)                                                   \tag{1.15}
$$



uniformly, then every $O(n)$-height product portfolio has



$$
\operatorname{Cap}_Q(\mathcal A)=o(n).                 \tag{1.16}
$$



Equations (1.14)–(1.16) are a universal product dichotomy.  No theorem
currently proves either a positive mass of high-efficiency returns or
the uniform decay (1.15) for the actual moving target $Q$.

Artificial repetition is completely visible.  If



$$
G_t(Q,h)=\gcd(Q,P_h(n)^t),\qquad G_0(Q,h)=1,
$$



then the new layers



$$
R_t(Q,h)={G_t(Q,h)\over G_{t-1}(Q,h)}
$$



satisfy



$$
\boxed{R_{t+1}(Q,h)\mid R_t(Q,h).}                     \tag{1.17}
$$



No new prime support is created, and the return per copy can only
decrease.

> **PROVED SCOPED NO-GO — unbounded canonical anti-period products.**
> If one uses only the guaranteed factors
> $p^b\mid P_{p^b}(n)$, the exact least gap cost for certified depth
> $s$ is
> 

$$
> \boxed{s(p-1),}                                      \tag{1.18}
>
$$


> attained by $s$ repeated depth-one factors.  Therefore every
> $O(n)$-height canonical portfolio, even with unbounded $K$, has
> certified logarithmic capacity
> 

$$
> \boxed{O(n/\log n)=o(n)}                              \tag{1.19}
>
$$


> uniformly over odd primes, and likewise after summing factors assigned
> to different odd primes.

So the canonical portfolio cannot have positive linear capacity.
The first potentially admissible product regime is noncanonical:
a proved actual-family weighted short-return cover with the
high-efficiency mass required by (1.14).

Sums are different.  A homogeneous sum of product monomials reduces
modulo $Q$ to a sum of their primitive residuals.  A unique least
$p$-adic term cannot add depth; only tied-minimum cancellation can.
Such cancellation can in principle touch a strictly isolated prime and
is not ruled out here.  A nonzero, prime-independent residual sum of
height $O(n)$ with proved target divisibility would be genuinely
admissible, but no such theorem is available.

No actual-family positive mass, uniform prime-power-height theorem, or
strict retained ceiling is proved.  Booking remains zero.

## 2. Exact product depth and de-overlap

The transfer identity and adjacent coprimality give



$$
q_{n+h}\equiv P_h(n)q_{n+1}\pmod {q_n},                \tag{2.1}
$$





$$
\mathcal C_h(n)
\equiv-P_h(n)q_{n+1}^{\,2}\pmod {q_n}.                 \tag{2.2}
$$



Let $p^s\Vert Q$.  Since $Q\mid q_n$, the value $q_{n+1}$ is a
$p$-unit.  Therefore



$$
\min\{s,v_p(P_h(n))\}
=\min\{s,v_p(\mathcal C_h(n))\}
=\min\{s,v_p(q_{n+h})\}.                               \tag{2.3}
$$



For the product,



$$
v_p(\mathcal A)=\sum_hw_hv_p(P_h(n)).
$$



Consequently



$$
\begin{aligned}
v_p\bigl(\gcd(Q,\mathcal A)\bigr)
&=\min\!\left\{s,\sum_hw_hv_p(P_h(n))\right\}\\
&\le\sum_hw_h\min\{s,v_p(P_h(n))\}\\
&=v_p\!\left(
\prod_h\gcd(Q,P_h(n))^{w_h}
\right).
\end{aligned}                                          \tag{2.4}
$$



This proves (1.8) prime by prime.  It also proves (1.10), because
(2.3) makes the truncated product valuations of
$\mathcal A$ and $\mathcal D$ equal at every prime of $Q$.

Taking logarithms in (1.8) gives



$$
\operatorname{Cap}_Q(\mathcal A)
\le\sum_hw_h\log\gcd(Q,P_h(n)).                         \tag{2.5}
$$



The right side divided by



$$
H=\sum_hw_h\log P_h(n)
$$



is a weighted average of the primitive overlap efficiencies.  This
proves (1.9).

The target $Q$ is arbitrary.  To apply the theorem after the Item-265
clearing reservoir, take any



$$
Q\mid\overline q_{m,n}.
$$



Prime by prime this means that its target exponent $s_p$ satisfies



$$
0\le s_p\le
\bigl(v_p(q_n)-v_p(D_m)\bigr)_+.                       \tag{2.6}
$$



Thus every displayed product identity is already de-overlapped.  One
may choose $Q$ to be the whole normalized beta denominator, its
powerful-supported part, its excess factor, or only the matching-smooth
high-singleton target, provided the choice is stated.

## 3. Artificial multiplicity and diminishing layers

Fix $Q,h$, and write



$$
s_p=v_p(Q),\qquad b_p=v_p(P_h(n)).
$$



The exponent of $p$ in $G_t(Q,h)$ is



$$
\min\{s_p,tb_p\}.
$$



Hence its new $t$-th layer has exponent



$$
\begin{aligned}
v_p(R_t(Q,h))
&=\min\{s_p,tb_p\}-\min\{s_p,(t-1)b_p\}\\
&=\min\{b_p,(s_p-(t-1)b_p)_+\}.
\end{aligned}                                          \tag{3.1}
$$



This is nonincreasing in $t$, proving (1.17).  In particular,



$$
\operatorname{rad}G_t(Q,h)
\mid\operatorname{rad}G_1(Q,h),                        \tag{3.2}
$$



and later copies contain no prime which was absent from the first
primitive return.

For a general product, every captured prime therefore comes from at
least one base overlap



$$
\gcd(Q,P_h(n))
=\gcd(Q,q_{n+h}).                                      \tag{3.3}
$$



Weights amplify those overlaps formally; they do not establish another
independent return or a new prime-support fact.

This also settles repeated low-level returns.  Suppose throughout the
allowed gaps that



$$
\log\gcd(Q,P_h(n))
=o\bigl(\log P_h(n)\bigr)                               \tag{3.4}
$$



uniformly.  Equation (1.9) implies (1.16), irrespective of how
$K(n)$ grows within the height budget.  In particular, repeatedly
powering a bounded-depth return at a fixed prime has only
$O(K)=O(n/\log n)=o(n)$ captured logarithmic mass.

The qualification “fixed prime” matters.  A depth-one return at a prime
whose logarithm is comparable to $(h-1)\log n$ can have positive
primitive efficiency.  Such a large prime factor of $P_h(n)$ is not
excluded by height alone.  It is exactly the noncanonical
high-efficiency regime in (1.14), and it requires actual arithmetic
control rather than another multiplicity optimization.

## 4. Exact unbounded canonical optimizer

The odd-modulus anti-period gives



$$
q_{n+p^b}\equiv-q_n\pmod {p^b}.
$$



Thus, if $p^b\mid q_n$,



$$
p^b\mid P_{p^b}(n).                                    \tag{4.1}
$$



Assigning certified depth $b\ge1$ to one canonical factor costs gap



$$
p^b-1.
$$



For every odd prime $p$,



$$
p^b-1=(p-1)(1+p+\cdots+p^{b-1})
\ge b(p-1).                                            \tag{4.2}
$$



Therefore any canonical multiset with total certified depth at least
$s$ has total gap cost at least $s(p-1)$.  Equality is attained by
$s$ copies with $b=1$, proving (1.18).  This is the exact optimizer
when the number of factors is unrestricted.

The residual height is at least the gap cost times
$\log(4n+6)$.  Hence a canonical portfolio of height at most $Cn$
has, for a factor assignment to prime $p$,



$$
s\log p
\le {Cn\log p\over(p-1)\log(4n+6)}.                    \tag{4.3}
$$



For odd primes,



$$
{\log p\over p-1}\le{\log3\over2}.                     \tag{4.4}
$$



Thus (4.3) is $O(n/\log n)=o(n)$, uniformly in $p$.

The same conclusion holds if different factors are assigned to
different primes.  Indeed, each certified logarithmic unit
$b\log p$ costs at least



$$
b(p-1)\log(4n+6),
$$



so its yield-to-height ratio is at most



$$
{\log3\over2\log(4n+6)}.
$$



Summing over all assignments proves the multi-prime form of (1.19).
Accidental divisibility of these continuants by other target primes is
not part of the canonical certificate; it belongs to the actual
high-efficiency overlap regime of Section 3.

## 5. The exact missing product lemma

For a target $Q\mid\overline q_{m,n}$ and a gap budget $B$, define



$$
\mathscr Y_Q(n;B)
:=\max_{\substack{w_h\in\mathbb Z_{\ge0}\\
                  \sum_hw_h(h-1)\le B}}
\log\gcd\!\left(Q,\prod_hP_h(n)^{w_h}\right).           \tag{5.1}
$$



This is a finite integer optimization, because every nonzero weight has
$2\le h\le B+1$ and total multiplicity at most $B$.

The first genuinely admissible positive-capacity product theorem would
be an actual-family statement of the form



$$
\boxed{
\mathscr Y_Q\!\left(n;{Cn\over\log n}\right)
\ge\delta n}                                           \tag{5.2}
$$



for fixed $C,\delta>0$, with $Q$ the explicitly declared
de-overlapped target and with enough uniform or weighted mass to enter
the Route-1 capacity ledger.  An even stronger closing statement would
produce weights of that budget for which



$$
Q\mid\prod_hP_h(n)^{w_h}.                              \tag{5.3}
$$



Then (1.11) would give



$$
\log Q=O(n),
$$



which is the desired uniform prime-power-height scale for that target.

Equations (1.8)–(1.14) prove that any theorem (5.2) must contain
genuine high-efficiency return information.  Repetition alone cannot
supply it.  Conversely, (5.1) keeps all exponent saturation and all
possible mixing of different gaps, so it is the exact remaining
product lemma rather than a heuristic proxy.

No bound proving (5.2), (5.3), or the uniform decay (1.15) is currently
available for the actual moving rows.

## 6. Sums: the cancellation branch is genuinely different

Products have no additive cancellation.  To keep sums precise, consider
finitely many product monomials



$$
\mathcal A_j(n)=\prod_hP_h(n)^{w_{j,h}}
$$



of one common total factor degree



$$
\sum_hw_{j,h}=K,                                       \tag{6.1}
$$



and integer coefficients $c_j$.  Define the primitive residual sum



$$
\mathcal R(n)=\sum_jc_j\mathcal A_j(n).                 \tag{6.2}
$$



Its conservative coefficient height is



$$
H_\Sigma
:=\log\left(\sum_j|c_j|\mathcal A_j(n)\right).          \tag{6.3}
$$



This definition does not claim a saving from accidental archimedean
cancellation.  Zero-coefficient terms are omitted, and the admissible
sum is required to be nonzero.

Let



$$
\mathcal D_j(n)=\prod_h\mathcal C_h(n)^{w_{j,h}}.
$$



Because all monomials have degree $K$, equation (2.2) gives, modulo
every $Q\mid q_n$,



$$
\sum_jc_j\mathcal D_j(n)
\equiv
\bigl(-q_{n+1}^{\,2}\bigr)^K\mathcal R(n)\pmod Q.       \tag{6.4}
$$



The factor on the right is a unit modulo $Q$.  Therefore



$$
\boxed{
\gcd\!\left(Q,\sum_jc_j\mathcal D_j(n)\right)
=\gcd(Q,\mathcal R(n)).}                               \tag{6.5}
$$



Now fix $p^s\Vert Q$, and put



$$
u_j=v_p(c_j\mathcal A_j(n)),\qquad
u=\min_j u_j.                                          \tag{6.6}
$$



If the minimum is attained at exactly one index, then the ultrametric
inequality is strict and



$$
\boxed{v_p(\mathcal R(n))=u.}                          \tag{6.7}
$$



No new depth appears.  If the minimum is tied, factor $p^u$:



$$
v_p(\mathcal R(n))
=u+v_p\!\left(\sum_j{c_j\mathcal A_j(n)\over p^u}\right).
                                                               \tag{6.8}
$$



The second term is a genuine cancellation congruence.  It is not
determined by the separate return valuations.

This split can be expressed globally.  Put



$$
B=\gcd_j|c_j\mathcal A_j(n)|,
$$





$$
G_0=\gcd(Q,B),\qquad G_\Sigma=\gcd(Q,\mathcal R(n)).
                                                               \tag{6.9}
$$



Then $G_0\mid G_\Sigma$.  The quotient



$$
\boxed{\mathcal X_\Sigma={G_\Sigma\over G_0}}           \tag{6.10}
$$



is the sum-only cancellation factor.  At a prime where the minimum in
(6.6) is unique, that prime does not occur in
$\mathcal X_\Sigma$.

Unlike a product, a tied sum of $p$-unit monomials may vanish modulo
$p$.  Sums can therefore touch a prime which is strictly isolated
from every selected return.  This is why the product no-go cannot be
extended to arbitrary sums.

The first genuinely admissible sum theorem would exhibit a deterministic,
prime-independent choice of gaps and coefficients such that



$$
\mathcal R(n)\ne0,\qquad H_\Sigma=O(n),                 \tag{6.11}
$$



and prove either



$$
Q\mid\mathcal R(n)                                     \tag{6.12}
$$



or a positive-linear actual-family bound



$$
\log\mathcal X_\Sigma\ge\delta n.                      \tag{6.13}
$$



Equation (6.12) would immediately give $\log Q=O(n)$.  Equation
(6.13), with the required capacity correlation, would be a genuinely
new positive-linear source.  Neither statement is proved.

Allowing coefficients to depend on the unknown factorization of $Q$,
on the target prime, or on $v_p(q_n)$ makes (6.12) tautological and is
not admitted.  Nonhomogeneous scalar sums have different boundary-unit
powers in (6.4); they may also cancel, but are outside the clean
homogeneous reduction and remain open.

## 7. Capacity decision

### PROVED

* The unbounded product divisor and efficiency bounds (1.8)–(1.10).
* The $O(n)$-height multiplicity ceiling (1.12).
* The positive-linear high-efficiency necessity (1.14) and conditional
  zero-capacity statement (1.15)–(1.16).
* The diminishing power-layer theorem (1.17).
* The exact unrestricted canonical optimizer (1.18) and uniform
  sublinear certified capacity (1.19).
* The exact de-overlapped optimization (5.1).
* The homogeneous sum reduction (6.4)–(6.5), unique-minimum theorem
  (6.7), and cancellation quotient (6.10).

### PROVED SCOPED NO-GO

* Unbounded artificial powering cannot improve primitive overlap
  efficiency or create new support.
* Repeated bounded-depth returns at fixed primes have zero
  positive-linear capacity under an $O(n)$ height budget.
* Unbounded canonical anti-period portfolios have only $o(n)$
  certified capacity.
* A product can have positive linear de-overlapped capacity only through
  actual high-efficiency short returns.  This does not rule out those
  returns.

### EXACT FINITE ONLY

* The deterministic checker replays product capture, overlap
  majorization, scalar/residual equality, diminishing layers, the
  unrestricted canonical optimizer, and homogeneous-sum cancellation.
* Its tied-cancellation witness illustrates the exact algebraic branch;
  it is not a density claim or an exceptional-prime census.

### OPEN

* An actual-family high-efficiency or weighted return-cover theorem such
  as (5.2) or (5.3).
* A prime-independent homogeneous sum with proved target cancellation
  divisibility or positive-linear cancellation mass.
* Nonhomogeneous sums, arbitrary growing block/Hankel determinants, and
  other genuinely new global constructions.
* The uniform estimate $v_p(q_n)\log p=O(n)$, a sufficient little-oh
  squarefull aggregate, and the clearing/transverse matching
  correlation.
* Route 1 and every conclusion about $e+\pi$.

### BOOKING



$$
\boxed{
\text{new Route-1 rate}=0,\qquad
\text{new beta capacity reduction}=0.}                 \tag{7.1}
$$



The Item-265 high-singleton ceiling and its two-copy normalization remain
unchanged.

## 8. Deterministic replay

From the archive root:

~~~text
python scripts/item282_beta_unbounded_portfolio_certificate.py ^
  --output results/item282_beta_unbounded_portfolio_certificate_replay.json
~~~

The checker is Python-standard-library only, deterministic, and uses
exact integer arithmetic.  The canonical result and replay must be
byte-identical.
