> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 346 — first-hit localization of the beta (t)-avoiding radical

Checked: 2026-09-01 (Beijing time)

## 1. Strict verdict and capacity admission

Assume the actual Item-316 target.  Retain



$$
A=4n-2,
\qquad
m=n-2,
\qquad
a=q_{n-1},\quad b=q_n,\quad c=q_{n-2},
\tag{1.1}
$$



Item 340's exact quotient



$$
t=c-\kappa,
\qquad
bt=T+\epsilon R,
\tag{1.2}
$$



and Item 337's nonzero adjacent cofactors



$$
\mathfrak z_j
=\epsilon(\delta_j-w_j\delta_{j-1})
\qquad(3\le j\le m).
\tag{1.3}
$$



For a declared de-overlapped target $Q\mid b$, Item 343 isolates



$$
R_Q^\perp
=\prod_{\substack{p\mid Q,\ p\mid\Lambda\\p\nmid t}}p,
\qquad
\Xi_Q=\log R_Q^\perp.
\tag{1.4}
$$



This is the only new squarefree part of (K_Q).  Neither the quotient-covered
part (H_Q) nor Item 265's repeated-prime squarefull excess is included in
Item 346.

The capacity screen must come first.  Before using any new theorem,



$$
\boxed{
0\le\Xi_Q\le\log\operatorname{rad}(Q)
\le\log Q\le\log b.}
\tag{1.5}
$$



Thus the raw maximum is still one complete beta-scale target copy.  The
height screen alone does not give a strict fraction.

Item 346 proves three global statements.

1. $R_Q^\perp$ has an exact specialization-first carrier and a pairwise
   coprime first-hit factorization over all depths.
2. All primes at most (A) have zero beta rate.  Every remaining first-hit
   factor is either one or a single prime in ((A,A^2)).  Hence positive
   linear (Xi_Q) requires linearly many distinct active depths.
3. The formal target equation, the raw cofactor-union congruence, and the
   condition $p\nmid t$ have no integer resultant smaller than the original
   carrier (b).  A uniform unstratified resultant therefore cannot prove the
   missing average theorem.

These statements meaningfully localize the open branch, but they do not bound
its mesoscopic first-hit average.  No capacity is booked.

## 2. Exact global carrier away from (t)

Let



$$
\mathcal J(\delta)
=\{j:3\le j\le m,\ \mathfrak z_j(\delta)\ne0\}.
\tag{2.1}
$$



The omission of exact zero rows is essential: a zero integer contributes no
prime to the lcm.  Put



$$
M_A=\left\lceil\log_2(A^2)\right\rceil
\tag{2.2}
$$



and, for $j\in\mathcal J(\delta)$, define the full $t$-away part



$$
u_j
=\frac{|\mathfrak z_j|}
{\gcd(|\mathfrak z_j|,t^{M_A})}.
\tag{2.3}
$$



Every canonical digit satisfies



$$
|\mathfrak z_j|
\le w_jw_{j-1}<A^2.
\tag{2.4}
$$



Consequently $M_A\ge v_p(\mathfrak z_j)$ for every prime $p$.  If
$p\mid t$, the gcd in (2.3) removes the complete $p$-primary part of
$\mathfrak z_j$; if $p\nmid t$, it removes none of it.  Therefore the
exact global (t)-away carrier is



$$
\mathcal C_t(\delta)
=\operatorname{rad}
\operatorname{lcm}_{j\in\mathcal J(\delta)}u_j,
\tag{2.5}
$$



with an empty lcm equal to one, and



$$
\boxed{
R_Q^\perp
=\gcd(\operatorname{rad}(Q),\mathcal C_t(\delta)).}
\tag{2.6}
$$



Equation (2.6) is an actual-family implication: the word, its nonzero-row
set, (t), and (Q) are precisely those supplied by the hypothetical
Item-316 target.  It does not replace that word by an ambient witness.

## 3. Pairwise-coprime first-hit localization

Order the depths increasingly.  Put (F_2=1).  For
$j=3,\ldots,m$, set $B_j=1$ when $\mathfrak z_j=0$, and otherwise set



$$
B_j
=\gcd\!\left(
\operatorname{rad}(Q),\operatorname{rad}(u_j)
\right).
\tag{3.1}
$$



Define recursively



$$
D_j=\frac{B_j}{\gcd(B_j,F_{j-1})},
\qquad
F_j=\operatorname{lcm}(F_{j-1},B_j)=F_{j-1}D_j.
\tag{3.2}
$$



All (B_j,F_j,D_j) are squarefree.  The factors (D_j) are pairwise
coprime, and induction gives



$$
F_m=R_Q^\perp.
\tag{3.3}
$$



Thus



$$
\boxed{
R_Q^\perp=\prod_{j=3}^{m}D_j,
\qquad
\Xi_Q=\sum_{j=3}^{m}\log D_j.}
\tag{3.4}
$$



Equivalently, every prime is assigned to the first depth at which it divides
a nonzero cofactor.  Repeated appearances at later depths contribute zero.
This is an exact average-gcd formulation, not a union bound.

For every subset $S\subseteq\{3,\ldots,m\}$, (2.4) gives



$$
\boxed{
\sum_{j\in S}\log D_j
\le\sum_{j\in S}\log^+|\mathfrak z_j|
<2|S|\log A.}
\tag{3.5}
$$



Consequently every $o(n)$-depth portfolio has $o(\log b)$ capacity.
This extends the fixed-complexity closure of Item 335 to every sublinear
number of explicitly selected cofactor depths.

## 4. The mesoscopic-prime theorem

Split each first-hit factor at (A):



$$
D_j=D_j^{\le A}D_j^{>A}.
\tag{4.1}
$$



Because the (D_j)'s are pairwise coprime,



$$
\sum_j\log D_j^{\le A}
\le\vartheta(A)
:=\sum_{p\le A}\log p.
\tag{4.2}
$$



The elementary Chebyshev bound obtained from central binomial coefficients is



$$
\vartheta(x)=O(x).
\tag{4.3}
$$



Since $A=4n-2$ and $\log b=n\log n+O(n)$,



$$
\boxed{
\sum_j\log D_j^{\le A}
=O(A)=o(\log b).}
\tag{4.4}
$$



For the remaining factors, (2.4) implies a much sharper structure.  A
nonzero integer smaller than (A^2) cannot contain two distinct prime
divisors larger than (A).  Hence



$$
\boxed{
D_j^{>A}=1
\quad\hbox{or}\quad
D_j^{>A}=p_j\text{ for one prime }A<p_j<A^2.}
\tag{4.5}
$$



The nontrivial $p_j$'s are pairwise distinct, divide $Q$ and hence $b$,
divide $\mathfrak z_j$, and do not divide $t$.

There is also an exact local shape.  If $p>A$ divides a nonzero
$\mathfrak z_j$, then $\delta_{j-1}$ cannot be zero.  If
$\delta_{j-1}=1$, canonicality gives $\delta_j\le w_j-1$, making



$$
|\delta_j-w_j\delta_{j-1}|<A.
\tag{4.6}
$$



Thus $\delta_{j-1}\ge2$, the unsigned cofactor is negative before taking
absolute values, and



$$
\boxed{
w_j\delta_{j-1}-\delta_j=p_jh_j,
\qquad
1\le h_j<A.}
\tag{4.7}
$$



Equations (4.4)-(4.5) yield the exact asymptotic reformulation



$$
\boxed{
\Xi_Q
=\sum_{\substack{3\le j\le m\\D_j^{>A}>1}}
\log p_j+o(\log b).}
\tag{4.8}
$$



In particular,



$$
\Xi_Q=o(\log b)
\iff
\frac1m\sum_{j=3}^{m}\log D_j^{>A}=o(\log A).
\tag{4.9}
$$



If, along a subsequence, $\Xi_Q\ge\eta\log b$ for a fixed
$\eta>0$, let



$$
r_A=\#\{j:D_j^{>A}>1\}.
\tag{4.10}
$$



Then (4.5) and $\log b/\log A=(1+o(1))n$ give



$$
\boxed{
r_A\ge\left(\frac\eta2+o(1)\right)n.}
\tag{4.11}
$$



Thus positive-linear (t)-avoiding radical mass cannot be supported on a
thin exceptional set of depths.  It requires a positive-density matching
between distinct mesoscopic prime divisors of (b) and the actual canonical
cofactors.

No theorem here bounds that matching.  The raw one-copy ceiling (1.5)
therefore remains possible under the current knowledge.

## 5. Why the raw resultant returns only (b)

This section proves a scoped algebraic obstruction.  It does not replace the
actual nonzero-row carrier (2.5).

Let



$$
\mathcal A=\mathbb Z[d_1,\ldots,d_m]
\tag{5.1}
$$



and retain Item 333's target defect



$$
\Delta_\sigma=\sigma E_{m+1}-a.
\tag{5.2}
$$



Put



$$
z=\epsilon(d_m-w_md_{m-1})=\mathfrak z_m.
\tag{5.3}
$$



Item 333's unimodular transformation gives



$$
\mathcal A/(\Delta_\sigma)
\cong
\mathbb Z[d_1,\ldots,d_{m-2},z].
\tag{5.4}
$$



Write the lower part of $\kappa=\sigma E_m$ as



$$
\kappa_<
=\sigma\sum_{i=1}^{m-2}
(-1)^{i-1}\Delta_{i-1}d_i.
\tag{5.5}
$$



The two top coefficients of (E_m) give the exact identity



$$
\boxed{
\kappa=\kappa_<-z,
\qquad
t=c-\kappa_<+z.}
\tag{5.6}
$$



On the component (z=0), the quotient polynomial is



$$
t_0=c-\kappa_<.
\tag{5.7}
$$



It is primitive over $\mathbb Z$.  For $m\ge4$, the coefficient list in
(5.5) contains two consecutive suffix continuants
$\Delta_{m-4},\Delta_{m-3}$, whose gcd is one by the continuant recurrence
and the boundary value $\Delta_{m-1}=1$.  For the sole case $m=3$,



$$
c=71,
\qquad
\Delta_0=K(10,14)=141,
\qquad
\gcd(71,141)=1.
\tag{5.8}
$$



For an ideal (I), write



$$
I:t^\infty
=\{F:\ t^kF\in I\text{ for some }k\ge0\}.
\tag{5.9}
$$



Then



$$
\boxed{
\bigl((b,\Delta_\sigma,z):t^\infty\bigr)\cap\mathbb Z
=(b).}
\tag{5.10}
$$



Indeed, if an integer (r) belongs to the left side, then in the quotient
by $\Delta_\sigma,z$, every coefficient of $r t_0^k$ is divisible by
(b) for some (k).  Gauss's content lemma and primitivity of (t_0) give



$$
\operatorname{cont}(r t_0^k)=|r|.
\tag{5.11}
$$



Hence $b\mid r$.  The reverse inclusion is immediate.

Now form the raw algebraic union polynomial



$$
\mathscr P=\prod_{j=3}^{m}\mathfrak z_j.
\tag{5.12}
$$



Since $\mathscr P\in(z)$, (5.10) implies



$$
\boxed{
\bigl((b,\Delta_\sigma,\mathscr P):t^\infty\bigr)
\cap\mathbb Z=(b).}
\tag{5.13}
$$



Therefore a formal elimination or resultant which encodes “some cofactor
vanishes modulo $p$” only through the unstratified product $\mathscr P$,
even after enforcing $p\nmid t$, returns no integer carrier smaller than
$b$.  Its height is exactly the full unresolved target scale.

There is an important scope boundary.  The polynomial $\mathscr P$ has
exact-zero components, whereas $\Lambda$ omits exact zero rows before
taking its lcm.  Equation (5.13) explains why a raw resultant cannot perform
that arithmetic omission.  It does **not** close a growing stratification by
the actual zero pattern, nor the first-hit average in (4.9).  Those are
non-polynomial, specialization-first inputs.

## 6. Admission decision and next exact lemma

The Item-346 decision is now rigid.

* Small $t$-avoiding primes have zero rate by (4.4).
* Any (o(n)) selected depth portfolio has zero rate by (3.5).
* Every possible positive-rate survivor is a distinct prime
  (A<p_j<A^2) attached to its first active depth by (4.7).
* The raw target/resultant ideal supplies only (b), not a smaller carrier.

The smallest remaining Closer statement is



$$
\boxed{
\sum_{j=3}^{m}\log D_j^{>A}=o(n\log n).}
\tag{6.1}
$$



Equivalently, prove that the actual canonical target cannot have a
positive-density matching of the form (4.7) with distinct primes dividing
(b) and avoiding (t).

A Builder theorem would require the opposite kind of actual-family result:
for some explicit $\eta>0$, prove such a matching at at least
$(\eta/2+o(1))n$ depths and hence obtain $\Xi_Q\ge\eta\log b$ after all
old factors are removed.  Ambient digit words do not qualify.

No presently proved theorem gives either conclusion.  Increasing quotient
precision, using a bounded number of cofactors, or taking one unstratified
resultant cannot decide (6.1).

## 7. Strict labels

### PROVED

* The specialization-first (t)-away carrier (2.5)-(2.6).
* The pairwise-coprime first-hit factorization (3.1)-(3.4).
* The (o(n))-depth capacity bound (3.5).
* The small-prime zero-rate theorem (4.4).
* The one-mesoscopic-prime-per-active-depth theorem (4.5)-(4.7).
* The exact average formulation (4.8)-(4.9) and density necessity (4.11).
* The primitive quotient identity (5.6)-(5.8).
* The localized constant-ideal equalities (5.10) and (5.13).

### PROVED SCOPED NO-GO

* No sublinear-depth cofactor portfolio can carry positive beta-scale
  (t)-avoiding radical mass.
* Formal target elimination with the raw cofactor-union product and (t)
  inverted yields only the original full-height carrier (b).
* These statements do not close the growing specialization-first first-hit
  average.

### EXACT FINITE ONLY

* The deterministic replay's declared coordinate, carrier, first-hit, and
  mesoscopic-factor controls.
* Declared off-target seed rows test identities only.  No bounded row is used
  as evidence for density, the half-bound, or an actual target.

### OPEN

* The actual average (6.1), every strict fractional bound for $\Xi_Q$, and
  every positive actual-family lower bound.
* Growing zero-pattern stratification or a genuinely arithmetic global
  resultant after exact-zero rows are omitted.
* $H_Q$, Item 265's squarefull excess, and hence $K_Q$ and $\Gamma_Q$.
* The Item-316 centered half-bound, beta capacity, Route 1, and $e+\pi$.

### BOOKING



$$
\boxed{
\text{new beta capacity reduction}=0,
\qquad
\text{new Route-1 rate}=0.}
\tag{7.1}
$$



No canonical, master, status, checkpoint, or research-log file is edited by
this work package.

## 8. Deterministic replay

From the archive root:

~~~text
python work/item346_beta_t_avoiding_radical_localization_certificate.py ^
  --output work/item346_beta_t_avoiding_radical_localization_certificate.replay.json
~~~

The checker uses only the Python standard library and exact integer
arithmetic.  It performs no prime census, target search, or half-bound scan
and promotes no bounded row.
