> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 399 — ordinary-$j=2$ raywise chosen-prime collision invariant

Checked: 2026-09-01 (Beijing time)

## 1. Scope and outcome

Item 397 proved that the safely saturated fixed-$M$ factors are atomic:
each nontrivial factor is its own selected prime, and distinct rows have
no high-prime gcd to reuse.  This item therefore abandons gcd overlap and
attacks the collision condition itself on the two prime rays.

No positive-density exclusion is proved.  The main result is instead an
exact chosen-prime algebraic-integer formulation of the live
nondegenerate condition, together with a proof that taking its ordinary
Galois norm loses precisely the selected cutoff and has noncompetitive
height.

> **PROVED — exact chosen-prime residual integer.**  On the
> $\ell_r\ne0\pmod p$ chart, there is an explicit algebraic integer
> $\Xi_{p,r,s}\in\mathbb Z[\mu_{p-1}]$, retaining the actual moving
> target, such that at the Teichmuller-selected prime
> $\mathfrak P_p\mid p$,
> 

$$
>  \boxed{\Xi_{p,r,s}\equiv
>  Q_{r,s}\bigl(H_{s-1}-\Theta_{r,s}\bigr)
>  \pmod{\mathfrak P_p},}
> \tag{1.1}
>
$$


> where $Q_{r,s}$ is a certified $p$-unit denominator clearer.

> **PROVED — exact two-coordinate ideal.**  Put
> 

$$
>  E_{p,r,s}
>  =\operatorname{num}\!\left(
>  18\,4^s\mathfrak a_r+11\mathfrak b_r\right).
> \tag{1.2}
>
$$


> Then on the nondegenerate chart,
> 

$$
> \boxed{
> p\text{ is an actual collision}
> \iff
> p\mid E_{p,r,s}
> \ \text{and}\ 
> \mathfrak P_p\mid\Xi_{p,r,s}.}
> \tag{1.3}
>
$$


> Equivalently, the ideal
> $(E_{p,r,s},\Xi_{p,r,s})$ is contained in
> $\mathfrak P_p$.

> **PROVED — Galois-norm selector obstruction.**  The conjugates of
> $\Xi_{p,r,s}$ replace the ordered cutoff
> $\{0,1,\ldots,m\}$ by the multiplicatively permuted cutoffs
> 

$$
>  a\{0,1,\ldots,m\}\pmod{p-1},
>  \qquad a\in(\mathbb Z/(p-1)\mathbb Z)^\times.
> \tag{1.4}
>
$$


> Thus
> 

$$
>  \mathfrak P_p\mid\Xi_{p,r,s}
>  \Longrightarrow p\mid
>  \operatorname{Norm}_{\mathbb Q(\mu_{p-1})/\mathbb Q}
>  (\Xi_{p,r,s}),
> \tag{1.5}
>
$$


> but the converse asks only that some conjugate cutoff vanish at some
> prime above $p$.  It does not retain the selected cutoff.

> **PROVED — norm height is noncompetitive.**  On the positive-rate
> bulk, the currently certified bound is
> 

$$
>  \log^+\left|
>  \operatorname{Norm}(\Xi_{p,r,s})\right|
>  =O(M^2\log M)
> \tag{1.6}
>
$$


> per row.  This is far larger than the whole ray's $O(M)$ prime
> mass.  Exact-zero norms would require a separate stratum and give no
> divisor bound at all.

The minimal missing nondegenerate theorem is now a chosen-prime
nonconcentration statement for (1.3), not complex nonvanishing of a
Jacobi sum and not divisibility of its rational norm.  A full ray theorem
must also control Item 349's degenerate carrier; otherwise the
degenerate chart could still occupy the entire ray.

Each ray has logarithmic mass



$$
\frac1{35}M+o(M)
\tag{1.7}
$$



and normalized capacity $1/210$.  Hence a full $o(M)$ theorem on
one ray would improve the ordinary-$j=2$ ceiling by $1/210$; a
weighted exclusion of a fraction $\rho$ of that ray would improve it
by $\rho/210$.  This item proves neither, so



$$
\boxed{\eta=0},\qquad
 \boxed{\Delta\text{ capacity}=0},\qquad
 \boxed{\text{shared ceiling}=1/105}.
\tag{1.8}
$$



## 2. The two rays and their capacity

For an actual row,



$$
p=2r+6s+3,\qquad
 r=6M-7p,\qquad
 s=\frac{5p-4M-1}{2}.
\tag{2.1}
$$



The two admissible residues are



$$
\begin{array}{c|c}
r\bmod6&p\bmod6\\ \hline
1&5\\
5&1.
\end{array}
\tag{2.2}
$$



The prime number theorem in arithmetic progressions, applied at the two
fixed proportional endpoints, gives



$$
\sum_{\substack{p\in I_M\\p\equiv1\pmod6}}\log p
 =\frac1{35}M+o(M),
\qquad
 \sum_{\substack{p\in I_M\\p\equiv5\pmod6}}\log p
 =\frac1{35}M+o(M).
\tag{2.3}
$$



Let $W_e^{\rm nd}(M)$ and $W_e^{\rm deg}(M)$ denote the actual
collision masses on the $r\equiv e\pmod6$ ray, split by whether the
three connection minors vanish.  Then



$$
W_e(M)=W_e^{\rm nd}(M)+W_e^{\rm deg}(M)
 \leq\frac1{35}M+o(M).
\tag{2.4}
$$



An $o(M)$ theorem for $W_e^{\rm nd}$ alone does not permit a fixed
booking unless a complementary upper bound for $W_e^{\rm deg}$ is
also proved.

## 3. The exact nondegenerate affine coordinates

Put $m=s-1$.  Item 341 gives, on $\ell_r\ne0\pmod p$,



$$
D=9\ell_r(4^s-c_r^*),
\qquad
 T_\ell=-\epsilon_pK_{r,s}\ell_r
          (H_m-\Theta_{r,s}),
\tag{3.1}
$$



with all displayed multipliers $p$-units.  The branch normalization is



$$
c_r^*=-\frac{11\mathfrak b_r}{18\mathfrak a_r}.
\tag{3.2}
$$



Therefore the first coordinate is exactly



$$
p\mid
 \operatorname{num}\!\left(
 18\,4^s\mathfrak a_r+11\mathfrak b_r\right),
\tag{3.3}
$$



which is (1.2).  The second coordinate is the genuine incomplete-beta
prefix



$$
H_m=\sum_{u=0}^m\frac1{8^u}\binom{2u}{u}
\tag{3.4}
$$



against the moving connection target $\Theta_{r,s}$.

The Jacobian in Item 341 is a unit.  Thus (3.3) and
$H_m=\Theta_{r,s}$ are independent affine coordinates after
localization.  No polynomial manipulation of the first gate forces the
second one.

## 4. Construction of the chosen-prime algebraic integer

Set



$$
N=p-1,\qquad
 K_p=\mathbb Q(\mu_N).
\tag{4.1}
$$



Choose the prime $\mathfrak P_p\mid p$ determined by the
Teichmuller character



$$
\omega:\mathbb F_p^\times\longrightarrow\mu_N,
\qquad
 \omega(x)\equiv x\pmod{\mathfrak P_p}.
\tag{4.2}
$$



Put



$$
B_u=\omega^{-u},\qquad
 \varphi=\omega^{N/2}.
\tag{4.3}
$$



Item 347's chosen-prime identity is



$$
H_m\equiv
 -\sum_{u=0}^mB_u(2)J(B_u,\varphi)
 \pmod{\mathfrak P_p}.
\tag{4.4}
$$



Write the reduced moving target as



$$
\Theta_{r,s}=\frac{A_{r,s}}{Q_{r,s}},
\qquad Q_{r,s}>0,\qquad
 p\nmid Q_{r,s}.
\tag{4.5}
$$



Jacobi sums are algebraic integers.  Hence



$$
\boxed{
 \Xi_{p,r,s}
 =-Q_{r,s}\sum_{u=0}^m
       B_u(2)J(B_u,\varphi)-A_{r,s}
 \in\mathcal O_{K_p}.}
\tag{4.6}
$$



Reducing (4.6) at $\mathfrak P_p$ proves (1.1).  Combining it with
(3.3) proves (1.3).

The construction retains all three pieces that cannot be discarded:

1. the actual ordered cutoff $0\leq u\leq m$;
2. the actual Teichmuller prime above $p$; and
3. the actual moving rational target $\Theta_{r,s}$.

## 5. Exact Galois action and why the norm is the wrong invariant

For



$$
a\in(\mathbb Z/N\mathbb Z)^\times,
\tag{5.1}
$$



let $\sigma_a(\zeta_N)=\zeta_N^a$.  Since every such $a$ is odd,
$\sigma_a(\varphi)=\varphi$, while



$$
\sigma_a(B_u)=B_{au}.
\tag{5.2}
$$



The target in (4.5) is rational and fixed.  Consequently



$$
\boxed{
 \sigma_a(\Xi_{p,r,s})
 =-Q_{r,s}\sum_{u=0}^m
 B_{au}(2)J(B_{au},\varphi)-A_{r,s}.}
\tag{5.3}
$$



This proves the cutoff permutation (1.4).  Except for stabilizers, the
conjugates are different incomplete subsets of the $N$ Kummer modes.
Only $a=1$ is the actual ordered prefix.

The rational norm is



$$
\operatorname{Norm}(\Xi_{p,r,s})
 =\prod_{a\in(\mathbb Z/N\mathbb Z)^\times}
       \sigma_a(\Xi_{p,r,s}).
\tag{5.4}
$$



Because $p\equiv1\pmod N$, $p$ splits completely in $K_p$.
If the selected prime divides $\Xi$, then $p$ divides (5.4).
Conversely, $p\mid\operatorname{Norm}(\Xi)$ says that some prime
above $p$ divides $\Xi$, equivalently that a conjugate cutoff can
vanish after the corresponding Teichmuller identification.  It is a
strict support enlargement unless a new theorem proves all conjugate
cutoffs equivalent.

This is the exact chosen-prime obstruction: an ordinary norm converts
one specified local coordinate into an existential statement over its
whole Galois orbit.

## 6. Height of the norm

For the two exceptional Jacobi modes the complex absolute value is one;
for every other mode it is $\sqrt p$.  Therefore every embedding
satisfies



$$
|\sigma_a(\Xi_{p,r,s})|
 \leq Q_{r,s}\bigl(1+m\sqrt p\bigr)+|A_{r,s}|.
\tag{6.1}
$$



Items 334 and 341 give



$$
h(\Theta_{r,s})=O(M\log M),
\qquad p,m=O(M).
\tag{6.2}
$$



Since



$$
[K_p:\mathbb Q]=\varphi(p-1)\leq p-1=O(M),
\tag{6.3}
$$



multiplying (6.1) over the embeddings yields



$$
\log^+|\operatorname{Norm}(\Xi_{p,r,s})|
 \leq\varphi(p-1)
 \left(h(\Theta_{r,s})+\log(2+m\sqrt p)+O(1)\right)
 =O(M^2\log M).
\tag{6.4}
$$



Thus the norm is not a low-height prime-independent replacement for the
chosen-prime residual.  Moreover, if $\Xi_{p,r,s}=0$ as an algebraic
integer, its norm is zero and height supplies no divisor restriction;
that stratum is not presently excluded.

## 7. The exact raywise theorem still missing

For $e\in\{1,5\}$, define the nondegenerate chosen-prime zero set



$$
\begin{aligned}
 \mathcal Z_e^{\rm nd}(M)=
 \{p\in I_M:\;&r=6M-7p\equiv e\pmod6,\ 
 \ell_r\ne0\pmod p,\\
 &p\mid E_{p,r,s},\
 \mathfrak P_p\mid\Xi_{p,r,s}\}.
\end{aligned}
\tag{7.1}
$$



The desired nondegenerate theorem is



$$
\boxed{
 \sum_{p\in\mathcal Z_e^{\rm nd}(M)}\log p=o(M).}
\tag{7.2}
$$



For the degenerate chart, Item 349 supplies



$$
p\mid\widehat\Pi_{r,s}
\tag{7.3}
$$



as the exact triple-minor gate, after which the surviving Item-334
coordinate residual must still vanish.  Let the corresponding actual
zero set be $\mathcal Z_e^{\rm deg}(M)$.  A full ray theorem requires



$$
\boxed{
 \sum_{p\in\mathcal Z_e^{\rm deg}(M)}\log p=o(M)}
\tag{7.4}
$$



as well as (7.2).

Equations (7.2) and (7.4) are the minimal arithmetic inputs still
missing.  The first is a chosen-prime, moving-target, growing-rank
hypergeometric nonconcentration theorem.  The second is a moving-divisor
theorem for the degenerate primitive carrier plus its surviving target
coordinate.

## 8. Capacity audit

Suppose a theorem excludes a subset of one complete ray having
Chebyshev mass



$$
\frac{\rho}{35}M+o(M),
\qquad0\leq\rho\leq1.
\tag{8.1}
$$



Then



$$
\eta=\frac{\rho}{35}\quad\text{per }M,
\qquad
 \Delta\mathcal C=\frac{\rho}{210}\quad\text{per }6M.
\tag{8.2}
$$



The cases are:



$$
\begin{array}{c|c|c}
\text{result}&\eta\text{ per }M&
\Delta\mathcal C\text{ per }6M\\ \hline
\text{half of one full ray}&1/70&1/420\\
\text{one full ray }o(M)&1/35&1/210\\
\text{both rays }o(M)&2/35&1/105.
\end{array}
\tag{8.3}
$$



If only (7.2) is proved and no strict upper bound is known for (7.4),
the bookable $\rho$ remains zero.  The same warning applies with the
charts reversed.

## 9. What has and has not been closed

**Closed as sufficient by itself:**

- complex nonvanishing or Weil size of the individual Jacobi sums;
- taking the ordinary Galois norm of the chosen-prime residual;
- a theorem about an unspecified prime above $p$;
- a nondegenerate theorem with no quantitative control of the degenerate
  chart; and
- endpoint local solubility alone, already settled by Item 397.

**Still live:**

- a $p$-adic unit-root or Frobenius-coordinate theorem at the specified
  $\mathfrak P_p$;
- a target-specific cancellation compressing (4.6) without permuting its
  cutoff;
- weighted distribution for the growing-rank selected residual ideal
  $(E,\Xi)$;
- a direct one-ray nonvanishing theorem for the actual Item-334 carrier;
  and
- the degenerate moving-divisor theorem (7.4).

## 10. Deterministic certificate and ledger

The certificate verifies the frozen Items 341, 347, 349, 394, and 397
dependencies, reconstructs the actual moving target on declared rows,
replays the complete quadratic/Jacobi reduction of (4.4), checks the two
ray parametrizations, and verifies the exact capacity fractions.

Every enumerated row and character sum is labelled
**EXACT FINITE ONLY / DIAGNOSTIC**.  The algebraic-integer construction,
Galois action, norm implication, height audit, and capacity statements
are proved in Sections 4-8 and are not inferred from finite data.

Ledger:

- proved ray exclusion: none;
- proved $\eta$: $0$;
- booked lower bound: unchanged;
- ordinary-$j=2$ ceiling: $1/105$;
- new minimal invariant: the selected-prime ideal
  $(E_{p,r,s},\Xi_{p,r,s})$, together with the separate degenerate
  target-retaining gate.

