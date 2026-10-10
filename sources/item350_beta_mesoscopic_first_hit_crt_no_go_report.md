> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 350 — mesoscopic first-hit coordinates and the CRT resultant barrier

Checked: 2026-09-01 (Beijing time)

## 1. Strict verdict and raw capacity

Assume the actual Item-316 target and retain Items 343 and 346.  Thus



$$
\Xi_Q
=\sum_{j=3}^{m}\log D_j
=\sum_{j\in\mathcal H}\log p_j+o(\log b),
\tag{1.1}
$$



where the first-hit primes $p_j$ are pairwise distinct and



$$
A<p_j<A^2,
\qquad
p_j\mid Q\mid b,
\qquad
p_j\nmid t,
\tag{1.2}
$$



and the actual canonical digits satisfy



$$
w_j\delta_{j-1}-\delta_j=p_jh_j,
\qquad
\delta_{j-1}\ge2,
\qquad
1\le h_j<A.
\tag{1.3}
$$



The raw capacity is still



$$
\boxed{
\sum_{j\in\mathcal H}\log p_j
\le\log\operatorname{rad}(Q)
\le\log Q\le\log b.}
\tag{1.4}
$$



Item 350 derives the strongest exact cross-depth relation supplied by the
Ostrowski transition itself.  The result is a negative structural decision:
the signed cofactor loads are independent integral triangular coordinates.
Distinct first-hit primes enter separate coordinates, and the one target
equation does not couple them after localization away from $t$.

More precisely, Item 350 proves all of the following.

1. Every window has an exact telescoping identity, but the corresponding
   transition ideal has zero elimination ideal in the load coordinates.
2. Any window containing $r$ active depths has the exact product carrier of
   height below $2r\log A$; no recurrence resultant compresses it.
3. For any assigned distinct primes $p_j>A$ dividing $b$ and any assigned
   distinct depths, the formal target equation is exactly compatible with
   the selected hit congruences $p_j\mid\mathfrak z_j$, with every selected
   cofactor nonzero and with $p_j\nmid t$ simultaneously.  It does not impose
   $p_j\nmid\mathfrak z_i$ at every earlier depth $i<j$, so it is not a
   formal first-occurrence theorem.  At the penultimate depth the three top
   gradients are resonant, but an exact lower-coordinate term restores the
   missing freedom.

The third statement uses the exact target equality over the integers, not
only a modular surrogate, and it stratifies away exact-zero selected rows.
It does not assert canonical digit bounds, the sign/window language, or the
small quotients in (1.3).  Those arithmetic inequalities are precisely the
remaining possible source of a weighted upper bound.

No such upper bound is proved here.  Booking remains zero.

## 2. Integral load coordinates

For arbitrary integral digit variables $d_1,\ldots,d_m$, define



$$
x_j=w_jd_{j-1}-d_j
=-\epsilon\mathfrak z_j
\qquad(3\le j\le m).
\tag{2.1}
$$



Then



$$
d_j=w_jd_{j-1}-x_j.
\tag{2.2}
$$



Hence the map



$$
\boxed{
(d_1,\ldots,d_m)
\longleftrightarrow
(d_1,d_2,x_3,\ldots,x_m)}
\tag{2.3}
$$



is an integral triangular automorphism.  Its determinant is
$(-1)^{m-2}$.  In particular, the $x_j$ are algebraically independent over
$\mathbb Z$ before the target equation is imposed.

For $2\le u<v\le m$, iteration of (2.2) gives the exact window identity



$$
\boxed{
d_v
=\left(\prod_{r=u+1}^{v}w_r\right)d_u
-\sum_{k=u+1}^{v}
x_k\left(\prod_{r=k+1}^{v}w_r\right).}
\tag{2.4}
$$



An empty product equals one.  Equivalently,



$$
\frac{d_v}{\prod_{r=u+1}^{v}w_r}
=d_u-
\sum_{k=u+1}^{v}
\frac{x_k}{\prod_{r=u+1}^{k}w_r}.
\tag{2.5}
$$



This is the complete cross-depth relation.  It is additive in the loads; it
does not make the product of distinct hit primes divide an endpoint or a
determinant.

There is an exact elimination statement behind this observation.  Let



$$
I_{u,v}
=\bigl(
x_k-w_kd_{k-1}+d_k: u<k\le v
\bigr)
\tag{2.6}
$$



in the polynomial ring over the displayed digit and load variables.  Solving
successively for $d_{u+1},\ldots,d_v$ gives



$$
\boxed{
I_{u,v}\cap
\mathbb Z[x_{u+1},\ldots,x_v]=(0).}
\tag{2.7}
$$



Thus any nonzero pairwise or finite-window resultant involving only these
load coordinates imports information not contained in the continuant/load
recurrence.

## 3. Exact window carriers and their height

On the actual Item-316 word, let



$$
\mathcal H_{u,v}
=\mathcal H\cap\{u+1,\ldots,v\}.
\tag{3.1}
$$



By (1.3),



$$
P_{u,v}:=\prod_{j\in\mathcal H_{u,v}}p_j
\quad\mid\quad
\prod_{j\in\mathcal H_{u,v}}x_j.
\tag{3.2}
$$



The first-hit primes are distinct, so no cross-depth multiplicity is counted.
Canonicality gives $0<x_j<A^2$ at every active mesoscopic depth.  Therefore



$$
\boxed{
\log P_{u,v}
\le\sum_{j\in\mathcal H_{u,v}}\log x_j
<2|\mathcal H_{u,v}|\log A.}
\tag{3.3}
$$



This is the exact product carrier available in a window.  If the window has
length $L=v-u$, every polynomial coefficient in (2.4) is at most $A^L$,
so its logarithmic height is $O(L\log A)$.  Consequently:

* a bounded or $o(n)$ window has zero beta rate;
* covering a positive density of active depths has total height
  $\Theta(n\log A)=\Theta(\log b)$; and
* the recurrence itself supplies no sublinear-height carrier for a
  positive-density first-hit set.

The last statement is a scoped algebraic no-go, not a lower bound for every
conceivable arithmetic invariant.  A successful compression must use the
canonical box, the small quotients $h_j$, or a new global arithmetic theorem.

## 4. Per-prime target compatibility away from (t)

Fix a sign chamber $\sigma$ and put



$$
\Delta_\sigma=\sigma E_{m+1}-a,
\qquad
t=c-\sigma E_m.
\tag{4.1}
$$



For every prime $p>A$ dividing $b$ and every depth $3\le j\le m$, the affine
system



$$
\boxed{
\Delta_\sigma=0,
\qquad
\mathfrak z_j=0,
\qquad
t\ne0}
\tag{4.2}
$$



has a solution over $\mathbb F_p$.

There are three cases.

### 4.1 Lower depths

If $j\le m-2$, use Item 333's coordinates



$$
\mathbb Z[d_1,\ldots,d_m]/(\Delta_\sigma)
\cong
\mathbb Z[d_1,\ldots,d_{m-2},z_m].
\tag{4.3}
$$



The equation $\mathfrak z_j=0$ involves only the lower variables.  Set all
of them to zero.  Item 346 gives



$$
t=c-\kappa_<+z_m=c+z_m.
\tag{4.4}
$$



Choose $z_m\ne-c$ modulo $p$.

### 4.2 The top depth

If $j=m$, set $z_m=0$.  Then



$$
t=t_0=c-\kappa_<.
\tag{4.5}
$$



Item 346 proves that $t_0$ is a primitive affine polynomial.  Its reduction
modulo any prime is nonzero, so it takes a nonzero value over
$\mathbb F_p$.

### 4.3 The penultimate depth

Let



$$
D=w_{m-1}w_m+1.
\tag{4.6}
$$



This case occurs only for $m\ge4$.  In the three top variables
$d_{m-2},d_{m-1},d_m$, remove the harmless common sign $\epsilon$.  The
gradients of $t,\Delta_\sigma,\mathfrak z_{m-1}$ are



$$
\begin{pmatrix}
D&-w_m&1\\
-(AD+w_{m-1})&Aw_m+1&-A\\
-w_{m-1}&1&0
\end{pmatrix}.
\tag{4.7}
$$



The determinant is identically zero.  More precisely, the second row is
$-A$ times the first row plus the third row.  This is not a defect of the
calculation: it is the exact penultimate resonance.

Let $E_{m-1,<}$ denote the part of $E_{m-1}$ supported on
$d_1,\ldots,d_{m-3}$, and put



$$
\rho_<
=\sigma E_{m-1,<}(d_1,\ldots,d_{m-3}).
\tag{4.8}
$$



The continuant recurrence $E_{m+1}=AE_m+E_{m-1}$ gives the global affine
identity



$$
\boxed{
\Delta_\sigma+A t-\mathfrak z_{m-1}
=Ac-a+\rho_<.}
\tag{4.9}
$$



On the lower-zero slice $\rho_<=0$.  If also $p\mid b$ and
$\Delta_\sigma=\mathfrak z_{m-1}=0$, then, using
$c\equiv-Aa\pmod p$ and $p\nmid Aa$,



$$
t\equiv-{a(A^2+1)\over A}\pmod p.
\tag{4.10}
$$



Thus the lower-zero construction has an exact exceptional carrier
$p\mid A^2+1$.  Its total possible logarithmic mass is bounded by



$$
\log\gcd(b,A^2+1)\le \log(A^2+1)=O(\log A)=o(\log b).
\tag{4.11}
$$



This is a zero-rate obstruction to that particular slice, not an exclusion
theorem for the canonical Item-316 word.

The full affine system remains compatible at every $p>A$ dividing $b$.
For $m\ge5$, the coefficient vector of $\rho_<$ is primitive: its last two
entries, up to signs, are



$$
K(w_{m-3},w_{m-2},w_{m-1}),
\qquad K(w_{m-2},w_{m-1}),
\tag{4.12}
$$



whose gcd is one by the continuant recurrence.  For the edge case $m=4$,
the sole coefficient is $K(10,14)=141$ and
$\gcd(141,q_6)=\gcd(141,398959)=1$.  Hence some lower coefficient is a unit
modulo every $p>A$ dividing $b$.  Choose the lower digits so that the right
side of (4.9) equals $A$, then solve the primitive target equation together
with $\mathfrak z_{m-1}=0$.  This gives $t=1$ modulo $p$ and completes the
proof of (4.2).

The resonance therefore produces no new target codimension.  It exposes the
zero-rate lower-slice carrier $A^2+1$, while the primitive lower coordinate
removes even that obstruction in the full formal digit space.

## 5. Exact CRT compatibility with nonzero selected rows

Let $S\subseteq\{3,\ldots,m\}$ be arbitrary.  Assign pairwise distinct
primes



$$
p_j>A,
\qquad
p_j\mid b
\qquad(j\in S),
\tag{5.1}
$$



and put



$$
P_S=\prod_{j\in S}p_j.
\tag{5.2}
$$



> **PROVED — EXACT FORMAL CRT COMPATIBILITY.**  There is an integral digit
> vector $d\in\mathbb Z^m$ such that
>
> 

$$
> \boxed{
> \Delta_\sigma(d)=0,
> \qquad
> p_j\mid\mathfrak z_j(d),
> \qquad
> \mathfrak z_j(d)\ne0\ (j\in S),
> \qquad
> \gcd(t(d),P_S)=1.}
> \tag{5.3}
>
$$



Here "formal" means the ambient integral digit lattice with the exact target
hyperplane imposed.  These vectors are not asserted to be the unique
canonical beta/Ostrowski digits, and no specialization bridge from this CRT
construction to an actual Item-316 word is proved.

For each $j\in S$, choose the solution of (4.2) modulo $p_j$.  The Chinese
remainder theorem gives one residue vector $d^{(0)}$ modulo $P_S$ satisfying



$$
\Delta_\sigma(d^{(0)})\equiv0\pmod{P_S},
\qquad
p_j\mid\mathfrak z_j(d^{(0)}),
\qquad
\gcd(t(d^{(0)}),P_S)=1.
\tag{5.4}
$$



Take an integral lift.  Write



$$
\Delta_\sigma(d^{(0)})=P_Sk.
\tag{5.5}
$$



The two top coefficients of the target defect are



$$
u=\epsilon(Aw_m+1),
\qquad
v=-\epsilon A,
\qquad
\gcd(u,v)=1.
\tag{5.6}
$$



Choose integers $r,s$ with $ur+vs=-k$ and replace



$$
d_{m-1}^{(0)}\mapsto d_{m-1}^{(0)}+P_Sr,
\qquad
d_m^{(0)}\mapsto d_m^{(0)}+P_Ss.
\tag{5.7}
$$



This preserves every residue modulo $P_S$ and makes
$\Delta_\sigma=0$ exactly over $\mathbb Z$.

It remains only to exclude exact-zero selected cofactors.  The integral
kernel of the primitive linear part of $\Delta_\sigma$ has rank $m-1$.
For every $j$, the restriction of $\mathfrak z_j$ to this kernel is nonzero:
when $j<m$, its gradient has zero $d_m$ coefficient while the target gradient
does not; when $j=m$, the two top gradients have determinant one.  Choose an
integral kernel vector $y$ outside these finitely many rational hyperplanes.
Then



$$
d(k)=d^{(0)}+kP_Sy
\tag{5.8}
$$



preserves (5.4) and the exact target equality.  Each selected
$\mathfrak z_j(d(k))$ is a nonconstant affine function of $k$, so only
finitely many integers $k$ produce an exact zero.  Choose any other $k$.
This proves (5.3).

The construction permits $S$ to have linear size.  Thus neither pairwise
resultants nor a growing collection of recurrence-only selected-hit
congruences creates a formal obstruction at this level.  The construction
does not enforce that $p_j$ avoids every earlier row; first-occurrence
avoidance remains part of the canonical arithmetic.

## 6. Scope of the obstruction

The CRT theorem deliberately distinguishes three levels.



$$
\begin{array}{c|c}
\text{condition}&\text{status in (5.3)}\\ \hline
\Delta_\sigma=0&\text{exact over }\mathbb Z\\
p_j\mid\mathfrak z_j&\text{exact divisibility at assigned primes}\\
\mathfrak z_j\ne0&\text{exact-zero rows stratified away}\\
p_j\nmid t&\text{simultaneous for every assigned prime}\\
p_j\nmid\mathfrak z_i\ (i<j)&\text{not imposed}\\
0\le d_i\le w_i&\text{not imposed}\\
\text{Markov/half-language}&\text{not imposed}\\
\mathfrak z_j=-\epsilon p_jh_j,\ 1\le h_j<A&\text{not imposed}.
\end{array}
\tag{6.1}
$$



Therefore (5.3) is not an ambient counterexample promoted to an actual
Item-316 target.  It is a scoped no-go for methods using only the linear
target/load recurrences, modular elimination, and quotient-unit localization.

The actual arithmetic problem left by Item 350 is stronger and now explicit:



$$
\boxed{
\begin{array}{c}
\text{bound the distinct primes }p_j\mid b\text{ for which the unique}\
\text{canonical target word has }
w_j\delta_{j-1}-\delta_j=p_jh_j,
\quad1\le h_j<A.
\end{array}}
\tag{6.2}
$$



A proof of



$$
\sum_{j\in\mathcal H}\log p_j=o(n\log n)
\tag{6.3}
$$



must use the bounded quotient $h_j$, canonical inequalities across a linear
number of depths, or genuinely external arithmetic of the common divisor
$b$.  No pairwise or fixed-window resultant from the existing recurrences can
provide it.

## 7. Strict labels

### PROVED

* The integral triangular load-coordinate automorphism (2.3).
* The exact all-window identity (2.4)-(2.5).
* The zero load-coordinate elimination ideal (2.7).
* The exact window carrier and height bound (3.2)-(3.3).
* Per-prime target/$t$-unit compatibility at every depth (4.2).
* The exact penultimate row resonance and affine identity (4.7)-(4.9).
* The zero-rate lower-zero-slice carrier $A^2+1$ and the primitive
  lower-coordinate escape from it.
* The exact integral CRT theorem (5.3), including nonzero selected rows.

### PROVED SCOPED NO-GO

* Pairwise, bounded-window, and recurrence-only resultants do not obstruct
  arbitrary distinct selected-hit congruences.
* This remains true after imposing the exact formal target equality and
  excluding primes dividing $t$.
* The theorem does not include earlier-row avoidance, canonical digit
  inequalities, or the small quotients $h_j$.

### EXACT FINITE ONLY

* The deterministic replay's declared triangular-coordinate, symbolic
  resonance, lower-slice carrier, CRT, exact-target lift, and nonzero-row
  controls.
* No bounded row is promoted to a target census or density theorem.

### OPEN

* The actual weighted bound (6.3), any strict fractional reduction of
  $\Xi_Q$, and any positive actual-family lower bound.
* Cross-depth consequences that genuinely use all canonical inequalities and
  the small positive quotients $h_j$.
* $H_Q$, Item 265's squarefull branch, $K_Q$, and $\Gamma_Q$.
* The centered half-bound, beta capacity, Route 1, and $e+\pi$.

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
python work/item350_beta_mesoscopic_first_hit_crt_no_go_certificate.py ^
  --output work/item350_beta_mesoscopic_first_hit_crt_no_go_certificate.replay.json
~~~

The checker uses only the Python standard library and exact integer
arithmetic.  It performs no prime census, target search, or half-bound scan
and promotes no bounded row.
