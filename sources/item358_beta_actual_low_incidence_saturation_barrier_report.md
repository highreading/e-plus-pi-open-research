> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 358 — actual low-incidence saturation and the singleton-squarefree barrier

Checked: 2026-09-01 (Beijing time)

## 1. Strict verdict and capacity admission

Assume the genuine canonical Item-316 target.  Retain



$$
A=4n-2,
\qquad m=n-2,
\qquad Q\mid b,
\qquad t=c-\kappa,
\tag{1.1}
$$



and Item 346's nonzero canonical cofactors



$$
\mathfrak z_j
=\epsilon(\delta_j-w_j\delta_{j-1}),
\qquad 3\le j\le m.
\tag{1.2}
$$



Exact-zero rows are omitted before every product below.  Item 354 reduces the
new $t$-avoiding radical problem to the actual low-incidence squarefree mass



$$
\Sigma_{<L}^{(1)}
=\sum_{\substack{A<p<A^2,\ p\mid Q,\ p\nmid t,\ v_p(Q)=1\\
1\le\nu_p<L}}
\log p,
\tag{1.3}
$$



where $\nu_p$ is the number of nonzero cofactor rows divisible by $p$.
The raw admission ceiling is still



$$
0\le\Sigma_{<L}^{(1)}\le\log Q\le\log b.
\tag{1.4}
$$



Item 358 gives an exact specialization-first carrier for every incidence set,
including the genuine first-and-only occurrence condition.  It then proves a
scoped barrier theorem.

1. Pairwise-gcd data and squarefull data are primewise disjoint from the
   singleton-squarefree carrier.
2. Every uniform scheme-theoretic polynomial union carrier which sees a
   singleton component at every possible row must contain the full row
   product; its degree grows linearly.
3. Splitting the rows into disjoint windows does not change the aggregate
   height budget.  The direct carrier retains the full $\log b$ ceiling.

No asymptotic upper bound for (1.3) is proved.  The first missing theorem is
an actual gcd-correlation estimate for the saturated low-incidence carrier.
Booking remains zero.

## 2. Exact incidence-set saturation on the canonical word

Let



$$
\mathcal J
=\{j:3\le j\le m,\ \mathfrak z_j\ne0\},
\qquad
Z_j=|\mathfrak z_j|\quad(j\in\mathcal J),
\tag{2.1}
$$



and retain Item 346's exponent



$$
M_A=\lceil\log_2(A^2)\rceil.
\tag{2.2}
$$



For every nonempty subset $S\subseteq\mathcal J$, define



$$
g_S=\gcd_{j\in S}Z_j,
\qquad
W_S=|t|\prod_{i\in\mathcal J\setminus S}Z_i,
\tag{2.3}
$$



and the fully saturated incidence-set cofactor



$$
\boxed{
s_S
=\frac{g_S}{\gcd(g_S,W_S^{M_A})}.}
\tag{2.4}
$$



An empty outside product is one.  If $t=0$, then $W_S=0$ and $s_S=1$,
which is correct because no prime is $t$-avoiding.

For a prime $p$, let



$$
\operatorname{Occ}(p)=\{j\in\mathcal J:p\mid Z_j\}.
\tag{2.5}
$$



Because $Z_j<A^2$, the power $W_S^{M_A}$ removes the complete $p$-primary
part of $g_S$ whenever $p\mid W_S$.  Also,



$$
p\mid g_S\iff S\subseteq\operatorname{Occ}(p),
\tag{2.6}
$$



while



$$
p\nmid W_S
\iff
p\nmid t\ \text{ and }\ \operatorname{Occ}(p)\subseteq S.
\tag{2.7}
$$



Therefore



$$
\boxed{
p\mid s_S
\iff
p\nmid t\ \text{ and }\ \operatorname{Occ}(p)=S.}
\tag{2.8}
$$



This is the exact all-depth incidence-set theorem.  The nontrivial $s_S$ are
pairwise coprime.  Unlike Item 350's ambient selected-hit CRT, (2.8) is
evaluated on the unique canonical word and imposes nondivisibility at every
row outside $S$.

For a singleton $S=\{j\}$, (2.4) becomes



$$
\boxed{
s_j
=\frac{Z_j}
{\gcd\!\left(Z_j,
 (|t|\prod_{i\in\mathcal J,\ i\ne j}Z_i)^{M_A}\right)}.}
\tag{2.9}
$$



Thus $p\mid s_j$ if and only if $p$ is $t$-avoiding and $j$ is its unique
cofactor depth.  Genuine first occurrence is automatic because there is no
earlier or later occurrence.

## 3. The exact fresh low-incidence carrier

Write



$$
E(Q)=\frac{Q}{\operatorname{rad}(Q)},
\qquad
Q^{[1]}
=\frac{\operatorname{rad}(Q)}
{\gcd(\operatorname{rad}(Q),\operatorname{rad}(E(Q)))}
=\prod_{v_p(Q)=1}p.
\tag{3.1}
$$



For an integer $N$, let $\operatorname{rad}_{>A}(N)$ be the product of its
prime divisors larger than $A$.  Define



$$
\boxed{
\mathcal U_{<L}^{(1)}
=\gcd\!\left(
Q^{[1]},
\operatorname{rad}_{>A}\!\left(
\prod_{\substack{\varnothing\ne S\subseteq\mathcal J\\|S|<L}}s_S
\right)
\right).}
\tag{3.2}
$$



By (2.8),



$$
\boxed{
\log\mathcal U_{<L}^{(1)}=\Sigma_{<L}^{(1)}.}
\tag{3.3}
$$



This is an exact actual-family formula, not a union bound.  Each relevant
prime appears in exactly one saturated factor $s_S$.

The first layer is the genuine singleton-squarefree carrier



$$
\boxed{
\mathcal U_{1,1}
=\mathcal U_{<2}^{(1)}
=\gcd\!\left(
Q^{[1]},
\operatorname{rad}_{>A}\!\left(\prod_{j\in\mathcal J}s_j\right)
\right).}
\tag{3.4}
$$



The desired first new theorem would be



$$
\log\mathcal U_{1,1}=o(\log b).
\tag{3.5}
$$



No such estimate follows from the exact formula alone.

## 4. Four primewise quadrants and exact overlap separation

For every mesoscopic prime in Item 354's $\mathcal R_1$, record the two
binary attributes



$$
\nu_p=1\ \text{ or }\ \nu_p\ge2,
\qquad
v_p(Q)=1\ \text{ or }\ v_p(Q)\ge2.
\tag{4.1}
$$



Let $\mathcal U_{a,b}$ be the radical carrier in the corresponding quadrant,
where $a=1$ means $\nu_p=1$, $a=2$ means $\nu_p\ge2$, and similarly for
$b$.  Then



$$
\boxed{
\mathcal R_1
=\mathcal U_{1,1}\mathcal U_{1,2}
 \mathcal U_{2,1}\mathcal U_{2,2}.}
\tag{4.2}
$$



Item 354's pairwise carrier and Item 265's excess carrier cover exactly



$$
\boxed{
\mathcal R_2=\mathcal U_{2,1}\mathcal U_{2,2},
\qquad
\gcd(\mathcal R_1,\operatorname{rad}E(Q))
=\mathcal U_{1,2}\mathcal U_{2,2}.}
\tag{4.3}
$$



Consequently



$$
\boxed{
\gcd(\mathcal U_{1,1},\mathcal R_2E(Q))=1.}
\tag{4.4}
$$



This is the exact reason pairwise and squarefull estimates cannot control the
fresh singleton layer.  Repetition of a prime among cofactors and excess
valuation of that prime in $Q$ are independent coordinates.  No squarefull
mass is rebooked in $\mathcal U_{1,1}$.

## 5. The pairwise-moment blind spot

Let $C_j$ be Item 354's mesoscopic row carrier.  The first and second
incidence moments are



$$
I_1=\sum_j\log C_j
=\sum_p\nu_p\log p,
\tag{5.1}
$$



and



$$
I_2=\sum_{j<k}\log\gcd(C_j,C_k)
=\sum_p\binom{\nu_p}{2}\log p.
\tag{5.2}
$$



Every prime in $\mathcal U_{1,1}$ contributes $\log p$ to $I_1$, zero to
$I_2$, and zero to $\log E(Q)$.  Therefore even perfect upper bounds for the
pairwise moment and the squarefull excess leave its full mass untouched.  A
moment argument would need either a new lower bound forcing collisions
relative to $I_1$, or a direct upper bound for (3.4).

The available first-moment height estimate is only



$$
I_1<2N_A\log A\le(2+o(1))\log b,
\tag{5.3}
$$



while intersecting with $Q$ gives



$$
\boxed{
\log\mathcal U_{1,1}\le\log Q\le\log b.}
\tag{5.4}
$$



This is exactly the unresolved one-copy scale.

## 6. Uniform resultant and disjoint-window barrier

The algebraic union obstruction can be stated without a finite scan.  In the
polynomial ring



$$
\mathbb Z[Y_1,\ldots,Y_N],
\tag{6.1}
$$



one has



$$
\boxed{
\bigcap_{j=1}^{N}(Y_j)
=\left(\prod_{j=1}^{N}Y_j\right).}
\tag{6.2}
$$



Indeed, the variables are pairwise coprime prime elements.  Thus any uniform
scheme-theoretic carrier which lies in every coordinate ideal $(Y_j)$ must
contain the full product $\prod_jY_j$.  Equivalently, the same conclusion
holds for a fixed integer polynomial which vanishes identically on every
coordinate hyperplane over characteristic zero.  Its row degree is at least
$N$.  A pairwise gcd or bounded-window resultant cannot replace this product,
because it vanishes on intersections rather than on the full union of
singleton components.

The common target divisor gives exactly one additional escape and no smaller
one.  Reduction modulo $Q$ and (6.2) give



$$
\boxed{
\bigcap_{j=1}^{N}(Q,Y_j)
=\left(Q,\prod_{j=1}^{N}Y_j\right).}
\tag{6.3}
$$



Thus a uniform algebraic-ideal singleton carrier must use either the original
constant carrier $Q$, already of full unresolved height, or the full row
product.  This is the precise product-versus-$Q$ resultant barrier.

After the actual saturation (2.9), the direct union carrier is



$$
\mathscr S=\prod_{j\in\mathcal J}s_j.
\tag{6.4}
$$



Since $s_j\mid Z_j$,



$$
\log\mathscr S
\le\sum_{j\in\mathcal J}\log Z_j
<2|\mathcal J|\log A
\le(2+o(1))\log b.
\tag{6.5}
$$



Intersecting its radical with $Q^{[1]}$ gives exactly (3.4), but only improves
the ceiling to one full copy, as in (5.4).

Now partition $\mathcal J$ into arbitrary disjoint windows
$\mathcal W_1,\ldots,\mathcal W_r$.  Put



$$
\mathscr S_k=\prod_{j\in\mathcal W_k}s_j.
\tag{6.6}
$$



The singleton factors are pairwise coprime, and



$$
\prod_k\mathscr S_k=\mathscr S,
\qquad
\sum_k\log\mathscr S_k
\le\sum_{j\in\mathcal J}\log Z_j.
\tag{6.7}
$$



Thus every $o(n)$ window has zero individual rate, but summing a growing
number of disjoint windows restores the full bound (6.5).  No choice of
window length produces a sublinear aggregate carrier from height alone.

The theorem in this section is scoped to uniform algebraic-ideal union
carriers, pairwise common-divisor data, and disjoint-window height arguments.
It does not classify polynomial functions over a varying finite field; a
Frobenius-degree identity can vanish as a function without belonging to the
displayed ideals.  Nor does it rule out a genuinely new large-sieve,
finite-field, or monodromy theorem for the actual canonical residues.

## 7. Exact missing arithmetic input

Combining Items 354 and 358, the first new correlation estimate required is



$$
\boxed{
\log\gcd\!\left(
Q^{[1]},
\operatorname{rad}_{>A}\!\left(\prod_{j\in\mathcal J}
\frac{Z_j}
{\gcd\!\left(Z_j,
(|t|\prod_{i\in\mathcal J,\ i\ne j}Z_i)^{M_A}\right)}
\right)
\right)
=o(\log b).}
\tag{7.1}
$$



This is precisely the singleton case of (3.2).  It uses all of the data that
the formal Item-350 model omitted: the unique canonical word, genuine
earlier- and later-row avoidance, and the actual common divisor $Q\mid b$.

For the complete Item-354 criterion one must ultimately prove, for some
$L(n)\to\infty$,



$$
\boxed{
\log\mathcal U_{<L(n)}^{(1)}=o(\log b),}
\tag{7.2}
$$



together with the old excess estimate if the full $\Xi_Q$ branch is to close.
Even (7.1) is presently open, so no larger low-incidence theorem is claimed.

## 8. Strict labels

### PROVED

* The actual incidence-set saturation theorem (2.3)-(2.8).
* The genuine singleton carrier (2.9), including all outside-row avoidance.
* The exact low-incidence squarefree carrier (3.2)-(3.3).
* The four-quadrant overlap decomposition (4.2)-(4.4).
* The pairwise-moment blind spot (5.1)-(5.4).
* The product-versus-$Q$ union-ideal and disjoint-window barriers
  (6.2)-(6.7).

### PROVED SCOPED NO-GO

* Pairwise shared-support data and $E(Q)$ have no primewise term on the
  singleton-squarefree carrier.
* Any uniform scheme-theoretic polynomial union carrier must contain a row
  product of linear depth, and disjoint-window height bounds sum back to the
  full scale.
* These theorems do not close a genuinely new distributional or large-sieve
  estimate for the actual canonical word.

### EXACT FINITE ONLY

* The deterministic replay's declared incidence-set saturation, quadrant,
  union-ideal monomial, and window-partition controls.
* Declared rows are algebraic controls, not actual Item-316 targets and not
  evidence for singleton density.

### OPEN

* The singleton correlation theorem (7.1).
* The growing low-incidence theorem (7.2) and $\Xi_Q=o(\log b)$.
* Item 265's squarefull/excess theorem, $H_Q$, $K_Q$, and $\Gamma_Q$.
* The centered half-bound, beta capacity, Route 1, and $e+\pi$.

### BOOKING



$$
\boxed{
\text{new beta capacity reduction}=0,
\qquad
\text{new Route-1 rate}=0.}
\tag{8.1}
$$



No canonical, master, status, checkpoint, or research-log file is edited by
this work package.

## 9. Deterministic replay

From the archive root:

~~~text
python work/item358_beta_actual_low_incidence_saturation_barrier_certificate.py ^
  --output work/item358_beta_actual_low_incidence_saturation_barrier_certificate.replay.json
~~~

The checker uses only the Python standard library and exact integer
arithmetic.  It performs no prime census, target search, or half-bound scan
and promotes no declared row.
